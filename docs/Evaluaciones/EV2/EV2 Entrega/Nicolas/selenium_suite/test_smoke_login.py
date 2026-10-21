"""
Smoke CP-01 (parcial): login médico en UI.
Requisito: Docker arriba (http://localhost:3333) y Chrome instalado.

Uso:
  .\\.venv\\Scripts\\Activate.ps1
  python test_smoke_login.py
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://localhost:3333"
EVIDENCIAS = Path(__file__).resolve().parent.parent / "Evidencias" / "CP-01"


def main() -> int:
    EVIDENCIAS.mkdir(parents=True, exist_ok=True)

    options = Options()
    # Quita el comentario siguiente si quieres Chrome sin ventana:
    # options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    wait = WebDriverWait(driver, 20)

    try:
        driver.get(f"{BASE_URL}/login")
        user = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="input-nombre-usuario"]'))
        )
        password = driver.find_element(By.CSS_SELECTOR, '[data-testid="input-password"]')
        btn = driver.find_element(By.CSS_SELECTOR, '[data-testid="button-login"]')

        user.clear()
        user.send_keys("medico")
        password.clear()
        password.send_keys("medico")
        btn.click()

        wait.until(EC.url_contains("/home"))
        time.sleep(1)
        shot = EVIDENCIAS / "selenium-login-medico.png"
        driver.save_screenshot(str(shot))
        print(f"[OK] Login medico -> {driver.current_url}")
        print(f"[OK] Captura: {shot}")
        return 0
    except Exception as exc:
        fail_shot = EVIDENCIAS / "selenium-login-medico-FAIL.png"
        try:
            driver.save_screenshot(str(fail_shot))
            print(f"[FAIL] Captura de error: {fail_shot}")
        except Exception:
            pass
        print(f"[FAIL] {exc}")
        return 1
    finally:
        driver.quit()


if __name__ == "__main__":
    sys.exit(main())
