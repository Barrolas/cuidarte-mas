from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from .base import BasePage


class ExamenesPage(BasePage):
    def open_list(self) -> None:
        self.open("/examenes")
        self.wait_until_loaded()

    def wait_until_loaded(self) -> None:
        def ready(driver):
            text = driver.find_element(By.TAG_NAME, "body").text
            if "Cargando exámenes" in text or "Cargando examenes" in text:
                return False
            return (
                "LISTAR EXÁMENES" in text.upper()
                or "LISTAR EXAMENES" in text.upper()
                or "NUEVO EXAMEN" in text.upper()
                or "Tipo de Examen" in text
                or "RUT Paciente" in text
            )

        self.wait.until(ready)
        self.sleep(0.6)

    def assert_list_ready(self) -> str:
        text = self.body_text()
        assert "Examen" in text or "EXÁMENES" in text.upper()
        return text

    def open_first_edit(self) -> None:
        # Esperar filas de tabla; el lapiz puede no exponer title/aria de forma estable
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//table//tbody//tr|.//*[contains(@class,'MuiTableBody')]//tr")
            )
        )
        edit_btns = self.driver.find_elements(
            By.XPATH,
            "//button[contains(@aria-label,'Editar') or @title='Editar']",
        )
        if not edit_btns:
            # Primera fila: ultimo boton de acciones (lapiz)
            edit_btns = self.driver.find_elements(
                By.XPATH, "(//table//tbody//tr)[1]//button"
            )
        assert edit_btns, "No se encontro boton Editar examen en el listado"
        self.driver.execute_script("arguments[0].click();", edit_btns[0])
        self.sleep(1.0)
        self.wait.until(
            lambda d: "Editar examen" in d.find_element(By.TAG_NAME, "body").text
            or "/examenes/" in d.current_url
        )

    def wait_edit_form_ready(self) -> None:
        def ready(driver):
            text = driver.find_element(By.TAG_NAME, "body").text
            if "Cargando datos" in text:
                return False
            return (
                "Observaciones" in text
                or driver.find_elements(By.CSS_SELECTOR, 'textarea[name="observaciones"]')
                or driver.find_elements(By.TAG_NAME, "textarea")
            )

        self.wait.until(ready)
        self.sleep(0.4)

    def assert_edit_form(self) -> str:
        self.wait_edit_form_ready()
        text = self.body_text()
        assert "Editar examen" in text or "Observaciones" in text or "Diagn" in text
        return text

    def set_observaciones(self, value: str) -> None:
        self.wait_edit_form_ready()
        named = self.driver.find_elements(By.CSS_SELECTOR, 'textarea[name="observaciones"]')
        if named:
            textarea = named[0]
        else:
            areas = self.driver.find_elements(By.TAG_NAME, "textarea")
            assert areas, "No hay textarea de observaciones"
            textarea = areas[0]

        textarea.click()
        textarea.send_keys(Keys.CONTROL, "a")
        textarea.send_keys(value)
        self.sleep(0.3)

    def save_examen(self) -> None:
        buttons = self.driver.find_elements(
            By.XPATH,
            "//button[contains(., 'Actualizar Examen') or contains(., 'Guardar') or contains(., 'Actualizar')]",
        )
        assert buttons, "No se encontro boton de guardar/actualizar examen"
        buttons[0].click()
        self.sleep(1.0)

    def wait_success_toast_or_list(self) -> str:
        def done(driver):
            text = driver.find_element(By.TAG_NAME, "body").text
            return (
                "exitosamente" in text.lower()
                or "actualizado" in text.lower()
                or "LISTAR EXÁMENES" in text.upper()
                or "LISTAR EXAMENES" in text.upper()
                or "/examenes" in driver.current_url and "Editar examen" not in text
            )

        self.wait.until(done)
        return self.body_text()
