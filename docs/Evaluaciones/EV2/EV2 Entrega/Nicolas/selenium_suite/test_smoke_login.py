"""
Smoke CP-01: wrapper hacia pytest -m smoke.

Uso (venv activo):
  python test_smoke_login.py

Equivale a:
  pytest -m smoke -v
"""
from __future__ import annotations

import os
import sys

import pytest


def main() -> int:
    os.environ.setdefault("SELENIUM_HEADLESS", os.environ.get("SELENIUM_HEADLESS", "0"))
    return pytest.main(["-m", "smoke", "-v", "--tb=short"])


if __name__ == "__main__":
    sys.exit(main())
