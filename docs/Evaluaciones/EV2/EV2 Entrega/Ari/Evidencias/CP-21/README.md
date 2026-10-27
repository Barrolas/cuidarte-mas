# Evidencias CP-21

## Ya en el repo (revisión documental)

- `docker-compose.yml` (raíz)
- `FRONTEND/nginx.conf`

## Captura a agregar (cuando Docker esté healthy)

1. `docker compose ps` con los tres servicios `Up` (Postgres `healthy`).  
2. Opcional: misma captura después de `docker compose restart cuidarteplus-backend-ev`.  
3. Guardar como `01-compose-ps.png` y `02-compose-ps-post-restart.png` en esta carpeta.

Si Postgres está vacío (`relation "usuarios" does not exist`), anotar **Bloqueado** en otros CP, no en CP-21: este caso no depende de la tabla `usuarios`.
