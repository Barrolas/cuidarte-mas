# Ninna / Giannina Guerrero — EV5-6 (aporte QA Lead)

**Rol:** matriz, planillas, KPIs, informe §1–6, dictamen, integración de handoffs; luego guion/PPT/video.

## Word oficiales (mismo formato que EV2)

Paquete espejo de `EV2 Contexto` → [`../../EV5-6 Contexto/`](../../EV5-6%20Contexto/):

| Orden | Archivo | Estado 2026-11-25 |
|-------|---------|-------------------|
| 0 | [`00-Handoff-para-el-equipo.docx`](../../EV5-6%20Contexto/00-Handoff-para-el-equipo.docx) | Traspaso al equipo |
| 1 | [`01-Inventario-INC-y-KPIs.docx`](../../EV5-6%20Contexto/01-Inventario-INC-y-KPIs.docx) | INC + plantilla G1–G6 |
| 2 | [`02-Matriz-trazabilidad-40-ERS.docx`](../../EV5-6%20Contexto/02-Matriz-trazabilidad-40-ERS.docx) | 40 filas; EV2 cargado; EV5-6 pendiente salvo INC-04 |
| E | [`Entregables/EP5-Informe-Cuidarte-Mas-borrador.docx`](../../EV5-6%20Contexto/Entregables/EP5-Informe-Cuidarte-Mas-borrador.docx) | Portada EP3-style; §1–§3; huecos handoff |
| E | [`Entregables/Guion-presentacion-EP6-Cuidarte.docx`](../../EV5-6%20Contexto/Entregables/Guion-presentacion-EP6-Cuidarte.docx) | Outline EP6 (frases al congelar) |
| E | [`EV5-6 Contexto/.../presentacion-ep6/index.html`](../../EV5-6%20Contexto/Entregables/presentacion-ep6/index.html) | Deck HTML (base EP4 → ciclo MITIGAR) |

Hay **PDF** junto a cada Word. Copia en [`Entregables/`](./Entregables/).

## Fuentes editables (Markdown / CSV)

| Archivo | Para qué |
|---------|----------|
| [`BACKLOG.md`](./BACKLOG.md) | Checklist personal |
| [`Entregables/01-Informe-EP5-borrador.md`](./Entregables/01-Informe-EP5-borrador.md) | Texto base del informe |
| [`Entregables/02-Evaluacion-contra-Guia-Unificada.md`](./Entregables/02-Evaluacion-contra-Guia-Unificada.md) | Evaluación vs guía |
| [`Planillas/EV56-22-Matriz-40-ERS-ciclo3.csv`](./Planillas/EV56-22-Matriz-40-ERS-ciclo3.csv) · [`EV56-22-Matriz-Trazabilidad.xlsx`](./Planillas/EV56-22-Matriz-Trazabilidad.xlsx) | Datos de la matriz |
| [`Planillas/EV56-22-Registro-Casos-Seguimiento.xlsx`](./Planillas/EV56-22-Registro-Casos-Seguimiento.xlsx) | Registro CP (plantilla docente llenada) |
| [`Planillas/EV56-22-Inventario-INC.md`](./Planillas/EV56-22-Inventario-INC.md) | Estados INC |
| [`Planillas/EV56-22-KPIs.md`](./Planillas/EV56-22-KPIs.md) | KPIs G1–G6 |
| [`Planillas/EV56-21-Diagrama-CICD-borrador.md`](./Planillas/EV56-21-Diagrama-CICD-borrador.md) | CI/CD borrador (Skarlett completa) |
| [`Guion/EV56-25-Outline-EP6.md`](./Guion/EV56-25-Outline-EP6.md) | Outline guion |
| [`Entregables/00-Checklist-handoff.md`](./Entregables/00-Checklist-handoff.md) | Qué pedir el vie 27 |

Regenerar Word tras editar fuentes:

```bash
python "docs/Evaluaciones/EV5-6/EV5-6 Contexto/_generar_formato_ev2.py"
```

## Continuidad EV3

Los ítems EV3-21…25 equivalen a EV56-22…25. El paquete vivo del examen es **EV5-6**.

## Regla

No inventar resultados de Selenium, JMeter, Sonar ni ZAP. Solo rellenar cuando exista path en bitácora del dueño.
