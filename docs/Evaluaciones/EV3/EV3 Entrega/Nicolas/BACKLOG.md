# BACKLOG — Nicolás Barra (EV3 / EP5)

**Continuidad EV2:** autenticación, sesión JWT, RBAC, auditoría, documentos, Selenium, SQLMap.  
**Tablero equipo:** [`../00_Backlog_Equipo.md`](../00_Backlog_Equipo.md)  
**Evidencias:** [`../Evidencias/`](../Evidencias/)  
**Suite base EV2:** `docs/Evaluaciones/EV2/EV2 Entrega/Nicolas/selenium_suite/`

Estándares a citar en bitácora al cerrar cada item: **ISO/IEC 25010** (seguridad/fiabilidad), **27001** (A.5 secretos, A.8/A.9 acceso y registro), **29119** (evidencia de prueba), Ley **20.584** art. 13 / **19.628** art. 11 / **DS 41** arts. 8–9.

---

## Checklist rápido

- [ ] EV3-00 Baseline  
- [ ] EV3-01 INC-01 bcrypt  
- [ ] EV3-02 INC-02 JWT env  
- [ ] EV3-03 INC-03 logout revoca  
- [ ] EV3-05 INC-07 `/roles`  
- [ ] EV3-06 INC-14 POST auditoría  
- [ ] EV3-07 INC-13 descarga auditada  
- [ ] EV3-10 Selenium obligatorio  
- [ ] EV3-11 SQLMap retest  
- [ ] EV3-15 Wireshark sesión  
- [ ] Handoff a Giannina  

---

## EV3-00 — Branch, Docker y baseline

### Objetivo
Dejar un punto de partida reproducible antes de tocar código.

### Pasos

1. **Git**
   1. `git fetch origin && git checkout main && git pull`
   2. `git checkout -b feature/ev3-remediacion` (si ya existe, `git checkout feature/ev3-remediacion && git pull`)
   3. Confirmar working tree limpio o solo archivos EV3 Entrega.

2. **Docker**
   1. Abrir Docker Desktop.
   2. En la raíz del repo: `docker compose up -d --build`
   3. Verificar: FE http://localhost:3333 · API http://localhost:4444/docs
   4. Login smoke con `medico` / seed actual (anotar si aún es texto plano).

3. **Baseline Selenium (pre-remediación)**
   1. Ir a la suite EV2 o copiarla a `EV3 Entrega/Nicolas/selenium_suite/` (preferible copiar para no pisar EV2).
   2. Activar venv e instalar `requirements.txt`.
   3. Ejecutar:
      ```powershell
      $env:SELENIUM_HEADLESS="1"
      pytest -v --html=../../Evidencias/Selenium/EV3-00-baseline-report.html --self-contained-html
      ```
   4. Guardar `report.json` / capturas con prefijo `EV3-00-baseline-`.
   5. En bitácora: pass/fail count y commit hash.

### DoD
- [ ] Branch activa  
- [ ] Compose healthy  
- [ ] Baseline Selenium archivada en `Evidencias/Selenium/`  

### Criterio de aceptación
Ambiente usable por Ari/Skarlett el mismo día; baseline con fecha y hash.

---

## EV3-01 — INC-01 Contraseñas con bcrypt

### Objetivo
Dejar de guardar/comparar contraseñas en texto plano (crítico EV2 / CP-15).

### Subpasos técnicos

1. **Localizar código**
   - Backend: rutas de `auth` (login, registro), modelo/tabla `usuarios`, seeds.
   - Confirmar campo `contrasena` y puntos de comparación (`===` texto plano).

2. **Implementar**
   1. Añadir dependencia `bcrypt` (o la ya usada en el stack) al backend.
   2. Al **crear/actualizar** usuario: `hash = bcrypt.hash(plain, rounds≥10)`.
   3. Al **login**: `bcrypt.compare(plain, hash)`; nunca loguear el hash ni la plain.
   4. Política: rechazar claves &lt; 12 caracteres (alineado a recomendación EP4).
   5. Actualizar seeds: generar hashes para `admin`, `medico`, `paciente` (documentar las nuevas claves de prueba en bitácora **privada del equipo**, no en README público si el repo es compartido; si deben quedar en informe, usar claves sintéticas de laboratorio).

3. **Migración de datos existentes**
   - Script one-shot o recrear volumen Docker limpio + seeds.
   - Anotar en bitácora el método elegido.

4. **Prueba manual / Postman**
   1. Login válido → 200 + token.
   2. Login inválido → 401.
   3. Registro con clave corta → 400 (o el código que definan).
   4. Consulta SQL/`psql`: valor en `contrasena` **no** debe ser legible como `admin`/`medico`.

5. **Evidencia**
   - `Evidencias/Postman/EV3-01-login-ok.png`
   - `Evidencias/Postman/EV3-01-login-401.png`
   - `Evidencias/Postman/EV3-01-db-hash.png` (o volcado redactado)
   - Avisar a **Ari** para EV3-13 (John).

