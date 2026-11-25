# -*- coding: utf-8 -*-
"""Avanza §4, §6, diagrama CI/CD y Excel planillas (sin inventar resultados EV5-6)."""
from __future__ import annotations

import csv
import re
import shutil
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[2]  # EV5-6
NINNA = Path(__file__).resolve().parent
PLANILLAS = NINNA / "Planillas"
ENT = NINNA / "Entregables"
MD = ENT / "01-Informe-EP5-borrador.md"
CONTEXTO = ROOT / "EV5-6 Contexto"

SECTION4 = r'''## 4. Diseño de casos de prueba

Se reutilizan el catálogo y las fichas de la EP3 (23 casos → 40 códigos ERS B). En este ciclo MITIGAR, los casos ligados a INC-01…07, 05, 06, 13 y 14 se marcan como **Retest ciclo EV5-6**. El resultado de ejecución EV5-6 se completa con handoff (viernes 27); no se inventa.

### 4.1 Matriz de trazabilidad

La matriz 40/40 con columnas Resultado EV2 y Resultado EV5-6 está en:

- Trabajo: `Planillas/EV56-22-Matriz-40-ERS-ciclo3.csv`
- Word: `EV5-6 Contexto/02-Matriz-trazabilidad-40-ERS.docx`

### 4.2 Catálogo de casos (reuso EP3)

| Caso | Nombre | Códigos ERS | Herramienta | Ejecuta | Retest EV5-6 |
|------|--------|-------------|-------------|---------|--------------|
| CP-01 | Autenticación válida y rechazo de credenciales inválidas | RF-1.1, NFR-SEG-2, NFR-SEG-9 | UI, Postman/Swagger, Selenium | Nicolás | Sí (post bcrypt / JWT) |
| CP-02 | Registro de examen médico | RF-3.1, RB-3 | UI, Postman, Selenium | Nicolás | Sí (post INC-04) |
| CP-03 | Auditoría ante acciones críticas | RF-5.1, NFR-SEG-8 | Postman, BD auditoría | Nicolás | Sí (INC-13/14) |
| CP-04 | Control de acceso por rol e inyección | NFR-SEG-4, NFR-SEG-5, RB-1 | ZAP, SQLMap, Swagger | Ari / Nicolás | Sí (INC-05/07) |
| CP-05 | Tiempo CRUD bajo carga + estrés | NFR-PERF-1 (+ ramp 5000) | JMeter | Ari | Sí (INC-04; 5000 pendiente) |
| CP-06 | Usabilidad adulto mayor / responsivo | NFR-USAB-1/2/4, NFR-COMPAT-2 | Checklist, Lighthouse | Skarlett | Según alcance |
| CP-07 | Cierre de sesión y revocación de token | RF-1.2, NFR-SEG-9 | Postman, Selenium | Nicolás | Sí (INC-03) |
| CP-08 | Administración de usuarios (admin) | RF-2.5–2.7, NFR-SEG-4, RB-2 | UI, Postman, Selenium | Nicolás | Sí (INC-07) |
| CP-09…CP-13 | Registro, pacientes, exámenes, documentos | RF-2.*, RF-3.*, RF-4.* | UI / Postman / Selenium | Nicolás (+ Ari tiempo) | Selectivo |
| CP-14 | TLS frontend y API | NFR-SEG-1 | Revisión nginx / compose | Skarlett | Resultado o reserva |
| CP-15 | Hash de contraseñas / John | NFR-SEG-2 | BD + John the Ripper | Ari | Sí (INC-01) |
| CP-16 | Cifrado en reposo | NFR-SEG-3 | Esquema / uploads / Sonar | Skarlett | Resultado o reserva |
| CP-17 | Logs y errores sin fuga | NFR-SEG-6 | Sonar, Swagger | Skarlett / Ari | Sí (INC-06) |
| CP-18 | Respaldo / restauración | NFR-SEG-7 | pg_dump | Skarlett | Resultado o reserva |
| CP-19 | Perf página / 200 VU | NFR-PERF-2/3 | Lighthouse, JMeter | Ari | Tras INC-04 |
| CP-20…CP-22 | Usabilidad mensajes / disponibilidad / browsers | NFR-USAB-3, NFR-DIS-*, NFR-COMPAT-1 | Manual / doc | Varios | Según alcance |
| CP-23 | Cumplimiento normativo | NFR-SEG-8 | Checklist normativo | Giannina | Con tabla Skarlett |
| SEL-suite | Regresión UI Selenium post-mitigación | RF/RB críticos | Selenium report.html/json | Nicolás | **Obligatorio** |

### 4.3 Casos detallados (mínimo representativo + obligatorios)

Formato alineado al formato oficial EP5 (ID · Nombre · Requerimiento · Descripción · Precondiciones · Pasos · Resultado esperado · Criterio · Datos · Tipo). Fuente de diseño: fichas EP3. Columna adicional de este ciclo: **Retest EV5-6**.

#### Tabla. Ficha CP-01 (auth + hashes)

| Campo | Contenido |
|-------|-----------|
| ID / Nombre | CP-01 · Autenticación válida y rechazo de credenciales inválidas |
| Requerimiento | RF-1.1; NFR-SEG-2; NFR-SEG-9 |
| Descripción | Verificar que un usuario válido obtiene JWT; credenciales inválidas se rechazan sin filtrar si el usuario existe; post-mitigación las contraseñas no están en texto plano. |
| Precondiciones | Docker FE 3333 / API 4444. Usuario de prueba (p. ej. médico). |
| Pasos | 1. POST `/autenticacion/login` válido. 2. Verificar 200 + JWT. 3. Login inválido → 401. 4. (EV5-6) Confirmar hashes en BD / John carga hashes (con CP-15). |
| Resultado esperado | Login válido 200; rechazos 401; BD sin texto plano tras INC-01. |
| Criterio de aceptación | Token solo con credenciales válidas; NFR-SEG-2 cumplido en retest. |
| Datos de prueba | Credenciales semilla del laboratorio; variantes inválidas. |
| Tipo | Funcional y seguridad |
| Retest EV5-6 | Pendiente handoff Nicolás/Ari (post bcrypt) |
| Resultado EV2 | Aprobado en login; INC-01 abierto en almacenamiento (CP-15) |

#### Tabla. Ficha CP-15 (John / hashes)

| Campo | Contenido |
|-------|-----------|
| ID / Nombre | CP-15 · Almacenamiento de contraseñas y resistencia a crackeo |
| Requerimiento | NFR-SEG-2 |
| Descripción | Comprobar que las contraseñas en BD usan hash seguro (bcrypt) y que John the Ripper opera sobre hashes, no sobre texto plano. |
| Precondiciones | Acceso a BD de prueba; John instalado; baseline EV2: texto plano. |
| Pasos | 1. Consultar columna de contraseñas. 2. Exportar hashes si existen. 3. Ejecutar John. 4. Contrastar before (EV2) vs after (EV5-6). |
| Resultado esperado | Hashes bcrypt; John no ve texto plano. |
| Criterio de aceptación | NFR-SEG-2 cumplido; evidencia before/after archivada. |
| Datos de prueba | Usuarios semilla del laboratorio. |
| Tipo | Seguridad |
| Retest EV5-6 | Pendiente handoff Ari (bloqueado por INC-01) |
| Resultado EV2 | Fallido (INC-01) |

#### Tabla. Ficha CP-07 (logout)

| Campo | Contenido |
|-------|-----------|
| ID / Nombre | CP-07 · Cierre de sesión y revocación del token |
| Requerimiento | RF-1.2; NFR-SEG-9 |
| Descripción | Al cerrar sesión, el JWT previo deja de autorizar llamadas a la API. |
| Precondiciones | Docker arriba; usuario médico; al menos un recurso autenticado. |
| Pasos | 1. Login y guardar token. 2. GET autenticado → 200. 3. Logout. 4. Reutilizar token → 401. |
| Resultado esperado | 401 con el token post-logout. |
| Criterio de aceptación | Logout invalida sesión en servidor (no solo UI). |
| Datos de prueba | Token JWT del paso 1. |
| Tipo | Seguridad de sesión |
| Retest EV5-6 | Pendiente handoff Nicolás (INC-03) |
| Resultado EV2 | Fallido (INC-03) |

#### Tabla. Ficha CP-04 / CP-08 (RBAC e `/roles`)

| Campo | Contenido |
|-------|-----------|
| ID / Nombre | CP-04 · Control de acceso por rol; CP-08 · Administración de usuarios |
| Requerimiento | NFR-SEG-4, NFR-SEG-5, RB-1, RF-2.5–2.7, RB-2 |
| Descripción | Paciente no administra ni ve datos ajenos; médico no usa `/usuarios` ni `/roles` de admin; admin completa CRUD de usuarios; `/roles` exige JWT+admin. |
| Precondiciones | Tokens de los tres roles. |
| Pasos | 1. Paciente: escrituras / datos ajenos → 403. 2. Médico: `/usuarios`, `/roles` → 401/403. 3. Admin: listar/editar/eliminar → 2xx. 4. Sin token → 401. |
| Resultado esperado | Matriz 401/403/2xx según rol; sin inyección crítica. |
| Criterio de aceptación | Control efectivo en backend (INC-07 cerrado). |
| Datos de prueba | Tokens paciente / médico / admin; payloads SQLMap/ZAP según bitácora. |
| Tipo | Seguridad / funcional RBAC |
| Retest EV5-6 | Pendiente handoff Nicolás/Ari |
| Resultado EV2 | Parcial (403 en varios flujos; `/roles` sin prueba dinámica completa) |

#### Tabla. Ficha CP-05 + estrés 5000 VU

| Campo | Contenido |
|-------|-----------|
| ID / Nombre | CP-05 · Tiempo CRUD + ramp JMeter hasta 5000 VU |
| Requerimiento | NFR-PERF-1 (300 ms); estrés obligatorio del examen |
| Descripción | Medir latencia CRUD sin delay artificial y documentar ramp 100→1000→2500→5000 VU. |
| Precondiciones | INC-04 mitigado (delay fuera de rutas). Ambiente estable. |
| Pasos | 1. Humo 1 VU (timing API). 2. Planes JMeter por fase. 3. Archivar `.jtl` / dashboard. 4. Si HW no alcanza 5000, declarar techo. |
| Resultado esperado | 1 VU ≪ 300 ms; fases documentadas; intento 5000 con evidencia. |
| Criterio de aceptación | Evidencia before/after delay + tablas por VU. |
| Datos de prueba | GET/POST pacientes y exámenes; usuarios virtuales por fase. |
| Tipo | Rendimiento / estrés |
| Retest EV5-6 | **Parcial hecho:** after delay ~0,03 s (Ari EV56-04). JMeter 5000 pendiente. |
| Resultado EV2 | Fallido (INC-04, ~5 s) |

#### Tabla. Ficha SEL-suite (Selenium obligatorio)

| Campo | Contenido |
|-------|-----------|
| ID / Nombre | SEL-suite · Regresión UI post-mitigación |
| Requerimiento | Flujos críticos RF/RB (login, roles, pacientes, exámenes) |
| Descripción | Ejecutar suite Selenium tras mitigaciones P0; archivar `report.html` y `report.json` con pass rate. |
| Precondiciones | Mitigación mínima 01–05 en código desplegado en lab. |
| Pasos | 1. Levantar Docker. 2. Correr suite. 3. Guardar reportes bajo `Nicolas/Evidencias/`. 4. Anotar fallos → INC residual. |
| Resultado esperado | Pass rate informado; fallos trazados a INC. |
| Criterio de aceptación | Reportes archivados; no se sustituye DAST/SAST. |
| Datos de prueba | Usuarios semilla; baseline EV2 11/11 solo como referencia. |
| Tipo | Automatización UI |
| Retest EV5-6 | Pendiente handoff Nicolás |
| Resultado EV2 | Baseline 11/11 (no sustituye post-fix) |

---
'''

