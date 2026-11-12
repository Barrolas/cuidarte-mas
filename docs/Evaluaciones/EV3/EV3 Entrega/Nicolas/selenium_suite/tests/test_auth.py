import pytest
from selenium.webdriver.common.by import By

from pages import LoginPage, Layout


@pytest.mark.auth
@pytest.mark.case(id="AUTH-01", cp="CP-01", name="Login invalido")
def test_auth_01_login_invalido(driver, base_url, steps):
    login = LoginPage(driver, base_url)
    steps("abrir /login")
    steps("enviar credenciales invalidas")
    login.login("usuarioinvalido", "ClaveIncorrecta#1")
    steps("esperar mensaje Credenciales invalidas")
    text = login.wait_invalid_credentials_message()
    steps("assert URL contiene /login")
    assert "/login" in driver.current_url
    assert "Credenciales" in text or "inválid" in text.lower()


@pytest.mark.auth
@pytest.mark.smoke
@pytest.mark.case(id="AUTH-02", cp="CP-01", name="Login medico OK")
def test_auth_02_login_medico(driver, base_url, steps):
    login = LoginPage(driver, base_url)
    layout = Layout(driver, base_url)
    steps("login medico/medico")
    login.login_expect_home("medico", "medico")
    steps("assert URL /home")
    assert "/home" in driver.current_url
    steps("assert rol Medico visible")
    assert layout.role_label_visible("Medico") or layout.role_label_visible("medico")


@pytest.mark.auth
@pytest.mark.case(id="AUTH-03", cp="CP-07", name="Logout UI a login")
def test_auth_03_logout(driver, base_url, steps):
    login = LoginPage(driver, base_url)
    layout = Layout(driver, base_url)
    steps("login medico")
    login.login_expect_home("medico", "medico")
    steps("esperar home estable")
    layout.sleep(1.2)
    steps("abrir menu usuario y Cerrar sesion")
    layout.logout()
    steps("assert URL /login")
    assert "/login" in driver.current_url
