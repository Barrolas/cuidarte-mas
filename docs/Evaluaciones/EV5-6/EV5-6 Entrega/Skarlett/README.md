# Skarlett Tropan — EV5-6

**Rol:** SAST (SonarQube), errores y logs (INC-06 / CP-17), TLS / reposo / backup (CP-14, CP-16, CP-18), tabla normativa y diagrama CI/CD con controles de seguridad (con Ninna).

**Corte:** 27-nov-2026, America/Santiago.  
**Handoff:** empezar por [`HANDOFF_SKARLETT.md`](./HANDOFF_SKARLETT.md).

Arranque del laboratorio: Docker Compose (frontend `:3333`, API `:4444`, Postgres `:15442`).

| Documento | Uso |
|-----------|-----|
| [BACKLOG.md](./BACKLOG.md) | Checklist personal y estado de cada ítem |
| [HANDOFF_SKARLETT.md](./HANDOFF_SKARLETT.md) | Respuesta punto por punto a lo pedido por Ninna, con rutas |
| [Entregables/EV56-18-Retest-CP17-y-Sonar.md](./Entregables/EV56-18-Retest-CP17-y-Sonar.md) | Retest CP-17 + delta Sonar (el scan “final” post INC-01/02/07 sigue pendiente) |
| [Entregables/EV56-19-CP-14-16-18.md](./Entregables/EV56-19-CP-14-16-18.md) | Resultados y limitaciones de CP-14, CP-16 y CP-18 |
| [Entregables/EV56-Tabla-Normativa.md](./Entregables/EV56-Tabla-Normativa.md) | Artículo ↔ INC/CP |
| [Entregables/EV56-Plan-Mantenimiento.md](./Entregables/EV56-Plan-Mantenimiento.md) | Plan IE7/IE8 con residuales fechados |
| [Entregables/EV56-09-INC-06-Resumen-Bitacora.md](./Entregables/EV56-09-INC-06-Resumen-Bitacora.md) | Resumen y bitácora de INC-06 |
| [Planillas/EV56-21-Diagrama-CICD-Controles.md](./Planillas/EV56-21-Diagrama-CICD-Controles.md) | Pipeline propuesto (md + PNG + `security.yml`) |
| [Planillas/EV56-22-Matriz-Trazabilidad-Skarlett.xlsx](./Planillas/EV56-22-Matriz-Trazabilidad-Skarlett.xlsx) | Insumo de matriz (filas de Skarlett) |
| [Planillas/EV56-22-Registro-Casos-Skarlett.xlsx](./Planillas/EV56-22-Registro-Casos-Skarlett.xlsx) | Insumo del registro de casos |
| [Guion/EV56-25-Guion-Skarlett.md](./Guion/EV56-25-Guion-Skarlett.md) | Líneas habladas para láminas 9 y 10 del outline EP6 |
| [Evidencias/](./Evidencias/README.md) | Capturas, `curl`, JSON. **EV56-20 se conserva tal cual** |

Regla: no inventar números. Quality Gate en verde no significa producto seguro.
