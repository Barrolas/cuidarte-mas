# Resultados JMeter — CP-05 / NFR-PERF (Cuidarte+)

**Fecha:** 7–8 septiembre 2026  
**Plan:** [`CuidartePlus_CP05.jmx`](./CuidartePlus_CP05.jmx)  
**Motor:** Docker `justb4/jmeter:latest`  
**Target:** `http://host.docker.internal:4444` (API local)  
**Credenciales de prueba:** `medico` / `medico` (dump seed)  
**Artefactos:** `results_cp05.jtl`, carpeta `html_report/`

## Escenarios

| Grupo | VUs | Loops | Objetivo ERS |
|-------|-----|-------|--------------|
| TG-A | 20 | 2 | NFR-PERF-1 (CRUD &lt; 300 ms) |
| TG-B | 50 | 1 | Smoke concurrencia (hacia NFR-PERF-3) |

## Resultados agregados

| Muestra | n | Avg (ms) | p50 | p95 | p99 | max | Cumple &lt;300 ms |
|---------|---|----------|-----|-----|-----|-----|------------------|
| POST Login | 40 | 11 | 8 | 14 | 93 | 93 | **Sí** (40/40) |
| POST Login B | 50 | 10 | 10 | 13 | 14 | 14 | **Sí** (50/50) |
| GET Pacientes | 40 | 5007 | 5007 | 5010 | 5010 | 5010 | **No** (0/40) |
| GET Examenes | 40 | 5006 | 5006 | 5008 | 5016 | 5016 | **No** (0/40) |
| GET Examenes B | 50 | 5008 | 5008 | 5011 | 5013 | 5013 | **No** (0/50) |

**Totales:** 220 samples · **0% error HTTP** · throughput ~3.7 req/s.

## Interpretación (HALL-04 + CP-05)

1. El login cumple holgadamente el umbral (&lt; 100 ms).  
2. `GET /pacientes` y `GET /examenes` responden ~**5000–5016 ms** de forma sistemática → coincide con `delayMiddleware(5000)` en el backend (no es congestión real).  
3. **Veredicto NFR-PERF-1 en este ambiente:** **NO CUMPLE** mientras el delay artificial esté activo.  
4. TG-B (50 VUs) soportó la carga sin errores de aplicación; no se llegó a 200 VUs por límite práctico local, pero evidencia resiliencia básica bajo concurrencia moderada.

## Cómo reproducir

```powershell
docker run --rm --add-host=host.docker.internal:host-gateway `
  -v "${PWD}:/tests" justb4/jmeter:latest `
  -n -t /tests/CuidartePlus_CP05.jmx -l /tests/results_cp05.jtl -e -o /tests/html_report
```

Abrir reporte HTML: `html_report/index.html`.