SECTION6 = r'''## 6. Propuesta de mejora

Presenta acciones concretas de remediación (formato EP5: ID · impacto · propuesta) y el plan de residuales. Los estados «Verificado» solo se marcan con evidencia de retest.

### 6.1 Mitigaciones del ciclo (mínimo de examen)

#### INC-04 · Delay artificial 5 s

| Campo | Contenido |
|-------|-----------|
| ID / nombre | INC-04 / NFR-PERF-1 · `delayMiddleware(5000)` |
| Impacto | Grave — invalida mediciones de desempeño; CRUD ~5 s |
| Propuesta de remediación | Quitar `delayMiddleware` de rutas `pacientes`, `examenes`, `documentos` |
| Retest | Timing API + humo FE; luego JMeter ramp |
| Estado 25-11-2026 | **Medido AFTER** (Ari). Before ~5,03 s → after ~0,03 s. Paths: `Ari/Evidencias/EV56-04/`. Pendiente cierre/merge de equipo y JMeter 5000 |

#### INC-01 · Contraseñas en texto plano

| Campo | Contenido |
|-------|-----------|
| ID / nombre | INC-01 / NFR-SEG-2 · almacenamiento de autenticadores |
| Impacto | **Crítico** — exposición total de cuentas |
| Propuesta de remediación | Hash bcrypt al registrar/actualizar; migrar semillas; política de clave |
| Retest | CP-15 (John) + CP-01 login |
| Estado | **Abierto** — pendiente handoff Nicolás/Ari |

#### INC-02 · JWT_SECRET en repositorio

| Campo | Contenido |
|-------|-----------|
| ID / nombre | INC-02 / NFR-SEG-9 · secreto de sesión |
| Impacto | Grave — compromiso de sesiones |
| Propuesta de remediación | Secreto solo en variables de entorno; limpiar README/código versionado |
| Retest | Revisión repo + login |
| Estado | **Abierto** — pendiente Nicolás |

#### INC-03 · Logout sin revocación

| Campo | Contenido |
|-------|-----------|
| ID / nombre | INC-03 / RF-1.2 · sesión post-logout |
| Impacto | Grave — sesión usable en equipo compartido |
| Propuesta de remediación | Endpoint logout + blacklist/rotación de token |
| Retest | CP-07 |
| Estado | **Abierto** — pendiente Nicolás |

#### INC-07 · `/roles` sin control de rol

| Campo | Contenido |
|-------|-----------|
| ID / nombre | INC-07 / NFR-SEG-4 · autorización en `/roles` |
| Impacto | Grave — escalada de privilegios |
| Propuesta de remediación | Exigir JWT + rol administrador en la ruta |
| Retest | curl/Swagger 401/403/2xx (CP-04/08) |
| Estado | **Abierto** — pendiente Nicolás |

### 6.2 Residuales y plan (reserva §6 / ampliación)

| INC / tema | Impacto | Dueño | Fecha objetivo | Estado |
|------------|---------|-------|----------------|--------|
| INC-05 CORS + cabeceras | Moderado/Grave | Ari | Antes de ZAP after | Abierto |
| INC-06 fuga `err.message` | Grave | Skarlett | Con CP-17 | Abierto |
| INC-13 descarga sin auditoría | Grave | Nicolás | Tras P0 | Abierto |
| INC-14 POST `/auditoria` abierto | Grave | Nicolás | Tras P0 | Abierto |
| INC-09 baja lógica | Grave | Nicolás | Reserva si no alcanza | Abierto |
| INC-10 política de clave / registro | Moderado | Nicolás | Con INC-01 | Parcial |
| INC-15 formatos DOC/PPT | Moderado | Nicolás | Reserva | Abierto |
| INC-16 cifrado reposo / bytea | Grave | Skarlett | Reserva + plan | Abierto |
| INC-17 disponibilidad / réplica | Grave | Ari | Reserva | Abierto |
| CP-14 TLS laboratorio | P0 config | Skarlett | Resultado o limitación fechada | Pendiente |
| Lockout anti fuerza bruta | P1 | Ari (+ Nico) | Tras INC-01 | Pendiente |
| Wireshark sesión / carga | P1 | Nico / Ari | Según tiempo | Pendiente |

### 6.3 Mantenimiento continuo (IE7) y CI/CD

Objetivo: que los controles de calidad y seguridad no dependan solo del examen puntual.

Flujo propuesto (borrador Ninna para completar con Skarlett — EV56-21):

1. Commit / PR  
2. Build  
3. Pruebas unitarias  
4. SonarQube Quality Gate (SAST)  
5. Build imagen Docker  
6. Deploy a laboratorio  
7. Selenium (regresión UI)  
8. (Opcional / nocturno) ZAP autenticado  

Diagrama editable: `Planillas/EV56-21-Diagrama-CICD-borrador.md`.

Relación normativa de proceso: ISO/IEC/IEEE **29119** (proceso de pruebas) y controles alineados a **27001** (acceso, registro, desarrollo seguro).

### 6.4 Dictamen (borrador — no definitivo)

**Dictamen provisional al 25-11-2026: No certificado.**

Fundamento: INC-01 (crítico) sigue abierto; INC-02, 03 y 07 sin retest verificado. INC-04 muestra mejora medible de desempeño, pero no basta para certificar mientras exista un crítico abierto.

Meta del equipo al cierre: **Certificado con reservas**, si se verifican INC-01, 02, 03, 04 y 07 y se declaran reservas explícitas (p. ej. TLS de laboratorio, techo de hardware en 5000 VU, cifrado en reposo).

---
'''