### DoD
- [ ] Código en branch  
- [ ] Seeds/hashes OK  
- [ ] Evidencias Postman + DB  
- [ ] Norma citada: 19.628 art. 11 / 27001 control de autenticación  

### Criterio de aceptación
No es posible autenticarse comparando texto plano; DB no muestra claves en claro.

---

## EV3-02 — INC-02 Secreto JWT fuera del repositorio

### Objetivo
Eliminar el secreto hardcodeado / versionado.

### Pasos

1. Buscar en repo: `JWT_SECRET`, `secret`, strings de firma en `auth.js` y README.
2. Mover a variable de entorno (`process.env.JWT_SECRET`); fallar al arrancar si falta.
3. Añadir `.env.example` con placeholder `JWT_SECRET=change-me-in-local`.
4. Asegurar `.env` en `.gitignore`.
5. Rotar el valor respecto del filtrado en EV2.
6. Actualizar `docker-compose` / env del contenedor API.
7. Evidencia: grep limpio (captura) + README sin secreto real + login aún funciona.

### DoD
- [ ] Sin secreto real en git  
- [ ] Arranque exige env  
- [ ] Login OK con nuevo secreto  

---

## EV3-03 — INC-03 Logout con revocación de token

### Objetivo
Tras cerrar sesión, el mismo JWT no debe autorizar la API (falla histórica CP-07).

### Diseño mínimo aceptable
- Endpoint `POST /auth/logout` (o el path que use el FE) que:
  - Exige Bearer token.
  - Inserta `jti` (o el token hash) en denylist en memoria/Redis/tabla hasta `exp`.
- Middleware de autenticación consulta denylist.
- FE: botón cerrar sesión llama al endpoint y limpia storage.

### Pasos de prueba (retest CP-07)

1. Login → copiar token.
2. Logout UI (Selenium o manual).
3. Postman: `GET /examenes` con el **mismo** token → **401** (esperado post-fix).
4. Evidencias:
   - `EV3-03-token-antes-200.png`
   - `EV3-03-logout-ui.png`
   - `EV3-03-token-despues-401.png`

### DoD
- [ ] Endpoint + denylist  
- [ ] Retest CP-07 Aprobado  
- [ ] Caso Selenium AUTH-logout-revocado (ver EV3-10)  

### Criterio de aceptación
UI vuelve a login **y** API rechaza el token previo.

---

## EV3-05 — INC-07 Proteger `/roles`

### Objetivo
Crear/editar/eliminar roles solo con JWT de administrador.

### Pasos

1. Abrir `roles` router; identificar rutas POST/PUT/PATCH/DELETE sin middleware.
2. Aplicar el mismo middleware de auth + check de rol `administrador` (o el nombre seed).
3. Pruebas Postman:
   | Caso | Esperado |
   |------|----------|
   | Sin token | 401 |
   | Token médico | 403 |
   | Token admin | 2xx en operación permitida |
   | GET si aplica | según ERS (documentar) |
4. Evidencias `EV3-05-*.png`.
5. Coordinar con Skarlett: confirmación en código + Sonar no es suficiente; esta es prueba dinámica.

### DoD
- [ ] Middleware en todas las mutaciones  
- [ ] Matriz negativa/positiva archivada  

---

## EV3-06 — INC-14 Restringir `POST /auditoria`

### Objetivo
Impedir que un médico (u otro rol) fabrique registros de auditoría.

### Pasos

1. Revisar `auditoria` router: ¿quién puede POST?
2. Opciones válidas (elegir una y documentarla):
   - Solo el propio backend escribe auditoría (quitar POST público), **o**
   - Solo rol admin, **o**
   - Solo servicio interno.
3. Preferencia de seguridad: **escritura solo interna** desde capas de negocio; si se mantiene POST, exigir admin.
4. Retest: token médico + POST inventado → **401/403** (no 201).
5. Evidencia `EV3-06-medico-post-auditoria-rechazado.png`.

### DoD
- [ ] 201 arbitrario eliminado  
- [ ] Bitácora cruzada con INC-13  

---

## EV3-07 — INC-13 Auditar descargas de documentos

### Objetivo
Toda descarga de documento clínico deja traza en `auditoria` (DS 41 integridad/trazabilidad).

### Pasos

1. Localizar handler de descarga (`GET` documento / stream).
2. Tras autorización OK y antes/después de enviar el archivo, insertar evento p.ej.  
   `DOCUMENTOS_DESCARGAR: usuario X descargó documento Y del examen Z`.
3. Flujo de prueba:
   1. Login médico o paciente autorizado.
   2. Descargar un PDF de prueba.
   3. `GET /auditoria` (admin) → debe aparecer el evento.
