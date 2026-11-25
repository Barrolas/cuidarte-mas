# EV56-04 — INC-04 delay artificial (before / after + humo FE)

**Estado:** delay **quitado de las rutas**. Timing ANTES/DESPUÉS y humo FE archivados.  
**Ejecutora:** Ari Araya  
**Relacionado:** INC-04, NFR-PERF 300 ms, desbloquea EV56-13 (JMeter 5000 VU)

Pendiente operativo: aviso a Nicolás (Selenium/JMeter). No merge a `main` hasta retest de equipo.

## Archivos

| Archivo | Qué es |
|---------|--------|
| `EV56-04-before-GET-pacientes-examenes.png` | Curl ANTES (~5 s) |
| `EV56-04-before-delay-timing.txt` | Log ANTES |
| `EV56-04-after-GET-pacientes-examenes.png` | Curl DESPUÉS (~30 ms) |
| `EV56-04-after-delay-timing.txt` | Log DESPUÉS |
| `EV56-04-humo-FE-pacientes.png` | UI listado pacientes (médico, datos OK) |
| `EV56-04-humo-FE-examenes-network.png` | UI exámenes + Network 304 · 11 ms |
| `EV56-04-humo-FE.txt` | Bitácora del humo (incl. Network pacientes 304 · 23 ms) |

## Comparación curl (API)

| Endpoint | HTTP | ANTES (`time_total`) | DESPUÉS | vs NFR-PERF 300 ms |
|----------|------|----------------------|---------|--------------------|
| `GET /pacientes` | 200 | **5.028832 s** | **0.029100 s** | cumple (después) |
| `GET /examenes` | 200 | **5.053524 s** | **0.031565 s** | cumple (después) |

## Humo FE (2026-11-25 ~01:32)

Login `medico` en `http://localhost:3333`. Listados con datos. Network: `pacientes` **304 / 23 ms**, `examenes` **304 / 11 ms**. 304 = Not Modified (caché), no es error.

## Mitigación en código

`delayMiddleware` **ya no se usa** en rutas. Archivo huérfano: `BACKEND/src/middleware/delay.js`.

Quitado de:

- `BACKEND/src/routes/pacientes.js` — `GET /`
- `BACKEND/src/routes/examenes.js` — `POST /`, `GET /`, `PUT /:id`
- `BACKEND/src/routes/documentos.js` — `POST /`
