# 00 — Análisis del encargo final EV5-6 (EP5 + defensa EP6)

**Asignatura:** ISY1102 Seguridad y calidad en el desarrollo de software  
**Sección:** 001V  
**Integrantes:** Ari Araya · Nicolás Barra · Giannina Guerrero (Ninna) · Skarlett Tropan  
**Fase del semestre:** **MITIGAR** (EV1–EV2 = evidenciar/descubrir; este ciclo = corregir + retest + documentar)  
**Fuentes:** carpeta [`../`](../) (pauta, formato informe, planillas, pizarrón de clase)

> Este documento alinea al equipo. **No sustituye** el informe Word/PDF ni la presentación: eso lo produce cada rol según su backlog.

---

## 1. Qué pide el examen

### 1.1 Encargo (informe grupal)

Estructura del formato docente (§1–6):

1. Introducción  
2. Criterios de calidad (usabilidad, rendimiento, seguridad, normativas)  
3. Plan de pruebas (estrategia, tipos, aceptación, herramientas/recursos)  
4. Diseño de casos de prueba  
5. Ejecución (resumen, detalle, criticidad)  
6. Propuesta de mejora (**aquí: mitigaciones aplicadas + retest**, no solo ideas)

Aspectos formales: Word/PDF, Arial 12 títulos / 11 cuerpo, interlineado 1,5, justificado, portada con integrantes, evidencias legibles.

El informe debe incorporar:

- Ajustes respecto de evaluaciones previas y feedback docente  
- Resultados de **pruebas de seguridad**  
- Resultados de **pruebas automatizadas**  
- **Mitigaciones** a defectos  
- Propuestas para preservar calidad y cumplimiento normativo/legal  

### 1.2 Defensa (presentación / video)

- ~10 minutos de exposición + ~5 de preguntas  
- Trabajo grupal; **nota individual** según dominio en la defensa  
- Material de apoyo (PPT + video) se prepara **después** del cierre operativo  

### 1.3 Rúbrica (indicadores relevantes)

| IE | Peso | Qué demostrar |
|----|------|----------------|
| IE1 | 30% | Enfoques/herramientas de seguridad y su función (ZAP, SQLMap, Sonar, fuerza bruta, etc.) |
| IE3 | 14% | Diagramas con controles de seguridad automatizados + criterio normativo/legal |
| IE5 | 24% | Automatización de pruebas (Selenium obligatorio; eficiencia/calidad) |
| IE7 | 20% | Plan de mantenimiento (calidad, seguridad, norma en el ciclo de vida) |
| IE9 | 12% | Documentación técnica clara (automatización + mejora continua) |

### 1.4 Pizarrón de clase (obligatorios operativos)

- Mitigar (no solo evidenciar)  
- ZAP · SonarQube · fuerza bruta · SQL injection · estrés (“DDoS” de laboratorio)  
- **Selenium obligatorio**  
- **JMeter / estrés hasta 5000 usuarios concurrentes**  
- Ampliar plan de pruebas si hace falta  
- Mitigar **al menos 5** defectos, **≥1 crítico**; más es mejor  
- Wireshark donde aporte evidencia de tráfico  

**Interpretación ética:** “DDoS” = prueba de **estrés/carga controlada** con JMeter sobre Docker local (no ataque a terceros).

---

## 2. Delta vs ciclos anteriores

| Antes (EV1–EV2 / EP3–EP4) | Ahora (EV5–6) |
|---------------------------|---------------|
| Descubrir, evidenciar, dictamen No certificado | **Mitigar** + retest + evidencias before/after |
| Selenium “plus” | Selenium **obligatorio** |
| JMeter ~70 VU + delay 5 s | JMeter **5000 VU** (tras quitar delay) |
| Recomendaciones en §6 | §6 con **correcciones realizadas** |
| Continuidad de roles EV2 | Misma dinámica (ver §4) |

Base reutilizable: [`../../EV3/EV3 Entrega`](../../EV3/EV3%20Entrega) y entregables EP3/EP4.

---

## 3. Mitigación acordada

### 3.1 Mínimo de examen (≥5, ≥1 crítico)

