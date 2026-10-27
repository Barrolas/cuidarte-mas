# Handoff para Nicolás — filas §5.2 / Tablas 21 y 22

Copiá o fusioná estas filas en `Nicolas/Bitacora_Ejecucion.md`.  
Ejecutor de estas filas: **Ari Araya**.

| Fecha | CP | Resultado | Evidencia | INC / BUG |
|-------|----|-----------|-----------|-----------|
| 2026-09-08 | CP-04 (ZAP baseline) | Falla* headers/CORS | `docs/Evaluaciones/EV1/EV1 Entrega/Anexos/OWASP_ZAP_*` | INC-05 |
| 2026-09-07 | CP-05 | Falla | `Anexos/jmeter/` (p95 ~5 s) | INC-04 |
| 2026-10-26 | CP-15 | Falla | auth.js + dump | INC-01, INC-10 |
| 2026-10-26 | CP-17 | Falla | `glosa: err.message` | INC-06 |
| 2026-10-26 | CP-21 | Falla | `Ari/CP-21_Disponibilidad.md` | INC-17 |
| — | CP-04 ZAP auth / Burp / Nikto | No ejecutado | — | — |
| — | CP-05 sin delay | No ejecutado | — | INC-04 |
| — | CP-13 tiempo ≤10 s | No ejecutado | — | — |
| — | CP-19 | No ejecutado | — | — |

Para Tablas 21 y 22 (conteos):

- **Ejecutados (Ari, con evidencia):** CP-04 parcial, CP-05 (con delay), CP-15, CP-17 (código), CP-21  
- **Fallidos:** CP-05, CP-15, CP-17, CP-21; CP-04 falla en hardening / no cubre auth  
- **No ejecutados:** ZAP autenticado, CP-05 sin delay, CP-13 tiempo, CP-19  
- **Bloqueados:** 0 (salvo que el dump siga roto al reintentar login)

Detalle y notas: [`Bitacora_Ejecucion.md`](./Bitacora_Ejecucion.md).
