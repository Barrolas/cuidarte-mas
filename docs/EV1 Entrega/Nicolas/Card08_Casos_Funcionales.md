# Card 8 — Casos funcionales + auditoría (Nicolás)

**Casos:** CP-01, CP-02, CP-03  
**Rúbrica:** IE2 / IE3  
**API base:** `http://localhost:4444`

---

## CP-01 — Autenticación exitosa y rechazo de credenciales inválidas

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-01 |
| **6.2 Descripción** | Verificar que un usuario válido obtiene un JWT al autenticarse y que credenciales inválidas son rechazadas sin filtrar información sensible. |
| **6.3 Requerimiento asociado** | **RF-1.1**; apoyo **NFR-SEG-9** |
| **6.4 Datos de entrada** | Válidos: `nombre_usuario=medico.qa`, `password=PruebaSegura#2026`. Inválidos: mismo usuario con `password=ClaveIncorrecta#1` |
| **6.5 Resultado esperado** | Login OK → HTTP 200 + `token` JWT. Login fallido → HTTP 401, sin token, mensaje genérico (“Credenciales inválidas”). |
| **6.6 Criterios de aceptación** | Login exitoso genera token de sesión (JWT). El fallo no diferencia “usuario no existe” vs “clave mala” de forma explotable. No se registran contraseñas en claro en logs. |
| **6.7 Tipo de prueba** | Funcional / Seguridad |

**Precondiciones**

- Backend y PostgreSQL levantados (`docker-compose up -d`).
- Usuario `medico.qa` creado con rol Médico.

**Pasos**

1. `POST /autenticacion/login` con body JSON de credenciales válidas.
2. Verificar status 200 y presencia del campo `token`.
3. Decodificar/inspeccionar que el token sea JWT usable en requests posteriores (`Authorization: Bearer …` si aplica).
4. `POST /autenticacion/login` con contraseña inválida.
5. Verificar status 401 y ausencia de `token`.

**Evidencia sugerida:** captura Postman (request/response) de ambos escenarios.

---

## CP-02 — Médico registra examen médico a un paciente

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-02 |
| **6.2 Descripción** | Validar que un médico autenticado puede crear un examen asociado a un paciente existente, con validación de campos obligatorios. |
| **6.3 Requerimiento asociado** | **RF-3.1**; **RB-3** |
| **6.4 Datos de entrada** | Token de `medico.qa`. Paciente_id de prueba. Datos de examen según schema (ej. tipo_examen_id válido, fecha, observaciones: “Control rutinario”). |
| **6.5 Resultado esperado** | Creación exitosa (HTTP 201 o 200 según API) con examen persistido y asociado al `paciente_id` correcto; listable vía `GET /examenes` o `GET /examenes/paciente/:paciente_id`. |
| **6.6 Criterios de aceptación** | Operación de registro funciona; validación rechaza payload incompleto; el médico puede ver la información clínica del paciente (RB-3). |
| **6.7 Tipo de prueba** | Funcional |

**Precondiciones**

- Sesión/token de médico válido (desde CP-01).
- Paciente de prueba existente (`POST /pacientes` o seed).
- Catálogo `GET /tipo-examen` disponible.

**Pasos**

1. Autenticarse como médico (`POST /autenticacion/login`).
2. Obtener/confirmar `paciente_id` de prueba (`GET /pacientes`).
3. `POST /examenes` con payload válido.
4. Verificar persistencia con `GET /examenes/:id` o listado por paciente.
5. Reintentar `POST /examenes` omitiendo un campo obligatorio y verificar rechazo por validación.

**Evidencia sugerida:** IDs creados + respuestas HTTP.

---

## CP-03 — Auditoría de acción crítica (eliminación)

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-03 |
| **6.2 Descripción** | Comprobar que una acción crítica (eliminación de examen o de usuario) deja registro consultable en auditoría. |
| **6.3 Requerimiento asociado** | **RF-5.1**; apoyo **NFR-SEG-6** |
| **6.4 Datos de entrada** | Examen creado en CP-02 (o usuario de prueba). Actor: `medico.qa` (examen) o `admin.qa` (usuario). |
| **6.5 Resultado esperado** | Tras la eliminación, `GET /auditoria` (o registro equivalente) contiene evento con usuario, acción y referencia temporal al recurso afectado. |
| **6.6 Criterios de aceptación** | Se genera registro de auditoría en la acción crítica; si la UI elimina, debe pedir confirmación (criterio ERS RF-3). No deben auditarse secretos (password/token). |
| **6.7 Tipo de prueba** | Funcional / Auditoría (cumplimiento) |

**Precondiciones**

- Examen o usuario de prueba existente.
- Rol autorizado para la operación.
- Endpoint `/auditoria` accesible para el rol que consulta (admin).

**Pasos**

1. Ejecutar `DELETE /examenes/:id` (médico) **o** `DELETE /usuarios/:id` (admin).
2. Confirmar en UI (si aplica) antes de borrar.
3. Consultar `GET /auditoria`.
4. Verificar que existe un evento reciente asociado al actor y a la acción.
5. Verificar que el log no contiene contraseñas ni JWT completos.

**Nota técnica del producto:** el login ya inserta auditoría (`LOGIN: usuario inició sesión`); este caso exige además traza de **eliminación** u otra acción crítica de negocio.

---

## Resumen Card 8

| ID | ERS | Tipo | Prioridad |
|----|-----|------|-----------|
| CP-01 | RF-1.1 | Funcional / Seguridad | P0 |
| CP-02 | RF-3.1 + RB-3 | Funcional | P2 |
| CP-03 | RF-5.1 | Funcional / Auditoría | P1 |

**Checklist**

- [x] Campos 6.1–6.7 en los 3 casos
- [x] Endpoints reales del backend
- [x] Datos sintéticos
