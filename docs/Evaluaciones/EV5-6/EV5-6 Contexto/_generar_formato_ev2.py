# -*- coding: utf-8 -*-
"""Genera Word de EV5-6 con el mismo formato visual que EV2 Contexto."""
from __future__ import annotations

import csv
import re
import shutil
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, Twips

ROOT = Path(__file__).resolve().parents[1]
NINNA = ROOT / "EV5-6 Entrega" / "Ninna"
CONTEXTO = Path(__file__).resolve().parent
ENTREGABLES = CONTEXTO / "Entregables"
NINNA_ENT = NINNA / "Entregables"

FONT = "Arial"  # mismo default del informe EP3 / formato docente
TOKEN = re.compile(r"(\*\*[^*]+\*\*|`[^`]+`)")
EP3_PLANTILLA = (
    ROOT.parent
    / "EV2"
    / "EV2 Contexto"
    / "Entregables"
    / "EP3-Informe-Cuidarte-Mas-avance.docx"
)
EP4_GUION_PLANTILLA = (
    ROOT.parent
    / "EV2"
    / "EV2 Contexto"
    / "Entregables"
    / "Guion-presentacion-EP4-Cuidarte.docx"
)


def set_run_font(run, size=11, bold=False, italic=False, name=FONT):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic


def setup_doc(doc: Document, narrow=False):
    for section in doc.sections:
        section.page_width = Twips(11906)  # A4-ish like EV2 (~21cm)
        section.page_height = Twips(16838)
        m = Cm(2.0) if narrow else Cm(2.5)
        section.top_margin = m
        section.bottom_margin = m
        section.left_margin = m
        section.right_margin = m
    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(11)
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15
    for level, size in [(1, 14), (2, 12), (3, 11)]:
        h = doc.styles[f"Heading {level}"]
        h.font.name = FONT
        h.font.size = Pt(size)
        h.font.bold = True
        h._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)


def add_title(doc, text, size=18):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    set_run_font(run, size=size, bold=True)
    return p


def add_subtitle(doc, text, size=10):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(10)
    run = p.add_run(text)
    set_run_font(run, size=size, italic=False)
    return p


def add_body(doc, text, size=11, justify=True, bold=False):
    p = doc.add_paragraph()
    if justify:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    add_inline(p, text, size=size, force_bold=bold)
    return p


def add_inline(paragraph, text, size=11, force_bold=False):
    for part in TOKEN.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            set_run_font(run, size=size, bold=True)
        elif part.startswith("`") and part.endswith("`"):
            run = paragraph.add_run(part[1:-1])
            set_run_font(run, size=size, italic=True)
        else:
            run = paragraph.add_run(part)
            set_run_font(run, size=size, bold=force_bold)


def add_bullet(doc, text, size=10):
    p = doc.add_paragraph(style="List Bullet")
    add_inline(p, text, size=size)
    return p


def add_heading(doc, text, level=1):
    return doc.add_heading(text, level=level)


def style_table(table, header=True, size=9):
    table.style = "Table Grid"
    for i, row in enumerate(table.rows):
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.space_before = Pt(2)
                for run in p.runs:
                    set_run_font(run, size=size, bold=(header and i == 0))


def fill_table(doc, headers, rows, size=9):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    for j, h in enumerate(headers):
        t.rows[0].cells[j].text = h
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            t.rows[i + 1].cells[j].text = "" if val is None else str(val)
    style_table(t, size=size)
    doc.add_paragraph("")
    return t


def mirror_to_ninna(path: Path) -> None:
    """Copia a Ninna/Entregables; si el archivo está abierto en Word, avisa y sigue."""
    mirror = NINNA_ENT / path.name
    try:
        shutil.copy2(path, mirror)
    except PermissionError:
        print(f"AVISO: no pude copiar a Ninna (archivo abierto): {mirror.name}")


