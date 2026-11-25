from __future__ import annotations

import time
from typing import Callable

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str, timeout: int = 25):
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def open(self, path: str = "/") -> None:
        self.driver.get(f"{self.base_url}{path}")

    def body_text(self) -> str:
        return self.driver.find_element(By.TAG_NAME, "body").text

    def wait_until(self, condition: Callable, message: str = "") -> None:
        self.wait.until(condition, message=message)

    def wait_url_contains(self, fragment: str) -> None:
        self.wait.until(EC.url_contains(fragment))

    def sleep(self, seconds: float = 0.4) -> None:
        time.sleep(seconds)
