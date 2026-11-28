# EV56-20 — Retest CP-17 (INC-06) en la rama final

**Fecha:** 2026-11-27, 20:06 (UTC-3)  
**Ejecutora:** Skarlett Tropan  
**Commit probado:** `df6fd24d22145d3f7eaf5a66e3a1b9130fc1ea6d` (`origin/feature/skarlett-ep3`, PR #6; incluye los PR #3, #4 y #5 de `dev`)  
**Relacionado:** EV56-09 (INC-06, helper `BACKEND/src/utils/httpErrors.js`), NFR-SEG-6, ISO 27001 A.8.15

## Pasos

1. `git fetch` y checkout limpio de `origin/feature/skarlett-ep3`. Luego `docker compose up -d --build` (API `:4444`, BD `:15442`, FE `:3333`).
2. Login `medico` y errores internos provocados con un ID no numérico (`abc`): `GET /examenes/abc`, `POST /documentos` (`examen_medico_id=abc`), `GET /roles/abc`, `GET /pacientes/abc`, `GET /tipo-examen/abc`.
3. Duplicado 23505: `POST /pacientes` con el RUT existente `11111111-1`.
4. Códigos 401 (`GET /examenes` sin token) y 403 (`GET /auditoria` como médico; `GET /examenes/paciente/999` como paciente).
5. Revisión de `docker logs cuidarteplus-backend-ev` para confirmar que el detalle queda en el servidor.

## Resultado: **PASA**

| Prueba | Respuesta |
|---|---|
| 5 errores internos | `500` `{"error":"<acción>","glosa":"Ocurrió un error interno en el servidor"}`, sin stack, SQL ni mensajes de pg |
| Duplicado 23505 | `400` `{"error":"Error al crear paciente","glosa":"El RUT o email ya existe"}`, sin `duplicate key` ni nombre de restricción |
| 401 / 403 | Mensajes genéricos (`Token inválido`, permisos) |
| Log del servidor | 5 × `invalid input syntax for type bigint`, `code: '22P02'`, con archivo y línea de la ruta |

## Diferencias con la corrida del 25-nov (`46e0f25`)

- Mismos cuerpos `{error, glosa}` y mismos códigos HTTP.
- INC-05 (PR #4): ya no aparece `X-Powered-By`. CORS limitado a `http://localhost:3333` y nuevas cabeceras `X-Content-Type-Options: nosniff` y `X-Frame-Options: DENY`.
- INC-04 (PR #3): `POST /documentos` y el 401 responden en milisegundos; antes tardaban ~5 s por `delayMiddleware`.
- El duplicado 23505 ya no se escribe en el log (el `console.error` quedó solo en el helper de 500). Es esperado, porque es un error de cliente.

## Archivos

- `cp17-rama-final.png`: captura de la sesión de terminal (salida real renderizada).
- `cp17_rama_final_curl.txt`: comandos y respuestas completas, más el extracto de `docker logs`.

Credenciales de laboratorio redactadas como `<REDACTED>` en la captura y en el `.txt`. No se incluyen JWT: solo se muestra el largo del token.
