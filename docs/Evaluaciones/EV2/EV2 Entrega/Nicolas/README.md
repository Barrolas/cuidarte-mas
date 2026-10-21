# Paquete de ejecución — Nicolás Barra (EP3)

Material para ejecutar **tus** casos sin experiencia previa en las herramientas.

## Orden de lectura (no saltes pasos)

1. [`00_ANTES_DE_EMPEZAR.md`](./00_ANTES_DE_EMPEZAR.md) — qué es cada herramienta y el mapa mental  
2. [`01_Setup_Docker.md`](./01_Setup_Docker.md) — levantar Cuidarte+  
3. [`02_Setup_Postman.md`](./02_Setup_Postman.md) — primer request a la API  
4. [`03_Setup_Selenium.md`](./03_Setup_Selenium.md) — primer test UI automatizado  
5. [`04_Playbook_Ejecucion_CP.md`](./04_Playbook_Ejecucion_CP.md) — **paso a paso de cada CP** (ERS + evidencias)  
6. [`05_Buenas_Practicas_Observaciones.md`](./05_Buenas_Practicas_Observaciones.md) — **recomendaciones de informe** (lockout, formularios…; sin prueba ni captura extra)  
7. [`Bitacora_Ejecucion.md`](./Bitacora_Ejecucion.md) — resultados CP + borrador REC  

**Entregable EP3:** evidencia de CP + bitácora + texto de recomendaciones. **No** codear. 

## Carpetas

| Carpeta | Uso |
|---------|-----|
| `Evidencias/` | Capturas y exports por CP (`Evidencias/CP-01/`, etc.) |
| `postman/` | Colección importable |
| `selenium_suite/` | Script Python de smoke + requirements |

## Cuentas de prueba (dump del repo)

| Usuario | Contraseña | Rol |
|---------|------------|-----|
| `admin` | `admin` | Administrador |
| `medico` | `medico` | Médico |
| `paciente` | `paciente` | Paciente |

Solo ambiente local. No uses datos reales de pacientes.
