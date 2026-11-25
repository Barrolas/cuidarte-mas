# EV56-22 — KPIs y gráficos (§5.1)

Archivo de datos reproducible. Completar con handoffs del **viernes 27**.  
Insertar los gráficos en el Word del informe (no solo enlazar).

Cada gráfico lleva: título · fuente (path + fecha + autor) · 1–2 frases de lectura.

---

## G1 — Resultado de CP: EV2 vs EV5-6

| Estado | EV2 (cierre 27-10-2026) | EV5-6 (pendiente) |
|--------|-------------------------|-------------------|
| Aprobado | 10 códigos ERS | |
| Parcial | 10 | |
| Fallido | 20 | |
| No ejecutado / sin resultado | 0 | |
| **Total** | **40** | **40** |

Fuente EV2: matriz `02-Matriz-trazabilidad-40-ERS.docx` (nota de cierre).  
Fuente EV5-6: CSV `EV56-22-Matriz-40-ERS-ciclo3.csv` al congelar.

**Lectura (borrador):** En EV2 la cobertura de diseño fue 40/40, pero 20 códigos fallaron. El ciclo EV5-6 debe mostrar el desplazamiento Fallido → Aprobado en los CP ligados a INC P0.

---

## G2 — Incidentes abiertos vs cerrados por severidad

| Severidad | Abiertos | Verificados | Residual |
|-----------|----------|-------------|----------|
| Crítico | 1 (INC-01) | 0 | |
| Grave | (completar) | | |
| Moderado | | | |
| Leve | | | |

Fuente: `EV56-22-Inventario-INC.md`.

---

## G3 — Selenium (obligatorio)

| Métrica | Valor | Fuente |
|---------|-------|--------|
| Casos totales | | `Nicolas/.../report.json` |
| Passed | | |
| Failed | | |
| Pass rate % | | |
| Duración total | | |
| Flaky | | |
| Fecha ejecución | | |

**Baseline EV2 (referencia, no sustituye el post-fix):** suite 11/11 en `EV2 Entrega/Nicolas/Evidencias/Selenium/`.

---

## G4 — JMeter: latencia vs VU (umbral 300 ms NFR-PERF-1)

| VU | Samples | Avg (ms) | p90 | p95 | Max | Error % | Notas |
|----|---------|----------|-----|-----|-----|---------|-------|
| 1 (humo post-delay) | | ~30 (API GET) | | | | 0 | Ari EV56-04 after |
| 100 | | | | | | | Pendiente |
| 1000 | | | | | | | Pendiente |
| 2500 | | | | | | | Pendiente |
| 5000 | | | | | | | Pendiente; documentar techo si falla HW |

Línea de umbral en el gráfico: **300 ms**.

---

## G5 — JMeter: error % vs VU

Misma tabla de fases que G4; eje Y = error %. Incluir el punto 5000 aunque sea intento fallido por hardware (honestidad del análisis EV3).

---

## G6 — SonarQube: bugs / vulnerabilidades antes vs después

| Métrica | Backend EV2 | Backend EV5-6 | Frontend EV2 | Frontend EV5-6 |
|---------|-------------|---------------|--------------|----------------|
| Bugs | | | | |
| Vulnerabilities | | | | |
| Security Hotspots | | | | |
| Code smells | | | | |
| Security rating | | | | |
| Fecha | EV2 capturas Skarlett | | | |

Fuente EV2: `EV2 Contexto/Entregables/capturas-sonar/`.  
Fuente EV5-6: handoff Skarlett EV56-18.

---

## Extra — % INC P0 mitigados

| INC | Verificado |
|-----|------------|
| 01 | No |
| 02 | No |
| 03 | No |
| 04 | Medido AFTER; pendiente cierre equipo |
| 07 | No |
| **%** | **0 % Verificado formal** |

---

## Plantilla de tarjeta KPI (pegar en el informe)

```
KPI: <nombre>
Valor EV2 → Valor EV5-6
Umbral / meta: <...>
Interpretación (1–2 oraciones):
Evidencia: <ruta>
```
