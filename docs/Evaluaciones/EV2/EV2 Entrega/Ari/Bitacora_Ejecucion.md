# Bitácora de ejecución — Ari Araya (EP3)

**Rol:** QA de seguridad y rendimiento  
**Ambiente:** Docker local FE `:3333` / API `:4444` / Postgres `:15442` (26-10-2026: tres contenedores `healthy`)  
**Datos:** sintéticos `admin`/`admin`, `medico`/`medico`, `paciente`/`paciente`  
**Para:** Nicolás (§5.2, Tablas 21 y 22) y Giannina (integración del informe)  
**Evidencia canónica:** [`Evidencias/Evidencia_ARI.docx`](./Evidencias/Evidencia_ARI.docx) (36 figuras; las dos últimas son CP-19)

Estados: `Aprobado` | `Falla` | `Parcial` | `Bloqueado` | `No ejecutado`

---

## Resumen por caso (pasar a Nicolás)

| Fecha | CP | Ejecutor | Capa | Resultado | Evidencia | INC / BUG | Notas |
|-------|----|----------|------|-----------|-----------|-----------|-------|
| 2026-09-08 | CP-04 | Ari | DAST sin sesión | Falla* (hardening) | EV1 Anexos ZAP FE/API + GUI `feature/owasp-zap-ataque` | INC-05 | 0 High; Medium/Low de CSP, clickjacking, CORS, headers |
| 2026-10-26 | CP-04 | Ari | ZAP 2.17 activo autenticado | **Parcial** | Word fig. 9–13 (OpenAPI + reglas Bearer médico/paciente; escaneos 15:53 y 20:59) | — | **0 High**, 2 Medium, 4 Low. **No se exportó el reporte**; no se identifican las alertas. Tiempos ~5 s (INC-04). `POST /documentos` → 500 con ambos tokens |
| 2026-10-26 | CP-04 | Ari | Cabeceras (PowerShell + Swagger) | **Falla** | Word fig. 14–16 | INC-05 | API: `Access-Control-Allow-Origin: *`, `X-Powered-By: Express`, sin CSP/XFO/XCTO/HSTS. FE: `Server: nginx/1.31.8`. Solo `/docs` trae CSP (Swagger). Límite de intentos de login **no** se probó |
| 2026-10-26 | CP-04 / CP-17 | Ari | RBAC + IDOR (Swagger y PowerShell) | **Aprobado** | Word Tabla 3, fig. 17–28 | — | Paciente: GET ajeno 403, DELETE paciente/examen 403, POST examen 403, IDOR `/examenes/paciente/1` 200 `[]` vs `/2` 403. Médico: 200. Sin token: 401. Mensajes genéricos |
| 2026-10-20 | CP-04 | Nicolás | API SQLMap | Aprobado* (inyección login) | `Nicolas/Evidencias/CP-04/` | — | Ari no repite SQLMap |
| 2026-09-07 | CP-05 | Ari | JMeter EV1 | **Falla** | `EV1 Entrega/Anexos/jmeter/` | INC-04 | p95 GET ≈ 5008–5011 ms con delay |
| 2026-10-26 23:28 | CP-05 | Ari | JMeter 5.5 Docker `justb4/jmeter` | **Falla** | Word fig. 32–34; `Anexos/jmeter/EP3_CP05_con_delay.jtl` | INC-04 | Plan `CuidartePlus_CP05.jmx`. 220 samples / 59 s / 3,7 s⁻¹ / avg **2965 ms** / min 6 / max **5016 ms** / 0,00 % error. 70 VU (TG-A 20×2 + TG-B 50). NFR-PERF-1 no cumple |
| — | CP-05 | Ari | API sin delay | **No ejecutado** | — | INC-04 | Medición formal del umbral 300 ms. No bloquea el handoff |
| — | CP-13 | Ari | tiempo descarga | **No ejecutado** | formatos: Nicolás CP-13 | INC-15/16 | Dump con 0 exámenes / 0 documentos; hay que cargar uno sintético antes |
| 2026-10-26 | CP-15 | Ari | psql + John (Docker `ghcr.io/openwall/john`) | **Falla** | Word fig. 29–31; [`Evidencias/hashes.txt`](./Evidencias/hashes.txt) | INC-01, INC-10 | `\d usuarios`: `contrasena text`. Valores `admin`/`medico`/`paciente`. John: **No password hashes loaded**. Login 200 confirma el texto plano |
| 2026-10-26 | CP-17 | Ari | INC-06 runtime | **No demostrado** | Word fig. 12–13 (500 sin cuerpo); código `glosa: err.message` | INC-06 | El recorte IDOR/RBAC **aprobó**. El 500 de `POST /documentos` (Multer antes del rol) no se inspeccionó. No cerrar INC-06 |
| 2026-10-27 | CP-19 | Ari | Lighthouse + JMeter `CP19_200u.jmx` | **Falla** | Word fig. 35–36; [`Evidencias/CP-19-lighthouse-43.png`](./Evidencias/CP-19-lighthouse-43.png); [`Evidencias/CP-19-jmeter-powershell.png`](./Evidencias/CP-19-jmeter-powershell.png); `Anexos/jmeter/EP3_CP19.jtl` | INC-04 | Lighthouse Performance **43** en `:3333`. JMeter: 520 muestras, avg **3374 ms**, p95 **5024 ms**, max 74460 ms, pico **52** hilos, 0 % error. NFR-PERF-2 y NFR-PERF-3 no cumplen. El plan declara 200 VU en TG-B; el `.jtl` no muestra 200 concurrentes |
| 2026-10-26 | CP-21 | Ari | config Docker | **Falla** | [`CP-21_Disponibilidad.md`](./CP-21_Disponibilidad.md); Word fig. 1–3 | **INC-17** | El Word aún lo listaba [Pendiente]; la revisión documental **sí** está hecha. Sin SLO 99,5 %, sin runbook |

