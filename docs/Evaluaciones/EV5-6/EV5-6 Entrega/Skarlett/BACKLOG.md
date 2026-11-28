# BACKLOG — Skarlett Tropan (EV5-6)

**Rol:** SAST (SonarQube), errores/logs (CP-17), configuración TLS/backup, lectura normativa, apoyo diagrama CI/CD con controles de seguridad.  
**Tablero:** [`../00_Backlog_Equipo.md`](../00_Backlog_Equipo.md)  
**Análisis:** [`../00_Analisis_Encargo_Final.md`](../00_Analisis_Encargo_Final.md)  
**Handoff a Ninna:** [`HANDOFF_SKARLETT.md`](./HANDOFF_SKARLETT.md)

Estándares: **25010**, **27001**, Leyes **19.628**, **20.584**, **DS 41**.

Corte de este paquete: **27-nov-2026**, America/Santiago. Rama de docs: `skarlett/ev56-handoff` (base `origin/main` `d5829ed`, porque el paquete de Ninna solo está en `main`).

---

## Checklist

- [x] EV56-09 INC-06 sin fuga de errores — verificado en `origin/dev` `5707693` (PR #6/#7)
- [x] EV56-20 CP-17 retest — PASA con observaciones (evidencia en `Evidencias/EV56-20/`, sin alterar)
- [x] EV56-18 Sonar post-fix sobre `origin/dev` `5707693` (INC-04/05/06). **Pendiente** un re-scan cuando Nicolás mergee INC-01, INC-02 e INC-07
- [x] EV56-19 CP-14 / 16 / 18 — ejecutados 25-nov; fallidos o parciales con plan fechado
- [x] EV56-21 Diagrama CI/CD + controles (con Ninna) — propuesta IE7; el repo aún no tiene GitHub Actions
- [x] Tabla normativa → estado
- [x] Handoff a Ninna

---

## EV56-09 — INC-06 no exponer `err.message`

**Estado:** Verificado (retest). Severidad según inventario de Ninna: **Grave**.  
Helper `BACKEND/src/utils/httpErrors.js`. Bitácora: [`Entregables/EV56-09-INC-06-Resumen-Bitacora.md`](./Entregables/EV56-09-INC-06-Resumen-Bitacora.md).

## EV56-20 — Retest CP-17

**Estado:** Paso con observaciones. Evidencia intacta: [`Evidencias/EV56-20/`](./Evidencias/EV56-20/README.md). Pendiente de observación: INC-14 (Nicolás) e INC-11 (`npm audit`).

## EV56-18 — SonarQube post-mitigación

**Estado:** Ejecutado 27-nov ~22:00 America/Santiago sobre `origin/dev` `5707693`. Backend: 4→2 vulnerabilidades; Security sigue **E**. Frontend sin cambio (14 bugs, Security A). Falta la corrida posterior a INC-01/02/07.

## EV56-19 — CP-14 TLS / CP-16 reposo / CP-18 backup

**Estado:** CP-14 Fallido con reserva (plan 15-dic-2026). CP-16 Fallido / INC-16 (plan 15-dic-2026). CP-18 Fallido / Parcial con reserva (plan 20-dic-2026).

## EV56-21 — Diagrama CI/CD con controles de seguridad (IE3)

**Estado:** Diagrama + leyenda + `security.yml` de propuesta. Hoy el laboratorio es Docker manual; no hay workflow activo.

## Tabla normativa y handoff

Ver [`Entregables/EV56-Tabla-Normativa.md`](./Entregables/EV56-Tabla-Normativa.md) y [`HANDOFF_SKARLETT.md`](./HANDOFF_SKARLETT.md).
