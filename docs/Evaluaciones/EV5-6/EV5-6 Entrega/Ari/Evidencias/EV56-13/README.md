# EV56-13 — JMeter ramp 100 → 5000 VU

**Estado:** intento a **5000 VU** archivado (2026-11-27). Error HTTP **0 %** en todas las fases.  
**Ejecutora:** Ari Araya  
**Relacionado:** NFR-PERF 300 ms (p95), ISO 25010 / 29119, desbloqueado por EV56-04 (INC-04)

Plan: `POST /autenticacion/login` (Once Only) + `GET /pacientes` + `GET /examenes`, Bearer `$.token`, API `localhost:4444`, usuario `medico`. No-GUI. NFR-PERF se lee en **95th pct** (JMeter APDEX usa T=500 ms; no es el umbral del encargo).

No merge a `main` hasta retest de equipo.

## Conclusión

| Fase | VU | Logins | Samples | Error % | GET p95 (pacientes / exámenes) | Total p95 | txn/s | vs 300 ms |
|------|----|--------|---------|---------|--------------------------------|-----------|-------|-----------|
| A | 100 | 100 | 52 433 | 0 | 266 / 267 ms | 259 ms | 437 | **cumple** |
| B | 500 | 500 | 77 576 | 0 | 1285 / 1286 ms | 1319 ms | 429 | no (capacidad) |
| C | 1000 | 1000 | 70 631 | 0 | 3268 / 3287 ms | 3239 ms | 388 | no (capacidad) |
| D | 2500 | 2500 | 70 528 | 0 | 6736 / 6736 ms | 6772 ms | 380 | no (capacidad) |
| **E** | **5000** | **5000** | 127 371 | 0 | 14514 / 14515 ms | 13735 ms | 344 | no (capacidad) |

Solo la fase A cumple NFR-PERF en lecturas. De B a E sube la latencia y baja un poco el throughput, **sin fallos HTTP**. No reabre INC-04 (curl 1 VU ~30 ms; A ~200 ms avg). Residual: techo del host/Postgres/Node.

Login p95 siempre peor que GET (auditoría en cada `POST /autenticacion/login`). En E: login p95 **29 053 ms**.

## Intento E fallido (mismo día)

`EV56-13-faseE-5000-intento1-2500vu.jtl`: el no-GUI corrió con el `.jmx` aún en **2500** hilos (GUI 5000 sin guardar). POST Login = 2500. Se reejecutó con Duration 360 s; dashboard canónico = `dashboard-faseE/` (5000 logins, 3:31–3:38).

## Archivos (índice; no listar bower de dashboards)

| Archivo | Qué es |
|---------|--------|
| `EV56-13 Cuidarte 5000.jmx` | Plan (último save: 5000 hilos) |
| `JMeter_POST200_debug-EV56-13.png` | Humo 1 VU: POST login 200 |
| `JMeter_GET200_debug-EV56-13.png` | Humo 1 VU: GET 200 |
| `EV56-13-faseA-100.jtl` + `dashboard-faseA/` + `faseA-*.png` | Fase A |
| `EV56-13-faseB-500.jtl` + `dashboard-faseB/` + `faseB-*.png` | Fase B |
| `EV56-13-faseC-1000.jtl` + `dashboard-faseC/` + `faseC-*.png` | Fase C |
| `EV56-13-faseD-2500.jtl` + `dashboard-faseD/` + `faseD-*.png` | Fase D |
| `EV56-13-faseE-5000.jtl` + `dashboard-faseE/` + `faseE-*.png` | Fase E canónica |
| `EV56-13-faseE-5000-intento1-2500vu.jtl` | E abortada (2500 VU) |
| `fase*-JMeter.png` | Thread Group de esa fase en GUI |
| Abrir | `dashboard-fase*/index.html` |

No hay PNG de Administrador de tareas (CPU/RAM). Las métricas de saturación están en p95 + throughput.

Wireshark de D/E: [`../EV56-17/`](../EV56-17/README.md).
