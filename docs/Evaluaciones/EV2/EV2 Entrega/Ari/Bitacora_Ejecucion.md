# Bitácora de ejecución — Ari Araya (EP3)

**Rol:** QA de seguridad y rendimiento  
**Ambiente:** Docker local FE `:3333` / API `:4444` / Postgres `:15442`  
**Datos:** sintéticos `admin`/`admin`, `medico`/`medico`, `paciente`/`paciente`  
**Para:** Nicolás (§5.2, Tablas 21 y 22) y Giannina (integración del informe)

Estados: `Aprobado` | `Falla` | `Bloqueado` | `No ejecutado`

---

## Resumen por caso (pasar a Nicolás)

| Fecha | CP | Ejecutor | Capa | Resultado | Evidencia | INC / BUG | Notas |
|-------|----|----------|------|-----------|-----------|-----------|-------|
| 2026-09-08 | CP-04 | Ari | DAST sin sesión | Falla* (hardening) | EV1 Anexos ZAP FE/API + GUI `feature/owasp-zap-ataque` | INC-05 | 0 High; Medium/Low de CSP, clickjacking, CORS, headers. **No** cubre RBAC autenticado |
| 2026-10-20 | CP-04 | Nicolás | API SQLMap | Aprobado* (inyección login) | `Nicolas/Evidencias/CP-04/` | — | SQLMap no inyectable; `' OR 1=1 --` → 401. Ari no repite SQLMap |
| — | CP-04 | Ari | ZAP auth + Burp + Nikto | **No ejecutado** | — | — | Pendiente ciclo 2 (token paciente/médico). Si no se corre, el caso queda **parcial** |
| 2026-09-07 | CP-05 | Ari (EV1) / informe JMeter | API | **Falla** | `EV1 Entrega/Anexos/jmeter/` | INC-04 | p95 GET pacientes/exámenes ≈ 5008–5011 ms con delay; login p95 ≈ 14 ms |
| — | CP-05 | Ari | API sin delay | **No ejecutado** | — | INC-04 | El plan pide segunda corrida con `delayMiddleware` apagado |
| — | CP-13 | Ari | tiempo descarga | **No ejecutado** | formatos: Nicolás CP-13 | INC-15/16 | RF-4.2 ≤10 s queda sin métrica de Ari |
| 2026-10-26 | CP-15 | Ari | código + dump | **Falla** | `BACKEND/src/routes/auth.js` L21, L110; dump seed | INC-01, INC-10 | Comparación e insert en claro; `admin`/`admin`. John the Ripper no aporta si no hay hash |
| 2026-10-26 | CP-17 | Ari | código | **Falla** (parcial) | `app.js` / rutas `glosa: err.message` | INC-06 | Burp en ciclo 2 no ejecutado; el defecto está en todos los `catch` |
| — | CP-19 | Ari | Lighthouse + JMeter 200 VU | **No ejecutado** | — | INC-04 si delay on | NFR-PERF-2 y PERF-3 sin cifra de ciclo 2 |
| 2026-10-26 | CP-21 | Ari | config Docker | **Falla** | [`CP-21_Disponibilidad.md`](./CP-21_Disponibilidad.md) | **INC-17** | Sin SLO 99,5 %, sin runbook de mantenimiento |

\* = cumple una parte del criterio y falla otra.

## Bloqueos de ambiente (para no mezclar con Falla de producto)

Si al ejecutar aparece `relation "usuarios" does not exist`:

- Causa: `init-db.sh` con CRLF (`/bin/bash^M`) → dump no cargado; el volumen queda vacío.  
- Estado de login/API: **Bloqueado**, no “credencial incorrecta”.  
- Arreglo: `docker compose down -v`, pasar `BACKEND/sql/init-db.sh` a LF, `docker compose up -d`.

## Bugs nuevos

| ID | CP | Severidad | Descripción | Evidencia |
|----|----|-----------|-------------|-----------|
| **INC-17** | CP-21 | Moderado | DIS-1/DIS-2 no demostrables en Compose (sin HA, backup ni métrica mensual) | `CP-21_Disponibilidad.md` |
| BUG-001 | — | — | Sin defecto nuevo de ejecución dinámica ciclo 2 | — |

INC-17 se numera como incidente de plan (no como BUG-001) para no chocar con la lista INC-01…16. Si Giannina prefiere BUG-001 para CP-21, unificar en el Word.

## Firmas

| Oleada | Fecha | Comentario |
|--------|-------|------------|
| EV1 DAST + JMeter | 2026-09-07/08 | Línea base; no reemplaza ciclo 2 autenticado |
| CP-21 + cierre documental | 2026-10-26 | Este paquete |
