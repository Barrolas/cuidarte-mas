# EV56-09 — Resumen y bitácora de INC-06

**Incidente:** fuga de `err.message` (y mensajes internos de PostgreSQL) en el cuerpo HTTP 500.  
**Severidad:** **Grave** (se alinea al inventario EV56-22 de Ninna; no se usa «Moderado»).  
**Dueña del fix:** Skarlett Tropan.  
**Estado al 27-nov-2026:** **Verificado (retest)** y mergeado en `origin/dev` `5707693e2f7e9826d645800e89792533329e1b99` (PR #6 y merge PR #7).

## 1. Qué se cambió

Se reemplazaron **35 respuestas 500** que devolvían el error crudo al cliente por un mensaje genérico con el mismo contrato JSON `{ error, glosa }`, dejando el detalle en `console.error` del servidor.

En el refactor (`feature/skarlett-ep3`) el comportamiento se centralizó en:

`BACKEND/src/utils/httpErrors.js` → `sendInternalError(res, err, error, glosa = "Ocurrió un error interno en el servidor")`.

Archivos tocados: las rutas del backend (`auth`, `users`, `pacientes`, `examenes`, `documentos`, `roles`, `audit`, `tipo-examen`) y el middleware `validate.js` (este último usa la glosa `"Ocurrió un error interno al validar los datos"`).

**HTTP 400 intencionales (no son fuga):** por ejemplo el `23505` de paciente duplicado responde `"El RUT o email ya existe"` sin `err.detail` ni nombre de restricción; validaciones de campos requeridos siguen siendo 400 estáticos.

## 2. Bitácora de ejecución (solo localhost)

| Fecha (America/Santiago) | SHA / rama | Qué se hizo | Resultado |
|--------------------------|------------|-------------|-----------|
| 25-nov-2026 (mañana) | `dev` `2d0abc7` (antes) | CP-17: `GET /examenes/abc`, `POST /documentos` con `examen_medico_id=abc`, `GET /roles/abc`, `GET /pacientes/abc`, `GET /tipo-examen/abc` | Los 5 devolvieron HTTP 500 con `invalid input syntax for type bigint` en `glosa`. Evidencia: [`../Evidencias/EV56-09/`](../Evidencias/EV56-09/README.md) |
| 25-nov-2026 12:41 | `sk/inc-06-errores` `f8e2786` (fix inicial, 9 archivos) | Mismo juego de pruebas + 401/403 | 5×500 genéricos; 401 `"Token inválido"`; 403 de permiso; logs con `22P02` |
| 25-nov-2026 17:42 | `feature/skarlett-ep3` `46e0f25` (helper) | Retest CP-17 + Sonar de *New Code* | CP-17 sigue OK. Sonar: 0 issues nuevos; Quality Gate ERROR por duplicación de *New Code* 16,42 % (umbral 3 %) y cobertura nueva 0 % (umbral 80 %) |
| 27-nov-2026 20:06 | `df6fd24` (`origin/feature/skarlett-ep3`, ya con INC-04 e INC-05) | Retest CP-17 en la rama final remota, sin usar un merge local posterior | **PASA** para INC-06. Evidencia intacta: [`../Evidencias/EV56-20/`](../Evidencias/EV56-20/README.md) |
| 27-nov-2026 (después del PR #7) | `origin/dev` `5707693` | El código de INC-06 quedó en `dev` | No se repitió el `curl` sobre este SHA exacto: `5707693` es el merge del mismo trabajo ya retesteado en `df6fd24` |

## 3. Veredicto

- **INC-06:** Verificado.  
- **CP-17:** Paso con observaciones. Siguen abiertos, fuera de este INC, **INC-14** (`POST /auditoria`, Nicolás) e **INC-11** (`npm audit`).

## 4. Observación residual (no reabre INC-06)

Si `multer` rechaza un MIME no permitido y no hay un manejador global `(err, req, res, next)` en `app.js`, Express podría exponer un stack cuando `NODE_ENV` no es `production`. En el compose del laboratorio `NODE_ENV` por defecto es `production`. Queda como mejora del plan de mantenimiento, no como fallo del retest CP-17.
