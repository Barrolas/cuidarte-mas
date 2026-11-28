# EV56-19 — Evidencia CP-14, CP-16 y CP-18

Ejecutado el **25-nov-2026** contra `dev` (`2d0abc7`) en Docker local (FE `:3333`, API `:4444`, Postgres `:15442`). No se volvió a correr sobre `origin/dev` `5707693` (los merges posteriores de INC-04/05/06 no tocan TLS, `pgcrypto` ni la política de backup; `/files/documentos` sigue estático sin token en `app.js:63`).

| Archivo | Caso | Resultado breve |
|---------|------|-----------------|
| `2026-11-25_cp14-sin-tls.png` + `cp14_estado_real_dev.txt` | CP-14 | HTTP 200 en `:3333`/`:4444` sin HSTS; HTTPS error 35; Postgres `ssl=off` |
| `2026-11-25_cp14-tls-proxy.png` | CP-14 (lab) | Proxy Nginx autofirmado `:3443`, TLS 1.2/1.3 + HSTS, HTTP 200 |
| `2026-11-25_cp16-documentos-sin-token.png` + `cp16_estado_real_dev.txt` | CP-16 | Sin `pgcrypto`; `GET /files/documentos/...` sin token → 200 |
| `2026-11-25_cp18-backup-restore.png` + `2026-11-25_cp18.txt` | CP-18 | `pg_dump` 216 ms / 23.198 B; restore 190 ms; conteos 3/20/0/0/7/3 idénticos; sin cron ni copia externa |

Documento: [`../../Entregables/EV56-19-CP-14-16-18.md`](../../Entregables/EV56-19-CP-14-16-18.md).
