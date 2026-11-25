from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base import BasePage


class Layout(BasePage):
    USER_MENU = (By.CSS_SELECTOR, '[aria-label="Menú de usuario"]')
    LOGOUT = (By.CSS_SELECTOR, '[aria-label="Cerrar sesión"]')

    def nav_text(self) -> str:
        return self.body_text()

    def role_label_visible(self, role_fragment: str) -> bool:
        return role_fragment.lower() in self.body_text().lower()

    def open_user_menu(self) -> None:
        # Click JS sobre el IconButton del perfil (mas fiable en headless)
        btn = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[aria-label="Menú de usuario"], button[aria-haspopup="true"]')
            )
        )
        self.driver.execute_script("arguments[0].click();", btn)
        self.sleep(0.5)
        # Menu MUI: item por aria-label o texto
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//*[@aria-label='Cerrar sesión' or contains(., 'Cerrar Sesión') or contains(., 'Cerrar sesión')]",
                )
            )
        )

    def logout(self) -> None:
        self.open_user_menu()
        items = self.driver.find_elements(By.CSS_SELECTOR, '[aria-label="Cerrar sesión"]')
        if not items:
            items = self.driver.find_elements(
                By.XPATH, "//li[contains(., 'Cerrar Sesión') or contains(., 'Cerrar sesión')]"
            )
        assert items, "No se encontro item Cerrar sesion"
        self.driver.execute_script("arguments[0].click();", items[0])
        self.wait_url_contains("/login")

    def has_nav_label(self, label: str) -> bool:
        return label in self.body_text()
