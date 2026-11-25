"""Reporte JSON + resumen TXT para evidencias Selenium."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

EVIDENCIAS = Path(__file__).resolve().parent.parent / "Evidencias" / "Selenium"


def ensure_evid_dir() -> Path:
    EVIDENCIAS.mkdir(parents=True, exist_ok=True)
    return EVIDENCIAS


def write_reports(base_url: str, results: list[dict]) -> tuple[Path, Path]:
    evid = ensure_evid_dir()
    passed = sum(1 for r in results if r.get("status") == "passed")
    failed = sum(1 for r in results if r.get("status") == "failed")
    skipped = sum(1 for r in results if r.get("status") == "skipped")
    payload = {
        "suite": "Selenium profesional Nicolas EP3",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "base_url": base_url,
        "totals": {
            "total": len(results),
            "passed": passed,
            "failed": failed,
            "skipped": skipped,
        },
        "tests": results,
    }
    json_path = evid / "report.json"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        f"Suite Selenium profesional Nicolas EP3 — {payload['generated_at']}",
        f"Base URL: {base_url}",
        f"Resultado: {passed}/{len(results)} OK, {failed} FAIL, {skipped} SKIP",
        "",
    ]
    for r in results:
        lines.append(f"[{r['status'].upper()}] {r.get('id', '')} {r.get('name', '')}")
        lines.append(f"  cp={r.get('cp', '')} duration_ms={r.get('duration_ms', 0)}")
        for step in r.get("steps", []):
            lines.append(f"  - {step}")
        if r.get("screenshot"):
            lines.append(f"  screenshot: {r['screenshot']}")
        if r.get("error"):
            lines.append(f"  error: {r['error']}")
        lines.append("")

    txt_path = evid / "suite-output.txt"
    txt_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, txt_path
