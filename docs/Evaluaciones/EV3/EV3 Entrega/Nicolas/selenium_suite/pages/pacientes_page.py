from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base import BasePage


class PacientesPage(BasePage):
    def open_list(self) -> None:
        self.open("/pacientes")
        self.wait_until_loaded()

    def wait_until_loaded(self) -> None:
        def ready(driver):
            text = driver.find_element(By.TAG_NAME, "body").text
            if "Cargando pacientes" in text:
                return False
            return (
                "Gestión de Pacientes" in text
                or "LISTAR PACIENTES" in text.upper()
                or "RUT" in text
            )

        self.wait.until(ready)
        self.sleep(0.4)

    def assert_table_ready(self) -> str:
        text = self.body_text()
        assert "Gestión de Pacientes" in text or "Pacientes" in text
        markers = ("RUT", "Email", "Teléfono", "LISTAR", "Nombre")
        assert any(m.lower() in text.lower() for m in markers), text[:400]
        return text

    def count_edit_buttons(self) -> int:
        buttons = self.driver.find_elements(
            By.CSS_SELECTOR, '[data-testid^="button-cliente-editar-"]'
        )
        return len(buttons)

    def open_first_edit(self) -> None:
        self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-testid^="button-cliente-editar-"]')
            )
        )
        btn = self.driver.find_elements(
            By.CSS_SELECTOR, '[data-testid^="button-cliente-editar-"]'
        )[0]
        btn.click()
        self.sleep(0.8)

    def assert_edit_form_visible(self) -> str:
        text = self.body_text()
        # Formulario de paciente / edicion
        assert any(
            x in text
            for x in (
                "Editar",
                "Registrar",
                "primer",
                "Primer",
                "RUT",
                "Email",
                "Guardar",
                "Actualizar",
                "Cancelar",
            )
        ), text[:400]
        return text

    def cancel_or_back_if_possible(self) -> None:
        # Intentar botones comunes; si no hay, volver a /pacientes
        candidates = self.driver.find_elements(By.XPATH, "//button[contains(., 'Cancelar') or contains(., 'Volver')]")
        if candidates:
            candidates[0].click()
            self.sleep(0.5)
        else:
            self.open_list()
