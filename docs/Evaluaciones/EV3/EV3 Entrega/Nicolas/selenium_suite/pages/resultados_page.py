from __future__ import annotations

from selenium.webdriver.common.by import By

from .base import BasePage


class ResultadosPage(BasePage):
    def open(self) -> None:  # type: ignore[override]
        super().open("/mis-resultados")
        self.wait_until_loaded()

    def wait_until_loaded(self) -> None:
        def ready(driver):
            text = driver.find_element(By.TAG_NAME, "body").text
            if "Cargando" in text and "resultado" in text.lower():
                return False
            return (
                "Resultado" in text
                or "Mis Resultados" in text
                or "Examen" in text
                or "no tienes" in text.lower()
                or "sin examenes" in text.lower()
                or "sin exámenes" in text.lower()
            )

        self.wait.until(ready)
        self.sleep(0.5)

    def assert_patient_results_view(self) -> str:
        text = self.body_text()
        assert (
            "Resultado" in text
            or "Mis Resultados" in text
            or "Examen" in text
        ), text[:400]
        # Empty state controlado tambien es valido
        has_content = (
            "Anticuerpos" in text
            or "Glicemia" in text
            or "Completado" in text
            or "Fecha" in text
            or "no tienes" in text.lower()
            or "sin " in text.lower()
            or "0 Exámenes" in text
            or "Exámenes Cargados" in text
        )
        assert has_content, f"Vista sin contenido reconocible: {text[:400]}"
        return text
