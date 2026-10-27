# CP-21 — Disponibilidad y procedimiento de mantenimiento

| Campo | Valor |
|-------|--------|
| **ID** | CP-21 |
| **Ejecutor** | Ari Araya |
| **Fecha** | 2026-10-26 |
| **Requerimientos** | NFR-DIS-1 (disponibilidad 99,5 % mensual); NFR-DIS-2 (ventana de mantenimiento y migración segura) |
| **Tipo** | Verificación de configuración (sin escáner ni herramienta extra) |
| **Ambiente** | Docker Compose local (`docker-compose.yml`) |
| **Resultado** | **Falla** (no demostrable frente al umbral del ERS) |
| **INC / BUG** | **INC-17** (nuevo): disponibilidad y mantenimiento no operativizados |

## 1. Qué se hizo

El informe EP3 (§1.4 y ficha CP-21) indica que **no se mide uptime de un mes**. Se revisó el despliegue local y se contrastó con NFR-DIS-1 / NFR-DIS-2.

Checklist ejecutado sobre el repositorio (commit base `4bfffb0` / rama `feature/ari-ep3-qa-seguridad`):

| Comprobación | Dónde | Observado |
|--------------|-------|-----------|
| Reinicio automático | `docker-compose.yml` L23, L46, L62 | `restart: unless-stopped` en Postgres, backend y frontend |
| Healthcheck BD | L16–20 | `pg_isready` cada 5 s, 5 reintentos; **sin `start_period`** |
| Arranque ordenado | L39–41 | Backend espera `service_healthy` de Postgres |
| Persistencia | L12–13, L65 | Volumen `postgres_data`; backend monta `BACKEND/uploads` |
| Alta disponibilidad | compose | **Un** réplica por servicio; sin balanceador |
| TLS / HTTPS | `FRONTEND/nginx.conf` L2; compose L56 | nginx escucha **80**; no hay certificado ni redirección HTTPS |
| Respaldo automático | compose / repo | **No** hay cron, `pg_dump` programado ni runbook de restore en el producto |
| Ventana de mantenimiento | documentación de despliegue | **No** hay procedimiento versionado (solo `docker compose restart` manual) |
| Métrica 99,5 % | ambiente | **No** hay probe de uptime ni histórico mensual |

Comando de verificación (cuando Docker esté arriba):

```powershell
docker compose ps
docker compose restart cuidarteplus-backend-ev
docker compose ps
```

Esperado operativo: los tres contenedores `Up` y Postgres `healthy` tras el restart. Eso demuestra **recuperación local**, no el SLO mensual.

## 2. Resultado esperado vs observado

| ERS | Esperado | Observado |
|-----|----------|-----------|
| NFR-DIS-1 | 99,5 % mensual medible | No hay medición. El ambiente es un solo host Docker. |
| NFR-DIS-2 | Ventana de mantenimiento y migración segura | Se puede detener/levantar un contenedor a mano. No hay ventana, checklist ni prueba de migración de esquema. |

**Criterio de aceptación del plan:** un caso de seguridad/cumplimiento/calidad no funcional se marca **Falla** si no se puede demostrar el umbral. CP-21 **falla** de forma documental (limitación ya declarada en §1.4).

## 3. Incidente

**INC-17 — Disponibilidad y mantenimiento no demostrables**

- **Severidad propuesta:** Moderado (no es fuga de ficha clínica; impide certificar DIS).  
- **Recomendación:** documentar RTO/RPO, `pg_dump` + restore ensayado, `start_period` en el healthcheck (el primer `up` puede marcar Postgres *unhealthy* mientras corre `init-db.sh`), y staging con TLS si se quiere acercar a NFR-SEG-1 + DIS.

## 4. Evidencia

| Archivo | Uso |
|---------|-----|
| `docker-compose.yml` | restart, healthcheck, volúmenes, puertos |
| `FRONTEND/nginx.conf` | solo `listen 80` |
| `Evidencias/CP-21/README.md` | qué captura falta (compose ps) |
