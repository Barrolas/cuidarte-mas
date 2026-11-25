"""Utilidades compartidas para la suite Selenium de Nicolás (EP3)."""
from __future__ import annotations

import os
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = os.environ.get("CUIDARTE_BASE_URL", "http://localhost:3333")
EVIDENCIAS_ROOT = Path(__file__).resolve().parent.parent / "Evidencias"
SELENIUM_EVID = EVIDENCIAS_ROOT / "Selenium"


def make_driver() -> webdriver.Chrome:
    options = Options()
    if os.environ.get("SELENIUM_HEADLESS", "").lower() in {"1", "true", "yes"}:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1400,900")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )


def wait(driver: webdriver.Chrome, seconds: int = 20) -> WebDriverWait:
    return WebDriverWait(driver, seconds)


def shot(driver: webdriver.Chrome, name: str, subdir: str = "Selenium") -> Path:
    folder = EVIDENCIAS_ROOT / subdir
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / name
    driver.save_screenshot(str(path))
    return path


def login(driver: webdriver.Chrome, usuario: str, password: str) -> None:
    driver.get(f"{BASE_URL}/login")
    w = wait(driver)
    user = w.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="input-nombre-usuario"]'))
    )
    pwd = driver.find_element(By.CSS_SELECTOR, '[data-testid="input-password"]')
    btn = driver.find_element(By.CSS_SELECTOR, '[data-testid="button-login"]')
    user.clear()
    user.send_keys(usuario)
    pwd.clear()
    pwd.send_keys(password)
    btn.click()


def login_ok(driver: webdriver.Chrome, usuario: str, password: str) -> None:
    login(driver, usuario, password)
    wait(driver).until(EC.url_contains("/home"))
    time.sleep(0.8)


def open_user_menu(driver: webdriver.Chrome) -> None:
    btn = wait(driver).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Menú de usuario"]'))
    )
    btn.click()
    time.sleep(0.3)


def logout(driver: webdriver.Chrome) -> None:
    open_user_menu(driver)
    item = wait(driver).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Cerrar sesión"]'))
    )
    item.click()
    wait(driver).until(EC.url_contains("/login"))


def go(driver: webdriver.Chrome, path: str) -> None:
    driver.get(f"{BASE_URL}{path}")
    time.sleep(0.8)


def page_text(driver: webdriver.Chrome) -> str:
    return driver.find_element(By.TAG_NAME, "body").text
