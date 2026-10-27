# 03 — Setup Selenium (desde cero)

Objetivo: que un script abra Chrome, entre a Cuidarte+ y haga login solo.

---

## 3.1 ¿Qué hace Selenium?

En vez de hacer tú los clics, un programa:

1. Abre el navegador  
2. Va a http://localhost:3333  
3. Escribe usuario/contraseña  
4. Pulsa Entrar  
5. Comprueba que llegaste al home  
6. (Opcional) guarda una captura  

Tú solo ejecutas un comando. Si falla, el mensaje te dice qué no encontró.

---

## 3.2 Instalar Python

1. Abre https://www.python.org/downloads/  
2. Descarga Python 3.11 o 3.12 para Windows.  
3. En el instalador marca **“Add python.exe to PATH”**.  
4. Finish.

Comprobar en PowerShell **nueva**:

```powershell
python --version
pip --version
```

Si `python` no se reconoce, prueba `py --version`.

---

## 3.3 Crear entorno virtual e instalar paquetes

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

Cuando el venv está activo, el prompt suele mostrar `(.venv)`.

---

## 3.4 Tener Chrome instalado

Selenium usa Chrome (o Edge). Instala Google Chrome si no lo tienes.  
El paquete `webdriver-manager` descarga el driver solo la primera vez.

---

## 3.5 Docker debe estar arriba

Antes de correr el test:

1. `docker compose up -d` en la raíz del repo (guía 01).  
2. Abre http://localhost:3333 a mano y confirma que carga.

---

## 3.6 Primer test (smoke login)

Con el venv activado y en la carpeta `selenium_suite`:

```powershell
python test_smoke_login.py
```

### Éxito

Verás algo como:

```
[OK] Login medico -> /home
```

y una captura en `../Evidencias/CP-01/selenium-login-medico.png`.

### Fallo típico

| Mensaje / síntoma | Qué hacer |
|-------------------|-----------|
| Connection refused / ERR_CONNECTION | Docker no está up o puerto 3333 ocupado |
| Timeout finding element | La página cambió o carga lenta; espera y reintenta |
| Credenciales inválidas / no navega a home | Usuario/clave o seed BD; prueba login manual |

---

## 3.7 Suite de flujos (recomendado)

Además del smoke, corre la suite alineada a tus CP:

```powershell
python test_suite_flujos.py
```

Cubre: login inválido, login médico, pacientes, exámenes, RBAC médico/admin en `/usuarios`, Mis Resultados (paciente), logout UI.

Evidencias y log:

- Capturas: `../Evidencias/Selenium/01-…08-….png`
- Log terminal: `../Evidencias/Selenium/suite-output.txt`

Opcional sin ventana de Chrome:

```powershell
$env:SELENIUM_HEADLESS="1"
python test_suite_flujos.py
```

---

## 3.8 Cómo lo usarás en los CP

1. Suite Selenium = evidencia automatizable de humo + RBAC/navegación.  
2. Flujos profundos (upload formatos, auditoría API, SQLMap) siguen en manual/Postman.  
3. Anotas en la bitácora: smoke + suite.

---

## Listo → siguiente

[`04_Playbook_Ejecucion_CP.md`](./04_Playbook_Ejecucion_CP.md)
