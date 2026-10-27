# 03 — Setup Selenium (suite profesional)

Objetivo: automatizar la capa UI de tus CP con **pytest + Page Objects**, generar `report.html` / `report.json` y capturas.

---

## 3.1 ¿Qué hace esta suite?

No solo “abre el login”: valida flujos de autenticación, RBAC, pacientes, exámenes y resultados con esperas explícitas y reporte presentable para la defensa.

Herramientas: Selenium 4, pytest, pytest-html, webdriver-manager, Chrome.

---

## 3.2 Instalar Python y venv

```powershell
cd "E:\CODE\LEARNING\DUOC - INGENIERIA EN INFORMATICA\Seg. y Calidad del Software\cuidarte-mas\docs\Evaluaciones\EV2\EV2 Entrega\Nicolas\selenium_suite"

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Si PowerShell bloquea la activación:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
```

---

## 3.3 Docker arriba

1. En la raíz del repo: `docker compose up -d`  
2. Verifica http://localhost:3333  

---

## 3.4 Smoke (opcional)

```powershell
python test_smoke_login.py
```

Equivale a `pytest -m smoke` (AUTH-02 login médico).

---

## 3.5 Suite profesional (recomendado)

Con venv activo y en `selenium_suite`:

```powershell
$env:SELENIUM_HEADLESS="1"
pytest -v --html=../Evidencias/Selenium/report.html --self-contained-html
```

Sin headless (ves el Chrome): omite `SELENIUM_HEADLESS`.

### Casos (11)

| ID | Qué valida | CP |
|----|------------|-----|
| AUTH-01 | Login inválido + mensaje | CP-01 |
| AUTH-02 | Login médico → home + rol | CP-01 |
| AUTH-03 | Logout UI → login | CP-07 |
| RBAC-01 | Médico sin panel admin usuarios | CP-08 |
| RBAC-02 | Admin lista usuarios seed | CP-08 |
| RBAC-03 | Paciente: Mis Resultados, sin Auditoría/Usuarios admin | CP-12 |
| PAC-01 | Listado pacientes cargado (≥1 fila) | CP-10 |
| PAC-02 | Abrir editar paciente y volver | CP-10 |
| EXA-01 | Listado exámenes + abrir editar | CP-02/11 |
| EXA-02 | Editar observaciones y guardar | CP-11 |
| RES-01 | Paciente Mis Resultados | CP-12 |

### Evidencias generadas

Carpeta `../Evidencias/Selenium/`:

- `report.html` — informe pytest-html (abrir en navegador)
- `report.json` — totales, pasos, duración, screenshot por caso
- `suite-output.txt` — resumen legible
- `{ID}-passed.png` / `{ID}-failed.png`

Estructura del código:

- `pages/` — Page Objects (Login, Layout, Pacientes, Exámenes, Resultados)
- `tests/` — casos por área
- `conftest.py` — driver, capturas, reporte JSON
- `reporting.py` — escritura de report.json / suite-output.txt

---

## 3.6 Relación con las pruebas manuales

Los CP de UI ya ejecutados a mano **siguen válidos**. Selenium **repite en automático** esa capa UI para regresión y evidencia de ingeniería. No reemplaza Postman ni SQLMap.

---

## Fallos típicos

| Síntoma | Qué hacer |
|---------|-----------|
| Connection refused | Docker / puerto 3333 |
| Timeout Cargando… | Backend lento; reintenta |
| Menu logout no abre | Corre con ventana (`SELENIUM_HEADLESS` off) para depurar |

---

## Listo → siguiente

[`04_Playbook_Ejecucion_CP.md`](./04_Playbook_Ejecucion_CP.md)
