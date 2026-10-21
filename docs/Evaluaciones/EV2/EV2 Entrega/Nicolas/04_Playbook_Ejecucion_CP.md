# 04 — Playbook de ejecución (CP de Nicolás)

**Prerrequisito:** guías 00 → 01 → 02 → 03 hechas, checklist del final de `00_ANTES_DE_EMPEZAR.md` en verde.

Abre también [`Bitacora_Ejecucion.md`](./Bitacora_Ejecucion.md) y ve llenándola **al terminar cada CP**.

Convención de evidencias: `Evidencias/CP-XX/descripcion.png` (o `.json` exportado) — **solo** para lo que pide el ERS.

Recomendaciones de buenas prácticas (lockout, formularios, etc.) **no se ejecutan como prueba ni llevan captura**: van al informe más adelante. Ver [`05_Buenas_Practicas_Observaciones.md`](./05_Buenas_Practicas_Observaciones.md).

---

## Plantilla mental de cada CP

Para cada caso harás siempre:

1. **Precondiciones** (Docker, usuario correcto).  
2. **Pasos UI** (navegador o Selenium).  
3. **Pasos API** (Postman), si aplica.  
4. **Observar** resultado vs esperado (ERS).  
5. **Guardar evidencia** de ese resultado.  
6. **Anotar bitácora** (Aprobado / Falla / Bloqueado).  
7. Si falla de forma prevista → **INC-xx**; si es nuevo → **BUG-00x**.

Las REC del informe se arman al final (o de a poco en la tabla de recomendaciones), sin pasos extra aquí.

---

# OLEADA P0 — Autenticación y acceso

## CP-01 — Autenticación válida y rechazo de inválidas

**ERS:** RF-1.1, NFR-SEG-9 (y se observa NFR-SEG-2 de paso).  
**Herramientas:** Selenium o UI manual + Postman.

### A. Login válido (UI)

1. Abre http://localhost:3333/login  
2. En **Nombre de usuario** escribe `medico`  
3. En **Contraseña** escribe `medico`  
4. Pulsa **Entrar**  
5. **Esperado:** entras al sistema (URL con `/home` o dashboard); mensaje de éxito opcional.  
6. Captura: `Evidencias/CP-01/ui-login-medico-ok.png`

**Con Selenium (opcional si ya tienes el smoke):**

```powershell
cd ...\Nicolas\selenium_suite
.\.venv\Scripts\Activate.ps1
python test_smoke_login.py
```

### B. Login inválido (UI)

1. Cierra sesión si estás dentro (menú usuario → salir), o abre ventana privada.  
2. Usuario `medico`, contraseña `ClaveIncorrecta#1`  
3. Pulsa Entrar  
4. **Esperado:** NO entras; mensaje tipo “Credenciales inválidas”; sigues en login.  
5. Captura: `Evidencias/CP-01/ui-login-invalido.png`

### C. Mismo flujo por API (Postman)

1. Request **Login medico** → 200 + `token`  
2. Request nuevo o duplicado: body con password incorrecta → **401** y **sin** token usable  
3. Capturas de ambas respuestas (URL + status + body; token puedes recortar).

### Resultado

- Si A+B+C OK → **Aprobado**  
- Si login inválido igual deja entrar → **Falla** (seguridad)  
- Incidentes posibles: INC-01, INC-02 (password en claro / JWT débil si lo confirmas)

*(Lockout / mensajes de formulario: solo recomendación de informe — REC-01/03 en `05_…`; no hace falta evidenciarlo aquí.)*

---

## CP-07 — Cierre de sesión y revocación del token

**ERS:** RF-1.2, NFR-SEG-9.  
**Herramientas:** Postman (principal). UI de logout si existe.

### Pasos API (obligatorios)

1. **Login** como `medico` → guarda `token` en environment.  
2. **GET** `{{baseUrl}}/examenes` con header `Authorization: Bearer {{token}}`  
   - Esperado: **200** (el token sirve).  
3. En la UI: busca **Cerrar sesión / Logout** y úsalo.  
   - Si **no hay** botón/ruta de logout → anótalo (el handoff espera **INC-03**: no hay logout que invalide el JWT).  
4. Sin hacer login de nuevo, en Postman vuelve a **GET /examenes** con el **mismo** token de antes.  
   - **Esperado ideal:** **401**.  
   - **Esperado probable en este repo:** sigue **200** (token aún válido hasta expirar) → **Falla** del caso / confirma **INC-03**.

5. Evidencias:  
   - `CP-07/api-token-antes-200.png`  
   - `CP-07/api-token-despues-logout.png` (401 o 200)  
   - `CP-07/ui-logout-o-ausencia.png`

### Cómo marcar

