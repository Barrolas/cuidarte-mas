from __future__ import annotations

import os
import time
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from reporting import ensure_evid_dir, write_reports

BASE_URL = os.environ.get("CUIDARTE_BASE_URL", "http://localhost:3333")
EVID = ensure_evid_dir()


def pytest_configure(config):
    config._selenium_results = []


def pytest_sessionfinish(session, exitstatus):
    results = getattr(session.config, "_selenium_results", [])
    write_reports(BASE_URL, results)


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture
def steps():
    log: list[str] = []

    def add(msg: str) -> None:
        log.append(msg)

    add.steps = log  # type: ignore[attr-defined]
    return add


@pytest.fixture
def driver():
    options = Options()
    if os.environ.get("SELENIUM_HEADLESS", "").lower() in {"1", "true", "yes"}:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1400,900")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    drv = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call":
        return

    drv = item.funcargs.get("driver")
    step_fn = item.funcargs.get("steps")
    step_list = getattr(step_fn, "steps", []) if step_fn else []
    duration_ms = int((report.duration or 0) * 1000)
    status = "passed" if report.passed else ("skipped" if report.skipped else "failed")

    meta = item.get_closest_marker("case")
    case_id = meta.kwargs.get("id") if meta else item.name
    cp = meta.kwargs.get("cp") if meta else ""
    name = meta.kwargs.get("name") if meta else item.name

    screenshot = ""
    if drv is not None:
        safe_id = str(case_id).replace("/", "-")
        shot_name = f"{safe_id}-{status}.png"
        shot_path = EVID / shot_name
        try:
            drv.save_screenshot(str(shot_path))
            screenshot = str(shot_path)
            # Attach to pytest-html if available
            try:
                from pytest_html import extras

                if hasattr(report, "extras"):
                    report.extras = getattr(report, "extras", [])
                    report.extras.append(extras.image(str(shot_path)))
            except Exception:
                pass
        except Exception:
            screenshot = ""

    error = ""
    if report.failed and report.longrepr:
        error = str(report.longrepr)[:800]

    item.config._selenium_results.append(
        {
            "id": case_id,
            "name": name,
            "cp": cp,
            "nodeid": item.nodeid,
            "status": status,
            "duration_ms": duration_ms,
            "steps": list(step_list),
            "screenshot": screenshot,
            "error": error,
        }
    )


def pytest_html_report_title(report):
    report.title = "Suite Selenium profesional — Nicolás EP3"
