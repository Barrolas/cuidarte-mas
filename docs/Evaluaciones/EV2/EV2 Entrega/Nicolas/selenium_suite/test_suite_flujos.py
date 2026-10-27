"""
Suite Selenium — flujos útiles de los CP de Nicolás (EP3).

Casos:
  1. CP-01  Login inválido (queda en /login + mensaje)
  2. CP-01  Login médico OK (smoke)
  3. CP-10  Médico ve listado de pacientes
  4. CP-02  Médico ve listado de exámenes
  5. CP-08  Médico NO accede a administración de usuarios
  6. CP-08  Admin SÍ ve gestión de usuarios
  7. CP-12  Paciente ve Mis Resultados (menú paciente)
  8. CP-07  Logout UI redirige a /login

Requisito: Docker arriba (http://localhost:3333), Chrome, venv con requirements.

Uso:
  .\\.venv\\Scripts\\Activate.ps1
  python test_suite_flujos.py
"""
from __future__ import annotations

import sys
import time
import traceback
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from helpers import (
    BASE_URL,
    SELENIUM_EVID,
    go,
    login,
    login_ok,
    logout,
    make_driver,
    page_text,
    shot,
    wait,
)


@dataclass
class Result:
    name: str
    ok: bool
    detail: str
    evidence: str = ""
    errors: list[str] = field(default_factory=list)


def case_login_invalido(driver) -> Result:
    name = "CP-01 Login inválido"
    try:
        login(driver, "usuarioinvalido", "ClaveIncorrecta#1")
        time.sleep(1.2)
        url = driver.current_url
        text = page_text(driver)
        path = shot(driver, "01-login-invalido.png")
        assert "/login" in url, f"Debía quedarse en login, URL={url}"
        assert "Credenciales" in text or "inválid" in text.lower() or "invalid" in text.lower(), (
            f"No se vio mensaje de credenciales inválidas. Texto parcial: {text[:200]}"
        )
        return Result(name, True, f"Permanece en login. Captura: {path.name}", str(path))
    except Exception as exc:
        path = shot(driver, "01-login-invalido-FAIL.png")
        return Result(name, False, str(exc), str(path), [traceback.format_exc()])


def case_login_medico(driver) -> Result:
    name = "CP-01 Login médico OK"
    try:
        login_ok(driver, "medico", "medico")
        path = shot(driver, "02-login-medico-ok.png")
        assert "/home" in driver.current_url
        return Result(name, True, f"URL={driver.current_url}. Captura: {path.name}", str(path))
    except Exception as exc:
        path = shot(driver, "02-login-medico-ok-FAIL.png")
        return Result(name, False, str(exc), str(path), [traceback.format_exc()])


def case_medico_pacientes(driver) -> Result:
    name = "CP-10 Médico lista pacientes"
    try:
        login_ok(driver, "medico", "medico")
        go(driver, "/pacientes")
        w = wait(driver, 30)

        def pacientes_listos(d) -> bool:
            t = page_text(d)
            if "Cargando pacientes" in t:
                return False
            return (
                "Gestión de Pacientes" in t
                or "LISTAR PACIENTES" in t.upper()
                or "REGISTRAR PACIENTE" in t.upper()
                or "RUT" in t
            )

        w.until(pacientes_listos)
        time.sleep(0.5)
        text = page_text(driver)
        path = shot(driver, "03-medico-pacientes.png")
        assert "Gestión de Pacientes" in text or "Pacientes" in text
        markers = ("RUT", "Nombre", "LISTAR", "REGISTRAR", "Email", "Teléfono", "telefono")
        assert any(m.lower() in text.lower() for m in markers), f"Sin marcadores de listado. Texto: {text[:300]}"
        return Result(name, True, f"Listado visible. Captura: {path.name}", str(path))
    except Exception as exc:
        path = shot(driver, "03-medico-pacientes-FAIL.png")
        return Result(name, False, str(exc), str(path), [traceback.format_exc()])


def case_medico_examenes(driver) -> Result:
    name = "CP-02 Médico lista exámenes"
    try:
        login_ok(driver, "medico", "medico")
        go(driver, "/examenes")
        time.sleep(1.2)
        text = page_text(driver)
        path = shot(driver, "04-medico-examenes.png")
        assert "Examen" in text or "EXÁMENES" in text.upper() or "Exámenes" in text
        return Result(name, True, f"Listado visible. Captura: {path.name}", str(path))
    except Exception as exc:
        path = shot(driver, "04-medico-examenes-FAIL.png")
        return Result(name, False, str(exc), str(path), [traceback.format_exc()])


