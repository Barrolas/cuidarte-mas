# EV56-08 — INC-05 CORS acotado + cabeceras

**Estado:** mitigado en lab. Curl ANTES/DESPUÉS, humo FE y `/docs` archivados.  
**Ejecutora:** Ari Araya  
**Relacionado:** INC-05, ISO 27001 (hardening), ISO 25010 (seguridad), desbloquea EV56-15 (ZAP)

Ítem de backlog **EV56-08**; hallazgo **INC-05**. No merge a `main` hasta retest de equipo.

## Archivos

| Archivo | Qué es |
|---------|--------|
| `ANTES-INC-05.png` | Curl `GET /` con Origin FE y Origin `evil.example`: `Allow-Origin: *` + `X-Powered-By: Express` |
| `DESPUES-INC-05.png` | Mismos curls tras el cambio: origen FE acotado; `evil.example` sin `Allow-Origin`; `nosniff` + `DENY`; sin `X-Powered-By` |
| `EV56-08-curl-headers.txt` | Transcripción de los curls (no se inventó timing) |
| `Humo_1-INC-05.png` | Home médico + Network: `login`/`examenes`/`pacientes` **200**; Console sin CORS |
| `Humo_2-INC-05.png` | `POST /autenticacion/login` 200 — Response: `Allow-Origin: http://localhost:3333`, `nosniff` |
| `Humo_3-INC-05.png` | Mismo POST — Response `X-Frame-Options: DENY`; Request `Origin: http://localhost:3333` |
| `Humo_pacientes-INC-05.png` | Listado pacientes con datos + `GET /pacientes` 200 + mismas cabeceras |
| `Humo_examenes-INC-05.png` | Listado exámenes con datos + `GET /examenes` 200 + mismas cabeceras |
| `Swagger-INC-05.png` | `http://localhost:4444/docs/` abre (INC-05 no rompe Swagger) |
| `EV56-08-humo-FE.txt` | Bitácora del humo |

El preflight **OPTIONS** no se capturó: el filtro Fetch/XHR de Chrome lo oculta. El DoD se cubre con el POST login + headers.

## Comparación curl (`GET http://localhost:4444/`)

| Origin | ANTES (03:37 GMT) | DESPUÉS (03:46 GMT) |
|--------|-------------------|---------------------|
| `http://localhost:3333` | `Allow-Origin: *` · `X-Powered-By: Express` · sin `nosniff`/`DENY` | `Allow-Origin: http://localhost:3333` · `nosniff` · `DENY` · sin `X-Powered-By` |
| `http://evil.example` | `Allow-Origin: *` · `X-Powered-By: Express` | **sin** `Allow-Origin` · `nosniff` · `DENY` · sin `X-Powered-By` |

HTTP 200 en todos los curls (el recurso sigue existiendo; CORS restringe al browser, no al `curl`).

## Humo FE (2026-11-27 ~00:54–01:06 UTC-3)

Login `medico` en `http://localhost:3333`. Home, pacientes y exámenes con datos. Network **200** (login 56 ms, exámenes 69 ms, pacientes 27 ms). Cabeceras alineadas al curl DESPUÉS. `/docs` operativo.

## Mitigación en código

`BACKEND/src/app.js`:

- `app.disable("x-powered-by")`
- `cors()` con origen `FRONTEND_URL` o `http://localhost:3333` (rechaza otros orígenes)
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