4. Evidencias UI + API: `EV3-07-descarga.png`, `EV3-07-auditoria-con-descarga.png`.

### DoD
- [ ] Evento reproducible  
- [ ] No rompe control de acceso existente (CP-12)  

---

## EV3-10 — Suite Selenium obligatoria (extensión)

### Objetivo
Automatización UI como evidencia principal de regresión post-remediación (requisito EP5).

### Subpasos

1. **Copiar / versionar suite** bajo `EV3 Entrega/Nicolas/selenium_suite/` (partir de EV2).
2. **Mantener** casos 11/11 que ya pasan (AUTH/RBAC/PAC/EXA/RES).
3. **Agregar** (mínimo):
   | ID | Qué valida | Relación |
   |----|------------|----------|
   | AUTH-04 | Logout + reuso token vía API helper o aserción documentada | INC-03 / CP-07 |
   | RBAC-04 | Admin accede gestión roles/usuarios; médico no | INC-07 / CP-08 |
   | AUD-01 | Tras descarga, mensaje/listado o verificación API en fixture | INC-13 |
   | SMOKE-POST | Login tres roles tras bcrypt | INC-01 |
4. Esperas explícitas (no `sleep` fijos); Page Objects.
5. Ejecución final:
   ```powershell
   $env:SELENIUM_HEADLESS="1"
   pytest -v --html=../../Evidencias/Selenium/EV3-10-report.html --self-contained-html
   ```
6. Archivar `report.html`, `report.json`, `*-passed.png`, log pytest en `Evidencias/Logs/`.

### DoD
- [ ] Suite verde post-remediación (o fallos solo por bugs residuales documentados)  
- [ ] Informe HTML autocontenido  
- [ ] KPI: pass rate y duración para Giannina  

### Criterio de aceptación
Selenium cubre al menos login, logout/revocación (o evidencia dual UI+API), RBAC y un flujo clínico básico.

---

## EV3-11 — SQLMap retest (login)

### Objetivo
Confirmar que el login sigue sin inyección SQL tras cambios de auth.

### Pasos

1. Levantar API.
2. Ejecutar SQLMap **solo** contra el endpoint de login de laboratorio (mismo alcance ético EV2).
3. Incluir marcador JSON correcto si el body es JSON.
4. Guardar output en `Evidencias/Logs/EV3-11-sqlmap.txt`.
5. Conclusión en bitácora: injectable / no injectable; payloads manuales OR 1=1 → 401.

### DoD
- [ ] Output archivado  
- [ ] Sin ampliar alcance a producción real (solo Docker local)  

---

## EV3-15 — Wireshark (sesión / login)

### Objetivo
Evidenciar tráfico HTTP de autenticación (riesgo residual sin TLS o mejora si ya hay TLS).

### Pasos

1. Instalar Wireshark; capturar interfaz loopback/`any` hacia puertos 3333/4444.
2. Filtro sugerido: `tcp.port == 4444 || tcp.port == 3333`.
3. Reproducir: login + una petición API con Bearer.
4. Si **no** hay TLS: anotar que credenciales/token viajan en claro (apoyo a CP-14 / DS 41 art. 8).
5. Si **hay** TLS: mostrar handshake; payload no legible.
6. Exportar `Evidencias/Wireshark/EV3-15-login.pcapng` + PNG del follow stream redactando secretos en la captura publicada si hace falta (en informe: enmascarar).

### DoD
- [ ] `.pcapng` + imagen anotada  
- [ ] Párrafo listo para Giannina (§2 o §5)  

---

## Handoff a Giannina

Al cerrar tus items P0, entregar:

1. `Bitacora_Ejecucion.md` (crear en esta carpeta cuando empieces a ejecutar).  
2. Tabla INC: ID · estado (Verificado/Abierto) · evidencia path · CP relacionado.  
3. Números Selenium: total, passed, failed, duración.  
4. Texto corto §5.2 para CP-01, 03, 07, 08, 12, 13 (y los que toques).  
5. Una frase de remediación por INC cerrado para §6.

Plantilla de fila de bitácora:

| Fecha | Item | Herramienta | Resultado | Evidencia | INC | Notas / norma |
|-------|------|-------------|-----------|-----------|-----|---------------|
| AAAA-MM-DD | EV3-03 | Postman+UI | Verificado | Evidencias/... | INC-03 | 25010 seguridad; 20.584 art.13 |

---

## Orden recomendado de trabajo (días)

| Día | Foco |
|-----|------|
| D1 | EV3-00 + EV3-02 + EV3-01 |
| D2 | EV3-03 + EV3-05 + EV3-06 |
| D3 | EV3-07 + EV3-15 |
| D4 | EV3-10 Selenium extensión + corrida final |
| D5 | EV3-11 + handoff Giannina + buffer flaky |

Coordinar con Ari el día de EV3-01 (John) y EV3-04 (delay) para no chocar en `app` middleware.
