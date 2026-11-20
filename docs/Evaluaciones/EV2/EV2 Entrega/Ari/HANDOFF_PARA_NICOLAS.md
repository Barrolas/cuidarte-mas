# Handoff definitivo para Nicolás — filas §5.2 / Tablas 21 y 22

Copiá o fusioná estas filas en `Nicolas/Bitacora_Ejecucion.md`.  
Ejecutor: **Ari Araya**. Evidencia canónica del 26-10-2026: [`Evidencias/EV2_Ari_Pruebas_Seguridad_Rendimiento.docx`](./Evidencias/EV2_Ari_Pruebas_Seguridad_Rendimiento.docx).

**No se usó Burp Suite ni Nikto.** Las peticiones y las cabeceras se probaron con Swagger y PowerShell.

| Fecha | CP | Resultado | Evidencia | INC / BUG |
|-------|----|-----------|-----------|-----------|
| 2026-09-08 | CP-04 (ZAP baseline, sin sesión) | Falla* headers/CORS | EV1 `Anexos/OWASP_ZAP_*` | INC-05 |
| 2026-10-26 | CP-04 (ZAP activo autenticado, médico + paciente) | Parcial: 0 High; 2 Medium / 4 Low **sin reporte exportado** | Word fig. 9–13 | (detalle → INC-05 si son headers) |
| 2026-10-26 | CP-04 (cabeceras; PowerShell) | **Falla** | Word fig. 14–16 | INC-05 |
| 2026-10-26 | CP-04 / CP-17 (RBAC + IDOR; Swagger y PowerShell) | **Aprobado** (ese recorte) | Word Tabla 3, fig. 17–28 | — |
| 2026-10-20 | CP-04 (SQLMap) | Aprobado* (Nicolás) | `Nicolas/Evidencias/CP-04/` | — |
| 2026-09-07 / 2026-10-26 | CP-05 con delay | **Falla** | EV1 JMeter + Word fig. 32–34; `EP3_CP05_con_delay.jtl` (220 samples, avg 2965 ms, max 5016 ms, 0 % error) | INC-04 |
| 2026-10-26 | CP-15 (John + psql) | **Falla** | Word fig. 29–31; [`Evidencias/hashes.txt`](./Evidencias/hashes.txt) | INC-01, INC-10 |
| 2026-10-26 | CP-17 INC-06 (`glosa` en 500) | **No demostrado en runtime** | código `glosa: err.message`; ZAP 500 en `POST /documentos` sin cuerpo | INC-06 |
| 2026-10-26 | CP-21 | **Falla** | [`CP-21_Disponibilidad.md`](./CP-21_Disponibilidad.md); Word fig. 1–3 (compose up) | INC-17 |
| — | CP-05 sin delay | No ejecutado | — | INC-04 |
| — | CP-13 tiempo ≤10 s | No ejecutado | 0 exámenes/documentos en el dump | — |
| 2026-10-27 | CP-19 Lighthouse + JMeter | **Falla** | Word fig. 35–36; `EP3_CP19.jtl` (520 muestras, p95 5024 ms, pico 52 hilos); Lighthouse 43 | INC-04 |

Para Tablas 21 y 22 (conteos **de Ari**):

- **Ejecutados con evidencia:** CP-04 (parcial: baseline + auth + cabeceras + IDOR), CP-05 con delay, CP-15, CP-17 recorte RBAC/IDOR, CP-19, CP-21  
- **Fallidos:** CP-04 hardening (INC-05), CP-05 con delay (INC-04), CP-15 (INC-01), CP-19 (NFR-PERF-2/3), CP-21 (INC-17)  
- **Aprobados (recorte):** RBAC/IDOR paciente (escrituras 403, IDOR 403, sin token 401)  
- **No ejecutados (no bloquean):** CP-05 sin delay, CP-13 tiempos, reporte ZAP HTML, cuerpo del 500 de documentos 
- **Bloqueados:** 0 (login `medico`/`paciente` = 200 el 26-10)

Dato para **tu** CP-07 / INC-03: JWT `expiresIn: "2h"` (`exp − iat = 7200`). Lo midió Ari en el login Swagger; no lo dupliques como hallazgo de Ari.

Observación (no es INC nuevo): con cuerpo inválido la API responde **400 antes de revisar el rol** (`validate` Yup delante de `requireRole`). Con cuerpo válido el paciente sí recibe 403.

Detalle: [`Bitacora_Ejecucion.md`](./Bitacora_Ejecucion.md).