\* = cumple una parte del criterio y falla otra.

## Observaciones (no son INC nuevos)

1. **400 antes de 403.** `POST /examenes` y `PUT /pacientes/:id` validan Yup **antes** de `requireRole`. Token de paciente + cuerpo inválido → 400. Con cuerpo válido → 403 (fig. 25). No es fuga.
2. **JWT 2 h.** `exp − iat = 7200` (`auth.js` `expiresIn: "2h"`). Pasar a Nicolás para CP-07 / INC-03.
3. **Mensaje 401.** Sin token, `GET /examenes` responde «Token inválido». Detalle de texto, no de seguridad.
4. **Herramientas de API y cabeceras.** Swagger Authorize y PowerShell. No se usó Burp Suite ni Nikto.

## Bloqueos de ambiente (para no mezclar con Falla de producto)

Si al ejecutar aparece `relation "usuarios" does not exist`:

- Causa: `init-db.sh` con CRLF (`/bin/bash^M`) → dump no cargado; el volumen queda vacío.  
- Estado de login/API: **Bloqueado**, no “credencial incorrecta”.  
- Arreglo: `docker compose down -v`, pasar `BACKEND/sql/init-db.sh` a LF, `docker compose up -d`.  
- El 26-10 **no** ocurrió: login médico y paciente = 200.

## Bugs / INC de este paquete

| ID | CP | Severidad | Descripción | Evidencia |
|----|----|-----------|-------------|-----------|
| INC-01 | CP-15 | **Crítico** | Contraseñas en texto plano; John no carga hashes | Word fig. 29–31 |
| INC-04 | CP-05 | **Grave** | `delayMiddleware(5000)`; max 5016 ms | Word fig. 3, 32–34; `.jtl` |
| INC-05 | CP-04 | **Moderado** | CORS `*` + sin cabeceras + `X-Powered-By` / `Server` | Word fig. 14–16 |
| INC-06 | CP-17 | **Moderado** | `glosa: err.message` en `catch`; 500 de documentos sin body capturado | código + Word fig. 12–13 |
| INC-10 | CP-15 | **Grave** (con INC-01) | Seed `admin`/`admin`, `medico`/`medico`, `paciente`/`paciente` | login 200; `hashes.txt` |
| **INC-17** | CP-21 | **Moderado** | DIS-1/DIS-2 no demostrables en Compose | `CP-21_Disponibilidad.md` |

No se abre BUG-001 por hallazgos ya cubiertos por INC-01…16. INC-17 es el único ID nuevo. Si Giannina prefiere BUG-001 para CP-21, unificar en el Word del informe.

## Firmas

| Oleada | Fecha | Comentario |
|--------|-------|------------|
| EV1 DAST + JMeter | 2026-09-07/08 | Línea base |
| Ciclo 2 ejecución | 2026-10-26 / 27 | ZAP auth, Swagger y PowerShell, John, JMeter CP-05 y CP-19, CP-21 |
