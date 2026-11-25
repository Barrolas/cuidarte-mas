# Bitácora de ejecución — Ari Araya (EV5-6)

Formato: fecha · ítem · resultado · evidencia.

---

## 2026-11-25 ~00:57 UTC-3 — EV56-04 baseline ANTES (INC-04)

- **Qué:** login médico + `GET /pacientes` y `GET /examenes` con `curl.exe -w time_total`.
- **Ambiente:** Docker local, API `http://localhost:4444`. Delay **aún activo**.
- **Resultado:** HTTP 200 en ambos. `time_total` 5.028832 s (`/pacientes`) y 5.053524 s (`/examenes`). Incumple NFR-PERF 300 ms. Confirma `delayMiddleware(5000)`.
- **Evidencia:** `Evidencias/EV56-04/EV56-04-before-GET-pacientes-examenes.png` y `EV56-04-before-delay-timing.txt`.
- **Siguiente:** quitar delay en rutas, rebuild, repetir medición AFTER.

---

## 2026-11-25 ~01:13 UTC-3 — EV56-04 medición DESPUÉS (INC-04)

- **Qué:** mismo login médico + `GET /pacientes` y `GET /examenes` con `curl.exe -w time_total`, tras quitar `delayMiddleware(5000)` de las rutas y rebuild de la API.
- **Ambiente:** Docker local, API `http://localhost:4444`. Delay **retirado de rutas**.
- **Resultado:** HTTP 200 en ambos. `time_total` **0.029100 s** (`/pacientes`) y **0.031565 s** (`/examenes`). Cumple NFR-PERF 300 ms en 1 VU. Caída ~5 s → ~30 ms.
- **Evidencia:** `Evidencias/EV56-04/EV56-04-after-GET-pacientes-examenes.png` y `EV56-04-after-delay-timing.txt`.
- **Siguiente:** humo FE; avisar a Nicolás; EV56-08 CORS/headers. No merge a `main` hasta retest de equipo.

---

## 2026-11-25 ~01:32 UTC-3 — EV56-04 humo FE (INC-04)

- **Qué:** login médico en `http://localhost:3333`, listados Pacientes y Exámenes con DevTools Network.
- **Resultado:** listados con datos. Network `pacientes` **304 / 23 ms**, `examenes` **304 / 11 ms**. Primer intento 401 (~01:27) descartado (token aún no aplicado); recaptura OK. Sin espera de ~5 s.
- **Evidencia:** `Evidencias/EV56-04/EV56-04-humo-FE-pacientes.png`, `EV56-04-humo-FE-examenes-network.png`, `EV56-04-humo-FE.txt`.
- **Siguiente:** avisar a Nicolás; EV56-08 CORS/headers.
