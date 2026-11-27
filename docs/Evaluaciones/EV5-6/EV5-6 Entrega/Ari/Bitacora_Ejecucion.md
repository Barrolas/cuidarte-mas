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

---

## 2026-11-27 ~00:37 UTC-3 — EV56-08 baseline ANTES (INC-05)

- **Qué:** `curl.exe -i` a `GET /` con `Origin: http://localhost:3333` y `Origin: http://evil.example`.
- **Ambiente:** Docker local, API `http://localhost:4444`. CORS por defecto (`app.use(cors())`).
- **Resultado:** HTTP 200 en ambos. `Access-Control-Allow-Origin: *`. `X-Powered-By: Express`. Sin `X-Content-Type-Options` ni `X-Frame-Options`. ISO 27001 / 25010: CORS abierto y fingerprint del stack.
- **Evidencia:** `Evidencias/EV56-08/ANTES-INC-05.png` (Date 03:37:12 / 03:37:18 GMT).
- **Siguiente:** acotar CORS y añadir cabeceras en `app.js`, rebuild, curl DESPUÉS.

---

## 2026-11-27 ~00:46 UTC-3 — EV56-08 medición DESPUÉS (INC-05)

- **Qué:** mismos curls tras `app.disable("x-powered-by")`, CORS a `FRONTEND_URL`/`http://localhost:3333` (otros orígenes sin `Allow-Origin`) y headers `nosniff` / `DENY`. Rebuild `cuidarteplus-backend-ev`.
- **Ambiente:** Docker local, API `http://localhost:4444`.
- **Resultado:** Origin FE → `Allow-Origin: http://localhost:3333`, `nosniff`, `DENY`, sin `X-Powered-By`. Origin `evil.example` → **sin** `Allow-Origin`; mismas cabeceras de hardening. HTTP 200 se mantiene (CORS no oculta el recurso a curl).
- **Evidencia:** `Evidencias/EV56-08/DESPUES-INC-05.png`, `EV56-08-curl-headers.txt`. Código: `BACKEND/src/app.js`.
- **Siguiente:** humo FE + `/docs`. No merge a `main` hasta retest de equipo.

---

## 2026-11-27 ~00:54–01:06 UTC-3 — EV56-08 humo FE + Swagger (INC-05)

- **Qué:** login `medico` en `http://localhost:3333`; home, pacientes y exámenes con DevTools Network; `http://localhost:4444/docs/`.
- **Resultado:** `POST /autenticacion/login` **200 / 56 ms**; `GET /examenes` **200 / 69 ms**; `GET /pacientes` **200 / 27 ms**. Listados con datos. Response: `Allow-Origin: http://localhost:3333`, `nosniff`, `DENY`; Request `Origin: http://localhost:3333`; Console sin error CORS. Swagger abre. OPTIONS no capturado (filtro Fetch/XHR).
- **Evidencia:** `Evidencias/EV56-08/Humo_1-INC-05.png`, `Humo_2-INC-05.png`, `Humo_3-INC-05.png`, `Humo_pacientes-INC-05.png`, `Humo_examenes-INC-05.png`, `Swagger-INC-05.png`, `EV56-08-humo-FE.txt`. Índice: [`Evidencias/EV56-08/README.md`](./Evidencias/EV56-08/README.md).
- **Siguiente:** EV56-13 JMeter 5000; EV56-15 ZAP (ya no bloqueado por headers); aviso a Nicolás (delay + CORS).

---

## 2026-11-27 ~02:25 UTC-3 — EV56-13 humo JMeter 1 VU

- **Qué:** plan GUI `EV56-13 Cuidarte 5000.jmx`: Once Only login + GET pacientes/exámenes, `localhost:4444`.
- **Resultado:** POST login 200 + GET 200 (~4 ms). View Results Tree en bucle largo no retuvo el POST (límite de samples); recaptura 1 loop.
- **Evidencia:** `Evidencias/EV56-13/JMeter_POST200_debug-EV56-13.png`, `JMeter_GET200_debug-EV56-13.png`.

---

## 2026-11-27 ~02:37–03:14 UTC-3 — EV56-13 fases A–D

- **Qué:** no-GUI, mismo `.jmx`, hilos 100 / 500 / 1000 / 2500. Error HTTP **0 %**.
- **Resultado (p95 GET pacientes / Total txn/s):** A 266 ms / 437 (cumple NFR-PERF 300 ms); B 1285 ms / 429; C 3268 ms / 388; D 6736 ms / 380. Saturación de capacidad, no INC-04.
- **Evidencia:** `dashboard-faseA`…`dashboard-faseD`, `fase*-apdex.png`, `fase*-statistics.png`, `.jtl` por fase. Índice: [`Evidencias/EV56-13/README.md`](./Evidencias/EV56-13/README.md).

---

## 2026-11-27 ~03:11–03:14 UTC-3 — EV56-17 Wireshark fase D (2500 VU)

- **Qué:** Npcap loopback, filtro `tcp.port == 4444`, paralelo a JMeter D.
- **Resultado:** ~448 k paquetes `127.0.0.1:4444`. I/O Graph ~2–2,7 k pkt/s; errores TCP ≈ 0.
- **Evidencia:** `Evidencias/EV56-17/EV56-17-faseD-2500.pcapng`, `Wireshark-2500VU.png`, `EV56-17-faseD-2500.png`.

---

## 2026-11-27 ~03:21 UTC-3 — EV56-13 fase E intento 1 (inválido)

- **Qué:** no-GUI `-o dashboard-faseE` con GUI en 5000 pero `.jmx` en disco aún 2500.
- **Resultado:** POST Login = **2500**. `.jtl` renombrado a `EV56-13-faseE-5000-intento1-2500vu.jtl`. No usar como E.

---

## 2026-11-27 ~03:31–03:38 UTC-3 — EV56-13 fase E canónica (5000 VU)

- **Qué:** `.jmx` guardado 5000 hilos, Duration 360 s, dashboard en carpeta vacía.
- **Resultado:** **5000 logins**, 127 371 samples, error **0 %**. GET p95 **14 514 / 14 515 ms**. Total p95 13 735 ms. 344 txn/s. Login p95 29 053 ms. DoD 5000 VU cumplido. NFR-PERF no se cumple (techo del host).
- **Evidencia:** `EV56-13-faseE-5000.jtl`, `dashboard-faseE/`, `faseE-apdex.png`, `faseE-statistics.png`.

---

## 2026-11-27 ~03:31–03:38 UTC-3 — EV56-17 Wireshark fase E (5000 VU)

- **Qué:** misma receta loopback `:4444` durante E.
- **Resultado:** HTTP `GET /pacientes` 200 en lista. I/O Graph ~2–3,5 k pkt/s ~380 s; **errores TCP** ~200–280 s (JMeter sigue 0 % HTTP).
- **Evidencia:** `Evidencias/EV56-17/EV56-17-faseE-5000.pcapng`, `Wireshark-5000VU.png`, `EV56-17-faseE-5000.png`. Índice: [`Evidencias/EV56-17/README.md`](./Evidencias/EV56-17/README.md).
- **Siguiente:** EV56-15 ZAP; EV56-14 / EV56-10 con Nico; ping Ninna con tabla JMeter. No merge a `main`.
