import pytest

from pages import LoginPage, Layout


@pytest.mark.rbac
@pytest.mark.case(id="RBAC-01", cp="CP-08", name="Medico sin panel admin usuarios")
def test_rbac_01_medico_sin_usuarios(driver, base_url, steps):
    login = LoginPage(driver, base_url)
    layout = Layout(driver, base_url)
    steps("login medico")
    login.login_expect_home("medico", "medico")
    steps("navegar a /usuarios")
    layout.open("/usuarios")
    layout.sleep(1.0)
    text = layout.body_text()
    steps("assert no aparece panel admin LISTAR USUARIOS")
    tiene_panel_admin = "Gestión de Usuarios" in text and "LISTAR USUARIOS" in text.upper()
    assert not tiene_panel_admin, "Medico pudo ver panel admin de usuarios"


@pytest.mark.rbac
@pytest.mark.case(id="RBAC-02", cp="CP-08", name="Admin lista usuarios seed")
def test_rbac_02_admin_usuarios(driver, base_url, steps):
    login = LoginPage(driver, base_url)
    layout = Layout(driver, base_url)
    steps("login admin")
    login.login_expect_home("admin", "admin")
    steps("navegar a /usuarios")
    layout.open("/usuarios")
    layout.sleep(1.2)
    text = layout.body_text()
    steps("assert Gestion de Usuarios y filas seed")
    assert "Gestión de Usuarios" in text or "USUARIOS" in text.upper()
    assert "admin" in text.lower()
    assert "medico" in text.lower() or "paciente" in text.lower()


@pytest.mark.rbac
@pytest.mark.case(id="RBAC-03", cp="CP-12", name="Paciente nav Mis Resultados sin Usuarios")
def test_rbac_03_paciente_nav(driver, base_url, steps):
    login = LoginPage(driver, base_url)
    layout = Layout(driver, base_url)
    steps("login paciente")
    login.login_expect_home("paciente", "paciente")
    text = layout.body_text()
    steps("assert Mis Resultados visible")
    assert "Mis Resultados" in text or "Resultados" in text
    steps("assert no Usuarios ni Auditoria en nav paciente")
    # El texto 'Usuarios' no debe aparecer como item de admin; tolerar 'usuario' en perfil
    assert "Auditoría" not in text and "Auditoria" not in text
    assert "Gestión de Usuarios" not in text