def save_and_mirror(doc, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(path)
    if path.parent == ENTREGABLES or path.name.startswith(("00-", "01-", "02-")):
        mirror_to_ninna(path)
    print(f"OK {path.relative_to(ROOT.parent.parent)} ({path.stat().st_size} bytes)")


# ---------------------------------------------------------------------------
# 00 Handoff
# ---------------------------------------------------------------------------
def gen_handoff():
    doc = Document()
    setup_doc(doc)
    add_title(doc, "Traspaso de mi parte de la EP5 (ciclo mitigación)")
    add_subtitle(
        doc,
        "Para Nicolás, Skarlett y Ari · Giannina Guerrero (Ninna) · 25 de noviembre de 2026",
    )
    add_body(
        doc,
        "Dejé armado el paquete de integración del ciclo MITIGAR (EV5-6 / EP5-EP6): "
        "matriz 40/40 con Resultado EV2 cargado, inventario INC, plantilla de KPIs G1–G6, "
        "borrador del informe §1–§3 y outline del guion EP6. "
        "Congelo cifras el **sábado 28-11-2026**. Necesito handoffs el **viernes 27** "
        "con paths de evidencia + estado INC/CP. No invento números.",
        size=10,
    )

    add_heading(doc, "Nicolás (auth, RBAC, Selenium, SQLMap)", level=3)
    for item in [
        "Bitácora actualizada INC-01, 02, 03, 07 (+ 13/14 si hubo).",
        "Selenium post-mitigación: `report.html` + `report.json` + pass rate.",
        "SQLMap retest (output + conclusión).",
        "Wireshark sesión (si alcanzó): `.pcapng` + PNG.",
        "Paths relativos bajo `EV5-6 Entrega/Nicolas/` (o EV3 si aplica).",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "Ari (rendimiento, ZAP, John)", level=3)
    for item in [
        "Confirmación cierre EV56-04 (delay) para el inventario.",
        "Tabla JMeter por fase (100 → 5000) + `.jtl` / dashboard.",
        "John post-bcrypt (cuando exista INC-01).",
        "ZAP before/after (+ headers/CORS si hubo).",
        "Paths bajo `EV5-6 Entrega/Ari/Evidencias/`.",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "Skarlett (Sonar, norma, configuración)", level=3)
    for item in [
        "Sonar backend/frontend post-fix (capturas + métricas).",
        "CP-14 / 16 / 17 / 18 (resultado o limitación fechada).",
        "Tabla normativa artículo ↔ INC/CP.",
        "Diagrama CI/CD con controles de seguridad (borrador OK).",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "Ninna (al recibir)", level=3)
    for item in [
        "Actualizar CSV matriz columna `Resultado_EV56`.",
        "Actualizar inventario INC → Verificado.",
        "Completar G1–G6 e insertar gráficos en el Word.",
        "Pegar §5 y §6 en el informe.",
        "Dictamen alineado a críticos abiertos/cerrados.",
        "Repartir frases del guion por voz.",
    ]:
        add_bullet(doc, item)

    headers = ["Integrante", "Entrega mínima viernes 27", "Dónde dejarlo"]
    rows = [
        ["Nicolás", "Selenium + INC-01/02/03/07 + SQLMap", "Nicolas/Evidencias o Bitácora"],
        ["Ari", "JMeter fases + cierre INC-04 + ZAP/John", "Ari/Evidencias"],
        ["Skarlett", "Sonar delta + norma + CP-14/16/17/18", "Skarlett/"],
        ["Ninna", "Congelar matriz, KPIs, informe y guion", "EV5-6 Contexto / Entregables"],
    ]
    add_heading(doc, "Resumen rápido", level=3)
    fill_table(doc, headers, rows, size=10)

    out = CONTEXTO / "00-Handoff-para-el-equipo.docx"
    doc.save(out)
    mirror_to_ninna(out)
    print(f"OK {out.name}")


# ---------------------------------------------------------------------------
# 01 Inventario INC + KPIs
# ---------------------------------------------------------------------------
def gen_inventario_kpis():
    doc = Document()
    setup_doc(doc, narrow=True)
    add_title(doc, "Inventario de incidentes y plantilla de KPIs — ciclo EV5-6")
    add_subtitle(
        doc,
        "Insumo para las secciones 5.1 y 5.3 del informe EP5 · Cuidarte+ (Caso B) · "
        "Integrantes: Ari Araya, Nicolás Barra, Giannina Guerrero, Skarlett Tropan · "
        "Actualización 25 de noviembre de 2026",
    )

    add_heading(doc, "1. Inventario de incidentes", level=1)
    add_body(
        doc,
        "Fuente baseline: informe EP3/EP4 y bitácoras EV2. "
        "Estados: Abierto · En remediación · Verificado (retest) · Residual / reserva. "
        "No se inventan cierres sin evidencia de retest.",
        size=10,
    )

    add_heading(doc, "1.1 Mínimo de examen (P0)", level=2)
    fill_table(
        doc,
        ["INC", "Severidad", "Defecto", "Dueño fix", "Retest", "Estado 25-11", "Evidencia"],
        [
            ["INC-01", "Crítico", "Contraseñas en texto plano", "Nicolás / Ari", "CP-15, John, login", "Abierto", "EV2: John sin hashes"],
            ["INC-02", "Grave", "JWT_SECRET en repo", "Nicolás", "Login + revisión repo", "Abierto", "EV2: .env / README"],
            ["INC-03", "Grave", "Logout no revoca JWT", "Nicolás", "CP-07", "Abierto", "EV2 bitácora CP-07"],
            ["INC-04", "Grave", "delayMiddleware(5000)", "Ari", "Timing + JMeter", "En remediación / medido AFTER", "Ari/Evidencias/EV56-04/"],
            ["INC-07", "Grave", "/roles sin JWT+admin", "Nicolás", "curl 401/403/2xx", "Abierto", "EV2 parcial CP-08"],
        ],
        size=8,
    )

    add_heading(doc, "1.2 Ampliación recomendada", level=2)
    fill_table(
        doc,
        ["INC", "Severidad", "Defecto", "Dueño", "Estado", "Nota"],
        [
            ["INC-05", "Moderado/Grave", "CORS abierto + cabeceras", "Ari", "Abierto", "Bloquea ZAP after limpio"],
            ["INC-06", "Grave", "Fuga err.message", "Skarlett", "Abierto", "Confirmado en código EV2"],
            ["INC-13", "Grave", "Descarga sin auditoría", "Nicolás", "Abierto", "CP-03 / RF-4.2 / RF-5.1"],
            ["INC-14", "Grave", "POST /auditoria abierto", "Nicolás", "Abierto", "CP-03"],
        ],
        size=8,
    )

    add_heading(doc, "1.3 Residuales (P2 / reserva §6)", level=2)
    fill_table(
        doc,
        ["INC", "Tema breve", "Estado"],
        [
            ["INC-09", "Borrado / baja lógica", "Abierto"],
            ["INC-10", "Política de clave / registro", "Abierto / parcial"],
            ["INC-15", "Rechazo DOC/PPT incompleto o UI", "Abierto"],
            ["INC-16", "Documentos en bytea / cifrado reposo", "Abierto"],
            ["INC-17", "Disponibilidad / réplica", "Abierto"],
        ],
        size=9,
    )

    add_heading(doc, "1.4 Contadores y regla de dictamen", level=2)
    fill_table(
        doc,
        ["Métrica", "Valor ahora", "Meta salida"],
        [
            ["INC P0 mínimo (01,02,03,04,07)", "1 en remediación (04); 4 abiertos", "≥5 Verificados"],
            ["Críticos abiertos", "1 (INC-01)", "0 para Certificado con reservas"],
            ["% P0 mitigados con retest", "0 % Verificado (04 medido)", "100 % del mínimo"],
        ],
        size=9,
    )
    add_body(
        doc,
        "Regla: ≥1 crítico abierto → **No certificado**. "
        "P0 cerrados + reservas explícitas (TLS, techo 5000 VU, etc.) → **Certificado con reservas**. "
        "El dictamen debe coincidir con la matriz y con §6.",
        size=10,
    )

    add_heading(doc, "2. Plantilla de KPIs (G1–G6)", level=1)
    add_body(
        doc,
        "Archivo de datos reproducible. Completar con handoffs del viernes 27. "
        "Insertar los gráficos en el Word del informe (no solo enlazar). "
        "Cada gráfico lleva: título · fuente (path + fecha + autor) · 1–2 frases de lectura.",
        size=10,
    )

    add_heading(doc, "G1 — Resultado de CP: EV2 vs EV5-6", level=2)
    fill_table(
        doc,
        ["Estado", "EV2 (cierre 27-10-2026)", "EV5-6 (pendiente)"],
        [
            ["Aprobado", "10 códigos ERS", ""],
            ["Parcial", "10", ""],
            ["Fallido", "20", ""],
            ["No ejecutado / sin resultado", "0", ""],
            ["Total", "40", "40"],
        ],
        size=9,
    )
    add_body(
        doc,
        "Lectura (borrador): En EV2 la cobertura de diseño fue 40/40, pero 20 códigos fallaron. "
        "El ciclo EV5-6 debe mostrar el desplazamiento Fallido → Aprobado en los CP ligados a INC P0.",
        size=10,
    )

    add_heading(doc, "G2 — Incidentes abiertos vs cerrados por severidad", level=2)
    fill_table(
        doc,
        ["Severidad", "Abiertos", "Verificados", "Residual"],
        [
            ["Crítico", "1 (INC-01)", "0", ""],
            ["Grave", "(completar)", "", ""],
            ["Moderado", "", "", ""],
            ["Leve", "", "", ""],
        ],
        size=9,
    )

    add_heading(doc, "G3 — Selenium (obligatorio)", level=2)
    fill_table(
        doc,
        ["Métrica", "Valor", "Fuente"],
        [
            ["Casos totales", "", "Nicolas/.../report.json"],
            ["Passed", "", ""],
            ["Failed", "", ""],
            ["Pass rate %", "", ""],
            ["Duración total", "", ""],
            ["Flaky", "", ""],
            ["Fecha ejecución", "", ""],
        ],
        size=9,
    )
    add_body(
        doc,
        "Baseline EV2 (referencia, no sustituye el post-fix): suite 11/11 en EV2 Entrega/Nicolas/Evidencias/Selenium/.",
        size=10,
    )

    add_heading(doc, "G4 — JMeter: latencia vs VU (umbral 300 ms NFR-PERF-1)", level=2)
    fill_table(
        doc,
        ["VU", "Samples", "Avg (ms)", "p90", "p95", "Max", "Error %", "Notas"],
        [
            ["1 (humo post-delay)", "", "~30 (API GET)", "", "", "", "0", "Ari EV56-04 after"],
            ["100", "", "", "", "", "", "", "Pendiente"],
            ["1000", "", "", "", "", "", "", "Pendiente"],
            ["2500", "", "", "", "", "", "", "Pendiente"],
            ["5000", "", "", "", "", "", "", "Pendiente; documentar techo HW"],
        ],
        size=8,
    )

    add_heading(doc, "G5 — JMeter: error % vs VU", level=2)
    add_body(
        doc,
        "Misma tabla de fases que G4; eje Y = error %. Incluir el punto 5000 aunque sea intento fallido por hardware.",
        size=10,
    )

    add_heading(doc, "G6 — SonarQube: bugs / vulnerabilidades antes vs después", level=2)
    fill_table(
        doc,
        ["Métrica", "Backend EV2", "Backend EV5-6", "Frontend EV2", "Frontend EV5-6"],
        [
            ["Bugs", "", "", "", ""],
            ["Vulnerabilidades", "", "", "", ""],
            ["Code smells", "", "", "", ""],
            ["Coverage %", "", "", "", ""],
            ["Fecha / path", "", "", "", ""],
        ],
        size=8,
    )

    out = CONTEXTO / "01-Inventario-INC-y-KPIs.docx"
    doc.save(out)
    mirror_to_ninna(out)
    print(f"OK {out.name}")


# ---------------------------------------------------------------------------
# 02 Matriz
# ---------------------------------------------------------------------------
def gen_matriz():
    csv_path = NINNA / "Planillas" / "EV56-22-Matriz-40-ERS-ciclo3.csv"
    rows = list(csv.DictReader(csv_path.open(encoding="utf-8-sig")))

    doc = Document()
    setup_doc(doc, narrow=True)
    add_title(doc, "Matriz de trazabilidad ERS B: 40 de 40 requisitos (ciclo EV5-6)")
    add_subtitle(
        doc,
        "Sección 4 / anexo del informe EP5 · Cuidarte+ (Caso B) · "
        "Integrantes: Ari Araya, Nicolás Barra, Giannina Guerrero, Skarlett Tropan · "
        "Borrador 25 de noviembre de 2026",
    )

    add_heading(doc, "Criterio de construcción", level=1)
    add_body(
        doc,
        "En la EV2 la matriz relacionó los 40 códigos del ERS B con caso, riesgo, módulo, "
        "ejecutor, incidente y Resultado del ciclo de verificación. "
        "Para el ciclo MITIGAR se conserva esa base y se agrega la columna **Resultado EV5-6** "
        "más la ruta de evidencia post-mitigación. "
        "La columna Riesgo usa la priorización heredada: P0 autenticación/acceso/documentos clínicos; "
        "P1 auditoría y configuración; P2 CRUD; P3 rendimiento/disponibilidad; P4 usabilidad/compatibilidad.",
        size=10,
    )
    add_body(
        doc,
        "Al 25-11-2026, Resultado EV5-6 está en **Pendiente handoff** salvo filas tocadas por INC-04 "
        "(delay retirado; JMeter 5000 pendiente). No se inventan resultados de Selenium, Sonar, ZAP ni John.",
        size=10,
    )

    headers = [
        "Código",
        "Descripción (ERS B)",
        "Caso",
        "Tipo de prueba",
        "Riesgo",
        "Módulo",
        "Ejecuta",
        "Incidente vinculado",
        "Resultado EV2",
        "Resultado EV5-6",
    ]

    def block(title, predicate):
        add_heading(doc, title, level=1)
        data = []
        for r in rows:
            if not predicate(r["Codigo_ERS"]):
                continue
            data.append(
                [
                    r["Codigo_ERS"],
                    r["Descripcion"],
                    r["Caso"],
                    r["Tipo"],
                    r["Riesgo"],
                    r["Modulo"],
                    r["Ejecuta"],
                    r["INC"],
                    r["Resultado_EV2"],
                    r["Resultado_EV56"],
                ]
            )
        fill_table(doc, headers, data, size=7)

    block("Requisitos funcionales (RF)", lambda c: c.startswith("RF-"))
    block("Requisitos no funcionales (NFR)", lambda c: c.startswith("NFR-"))
    block("Reglas de negocio (RB)", lambda c: c.startswith("RB-"))

    add_heading(doc, "Nota de cierre (provisional)", level=1)
    add_body(
        doc,
        "Cobertura de diseño: 40/40. Resultado EV2 (cierre 27-10-2026): 10 aprobados, 10 parciales, 20 fallidos. "
        "Resultado EV5-6 se congela el sábado 28-11-2026 tras handoffs del viernes 27. "
        "Fuente CSV de trabajo: EV5-6 Entrega/Ninna/Planillas/EV56-22-Matriz-40-ERS-ciclo3.csv.",
        size=10,
    )

    out = CONTEXTO / "02-Matriz-trazabilidad-40-ERS.docx"
    doc.save(out)
    mirror_to_ninna(out)
    print(f"OK {out.name}")


# ---------------------------------------------------------------------------
# Helpers: clonar plantilla EP3/EP4 (Arial, márgenes, estilos, pie)
# ---------------------------------------------------------------------------
def clone_blank(template: Path, dest: Path) -> Document:
    """Copia el .docx plantilla y vacía el body (deja sectPr = márgenes/pie)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(template, dest)
    doc = Document(str(dest))
    body = doc.element.body
    sectPr = body.find(qn("w:sectPr"))
    for child in list(body):
        if child is not sectPr:
            body.remove(child)
    return doc


def center_title(doc, text, size=None, bold=False, space_after_pt=None, line_spacing=1.1):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = line_spacing
    if space_after_pt is not None:
        p.paragraph_format.space_after = Pt(space_after_pt)
    run = p.add_run(text)
    # size=None → hereda Arial 11 del docDefaults (como EP3 en la 1ª línea)
    if size is not None:
        set_run_font(run, size=size, bold=bold)
    else:
        set_run_font(run, size=11, bold=bold)
        # quitar size explícito para parecerse a EP3 en "EVALUACIÓN PARCIAL…"
        if size is None and not bold:
            pass
    run.bold = bold
    return p


def add_md_body(doc: Document, md_text: str, heading_map: dict[str, str] | None = None):
    """Convierte un bloque Markdown (desde ## 1.) al doc, con Arial/justificado."""
    heading_map = heading_map or {}
    in_table = False
    table_rows: list[str] = []

    def flush_table():
        nonlocal in_table, table_rows
        if not table_rows:
            return
        parsed = []
        for r in table_rows:
            if set(r.replace("|", "").strip()) <= set("-: "):
                continue
            parsed.append([c.strip() for c in r.strip("|").split("|")])
        table_rows = []
        in_table = False
        if not parsed:
            return
        cols = max(len(r) for r in parsed)
        t = doc.add_table(rows=len(parsed), cols=cols)
        for i, r in enumerate(parsed):
            for j in range(cols):
                t.rows[i].cells[j].text = r[j] if j < len(r) else ""
        style_table(t, size=9)
        doc.add_paragraph("")

    for raw in md_text.splitlines():
        line = raw.rstrip()
        if line.startswith("|"):
            in_table = True
            table_rows.append(line)
            continue
        if in_table:
            flush_table()
        if not line or line.startswith("---") or line.startswith("*Elaborado"):
            continue
        if line.startswith("> "):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.5)
            add_inline(p, line[2:], size=10)
            for run in p.runs:
                run.italic = True
            continue
        if line.startswith("## "):
            title = line[3:].strip()
            title = heading_map.get(title, title)
            add_heading(doc, title, level=1)
            continue
        if line.startswith("### "):
            title = line[4:].strip()
            title = heading_map.get(title, title)
            add_heading(doc, title, level=2)
            continue
        if line.startswith("#### "):
            add_heading(doc, line[5:].strip(), level=3)
            continue
        if line.startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            add_inline(p, line[2:], size=11)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            continue
        m = re.match(r"^(\d+)\.\s+(.*)$", line)
        if m:
            p = doc.add_paragraph(style="List Number")
            add_inline(p, m.group(2), size=11)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            continue
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_inline(p, line, size=11)

    if in_table:
        flush_table()


# ---------------------------------------------------------------------------
# EP5 Informe — clona EP3 (Arial 11, portada, pie) + índice formato EP5
# ---------------------------------------------------------------------------
def gen_informe():
    if not EP3_PLANTILLA.exists():
        raise FileNotFoundError(EP3_PLANTILLA)

    out = ENTREGABLES / "EP5-Informe-Cuidarte-Mas-borrador.docx"
    doc = clone_blank(EP3_PLANTILLA, out)

    # Portada idéntica a EP3 (tamaños y espaciado)
    for _ in range(3):
        doc.add_paragraph("")

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.1
    run = p.add_run("EVALUACIÓN PARCIAL N° 5")
    set_run_font(run, size=11, bold=True)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.1
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run("Verificación de calidad, seguridad")
    set_run_font(run, size=24, bold=True)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.1
    p.paragraph_format.space_after = Pt(10)
    run = p.add_run("y cumplimiento normativo")
    set_run_font(run, size=24, bold=True)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.1
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run("Informe de seguridad y calidad en el desarrollo de software")
    set_run_font(run, size=14, bold=False)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.1
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run("Caso B: Sistema de exámenes médicos Cuidarte+")
    set_run_font(run, size=12, bold=False)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Borrador de trabajo — ciclo MITIGAR (EV5-6)")
    set_run_font(run, size=11, italic=True)

    doc.add_paragraph("")
    doc.add_paragraph("")

    # Tabla meta 1×2 como en EP3
    meta = doc.add_table(rows=1, cols=2)
    meta.style = "Table Grid"
    left = (
        "Asignatura\n"
        "ISY1102 · Seguridad y Calidad en el Desarrollo de Software\n\n"
        "Carrera: Ingeniería en Informática\n"
        "Sección: 001V\n"
        "Sede: Puente Alto\n"
        "Docente: Jose Sergio Collio Huennun\n"
        "Fecha: Noviembre de 2026 (borrador; cifras se congelan el 28-11-2026)"
    )
    right = (
        "Integrantes\n"
        "Ari Araya\n"
        "Nicolás Barra\n"
        "Giannina Guerrero\n"
        "Skarlett Tropan"
    )
    meta.rows[0].cells[0].text = left
    meta.rows[0].cells[1].text = right
    for cell in meta.rows[0].cells:
        for para in cell.paragraphs:
            for run in para.runs:
                set_run_font(run, size=10)

    doc.add_paragraph("")

    # ÍNDICE según formato oficial EP5
    p = doc.add_paragraph()
    run = p.add_run("ÍNDICE")
    set_run_font(run, size=12, bold=True)

    indice = [
        "1. Introducción",
        "1.1 Contexto del software",
        "1.2 Propósito del plan y de este informe",
        "1.3 Alcance y estructura del informe",
        "2. Criterios de calidad",
        "2.1 Calidad del producto",
        "2.2 Seguridad",
        "2.3 Cumplimiento normativo",
        "2.4 Criterios transversales de aceptación del ciclo",
        "3. Plan de pruebas",
        "3.1 Estrategia de pruebas",
        "3.2 Tipos de prueba",
        "3.3 Criterios de aceptación",
        "3.4 Herramientas utilizadas",
        "4. Diseño de casos de prueba",
        "5. Ejecución de pruebas",
        "5.1 Resumen de ejecución",
        "5.2 Detalle de ejecución de casos",
        "5.3 Criticidad de incidentes",
        "6. Propuesta de mejora",
        "Anexos",
    ]
    for line in indice:
        p = doc.add_paragraph()
        run = p.add_run(line)
        set_run_font(run, size=9.5)

    doc.add_page_break()

    md = (NINNA_ENT / "01-Informe-EP5-borrador.md").read_text(encoding="utf-8")
    body_start = md.find("## 1. Introducción")
    body = md[body_start:] if body_start >= 0 else md

    # Renombres para coincidir con el formato EP5 / índice EP3
    heading_map = {
        "1.2 Propósito de este informe": "1.2 Propósito del plan y de este informe",
        "1.3 Alcance y estructura": "1.3 Alcance y estructura del informe",
        "2.1 Calidad de producto (ISO/IEC 25010:2023)": "2.1 Calidad del producto",
        "2.2 Seguridad (controles alineados a ISO/IEC 27001 — enfoque)": "2.2 Seguridad",
        "2.3 Cumplimiento normativo (resumen)": "2.3 Cumplimiento normativo",
        "3.1 Estrategia": "3.1 Estrategia de pruebas",
        "3.3 Criterios de aceptación (ejemplos)": "3.3 Criterios de aceptación",
        "3.4 Herramientas y recursos": "3.4 Herramientas utilizadas",
        "5. Ejecución": "5. Ejecución de pruebas",
        "5.1 Resumen y KPIs": "5.1 Resumen de ejecución",
        "5.2 Detalle por caso": "5.2 Detalle de ejecución de casos",
    }
    add_md_body(doc, body, heading_map=heading_map)

    foot = doc.add_paragraph()
    foot.paragraph_format.space_before = Pt(12)
    run = foot.add_run(
        "Elaborado como avance de integración por Giannina Guerrero (Ninna). "
        "Congelar números el sábado 28-11-2026 tras handoffs del viernes 27. "
        "Formato: plantilla del informe EP3 (Arial 11, portada e índice) adaptada al "
        "formato oficial EP5 (secciones 1–6, con Propuesta de mejora)."
    )
    set_run_font(run, size=10, italic=True)

    doc.save(out)
    mirror_to_ninna(out)
    print(f"OK {out.name} (clon EP3 + estructura EP5)")


# ---------------------------------------------------------------------------
# Guion EP6 — clona guion EP4
# ---------------------------------------------------------------------------
def gen_guion():
    if not EP4_GUION_PLANTILLA.exists():
        raise FileNotFoundError(EP4_GUION_PLANTILLA)

    out = ENTREGABLES / "Guion-presentacion-EP6-Cuidarte.docx"
    doc = clone_blank(EP4_GUION_PLANTILLA, out)

    def center(text, size, bold=False, space_after=4):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(space_after)
        run = p.add_run(text)
        set_run_font(run, size=size, bold=bold)

    for _ in range(2):
        doc.add_paragraph("")

    center("Guion de presentación · Cuidarte+", 22, bold=True, space_after=8)
    center("Verificando la calidad, seguridad y cumplimiento normativo", 12)
    center("Caso B · Sistema de exámenes médicos Cuidarte+", 12)
    center("ISY1102 Seguridad y Calidad en el Desarrollo de Software", 12)
    center("Duoc UC · Sede Puente Alto · Sección 001V", 11)
    center("Evaluación Parcial 6 · Presentación", 11)
    center("Docente Jose Sergio Collio Huennun", 11)
    center("Integrantes", 12, bold=True, space_after=2)
    for name in ["Ari Araya", "Nicolás Barra", "Giannina Guerrero", "Skarlett Tropan"]:
        center(name, 11, space_after=0)
    center(
        "Guion cerrado: sábado 28-11-2026 · Grabación objetivo: domingo 29-11-2026",
        10,
        space_after=6,
    )
    center("(Outline — frases finales al congelar números)", 10, space_after=14)

    add_heading(doc, "Tiempos", level=1)
    add_body(
        doc,
        "Tenemos 10 minutos para exponer y 5 para preguntas. "
        "Cada persona habla aproximadamente 2 a 2,5 minutos. "
        "La nota es individual: cualquiera debe poder explicar cualquier lámina.",
        size=11,
    )

    fill_table(
        doc,
        ["Integrante", "Láminas (borrador)", "Tiempo"],
        [
            ["Giannina (Ninna)", "01–03, 11–12", "~2,5 min"],
            ["Nicolás", "04–06", "~2,5 min"],
            ["Ari", "07–08", "~2 min"],
            ["Skarlett", "09–10", "~2 min"],
            ["Todos", "13 Preguntas", "5 min"],
        ],
        size=10,
    )

    add_heading(doc, "Estructura de la exposición", level=2)
    for item in [
        "Del dictamen EV2 «No certificado» al ciclo MITIGAR (Ninna).",
        "Mitigaciones de autenticación, sesión y RBAC + Selenium (Nicolás).",
        "Rendimiento INC-04, JMeter hasta 5000 VU y DAST (Ari).",
        "Sonar, errores, norma y CI/CD (Skarlett).",
        "KPIs, dictamen, reservas y mantenimiento (Ninna).",
    ]:
        add_bullet(doc, item, size=11)

    add_heading(doc, "Antes de partir", level=2)
    for item in [
        "Deck en pantalla completa. Quien habla maneja el control.",
        "Alguien del grupo lleva el cronómetro a la vista.",
        "Si falta evidencia, quitar la lámina o marcarla «plan §6»; no mostrar capturas inventadas.",
        "Números del guion = números de §5 del informe.",
    ]:
        add_bullet(doc, item, size=11)

    laminas = [
        (
            "01",
            "Portada · Caso B Cuidarte+",
            "Ninna",
            "Logo / puertos Docker",
            "Buenas tardes. Presentamos la verificación de calidad, seguridad y cumplimiento normativo de Cuidarte+, "
            "sistema de exámenes médicos (Caso B). Arquitectura React + Express + PostgreSQL en Docker "
            "(FE 3333 / API 4444). Los integrantes son Ari, Nicolás, Skarlett y Giannina.",
        ),
        (
            "02",
            "Del dictamen EV2 «No certificado» al ciclo MITIGAR",
            "Ninna",
            "Inventario INC",
            "En EV2 diseñamos 40/40 requisitos y el dictamen fue No certificado por críticos y graves abiertos. "
            "Este ciclo mitiga, retestea con before/after y actualiza el dictamen. "
            "Regla: si INC-01 (crítico) sigue abierto, no certificamos.",
        ),
        (
            "03",
            "Estrategia por riesgo + cadena requisito→INC→retest→dictamen",
            "Ninna",
            "Matriz 40",
            "Estrategia mixta basada en riesgos. Cada requisito de la matriz tiene Resultado EV2 y Resultado EV5-6. "
            "La cadena es: requisito → incidente → remediación → retest con evidencia → dictamen.",
        ),
        (
            "04",
            "Mitigaciones auth: INC-01 bcrypt, INC-02 JWT, INC-03 logout",
            "Nicolás",
            "Before/after + Postman",
            "«Pendiente frase final con evidencia». Cubrir hash de contraseñas, secreto JWT fuera del repo y revocación en logout.",
        ),
        (
            "05",
            "RBAC: INC-07 /roles + IDOR paciente",
            "Nicolás",
            "curl 401/403/2xx",
            "«Pendiente frase final». Mostrar 401 sin token, 403 rol insuficiente y 2xx con rol correcto.",
        ),
        (
            "06",
            "Selenium obligatorio: pass rate post-fix",
            "Nicolás",
            "report.html/json",
            "«Pendiente frase final». Baseline EV2 11/11; reportar pass rate post-mitigación.",
        ),
        (
            "07",
            "INC-04 delay + JMeter ramp a 5000 VU",
            "Ari",
            "EV56-04 + jtl",
            "Ya medido: delay before ~5,03 s → after ~0,03 s. Completar con ramp 100→5000 y techo de hardware si aplica.",
        ),
        (
            "08",
            "ZAP / John / fuerza bruta (lo que exista)",
            "Ari",
            "Reportes",
            "«Pendiente frase final». Solo mostrar lo que tenga path de evidencia.",
        ),
        (
            "09",
            "Sonar delta + errores INC-06 + norma",
            "Skarlett",
            "Capturas Sonar",
            "«Pendiente frase final». Bugs/vulnerabilidades before/after y relación con 20.584 / DS 41 / 19.628.",
        ),
        (
            "10",
            "Diagrama CI/CD con controles de seguridad",
            "Skarlett (+ Ninna)",
            "Diagrama",
            "Commit → build → unitarias → Sonar Quality Gate → imagen Docker → deploy lab → Selenium → (opcional) ZAP.",
        ),
        (
            "11",
            "KPIs G1–G6 (1 lámina resumen)",
            "Ninna",
            "Gráficos",
            "Resumen de desplazamiento Fallido→Aprobado, INC por severidad, Selenium, JMeter y Sonar. "
            "Números congelados el 28.",
        ),
        (
            "12",
            "Dictamen + reservas + mantenimiento",
            "Ninna",
            "§6",
            "Dictamen provisional al 25-11: No certificado (INC-01 abierto). "
            "Meta: Certificado con reservas si se verifican INC-01, 02, 03, 04 y 07.",
        ),
        (
            "13",
            "Preguntas",
            "Todos",
            "—",
            "Ensayar: ¿por qué no certifican si el delay bajó a 30 ms? Porque INC-01 crítico sigue abierto.",
        ),
    ]

    fill_table(
        doc,
        ["Lámina", "Tema", "Habla", "Evidencia mínima"],
        [[a, b, c, d] for a, b, c, d, _ in laminas],
        size=9,
    )

    for num, tema, habla, evid, texto in laminas:
        add_heading(doc, f"Lámina {num} · {tema}", level=1)
        p = doc.add_paragraph()
        run = p.add_run("En pantalla")
        set_run_font(run, size=11, bold=True)
        add_bullet(doc, f"Habla: {habla}", size=10)
        add_bullet(doc, f"Evidencia: {evid}", size=10)
        p = doc.add_paragraph()
        run = p.add_run("Qué decir")
        set_run_font(run, size=11, bold=True)
        add_body(doc, texto, size=11)

    add_heading(doc, "Preguntas probables (ensayar)", level=1)
    for q in [
        "¿Por qué no certifican si el delay ya bajó a 30 ms? → Porque INC-01 crítico sigue abierto.",
        "¿Qué es Certificado con reservas? → P0 cerrados + limitaciones explícitas (TLS lab, techo HW).",
        "¿Dónde está la evidencia del requisito NFR-SEG-2? → Matriz → CP-15/CP-01 → INC-01 → path John.",
        "¿Qué hace Selenium en el pipeline? → Regresión UI post-merge; no reemplaza DAST/SAST.",
    ]:
        add_bullet(doc, q, size=11)

    add_heading(doc, "Checklist de ensayo (domingo AM)", level=1)
    for item in [
        "Cronómetro ≤ 10 min.",
        "Cada voz tiene 1 captura real.",
        "Números iguales a §5 del informe.",
        "Lista de reservas igual al dictamen.",
    ]:
        add_bullet(doc, item, size=11)

    doc.save(out)
    mirror_to_ninna(out)
    print(f"OK {out.name} (clon guion EP4)")


def main():
    ENTREGABLES.mkdir(parents=True, exist_ok=True)
    NINNA_ENT.mkdir(parents=True, exist_ok=True)
    gen_handoff()
    gen_inventario_kpis()
    gen_matriz()
    gen_informe()
    gen_guion()
    print("Listo.")


if __name__ == "__main__":
    main()