def case_medico_sin_usuarios(driver) -> Result:
    name = "CP-08 Médico sin acceso a /usuarios"
    try:
        login_ok(driver, "medico", "medico")
        go(driver, "/usuarios")
        time.sleep(1.2)
        url = driver.current_url
        text = page_text(driver)
        path = shot(driver, "05-medico-sin-usuarios.png")
        # Expectativa: no queda en gestión de usuarios admin
        blocked = (
            "/usuarios" not in url
            or "Gestión de Usuarios" not in text
            or "No autorizado" in text
            or "no tiene permisos" in text.lower()
            or "/home" in url
            or "/login" in url
        )
        # Si la ruta existe pero el contenido de admin no carga, también OK
        if "Gestión de Usuarios" in text and "LISTAR USUARIOS" in text.upper():
            raise AssertionError("Médico pudo ver Gestión de Usuarios (falla RBAC UI)")
        assert blocked or "Usuarios" not in driver.title
        return Result(
            name,
            True,
            f"Sin panel admin de usuarios. URL={url}. Captura: {path.name}",
            str(path),
        )
    except Exception as exc:
        path = shot(driver, "05-medico-sin-usuarios-FAIL.png")
        return Result(name, False, str(exc), str(path), [traceback.format_exc()])


def case_admin_usuarios(driver) -> Result:
    name = "CP-08 Admin lista usuarios"
    try:
        login_ok(driver, "admin", "admin")
        go(driver, "/usuarios")
        time.sleep(1.2)
        text = page_text(driver)
        path = shot(driver, "06-admin-usuarios.png")
        assert "Gestión de Usuarios" in text or "USUARIOS" in text.upper()
        assert "admin" in text.lower() or "medico" in text.lower() or "paciente" in text.lower()
        return Result(name, True, f"Admin ve usuarios. Captura: {path.name}", str(path))
    except Exception as exc:
        path = shot(driver, "06-admin-usuarios-FAIL.png")
        return Result(name, False, str(exc), str(path), [traceback.format_exc()])


def case_paciente_resultados(driver) -> Result:
    name = "CP-12 Paciente Mis Resultados"
    try:
        login_ok(driver, "paciente", "paciente")
        go(driver, "/mis-resultados")
        time.sleep(1.5)
        text = page_text(driver)
        path = shot(driver, "07-paciente-mis-resultados.png")
        assert "Resultado" in text or "Examen" in text or "Mis Resultados" in text
        # Paciente no debería ver menú Usuarios de admin
        nav_ok = "Gestión de Usuarios" not in text
        assert nav_ok
        return Result(name, True, f"Vista paciente OK. Captura: {path.name}", str(path))
    except Exception as exc:
        path = shot(driver, "07-paciente-mis-resultados-FAIL.png")
        return Result(name, False, str(exc), str(path), [traceback.format_exc()])


def case_logout_ui(driver) -> Result:
    name = "CP-07 Logout UI a login"
    try:
        login_ok(driver, "medico", "medico")
        logout(driver)
        time.sleep(0.5)
        path = shot(driver, "08-logout-a-login.png")
        assert "/login" in driver.current_url
        return Result(name, True, f"Logout -> {driver.current_url}. Captura: {path.name}", str(path))
    except Exception as exc:
        path = shot(driver, "08-logout-a-login-FAIL.png")
        return Result(name, False, str(exc), str(path), [traceback.format_exc()])


CASES = [
    case_login_invalido,
    case_login_medico,
    case_medico_pacientes,
    case_medico_examenes,
    case_medico_sin_usuarios,
    case_admin_usuarios,
    case_paciente_resultados,
    case_logout_ui,
]


def main() -> int:
    SELENIUM_EVID.mkdir(parents=True, exist_ok=True)
    started = datetime.now().isoformat(timespec="seconds")
    results: list[Result] = []

    def safe_print(msg: str) -> None:
        try:
            print(msg)
        except UnicodeEncodeError:
            print(msg.encode("ascii", "replace").decode("ascii"))

    safe_print("=== Suite Selenium Cuidarte+ ===")
    safe_print(f"Base URL: {BASE_URL}")
    safe_print(f"Inicio: {started}")
    safe_print(f"Evidencias: {SELENIUM_EVID}")
    safe_print("")

    for case in CASES:
        driver = make_driver()
        try:
            safe_print(f"-> Ejecutando: {case.__name__} ...")
            result = case(driver)
        except Exception as exc:
            result = Result(case.__name__, False, str(exc), errors=[traceback.format_exc()])
        finally:
            driver.quit()

        results.append(result)
        flag = "OK" if result.ok else "FAIL"
        safe_print(f"  [{flag}] {result.name}: {result.detail}")
        safe_print("")

    passed = sum(1 for r in results if r.ok)
    failed = len(results) - passed
    log_path = SELENIUM_EVID / "suite-output.txt"
    lines = [
        f"Suite Selenium Nicolás EP3 — {started}",
        f"Base URL: {BASE_URL}",
        f"Resultado: {passed}/{len(results)} OK, {failed} FAIL",
        "",
    ]
    for r in results:
        lines.append(f"[{'OK' if r.ok else 'FAIL'}] {r.name}")
        lines.append(f"  {r.detail}")
        if r.evidence:
            lines.append(f"  evidencia: {r.evidence}")
        if r.errors:
            lines.append("  traceback:")
            lines.extend("  " + ln for ln in r.errors[0].splitlines()[-15:])
        lines.append("")

    log_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Resumen: {passed}/{len(results)} OK")
    print(f"Log: {log_path}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
