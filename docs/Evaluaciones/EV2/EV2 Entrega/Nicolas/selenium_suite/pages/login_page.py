from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base import BasePage


class LoginPage(BasePage):
    USER = (By.CSS_SELECTOR, '[data-testid="input-nombre-usuario"]')
    PASS = (By.CSS_SELECTOR, '[data-testid="input-password"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-testid="button-login"]')

    def open_login(self) -> None:
        self.open("/login")
        self.wait.until(EC.presence_of_element_located(self.USER))

    def login(self, usuario: str, password: str) -> None:
        self.open_login()
        user = self.driver.find_element(*self.USER)
        pwd = self.driver.find_element(*self.PASS)
        btn = self.driver.find_element(*self.SUBMIT)
        user.clear()
        user.send_keys(usuario)
        pwd.clear()
        pwd.send_keys(password)
        btn.click()

    def login_expect_home(self, usuario: str, password: str) -> None:
        self.login(usuario, password)
        self.wait_url_contains("/home")
        self.sleep(0.6)

    def wait_invalid_credentials_message(self) -> str:
        def _has_msg(driver):
            text = driver.find_element(By.TAG_NAME, "body").text
            return "Credenciales" in text or "inválid" in text.lower() or "invalid" in text.lower()

        self.wait.until(_has_msg)
        return self.body_text()