| # | INC | Severidad | Acción | Dueño |
|---|-----|-----------|--------|-------|
| 1 | **INC-01** | **Crítico** | bcrypt + política de clave | Nicolás |
| 2 | INC-02 | Grave | Secreto JWT solo en env | Nicolás |
| 3 | INC-03 | Grave | Logout que revoque token | Nicolás |
| 4 | INC-04 | Grave | Quitar `delayMiddleware(5000)` | Ari |
| 5 | INC-07 | Grave | `/roles` exige JWT + admin | Nicolás |

### 3.2 Meta de calidad (recomendado)

| INC | Acción | Dueño |
|-----|--------|-------|
| INC-13 | Auditar descargas de documentos | Nicolás |
| INC-14 | Restringir `POST /auditoria` | Nicolás |
| INC-05 | CORS acotado + cabeceras | Ari |
| INC-06 | No exponer `err.message` al cliente | Skarlett |

### 3.3 Ampliación de pruebas (pizarrón)

| Prueba | Herramienta | Dueño evidencia |
|--------|-------------|-----------------|
| UI automatizada | Selenium pytest/POM | Nicolás |
| Estrés 5000 VU | JMeter | Ari |
| Vulnerabilidades dinámicas | OWASP ZAP (antes/después + ≥1 solución) | Ari |
| SAST | SonarQube pre/post | Skarlett |
| SQL injection | SQLMap retest | Nicolás |
| Fuerza bruta / lockout | Script o herramienta + mitigación | Ari (± Nicolás código) |
| Tráfico | Wireshark Windows | Según caso |

---

## 4. Roles (continuidad)

| Integrante | Continuidad | Entregable operativo |
|------------|-------------|----------------------|
| **Nicolás** | Auth, sesión, RBAC, auditoría, Selenium, SQLMap | Fixes P0 auth/RBAC/audit + suite Selenium + Wireshark sesión |
| **Ari** | DAST, rendimiento, hashes, headers | INC-04, JMeter 5000, ZAP, John, fuerza bruta, Wireshark carga |
| **Skarlett** | SAST, config, errores, norma | Sonar, INC-06/CP-17, TLS/config, diagrama CI/CD seguridad |
| **Ninna** | Matriz, informe, dictamen, planillas | Planillas, KPIs, informe §1–6, dictamen; luego guion/PPT/video |

Detalle: [`00_Backlog_Equipo.md`](./00_Backlog_Equipo.md) y `*/BACKLOG.md`.

---

## 5. Estándares a citar (sin relleno)

- **ISO/IEC 25010** — calidad de producto (seguridad, desempeño, fiabilidad)  
- **ISO/IEC 27001** (enfoque controles) — secretos, acceso, registro, criptografía  
- **ISO/IEC/IEEE 29119** — diseño/ejecución/evidencia de pruebas  
- Leyes: **20.584**, **19.628**, **DS 41**; **21.719** como horizonte  

---

## 6. Criterios de entrada / salida del ciclo

**Entrada:** Docker FE `:3333` / API `:4444`; branch de trabajo; baseline de defectos EV2 conocida; este paquete de alineación leído.

**Salida (equipo):**

- ≥5 INC mitigados y retesteados (incluye INC-01)  
- Selenium ejecutado y archivado  
- JMeter con intento documentado a 5000 VU  
- Evidencias ZAP / Sonar / SQLMap / Wireshark según dueño  
- Planillas + informe §1–6 + material de defensa  

---

## 7. Nota sobre archivos mal etiquetados en EV5-6

Varios archivos del docente tienen extensión incorrecta (PDF que es DOCX/XLSX, XLSX que es imagen). Usar:

- Formato informe: contenido §1–6 (aunque el `.docx` sea PDF por dentro)  
- Planilla consolidado métricas: `.xlsx` válido  
- Matriz: plantilla `3.4.2` (XLSX mal nombrado) + matriz EV2  
- Pauta de evaluación: `EP6_...Presentación (1).pdf`  

---

## 8. Siguiente paso

1. Leer [`README.md`](./README.md)  
2. Revisar [`00_Backlog_Equipo.md`](./00_Backlog_Equipo.md)  
3. Abrir el `BACKLOG.md` de tu carpeta y ejecutar tus ítems  
