# Texto para §3.4 — Entorno y herramientas (Ari)

Pegar o adaptar en el informe EP3, bloque de recursos técnicos / herramientas de seguridad y rendimiento.  
Ejecución: **26 de octubre de 2026**, Windows + Docker Desktop. Evidencia: `Ari/Evidencias/EV2_Ari_Pruebas_Seguridad_Rendimiento.docx` fig. 1–6.

---

Las pruebas de seguridad dinámica y de rendimiento a cargo de Ari Araya se ejecutaron sobre el **Docker Compose** del repositorio `Barrolas/cuidarte-mas`. No existe un ambiente de QA o staging separado. El frontend escucha **HTTP :80** (`FRONTEND/nginx.conf`); no hay certificado TLS en este despliegue, por lo que NFR-SEG-1 no se evalúa como canal cifrado en local.

| Contenedor | Imagen | Puerto publicado |
|------------|--------|------------------|
| `cuidarteplus-backend-ev` | build local | 4444 → 4000 (API, Swagger `/docs`) |
| `cuidarteplus-frontend-ev` | nginx | 3333 → 80 |
| `cuidarteplus-postgres-ev` | `postgres:15-alpine` | 15442 → 5432 |

Los tres servicios definen `restart: unless-stopped`. Postgres publica un `healthcheck` (`pg_isready`) y el backend espera `condition: service_healthy`. El 26-10 los tres estaban `healthy`. Datos sintéticos (`admin`/`admin`, `medico`/`medico`, `paciente`/`paciente`). No se usan RUT ni fichas reales. Alcance ético: solo el ambiente local (Ley 21.459).

En el log del backend, el login respondió en ~115 ms y `GET /examenes` / `GET /pacientes` en ~5019 / ~5043 ms (efecto de `delayMiddleware(5000)`, INC-04).

**Herramientas utilizadas en la parte de Ari**

| Herramienta del plan | Herramienta usada | Por qué | Casos |
|----------------------|-------------------|---------|-------|
| OWASP ZAP | OWASP ZAP **2.17.0** GUI | Se importó `http://localhost:4444/openapi.json` y se inyectó JWT con reglas de Reemplazo (`Authorization: Bearer …`), una de médico y otra de paciente. Escaneo activo por rol | CP-04 |
| Burp Suite | Swagger UI (Authorize) + `curl.exe -i` | Equivalente funcional: cambiar token, método e id y ver código/cabeceras/cuerpo. Mismo criterio que CP-14 | CP-04, CP-17 |
| Nikto | `curl.exe -i` / `-I` | Nikto no está instalado; se revisaron cabeceras de `:4444` y `:3333` | CP-04 |
| SQLMap | — (Nicolás) | Ari no duplica | CP-04 |
| John the Ripper | Docker `ghcr.io/openwall/john` sobre `hashes.txt` | Resultado: *No password hashes loaded* (texto plano) | CP-15 |
| JMeter | Docker `justb4/jmeter` 5.5, modo `-n` | Plan `CuidartePlus_CP05.jmx` (EV1), `host.docker.internal:4444`, usuario `medico` | CP-05 |
| psql | `docker exec … psql` | `\d usuarios` | CP-15 |
| Compose / nginx | lectura + `docker compose ps` | Única “herramienta” de disponibilidad | CP-21 |
| Lighthouse | no ejecutado | NFR-PERF-2 pendiente | CP-19 |

Se confirma que **Jest y k6 no se usan**. CP-21 no requiere escáner.

**Limitación de entorno.** Un primer `docker compose up` puede marcar Postgres *unhealthy* si `init-db.sh` tarda más que 5 reintentos o si el script tiene finales de línea Windows (`bash^M`); en ese caso el dump no carga y la API responde `relation "usuarios" does not exist`. Eso es un bloqueo de ambiente, no un hallazgo de credenciales. El 26-10 no ocurrió.
