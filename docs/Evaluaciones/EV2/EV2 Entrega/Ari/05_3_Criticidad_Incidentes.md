# §5.3 — Criticidad de incidentes (propuesta Ari)

Escala del informe: **Crítico / Grave / Moderado / Leve**.  
Criterio de lectura (equipo): la severidad la sube el **dato afectado** (ficha clínica, Ley 20.584 / DS 41).

**Decisión INC-09:** se **acepta la propuesta de Giannina**. INC-09 pasa de Moderado a **Grave**.  
`DELETE FROM usuarios` (`users.js` ~L574) y `DELETE FROM examen_medico` (`examenes.js` ~L408) son **borrado físico**, no baja lógica. DS 41 arts. 11–12 y Ley 20.584 art. 13 exigen conservación de ficha (~15 años). Un delete irreversible sobre datos de salud no es un defecto “de UX”.

**BUG-xxx:** no se abre BUG-001 por hallazgos ya cubiertos por INC-01…16. El único ID nuevo de este paquete es **INC-17** (CP-21).

Evidencia de ejecución Ari (26-10-2026): `Evidencias/EV2_Ari_Pruebas_Seguridad_Rendimiento.docx`.

---

## Tabla para el informe

| ID | Título corto | Severidad final | Evidencia / CP | BUG | Notas Ari (26-10) |
|----|--------------|-----------------|----------------|-----|-------------------|
| INC-01 | Contraseñas en texto plano | **Crítico** | CP-15; `auth.js` L21, L110; John *No password hashes loaded*; Word fig. 29–31 | — | Impide certificar. Columna `contrasena text`; valores = usuario |
| INC-02 | JWT_SECRET en repo / fallback `inseguro` | **Grave** | README, `.env`, rutas JWT | — | Código; no reejecutado el 26-10 |
| INC-03 | Logout no invalida JWT | **Grave** | Nicolás CP-07 | — | Ari midió `exp − iat = 7200` (2 h). Pasar a Nicolás |
| INC-04 | `delayMiddleware(5000)` | **Grave** | CP-05 JMeter 26-10: 220 samples, avg 2965 ms, max 5016 ms, 0 % error | — | NFR-PERF-1 no cumple **con** delay. Sin delay: no ejecutado |
| INC-05 | CORS abierto + headers ausentes | **Moderado** | CP-04 curl fig. 14–16; ZAP auth 0 High | — | `Access-Control-Allow-Origin: *`, `X-Powered-By: Express`, `Server: nginx/1.31.8`. Límite de login no probado |
| INC-06 | Errores 500 con `err.message` en `glosa` | **Moderado** | CP-17 código; ZAP 500 `POST /documentos` **sin cuerpo** | — | **No cerrado.** RBAC/IDOR del mismo CP **aprobó** |
| INC-07 | `/roles` sin control de rol | **Grave** | `roles.js` L18–90; CP-08 | — | |
| INC-08 | *(confirmar texto con Giannina)* | — | — | — | No reasignar sin la ficha del avance |
| INC-09 | Borrado físico de usuario/examen | **Grave** | `users.js` L571–589; `examenes.js` DELETE | — | **Sube a Grave** (DS 41 arts. 11–12) |
| INC-10 | Política de clave / seed trivial | **Grave** (junto a INC-01) | dump; login 200 `medico`/`medico` | — | Confirmado 26-10 |
| INC-11 | Dependencias vulnerables (npm audit) | **Moderado** | build backend | — | Skarlett/Sonar si hay cifra |
| INC-12 | *(confirmar texto con Giannina)* | — | — | — | |
| INC-13 | Descarga sin auditoría | **Grave** | Nicolás CP-03 | — | DS 41 art. 9 |
| INC-14 | `POST /auditoria` abierto | **Grave** | Nicolás CP-03 | — | |
| INC-15 | DOC/PPT rechazados (ERS RF-4.3) | **Moderado** | Nicolás CP-13 | — | |
| INC-16 | Documentos en bytea vs storage | **Moderado** | Nicolás CP-13 | — | |
| **INC-17** | DIS-1/2 no demostrables | **Moderado** | CP-21 Ari | — | Nuevo; o BUG-001 si el Word del informe no admite INC-17 |

## Qué no es BUG nuevo

- ZAP/curl de headers (`X-Powered-By`, CORS, CSP) → **INC-05**.  
- John sobre texto plano → **INC-01**, no un BUG de “John falló”.  
- 400 antes de 403 por Yup → observación de orden de validación, no INC.  
- JWT de 2 h → **INC-03** (Nicolás), no hallazgo duplicado de Ari.

Controles que **sí** funcionan (informar en 5.2): el backend rechaza escrituras del paciente (403), el IDOR de exámenes/pacientes ajenos (403) y las peticiones sin token (401).

## Dictamen (alineado a la presentación)

Mientras **INC-01** esté abierto: **No certificado**.  
Camino a “Certificado con reservas”: cerrar INC-01, INC-02 e INC-07 y plan con fechas para el resto de graves (incluye INC-09).