def patch_informe_md():
    text = MD.read_text(encoding="utf-8")
    text2 = re.sub(
        r"## 4\. Diseño de casos de prueba\n.*?(?=\n## 5\. )",
        SECTION4,
        text,
        count=1,
        flags=re.S,
    )
    text3 = re.sub(
        r"## 6\. Propuesta de mejora\n.*?(?=\n## Anexos)",
        SECTION6,
        text2,
        count=1,
        flags=re.S,
    )
    if text3 == text:
        raise RuntimeError("No se pudo reemplazar §4/§6 en el Markdown")
    # anexos
    text3 = text3.replace(
        "- E. Outline guion EP6",
        "- E. Outline guion EP6\n- F. Diagrama CI/CD borrador (EV56-21)",
    )
    MD.write_text(text3, encoding="utf-8")
    print("OK informe MD §4 y §6")


def write_cicd():
    path = PLANILLAS / "EV56-21-Diagrama-CICD-borrador.md"
    path.write_text(
        """# EV56-21 — Diagrama CI/CD con controles de seguridad (borrador)

**Autores borrador:** Giannina (Ninna) · completar con Skarlett  
**Uso:** sección 6.3 del informe EP5 + lámina 10 del guion EP6  
**Estado:** esquema; Skarlett ajusta herramientas reales del equipo

## Idea principal

El pipeline debe frenar un cambio inseguro **antes** de que llegue al laboratorio estable, y después verificar UI y (si alcanza) DAST.

## Diagrama (Mermaid)

```mermaid
flowchart LR
  A[Commit / PR] --> B[Build]
  B --> C[Pruebas unitarias]
  C --> D{SonarQube\\nQuality Gate}
  D -->|No pasa| X[Bloquear merge]
  D -->|Pasa| E[Imagen Docker]
  E --> F[Deploy laboratorio\\nFE 3333 / API 4444]
  F --> G[Selenium\\nregresión UI]
  G --> H[Artefactos\\nreport.html / json]
  F -.->|nocturno opcional| I[ZAP autenticado]
  I --> J[Reporte DAST]
```

## Controles por etapa

| Etapa | Control | Norma / estándar de apoyo | Dueño sugerido |
|-------|---------|---------------------------|----------------|
| PR / commit | Revisión + secretos fuera del repo (INC-02) | 27001 (secretos) | Nicolás |
| Unitarias | Regresión mínima auth/RBAC | 29119 (proceso) | Nicolás |
| Sonar Quality Gate | Bugs / vulnerabilidades / smells | 25010 mantenibilidad + SAST | Skarlett |
| Imagen Docker | Build reproducible del lab | Configuración segura | Equipo |
| Selenium | Regresión UI post-merge | IE5 / obligatorio examen | Nicolás |
| ZAP nocturno | DAST autenticado | 27001 / IE1 | Ari |
| Evidencias | Prefijo `EV56-` + path en bitácora | Trazabilidad informe | Ninna integra |

## Qué falta que complete Skarlett

- [ ] Herramientas exactas del equipo (GitHub Actions / otro CI, runner, etc.)
- [ ] Umbrales del Quality Gate (lo que ya usan en Sonar)
- [ ] Si ZAP va en pipeline o solo manual con evidencia
- [ ] Diagrama exportado a PNG/SVG para el PPT

## Nota

No inventar capturas de pipeline. Si el CI aún no está automatizado, el diagrama se presenta como **propuesta de mantenimiento continuo** (IE7) y se declara el estado actual del laboratorio Docker.
""",
        encoding="utf-8",
    )
    print(f"OK {path.name}")


