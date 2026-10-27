import pytest

from pages import LoginPage, PacientesPage


@pytest.mark.pacientes
@pytest.mark.case(id="PAC-01", cp="CP-10", name="Medico lista pacientes cargada")
def test_pac_01_lista(driver, base_url, steps):
    login = LoginPage(driver, base_url)
    pacientes = PacientesPage(driver, base_url)
    steps("login medico")
    login.login_expect_home("medico", "medico")
    steps("abrir /pacientes y esperar fin de carga")
    pacientes.open_list()
    steps("assert tabla con columnas y filas")
    pacientes.assert_table_ready()
    n = pacientes.count_edit_buttons()
    steps(f"botones editar encontrados={n}")
    assert n >= 1, "Se esperaba al menos 1 paciente en el listado"


@pytest.mark.pacientes
@pytest.mark.case(id="PAC-02", cp="CP-10", name="Abrir editar paciente y volver")
def test_pac_02_editar_form(driver, base_url, steps):
    login = LoginPage(driver, base_url)
    pacientes = PacientesPage(driver, base_url)
    steps("login medico")
    login.login_expect_home("medico", "medico")
    steps("abrir listado pacientes")
    pacientes.open_list()
    steps("click primer boton editar")
    pacientes.open_first_edit()
    steps("assert formulario de edicion visible")
    pacientes.assert_edit_form_visible()
    steps("cancelar o volver al listado")
    pacientes.cancel_or_back_if_possible()