| Observación | Resultado |
|-------------|-----------|
| Tras logout el token da 401 | Aprobado |
| No hay logout o el token sigue vivo | Falla + INC-03 |

---

## CP-08 — Administración de usuarios (admin)

**ERS:** RF-2.5, 2.6, 2.7, RB-2, NFR-SEG-4.  
**Herramientas:** UI (admin) + Postman.

### A. Como administrador (UI)

1. Login `admin` / `admin`  
2. Menú **Usuarios** (ruta `/usuarios`)  
3. Verifica que ves el listado. Captura: `CP-08/ui-admin-lista-usuarios.png`  
4. Edita un usuario de prueba (o crea uno vía registro previo): cambia correo o rol si la UI lo permite. Captura.  
5. Elimina un usuario **sintético** (no borres `admin`/`medico`/`paciente` del seed si puedes evitarlo). Debe pedir **confirmación**. Captura del diálogo.

### B. API admin

1. Login Postman como `admin` → token.  
2. `GET {{baseUrl}}/usuarios` → 200  
3. (Opcional) `PUT` / `DELETE` según Swagger sobre un usuario de prueba.

### C. Control negativo (médico no es admin)

1. Login Postman como `medico`.  
2. `GET {{baseUrl}}/usuarios`  
3. **Esperado:** **401 o 403** (no lista usuarios).  
4. Captura: `CP-08/api-medico-usuarios-403.png`

### Incidentes

- INC-07 / INC-09 si ves comportamientos raros en roles/borrado (documenta lo observado).

---

## CP-12 — Paciente ve solo sus exámenes

**ERS:** RF-4.1.  
**Herramientas:** UI paciente + API.

### Pasos

1. Login UI `paciente` / `paciente`  
2. Ve a la vista de resultados/exámenes del paciente (p. ej. mis resultados).  
3. Anota qué exámenes ves. Captura.  
4. Postman: login paciente → `GET /examenes/paciente/{paciente_id}` (usa el id del token/perfil; en dump suele existir paciente ligado).  
5. Intenta `GET /examenes` o un `GET /examenes/{id}` de un examen **ajeno** si conoces un id de otro paciente.  
6. **Esperado:** solo ves lo propio; acceso ajeno → 403/401/vacío controlado, nunca datos de otro.

Si ves datos de otros → **Falla** grave.

---

# OLEADA P1 — Auditoría y documentos

## CP-03 — Auditoría de acciones críticas

**ERS:** RF-5.1 (+ cumplimiento).  
**Herramientas:** Postman + UI admin/médico.

### Pasos (hazlos en orden y anota la hora)

1. Login `medico` (API + UI).  
2. **Sube** un PDF pequeño a un examen (UI detalle de examen o Postman `POST /documentos` multipart).  
3. **Descarga** ese documento (`GET /documentos/:id`).  
4. Con token `admin` (o quien pueda): `GET {{baseUrl}}/auditoria`  
5. Busca eventos recientes de subida/descarga/eliminación.

### Esperado vs INC

| Qué buscas | Si no aparece | Marca |
|------------|---------------|-------|
| Evento de **descarga** | Confirmado en handoff | Falla / **INC-13** |
| Evento de subida/creación | Según implementación | Anota si falta |
| `POST /auditoria` abierto sin control | Probar POST sin sentido | **INC-14** si acepta |

Evidencias: request/response de upload, download, listado auditoría.

### Extra INC-14 (rápido)

1. Sin privilegios especiales, prueba `POST {{baseUrl}}/auditoria` con body inventado (mira Swagger).  
2. Si crea registro sin autenticación/rol adecuado → INC-14.

---

## CP-11 — Editar y baja lógica de exámenes/documentos

**ERS:** RF-3.2, RF-3.3.

### Pasos UI (médico)

1. Login `medico`  
2. Lista de exámenes → abre uno → **Editar** (cambiar observación). Guardar. Captura.  
3. Eliminar examen o documento: debe pedir **confirmación**.  
4. Tras eliminar, verifica que no aparece como activo (baja lógica) o que ya no está listado.  
5. API opcional: `PUT /examenes/:id`, `DELETE /examenes/:id` con token médico.

Si borra sin confirmación → anotar desviación (puede ligar INC-09).

---

## CP-13 — Documentos: formatos, storage y tiempo (flujo Nicolás)

**ERS:** RF-4.2, 4.3, 4.4.  
**Tú:** flujo y formatos. **Ari:** medir ≤10 s / JMeter.

### Partición de formatos (médico)

Prepara 5 archivos chicos: `.pdf`, `.doc` o `.docx`, `.ppt` o `.pptx`, `.jpg`, `.png`.

Para cada uno:

1. Intenta adjuntarlo al examen.  
2. Anota: ¿aceptó? ¿rechazó? ¿mensaje?  
3. Captura por formato: `CP-13/upload-pdf.png`, etc.

