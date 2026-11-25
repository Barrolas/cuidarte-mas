# EV5-6 Contexto (formato EV2)

Misma estructura y estilo que `docs/Evaluaciones/EV2/EV2 Contexto`:

| Archivo | Equivalente EV2 |
|---------|-----------------|
| `00-Handoff-para-el-equipo.docx` (+ PDF) | Traspaso al equipo |
| `01-Inventario-INC-y-KPIs.docx` (+ PDF) | Insumo §§5.1 / 5.3 (nuevo en este ciclo) |
| `02-Matriz-trazabilidad-40-ERS.docx` (+ PDF) | Matriz 40 ERS con Resultado EV2 + EV5-6 |
| `Entregables/EP5-Informe-Cuidarte-Mas-borrador.docx` (+ PDF) | Como `EP3-Informe-…` |
| `Entregables/Guion-presentacion-EP6-Cuidarte.docx` (+ PDF) | Como `Guion-presentacion-EP4-…` |

**Formato:**
- Contexto `00`–`02`: Arial, título 18 pt, subtítulo 10 pt, tablas con borde (como los Word numerados de EV2).
- **Informe EP5:** clona el `.docx` del EP3 (Arial 11 por defecto, márgenes, pie, portada N° + título 24 pt + tabla Asignatura/Integrantes) y usa el **índice del formato oficial EP5** (secciones 1–6, con *Propuesta de mejora*).
- **Guion EP6:** clona el guion EP4.
- **Presentación EP6:** `Entregables/presentacion-ep6/index.html` (misma base visual que EP4; 13 láminas del ciclo MITIGAR).

Los Markdown/CSV de trabajo siguen en `EV5-6 Entrega/Ninna/` (Planillas, borrador `.md`).  
Hay copia espejo de los Word/PDF en `EV5-6 Entrega/Ninna/Entregables/`.

Para regenerar tras editar fuentes:

```bash
python "docs/Evaluaciones/EV5-6/EV5-6 Contexto/_generar_formato_ev2.py"
```
