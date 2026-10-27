# Texto para §3.4 — Entorno y herramientas (Ari)

Pegar o adaptar en el informe EP3, bloque de recursos técnicos / herramientas de seguridad y rendimiento.  
Ejecución: **26 y 27 de octubre de 2026**, Windows + Docker Desktop. Evidencia: `Ari/Evidencias/Evidencia_ARI.docx`.

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

| Herramienta | Uso | Casos |
|-------------|-----|-------|
| OWASP ZAP **2.17.0** GUI | OpenAPI + JWT Bearer por rol (médico y paciente). Escaneo activo | CP-04 |
| Swagger UI + PowerShell | Token, método, id y cabeceras. No se usó Burp ni Nikto | CP-04, CP-17 |
| SQLMap | Nicolás; Ari no duplica | CP-04 |
| John the Ripper (`ghcr.io/openwall/john`) | *No password hashes loaded* (texto plano) | CP-15 |
| JMeter 5.5 Docker `justb4/jmeter` | `CuidartePlus_CP05.jmx` y `CP19_200u.jmx`, desde PowerShell | CP-05, CP-19 |
| Lighthouse (Chrome) | Performance **43** en `:3333` (27-10) | CP-19 |
| psql | `\d usuarios` | CP-15 |
| Compose / nginx | `docker compose ps` | CP-21 |

Se confirma que **Jest y k6 no se usan**. CP-21 no requiere escáner.

**Limitación de entorno.** Un primer `docker compose up` puede marcar Postgres *unhealthy* si `init-db.sh` tarda más que 5 reintentos o si el script tiene finales de línea Windows (`bash^M`); en ese caso el dump no carga y la API responde `relation "usuarios" does not exist`. Eso es un bloqueo de ambiente, no un hallazgo de credenciales. El 26-10 no ocurrió.
