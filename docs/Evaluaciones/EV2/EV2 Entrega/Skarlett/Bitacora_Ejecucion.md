# Bitácora de ejecución — Skarlett Tropan (CP-17)

**Rol:** QA de calidad y normativa técnica  
**Caso:** CP-17 — Gestión de log y manejo de errores sin fuga de información  
**ERS:** NFR-SEG-6  
**Ambiente de código:** rama `main` (`BACKEND/src`, `FRONTEND/src`)  
**Ambiente dinámico (Ari):** Docker local FE `:3333` / API `:4444`, 26 de octubre de 2026  
**Datos:** sintéticos `admin` / `medico` / `paciente`

Estados: `Aprobado` | `Falla` | `Parcial` | `Bloqueado` | `No ejecutado`

---

## Resumen

| Fecha | CP | Capa | Resultado | Evidencia | INC / BUG | Notas |
|-------|----|------|-----------|-----------|-----------|-------|
| 2026-10-20 | CP-17 | estática (SonarQube) | Falla* | `Entregables/capturas-sonar/`; informe §5.4 | INC-06 no marcado por el escáner | 0 Security Hotspots. Community Build no vio `glosa: err.message`. Sí marcó la divulgación de versión en `app.js` (Low). |
| 2026-10-27 | CP-17 | revisión manual | **Falla** | `BACKEND/src/app.js`, `BACKEND/src/routes/*.js` | INC-06 | 34 `catch` responden `glosa: err.message` y hacen `console.error(err)`. `morgan("dev")` en el acceso. |
| 2026-10-20 | CP-17 / CP-03 | API (Nicolás) | Falla | `Nicolas/Bitacora_Ejecucion.md`, `Evidencias/CP-03/` | INC-14 | `POST /auditoria` con token de médico → 201. El `GET` sí exige admin. |
| 2026-10-26 | CP-17 | dinámica (Ari, equiv. Burp) | Parcial | Rama `feature/ari-ep3-qa-seguridad`, commit `785062d`; Word fig. 12–13 y 17–28 | INC-06 no cerrado en runtime | 401/403 con mensaje genérico: cumple. `POST /documentos` → 500 y el cuerpo no se guardó. |

\* El Quality Gate figura Passed porque mide código nuevo. Sobre el código total, la seguridad del backend es E. Eso no cumple NFR-SEG-6.

**Resultado del caso:** **Fallido** (27 de octubre de 2026).

## Incidentes de este caso

| ID | ¿Confirmado? | Severidad (informe) | Evidencia |
|----|--------------|---------------------|-----------|
| INC-06 | Sí en el código. La reproducción del cuerpo HTTP 500 sigue abierta. | Moderado | 34 `catch` en 8 rutas. Ari no archivó el body del 500. CP-20 no lo vio: el 401 de login es genérico. |
| INC-14 | Sí | Moderado | Nicolás, 20 de octubre de 2026. `audit.js` inserta con cualquier token válido. |
| INC-11 | No ejecutado | Grave | SonarQube omitió dependencias. `npm` no está en el PATH de este equipo. No se inventan CVE. |

## Firmas

| Pasada | Fecha | Comentario |
|--------|-------|------------|
| SonarQube | 2026-10-20 | Ya integrada en el informe §5.4. |
| Burp / curl (Ari) | 2026-10-26 | Traída desde `feature/ari-ep3-qa-seguridad`. |
| Cierre Skarlett | 2026-10-27 | Revisión manual sobre `main` + cruce con Nicolás y Ari. |
