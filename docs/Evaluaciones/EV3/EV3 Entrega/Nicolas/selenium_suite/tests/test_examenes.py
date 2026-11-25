import pytest

from pages import LoginPage, ExamenesPage, ResultadosPage


@pytest.mark.examenes
@pytest.mark.case(id="EXA-01", cp="CP-02/11", name="Listado examenes y abrir editar")
def test_exa_01_lista_y_abrir(driver, base_url, steps):
    login = LoginPage(driver, base_url)
    examenes = ExamenesPage(driver, base_url)
    steps("login medico")
    login.login_expect_home("medico", "medico")
    steps("abrir /examenes")
    examenes.open_list()
    steps("assert listado listo")
    examenes.assert_list_ready()
    steps("abrir primer examen en edicion")
    examenes.open_first_edit()
    steps("assert formulario editar examen")
    examenes.assert_edit_form()


@pytest.mark.examenes
@pytest.mark.case(id="EXA-02", cp="CP-11", name="Editar observaciones y guardar")
def test_exa_02_editar_guardar(driver, base_url, steps):
    login = LoginPage(driver, base_url)
    examenes = ExamenesPage(driver, base_url)
    steps("login medico")
    login.login_expect_home("medico", "medico")
    steps("abrir listado y editar primer examen")
    examenes.open_list()
    examenes.open_first_edit()
    marker = "Selenium CP-11 auto"
    steps(f"escribir observaciones: {marker}")
    examenes.set_observaciones(marker)
    steps("guardar examen")
    examenes.save_examen()
    text = examenes.wait_success_toast_or_list()
    steps("assert toast exito o vuelta a listado")
    assert (
        "exitosamente" in text.lower()
        or "actualizado" in text.lower()
        or "LISTAR" in text.upper()
        or marker in text
    ), text[:500]


@pytest.mark.resultados
@pytest.mark.case(id="RES-01", cp="CP-12", name="Paciente Mis Resultados")
def test_res_01_mis_resultados(driver, base_url, steps):
    login = LoginPage(driver, base_url)
    resultados = ResultadosPage(driver, base_url)
    steps("login paciente")
    login.login_expect_home("paciente", "paciente")
    steps("abrir /mis-resultados")
    resultados.open()
    steps("assert vista resultados o empty state")
    resultados.assert_patient_results_view()
