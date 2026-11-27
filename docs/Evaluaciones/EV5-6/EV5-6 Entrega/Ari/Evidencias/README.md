# Evidencias Ari — EV5-6

Convención de nombre: `EV56-<ID>-<descripcion-corta>.<ext>`  
Ejemplo: `EV56-04-before-GET-pacientes-examenes.png`

No subir JWT completos ni `.env`. Recortar tokens en capturas.

| Carpeta | Ítem | Estado |
|---------|------|--------|
| `EV56-04/` | INC-04 delay: medición ANTES (~5 s) | capturado 2026-11-25 00:57 |
| `EV56-04/` | INC-04 delay: AFTER (~30 ms) | capturado 2026-11-25 01:13 |
| `EV56-04/` | INC-04 delay: humo FE (listados + Network) | capturado 2026-11-25 01:32 |
| `EV56-08/` | INC-05 CORS + headers: curl ANTES (`*`, `X-Powered-By`) | capturado 2026-11-27 00:37 |
| `EV56-08/` | INC-05 CORS + headers: curl DESPUÉS (origen acotado, `nosniff`, `DENY`) | capturado 2026-11-27 00:46 |
| `EV56-08/` | INC-05 CORS + headers: humo FE + `/docs` | capturado 2026-11-27 00:54–01:06 |
| `EV56-10/` | Fuerza bruta / lockout | pendiente (sync Nico) |
| `EV56-13/` | JMeter fases A–D (100–2500 VU, error 0 %) | capturado 2026-11-27 02:37–03:14 |
| `EV56-13/` | JMeter fase E 5000 VU (5000 logins, GET p95 ~14,5 s) | capturado 2026-11-27 03:31–03:38 |
| `EV56-14/` | John retest | pendiente (tras bcrypt Nico) |
| `EV56-15/` | ZAP before/after | pendiente |
| `EV56-17/` | Wireshark D 2500 + E 5000 (pcap + I/O Graph) | capturado 2026-11-27 |
