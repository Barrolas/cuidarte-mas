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
| `EV56-13/` | JMeter 5000 VU | pendiente (tras EV56-04) |
| `EV56-14/` | John retest | pendiente (tras bcrypt Nico) |
| `EV56-15/` | ZAP before/after | pendiente |
| `EV56-17/` | Wireshark bajo carga | pendiente |