**Handoff:** DOC/PPT pueden rechazarse → **INC-15** si ocurre.

### Storage (RF-4.4) — INC-16

1. Tras un upload PDF exitoso, revisa carpeta del repo `BACKEND/uploads` (volumen Docker).  
2. O consulta en BD (con ayuda) si el documento quedó como `bytea` en tabla.  
3. Si está en BD como bytes y no en storage interno limpio → documentar **INC-16**.

### Descarga paciente

1. Login `paciente`  
2. Descargar un documento propio.  
3. Anota si funciona; el **cronómetro formal** lo deja Ari, pero puedes anotar tiempo aproximado.

---

# OLEADA P2 — CRUD clínico

## CP-02 — Médico registra examen

1. Login `medico`  
2. Ir a Exámenes → crear nuevo: elegir paciente, tipo, observaciones.  
3. Guardar.  
4. Verificar que aparece en listado/detalle.  
5. Postman: `POST /examenes` con JSON válido (mira Swagger para campos).  
6. Evidencias UI + API 200/201.

---

## CP-09 — Registro rápido (rol paciente)

1. En http://localhost:3333/registro (o link “Regístrate”)  
2. Crea usuario sintético: ej. `paciente.cp09` / clave que cumpla política (≥12 con mayúscula, minúscula, número, símbolo) si el front la exige.  
3. Tras registro, login con esa cuenta.  
4. Verifica que el rol es paciente (menú limitado).  
5. Prueba también una clave débil `123` → debe rechazar (valores límite).

Si acepta claves débiles o no asigna rol paciente → Falla / posible INC-10.

---

## CP-10 — Gestión de pacientes (médico/admin)

1. Login `medico` o `admin`  
2. **Crear** paciente sintético (nombre, rut ficticio, etc.).  
3. **Editar** ese paciente.  
4. **Ver** detalle.  
5. Capturas de los tres pasos.  
6. Relaciona con RB-3: el médico puede ver clínica del paciente (OC-01 es observación normativa; anótala si el handoff lo pide).

---

# CP-04 (tu parte) — SQLMap en login

**Solo Docker local.** No escanees internet.

### Setup rápido SQLMap (Windows)

Opción A — pip:

```powershell
pip install sqlmap
```

(Si el comando es un script, a veces se invoca como `python -m sqlmap` según instalación.)

Opción B — clonar https://github.com/sqlmapproject/sqlmap y correr `python sqlmap.py ...`

### Comando acotado (educativo)

Con Docker arriba:

```powershell
python sqlmap.py -u "http://localhost:4444/autenticacion/login" --data="nombre_usuario=medico&password=medico" --batch --level=1 --risk=1 --technique=B --timeout=10
```

Ajusta si la API solo acepta JSON (entonces usa `--headers="Content-Type: application/json"` y data JSON; consulta la ayuda de sqlmap para JSON).

### Qué reportar

- ¿Encontró inyección?  
- Captura del resumen.  
- Ari completa ZAP/Burp/Nikto; tú adjuntas solo tu evidencia SQLMap en `Evidencias/CP-04/`.

Si SQLMap no corre por formato JSON, documenta el intento y prueba alternativa Postman con payload `' OR 1=1 --` en `nombre_usuario` (como EV1): esperado **401**.

---

# Cierre del día de pruebas

1. Revisa que cada CP tuyo tiene fila en la bitácora.  
2. Carpeta `Evidencias/CP-*` con al menos 1 archivo por CP ejecutado.  
3. Lista INC-13…16: confirmado / no confirmado.  
4. Avisa a **Giannina** (integración §5) y coordina con **Ari** lo compartido (CP-04, tiempos CP-13).  
5. (Opcional) `git add` + commit de bitácora y evidencias cuando el equipo acuerde.

---

## Tabla rápida — tus CP

| CP | Prioridad | UI | API | Notas |
|----|-----------|----|-----|-------|
| 01 | P0 | Sí | Sí | Login ok/fail |
| 07 | P0 | Logout si hay | Sí | INC-03 probable |
| 08 | P0 | Admin | Sí + negativo médico | INC-07/09 |
| 12 | P0 | Paciente | Sí | Solo lo propio |
| 03 | P1 | Parcial | Sí | INC-13/14 |
| 11 | P1 | Sí | Opcional | Confirmación borrado |
| 13 | P1 | Sí | Sí | INC-15/16; tiempo=Ari |
| 02 | P2 | Sí | Sí | Crear examen |
| 09 | P2 | Sí | Opcional | Registro + política clave |
| 10 | P2 | Sí | Opcional | CRUD pacientes |
| 04 | P0 seg. | — | SQLMap | Compartido con Ari |
