# Evidencias CP-21

## Ya en el repo (revisión documental)

- `docker-compose.yml` (raíz)
- `FRONTEND/nginx.conf`
- Resultado escrito: `../../CP-21_Disponibilidad.md`

## Capturas (26-10-2026)

Están en el Word `EV2_Ari_Pruebas_Seguridad_Rendimiento.docx`:

- Figura 1–2: contenedores up / `docker compose ps` (puertos 4444, 3333, 15442).
- Figura 3: Docker Desktop + log del backend (login ~115 ms; GET ~5 s).

Eso demuestra **recuperación/arranque local**, no el SLO 99,5 % mensual. CP-21 sigue en **Falla** (INC-17).
