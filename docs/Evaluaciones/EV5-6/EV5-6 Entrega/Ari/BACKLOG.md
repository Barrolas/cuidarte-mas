# BACKLOG — Ari Araya (EV5-6)

**Rol:** Rendimiento, DAST (ZAP), John, headers/CORS, fuerza bruta, Wireshark bajo carga.  
**Tablero:** [`../00_Backlog_Equipo.md`](../00_Backlog_Equipo.md)  
**Análisis:** [`../00_Analisis_Encargo_Final.md`](../00_Analisis_Encargo_Final.md)

Estándares: **25010** (desempeño, seguridad), **27001** (hardening), **29119**; NFR-PERF umbral **300 ms**.

---

## Checklist

- [x] EV56-04 INC-04 quitar delay *(before/after + humo FE 2026-11-25; aviso Nico pendiente)*  
- [ ] EV56-08 INC-05 CORS + headers  
- [ ] EV56-10 Fuerza bruta / lockout (evidencia + sync Nico)  
- [ ] EV56-13 JMeter → 5000 VU  
- [ ] EV56-14 John retest  
- [ ] EV56-15 ZAP before/after  
- [ ] EV56-17 Wireshark carga  
- [ ] Handoff KPIs a Ninna  

---

## EV56-04 — INC-04 quitar delay (bloqueante para 5000 VU)

1. Buscar `delayMiddleware` / `5000` en backend. **Hecho.**  
2. Medir **antes** con curl. **Hecho** 2026-11-25 00:57: `GET /pacientes` 200 **5.028832 s**, `GET /examenes` 200 **5.053524 s**.  
3. Eliminar delay; rebuild API. **Hecho** — `delayMiddleware` retirado de `pacientes.js`, `examenes.js`, `documentos.js`. Queda `BACKEND/src/middleware/delay.js` sin usos.  
4. Medir **después**. **Hecho** 2026-11-25 01:13: `GET /pacientes` 200 **0.029100 s**, `GET /examenes` 200 **0.031565 s**. Carpeta [`Evidencias/EV56-04/`](./Evidencias/EV56-04/README.md).  
5. Humo FE: login + listados. **Hecho** 2026-11-25 01:32: pacientes 304 / 23 ms, exámenes 304 / 11 ms, listas con datos.  
6. Avisar a Nicolás (Selenium) y liberar JMeter.

**DoD:** sin espera artificial; timing before/after archivado. **Cumplido** (curl 1 VU + humo FE). Aviso a Nico sigue.

---

## EV56-08 — INC-05 CORS y cabeceras

1. Revisar `cors` / headers en `app.js`.  
2. CORS al origen FE (`http://localhost:3333`), no `*`.  
3. Headers: `X-Content-Type-Options`, `X-Frame-Options`, ocultar `X-Powered-By` si aplica.  
4. Verificar con `curl -i`; no romper FE ni `/docs`.  
5. Evidencias TXT/PNG.

**DoD:** headers presentes; FE operativo.

---

## EV56-10 — Fuerza bruta (pizarrón)

1. **Antes:** N intentos fallidos de login sin bloqueo (captura/conteo).  
2. Definir con Nicolás mitigación (rate-limit / lockout temporal / captcha de lab).  
3. **Después:** mismo ataque controlado → bloqueo o 429.  
4. Relacionar con ISO 25010 (seguridad) y REC lockout de EV2.  
5. Entregar before/after a Ninna.

**DoD:** caso SEG documentado; si no hay código aún, dejar evidencia del fallo + requisito de mitigación (pero el examen pide mitigar: priorizar fix).

---

## EV56-13 — JMeter 5000 usuarios (obligatorio)

**Precondición:** EV56-04 hecho.

1. Plan `.jmx` no-GUI con login + GET de lectura (exámenes/pacientes).  
2. Ramp: 100 → 500 → 1000 → 2500 → **5000**.  
3. Registrar por fase: samples, avg, p90, p95, error %, throughput, CPU/RAM.  
4. Dashboard HTML desde `.jtl`.  
5. Comparar p95 vs **300 ms**.  
6. Si el host no aguanta 5000: documentar techo estable **y** el intento a 5000 (errores de conexión), sin ocultar el requisito.

**DoD:** intento 5000 documentado + gráficos para §5.1.

---

## EV56-14 — John retest (post-bcrypt)

1. Esperar EV56-01 de Nicolás.  
2. Extraer hashes a archivo de laboratorio.  
3. Ejecutar John: debe reconocer bcrypt (no “No password hashes loaded” por plain).  
4. Evidencia terminal + conclusión CP-15.

**DoD:** INC-01 verificado desde lado hashes.

---

## EV56-15 — ZAP autenticado

1. Baseline o reuso EV2: alertas High/Medium/Low.  
2. Tras EV56-08 (y mitigaciones): ZAP con Bearer médico/paciente.  
3. Exportar reporte HTML/PDF.  
4. En informe: tabla alerta → severidad → estado (mitigado/residual) — pizarrón: evidencias + **≥1 solución**.  
5. Cruzar con headers curl.

**DoD:** reporte + al menos un hallazgo cerrado con evidencia.

---

## EV56-17 — Wireshark bajo carga

1. Iniciar captura en puerto API antes de fase alta de JMeter.  
2. Guardar `.pcapng` + I/O Graph / retransmissions.  
3. Párrafo corto para Ninna (volumen, errores TCP).

**DoD:** anexo de red ligado a estrés.

---

## Handoff a Ninna

1. Tabla fases JMeter completa.  
2. Paths ZAP / John / headers / Wireshark.  
3. Estado CP-04, CP-05, CP-15 (+ SEG fuerza bruta).  
4. Bullets remediación: INC-04, INC-05, INC-01 (verificación).  
5. Gráficos sugeridos: latencia vs VU; error % vs VU; before/after delay.

---

## Orden sugerido

| Bloque | Foco |
|--------|------|
| 1 | EV56-04 |
| 2 | EV56-08 + sync lockout |
| 3 | EV56-13 fases A–C |
| 4 | EV56-13 D–E + EV56-17 |
| 5 | EV56-14 + EV56-15 + handoff |
