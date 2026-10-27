# Texto para §3.4 — Entorno y herramientas (Ari)

Pegar o adaptar en el informe EP3, bloque de recursos técnicos / herramientas de seguridad y rendimiento.

---

Las pruebas de seguridad dinámica y de rendimiento a cargo de Ari Araya se ejecutan sobre el **Docker Compose** del repositorio `Barrolas/cuidarte-mas`: frontend nginx en `http://localhost:3333`, API Express en `http://localhost:4444` (Swagger en `/docs`) y PostgreSQL 15 en `localhost:15442`, red `cuidarteplus-network`. No existe un ambiente de QA o staging separado. El frontend escucha **HTTP :80** (`FRONTEND/nginx.conf`); no hay certificado TLS en este despliegue, por lo que NFR-SEG-1 no se evalúa como canal cifrado en local.

Los tres servicios definen `restart: unless-stopped`. Postgres publica un `healthcheck` (`pg_isready`) y el backend espera `condition: service_healthy`. Los datos de prueba son sintéticos (`admin`/`admin`, `medico`/`medico`, `paciente`/`paciente`). No se usan RUT ni fichas reales.

**Herramientas utilizadas en la parte de Ari**

| Herramienta | Uso en Cuidarte+ | Casos |
|-------------|------------------|-------|
| OWASP ZAP 2.17 (GUI) y baseline Docker EV1 | DAST de superficie pública (headers, CORS, CSP). El ciclo 2 pide además ZAP **autenticado** (pendiente) | CP-04 |
| SQLMap | A cargo de Nicolás sobre el login; Ari no duplica | CP-04 |
| Burp Suite / Nikto | Previstos en la ficha CP-04; no ejecutados en este cierre documental | CP-04 |
| John the Ripper | No aplica mientras las contraseñas estén en texto plano (no hay hash que romper) | CP-15 |
| JMeter (`CuidartePlus_CP05.jmx`) | p95 CRUD con delay activo (EV1). Segunda corrida sin delay y 200 VU (CP-19): pendientes | CP-05, CP-13, CP-19 |
| Lighthouse | Previsto para NFR-PERF-2; no ejecutado en este paquete | CP-19 |
| Revisión de Compose / nginx | Única “herramienta” de CP-21: lectura de configuración y rearranque manual | CP-21 |

Respecto de la EV1 se mantienen ZAP y JMeter como evidencia de línea base. Se confirma que **Jest y k6 no se usan** (el repo no tiene suite unitaria; la carga se midió con JMeter). CP-21 no requiere escáner.

**Limitación de entorno.** Un primer `docker compose up` puede marcar Postgres *unhealthy* si `init-db.sh` tarda más que 5 reintentos o si el script tiene finales de línea Windows (`bash^M`); en ese caso el dump no carga y la API responde `relation "usuarios" does not exist`. Eso es un bloqueo de ambiente, no un hallazgo de credenciales.