def write_excels():
    PLANILLAS.mkdir(parents=True, exist_ok=True)
    thin = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin"),
    )
    header_fill = PatternFill("solid", fgColor="1F4E79")
    header_font = Font(color="FFFFFF", bold=True, name="Arial", size=10)
    body_font = Font(name="Arial", size=9)
    wrap = Alignment(wrap_text=True, vertical="top")

    # --- Matriz desde CSV ---
    csv_path = PLANILLAS / "EV56-22-Matriz-40-ERS-ciclo3.csv"
    rows = list(csv.DictReader(csv_path.open(encoding="utf-8-sig")))
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Matriz 40 ERS"
    headers = [
        "Codigo_ERS",
        "Descripcion",
        "Caso",
        "Tipo",
        "Riesgo",
        "Modulo",
        "Ejecuta",
        "INC",
        "Resultado_EV2",
        "Resultado_EV56",
        "Evidencia_path",
        "Dueño_dato",
    ]
    for c, h in enumerate(headers, 1):
        cell = ws.cell(1, c, h)
        cell.fill = header_fill
        cell.font = header_font
        cell.border = thin
    for r, row in enumerate(rows, 2):
        for c, h in enumerate(headers, 1):
            cell = ws.cell(r, c, row.get(h, ""))
            cell.font = body_font
            cell.border = thin
            cell.alignment = wrap
    for c in range(1, len(headers) + 1):
        ws.column_dimensions[get_column_letter(c)].width = 18 if c != 2 else 40
    ws.auto_filter.ref = f"A1:L{len(rows)+1}"
    ws.freeze_panes = "A2"
    out_m = PLANILLAS / "EV56-22-Matriz-Trazabilidad.xlsx"
    wb.save(out_m)
    print(f"OK {out_m.name}")

    # --- Registro / consolidado Cuidarte ---
    catalog = [
        ("CP-01", "Autenticación válida y rechazo de credenciales inválidas", "P0", "Autenticación", "Login JWT", "seguridad / funcional", "P0 auth", "INC-01, INC-02", "Docker FE3333/API4444", "POST login válido/inválido", "200+JWT; 401 inválido; sin plain text post-fix", "Lab Docker", "", "CP-15", "Aprobado login EV2; INC-01 abierto en almacenamiento", "PENDIENTE_RETEST", "Giannina", "Nicolás", "", "Retest post bcrypt", "", ""),
        ("CP-04", "Control de acceso por rol e inyección", "P0", "Autorización", "RBAC / IDOR", "seguridad", "P0 acceso", "INC-05, INC-07", "Tokens 3 roles", "GET indebidos + SQLMap/ZAP", "401/403; sin inyección crítica", "Lab Docker", "", "CP-08", "Parcial EV2", "PENDIENTE_RETEST", "Giannina", "Ari/Nicolás", "", "", "", ""),
        ("CP-05", "Tiempo CRUD + estrés hasta 5000 VU", "P0", "Rendimiento", "CRUD / stress", "rendimiento", "P3→P0 examen", "INC-04", "Sin otras pruebas en curso; delay off", "JMeter fases", "1 VU ≪300ms; ramp documentado", "Lab Docker", "JMeter", "SEL-suite", "Fallido EV2 (~5s); AFTER delay ~0.03s", "EN_CURSO", "Giannina", "Ari", "2026-11-25", "Delay retirado; falta JMeter 5000", "Quitar delayMiddleware de rutas", "2026-11-25"),
        ("CP-07", "Cierre de sesión y revocación de token", "P0", "Autenticación", "Logout", "seguridad sesión", "P0 sesión", "INC-03", "Usuario médico", "Login → uso → logout → reuse token", "401 post-logout", "Lab Docker", "", "CP-01", "Fallido EV2 INC-03", "PENDIENTE_RETEST", "Giannina", "Nicolás", "", "", "", ""),
        ("CP-08", "Administración de usuarios por administrador", "P0", "Usuarios", "CRUD usuarios/roles", "funcional + RBAC", "P0 admin", "INC-07, INC-09", "Admin + médico + usuario sintético", "GET/PUT/DELETE usuarios; /roles", "Solo admin 2xx; otros 401/403", "Lab Docker", "", "CP-04", "Aprobado parcial EV2; /roles pendiente", "PENDIENTE_RETEST", "Giannina", "Nicolás", "", "", "", ""),
        ("CP-15", "Hash de contraseñas / John the Ripper", "P0", "Autenticación/BD", "NFR-SEG-2", "seguridad", "P0 crítico", "INC-01", "Acceso BD + John", "Exportar hashes; John", "Hashes bcrypt; no plain text", "Lab Docker", "John", "CP-01", "Fallido EV2 INC-01", "PENDIENTE_RETEST", "Giannina", "Ari", "", "", "", ""),
        ("SEL-suite", "Regresión UI Selenium post-mitigación", "P0", "UI transversal", "Suite automatizada", "automatización", "Obligatorio EP5", "INC P0", "Mitigaciones mínimas desplegadas", "Correr suite; archivar reportes", "Pass rate + fallos→INC", "Lab Docker + Selenium", "Selenium", "CP-01,07,08,10…", "Baseline EV2 11/11 (no sustituye)", "PENDIENTE_RETEST", "Giannina", "Nicolás", "", "", "", ""),
        ("CP-02", "Registro de examen médico", "P2", "Exámenes", "Alta examen", "funcional", "P2", "INC-04", "Médico autenticado", "Crear examen", "200; datos visibles", "Lab Docker", "", "", "Aprobado EV2", "EV2_OK_RETEST_SI_APLICA", "Giannina", "Nicolás", "", "Humo FE post-delay OK (Ari)", "", ""),
        ("CP-03", "Auditoría acciones críticas", "P1", "Auditoría", "RF-5.1", "funcional/cumplimiento", "P1", "INC-13, INC-14", "Acciones con descarga/CRUD", "Ver tabla auditoría", "Eventos registrados", "Lab Docker", "", "", "Fallido EV2", "PENDIENTE_RETEST", "Giannina", "Nicolás", "", "", "", ""),
        ("CP-14", "TLS frontend y API", "P0", "Configuración", "NFR-SEG-1", "seguridad config", "P0", "", "Revisión nginx/compose", "Verificar HTTPS", "TLS o limitación fechada", "Lab Docker", "", "", "Fallido EV2", "PENDIENTE_RETEST", "Giannina", "Skarlett", "", "Candidato a reserva §6", "", ""),
        ("CP-16", "Cifrado en reposo", "P0", "BD/storage", "NFR-SEG-3", "seguridad", "P0", "INC-16", "Esquema + uploads", "Revisión", "Cifrado o reserva", "Lab Docker", "", "", "Fallido EV2", "PENDIENTE_RETEST", "Giannina", "Skarlett", "", "Candidato a reserva §6", "", ""),
        ("CP-17", "Logs / errores sin fuga", "P1", "Errores", "NFR-SEG-6", "seguridad", "P1", "INC-06", "Sonar + API error", "Forzar error controlado", "Mensaje genérico", "Lab Docker", "Sonar", "", "Fallido EV2", "PENDIENTE_RETEST", "Giannina", "Skarlett", "", "", "", ""),
        ("CP-19", "Perf página / 200 VU", "P3", "Frontend/API", "NFR-PERF-2/3", "rendimiento", "P3", "INC-04", "Post delay off", "Lighthouse + JMeter", "Cumple o documenta gap", "Lab Docker", "JMeter/Lighthouse", "CP-05", "Fallido EV2", "PENDIENTE_RETEST", "Giannina", "Ari", "", "", "", ""),
        ("CP-23", "Cumplimiento normativo", "P0", "Transversal", "NFR-SEG-8", "cumplimiento", "P0", "INC seguridad", "Tabla normativa Skarlett", "Checklist arts.", "Trazable a INC/CP", "Documental", "", "CP-03, CP-04", "Fallido EV2", "PENDIENTE_RETEST", "Giannina", "Giannina", "", "Espera tabla Skarlett", "", ""),
    ]

    # Preferir copiar plantilla docente si es xlsx válido
    template = ROOT / "Planilla_Consolidado_Avance_Metricas_Ejecucion_Casos_Prueba.xlsx"
    out_r = PLANILLAS / "EV56-22-Registro-Casos-Seguimiento.xlsx"
    shutil.copy2(template, out_r)
    wb = openpyxl.load_workbook(out_r)
    ws = wb["Listado de Casos de Prueba"]
    ws["A2"] = "Proyecto: Cuidarte+ (Caso B)"
    ws["A3"] = "Versión: ciclo MITIGAR EV5-6 / EP5 (borrador 25-11-2026)"
    ws["A4"] = "Stakeholders: Ari Araya, Nicolás Barra, Giannina Guerrero, Skarlett Tropan"
    ws["A5"] = "Comentarios: Resultado_EV56 / Estado se completan con handoff vie 27. No inventar cifras."
    ws["A6"] = "Ciclo de Pruebas: Retest post-mitigación + Selenium + JMeter 5000"

    # borrar filas de ejemplo (desde 9 hasta max con datos de ejemplo)
    for r in range(9, 200):
        for c in range(1, 27):
            ws.cell(r, c).value = None

    fields = [
        # map to columns 1..24 (A=Id empty, B=Caso...)
        "caso", "desc", "prio", "fecha", "area", "func", "obj", "riesgo", "mitig",
        "pre", "datos", "esperado", "ambiente", "proc", "deps", "resultado", "estado",
        "visado", "realizado", "ult_fecha", "obs", "correcciones", "fecha_corr",
    ]
    # Actually columns: A Id, B Caso, C Desc, ... 
    for i, row in enumerate(catalog):
        r = 9 + i
        ws.cell(r, 1).value = i + 1  # Id
        # row tuple aligns to B..X roughly
        values = [
            row[0],  # B caso
            row[1],  # C desc
            row[2],  # D prio
            "2026-11-25",  # E fecha diseño
            row[3],  # F area
            row[4],  # G func
            row[5],  # H obj calidad
            row[6],  # I riesgo
            row[7],  # J mitig plan
            row[8],  # K pre
            row[9],  # L datos
            row[10],  # M esperado
            row[11],  # N ambiente
            row[12],  # O proc especiales
            row[13],  # P deps
            row[14],  # Q resultado obtenido (EV2 + parcial EV56 si hay)
            row[15],  # R estado
            row[16],  # S visado
            row[17],  # T realizado
            row[18] or "",  # U ultima fecha estado
            row[19],  # V obs
            row[20],  # W correcciones
            row[21],  # X fecha correcciones
        ]
        for c, val in enumerate(values, start=2):
            cell = ws.cell(r, c, val)
            cell.font = body_font
            cell.alignment = wrap

    # hoja KPIs vacía útil
    if "KPIs EV5-6" in wb.sheetnames:
        del wb["KPIs EV5-6"]
    k = wb.create_sheet("KPIs EV5-6")
    k["A1"] = "KPI"
    k["B1"] = "EV2"
    k["C1"] = "EV5-6 (pendiente handoff)"
    k["D1"] = "Fuente"
    for cell in k[1]:
        cell.fill = header_fill
        cell.font = header_font
    kpi_rows = [
        ("G1 Aprobados", 10, "", "Matriz / §5.1"),
        ("G1 Parciales", 10, "", "Matriz"),
        ("G1 Fallidos", 20, "", "Matriz"),
        ("G1 Total códigos ERS", 40, 40, "Matriz"),
        ("G2 Críticos abiertos", 1, "", "Inventario INC-01"),
        ("G3 Selenium pass rate %", "11/11 baseline EV2", "", "Nicolas report.json"),
        ("G4 JMeter avg ms @1 VU post-delay", "~30", "", "Ari EV56-04"),
        ("G4 JMeter @5000 VU", "", "", "Pendiente Ari"),
        ("G6 Sonar bugs/vuln delta", "", "", "Pendiente Skarlett"),
        ("% P0 mínimo verificados", "0% verificado (04 medido)", "", "Inventario"),
    ]
    for i, row in enumerate(kpi_rows, 2):
        for c, v in enumerate(row, 1):
            k.cell(i, c, v).font = body_font
    for c in range(1, 5):
        k.column_dimensions[get_column_letter(c)].width = 28

    wb.save(out_r)
    print(f"OK {out_r.name}")


def regenerate_word():
    gen = CONTEXTO / "_generar_formato_ev2.py"
    import importlib.util

    spec = importlib.util.spec_from_file_location("gen_ev2", gen)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.gen_informe()
    # también refrescar inventario/kpi word porque §6 cambió fuentes
    mod.gen_inventario_kpis()


def main():
    patch_informe_md()
    write_cicd()
    write_excels()
    regenerate_word()
    print("Listo 1–4.")


if __name__ == "__main__":
    main()
