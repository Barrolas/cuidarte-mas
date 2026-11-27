# BACKLOG — Ari Araya (EV5-6)

**Rol:** Rendimiento, DAST (ZAP), John, headers/CORS, fuerza bruta, Wireshark bajo carga.  
**Tablero:** [`../00_Backlog_Equipo.md`](../00_Backlog_Equipo.md)  
**Análisis:** [`../00_Analisis_Encargo_Final.md`](../00_Analisis_Encargo_Final.md)

Estándares: **25010** (desempeño, seguridad), **27001** (hardening), **29119**; NFR-PERF umbral **300 ms**.

---

## Checklist

- [x] EV56-04 INC-04 quitar delay *(before/after + humo FE 2026-11-25; Nico avisado)*  
- [x] EV56-08 INC-05 CORS + headers *(curl + humo FE + /docs 2026-11-27)*  
- [ ] EV56-10 Fuerza bruta / lockout (evidencia + sync Nico)  
- [x] EV56-13 JMeter → 5000 VU *(A–E 2026-11-27; E = 5000 logins, error HTTP 0 %)*  
- [ ] EV56-14 John retest  
- [ ] EV56-15 ZAP before/after  
- [x] EV56-17 Wireshark carga *(pcap + I/O Graph D 2500 y E 5000)*  
- [ ] Handoff KPIs a Ninna  

---

## EV56-04 — INC-04 quitar delay (bloqueante para 5000 VU)

1. Buscar `delayMiddleware` / `5000` en backend. **Hecho.**  
2. Medir **antes** con curl. **Hecho** 2026-11-25 00:57: `GET /pacientes` 200 **5.028832 s**, `GET /examenes` 200 **5.053524 s**.  
3. Eliminar delay; rebuild API. **Hecho** — `delayMiddleware` retirado de `pacientes.js`, `examenes.js`, `documentos.js`. Queda `BACKEND/src/middleware/delay.js` sin usos.  
4. Medir **después**. **Hecho** 2026-11-25 01:13: `GET /pacientes` 200 **0.029100 s**, `GET /examenes` 200 **0.031565 s**. Carpeta [`Evidencias/EV56-04/`](./Evidencias/EV56-04/README.md).  
5. Humo FE: login + listados. **Hecho** 2026-11-25 01:32: pacientes 304 / 23 ms, exámenes 304 / 11 ms, listas con datos.  
6. Avisar a Nicolás (Selenium) y liberar JMeter. **Hecho.**

**DoD:** sin espera artificial; timing before/after archivado. **Cumplido** (curl 1 VU + humo FE).

---

## EV56-08 — INC-05 CORS y cabeceras

1. Revisar `cors` / headers en `app.js`. **Hecho** — `app.use(cors())` sin origen.  
2. CORS al origen FE (`http://localhost:3333`), no `*`. **Hecho.**  
3. Headers: `X-Content-Type-Options`, `X-Frame-Options`, ocultar `X-Powered-By` si aplica. **Hecho** en `BACKEND/src/app.js`.  
4. Verificar con `curl -i`; no romper FE ni `/docs`. **Hecho** 2026-11-27: ANTES `Allow-Origin: *` + `X-Powered-By`; DESPUÉS origen acotado, `evil.example` sin `Allow-Origin`, `nosniff` + `DENY`. Humo FE login/listados 200; Swagger `/docs` abre.  
5. Evidencias TXT/PNG. **Hecho** — [`Evidencias/EV56-08/`](./Evidencias/EV56-08/README.md) (`*-INC-05.png`).

**DoD:** headers presentes; FE operativo. **Cumplido.** OPTIONS no capturado (filtro Fetch/XHR). No merge a `main` hasta retest de equipo.

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

1. Plan `.jmx` no-GUI con login + GET de lectura (exámenes/pacientes). **Hecho** — `EV56-13 Cuidarte 5000.jmx`.  
2. Ramp: 100 → 500 → 1000 → 2500 → **5000**. **Hecho** 2026-11-27. Primer intento E leyó 2500 VU (jmx sin guardar); reintento E: **5000 logins**.  
3. Registrar por fase: samples, avg, p90, p95, error %, throughput. **Hecho** — tabla en [`Evidencias/EV56-13/README.md`](./Evidencias/EV56-13/README.md). Sin PNG de CPU/RAM.  
4. Dashboard HTML desde `.jtl`. **Hecho** `dashboard-faseA`…`dashboard-faseE`.  
5. Comparar p95 vs **300 ms**. Solo **fase A** cumple (GET p95 ~266 ms). B–E residual de capacidad (0 % error HTTP).  
6. Intento 5000: **Hecho** (error HTTP 0 %; p95 GET ~14,5 s; throughput 344 txn/s).

**DoD:** intento 5000 documentado + gráficos para §5.1. **Cumplido.**

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

1. Iniciar captura en puerto API antes de fase alta de JMeter. **Hecho** — loopback, `tcp.port == 4444`, fases D y E.  
2. Guardar `.pcapng` + I/O Graph / retransmissions. **Hecho** — [`Evidencias/EV56-17/`](./Evidencias/EV56-17/README.md). D: errores TCP ≈ 0. E: errores TCP ~200–280 s.  
3. Párrafo corto para Ninna (volumen, errores TCP). **Hecho** en el README de EV56-17.

**DoD:** anexo de red ligado a estrés. **Cumplido.**

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
