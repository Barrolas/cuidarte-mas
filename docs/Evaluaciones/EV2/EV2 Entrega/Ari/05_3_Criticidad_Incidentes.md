# §5.3 — Criticidad de incidentes (propuesta Ari)

Escala del informe: **Crítico / Grave / Moderado / Leve**.  
Criterio de lectura (equipo): la severidad la sube el **dato afectado** (ficha clínica, Ley 20.584 / DS 41).

**Decisión INC-09:** se **acepta la propuesta de Giannina**. INC-09 pasa de Moderado a **Grave**.  
`DELETE FROM usuarios` (`users.js` ~L574) y `DELETE FROM examen_medico` (`examenes.js` ~L408) son **borrado físico**, no baja lógica. DS 41 arts. 11–12 y Ley 20.584 art. 13 exigen conservación de ficha (~15 años). Un delete irreversible sobre datos de salud no es un defecto “de UX”.

**BUG-xxx:** no se abre BUG-001 por hallazgos ya cubiertos por INC-01…16. El único ID nuevo de este paquete es **INC-17** (CP-21).

---

## Tabla para el informe

| ID | Título corto | Severidad final | Evidencia / CP | BUG | Notas Ari |
|----|--------------|-----------------|----------------|-----|-----------|
| INC-01 | Contraseñas en texto plano | **Crítico** | CP-15, CP-01; `auth.js` L21, L110 | — | Impide certificar (regla 2.4.2 / pentest sin críticos) |
| INC-02 | JWT_SECRET en repo / fallback `inseguro` | **Grave** | README, `.env`, rutas JWT | — | |
| INC-03 | Logout no invalida JWT | **Grave** | Nicolás CP-07 | — | Confirmado por él |
| INC-04 | `delayMiddleware(5000)` | **Grave** | CP-05 JMeter EV1 | — | p95 ~5 s; PERF-1 no cumple con delay |
| INC-05 | CORS abierto + headers ausentes | **Moderado** | ZAP EV1 / GUI Ari | — | 0 High de inyección en baseline |
| INC-06 | Errores 500 con `err.message` en `glosa` | **Moderado** | CP-17 (código) | — | |
| INC-07 | `/roles` sin control de rol | **Grave** | `roles.js` L18–90; CP-08 | — | Cualquier token (o ninguno, si no se exige) opera CRUD de roles |
| INC-08 | *(confirmar texto con Giannina)* | — | — | — | No reasignar sin la ficha del avance |
| INC-09 | Borrado físico de usuario/examen | **Grave** | `users.js` L571–589; `examenes.js` DELETE | — | **Sube a Grave** (DS 41 arts. 11–12) |
| INC-10 | Política de clave / seed trivial | **Grave** (junto a INC-01) | dump `admin`/`admin`; CP-09/15 | — | |
| INC-11 | Dependencias vulnerables (npm audit) | **Moderado** | build backend (multer 1.x, etc.) | — | Skarlett/Sonar si hay cifra |
| INC-12 | *(confirmar texto con Giannina)* | — | — | — | |
| INC-13 | Descarga sin auditoría | **Grave** | Nicolás CP-03 | — | DS 41 art. 9 |
| INC-14 | `POST /auditoria` abierto | **Grave** | Nicolás CP-03 | — | |
| INC-15 | DOC/PPT rechazados (ERS RF-4.3) | **Moderado** | Nicolás CP-13 | — | |
| INC-16 | Documentos en bytea vs storage | **Moderado** | Nicolás CP-13 | — | |
| **INC-17** | DIS-1/2 no demostrables | **Moderado** | CP-21 Ari | — | Nuevo; o BUG-001 si el Word no admite INC-17 |

## Qué no es BUG nuevo

ZAP sin sesión (CSP, clickjacking, `X-Powered-By`) se agrupa en **INC-05**, no en BUG-002…N.

## Dictamen (alineado a la presentación)

Mientras **INC-01** esté abierto: **No certificado**.  
Camino a “Certificado con reservas”: cerrar INC-01, INC-02 e INC-07 y plan con fechas para el resto de graves (incluye INC-09).
