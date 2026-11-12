# BACKLOG — Ari Araya (EV3 / EP5)

**Continuidad EV2:** seguridad dinámica (ZAP, curl/headers, John), rendimiento (JMeter), disponibilidad.  
**Tablero:** [`../00_Backlog_Equipo.md`](../00_Backlog_Equipo.md)  
**Evidencias:** [`../Evidencias/JMeter`](../Evidencias/JMeter), [`Wireshark`](../Evidencias/Wireshark), [`Postman`](../Evidencias/Postman), [`Logs`](../Evidencias/Logs)

Estándares: **ISO/IEC 25010** (eficiencia de desempeño, seguridad), **27001** (hardening, criptografía de claves), **29119** (métricas de ejecución), NFR-PERF del ERS (umbral **300 ms**).

---

## Checklist rápido

- [ ] EV3-04 INC-04 quitar delay  
- [ ] EV3-08 INC-05 CORS + headers  
- [ ] EV3-12 JMeter → 5000 VU  
- [ ] EV3-13 John retest CP-15  
- [ ] EV3-14 ZAP autenticado  
- [ ] EV3-16 Wireshark bajo carga  
- [ ] Handoff KPIs a Giannina  

---

## EV3-04 — INC-04 Eliminar `delayMiddleware(5000)`

### Objetivo
Quitar el retraso artificial de 5 s que hace fallar NFR-PERF-1 y vuelve inviable JMeter 5000.

### Pasos

1. Buscar en backend: `delayMiddleware`, `5000`, usos en rutas de exámenes/pacientes/documentos.
2. **Antes (evidencia baseline rápida):**
   ```powershell
   curl.exe -o NUL -s -w "time_total=%{time_total}\n" -H "Authorization: Bearer <TOKEN>" http://localhost:4444/examenes
   ```
   Capturar tiempo ~5 s → `Evidencias/Logs/EV3-04-before-timing.txt`.
3. Eliminar o desactivar el middleware (preferible eliminar en branch EV3; no dejar flag “accidentalmente on”).
4. Rebuild contenedor API: `docker compose up -d --build` (servicio API).
5. **Después:** mismo curl; tiempo debe ser ≪ 5 s (idealmente cientos de ms en vacío).
6. Humo: login + listar exámenes en FE.
7. Avisar a Nicolás (Selenium) y a ti mismo (JMeter listo).

### DoD
- [ ] Código sin delay 5000  
- [ ] Timing before/after archivado  
- [ ] Nota 25010 desempeño en bitácora  

### Criterio de aceptación
GET autenticado de listados clínicos sin espera artificial de 5 s.

---

## EV3-08 — INC-05 CORS y cabeceras de seguridad

### Objetivo
Cerrar CORS `*` abierto y ausencia de cabeceras (hallazgo CP-04 / INC-05).

### Pasos

1. Revisar `app.js` (o equivalente): `cors()`, helmet, headers manuales.
2. Configurar:
   - CORS: origen del FE (`http://localhost:3333`) — no `*`.
   - Headers mínimos: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY` o `SAMEORIGIN`, quitar/ocultar `X-Powered-By` si aplica, CSP acorde al FE.
   - HSTS solo tiene sentido con HTTPS (coordinar con Skarlett CP-14); si solo HTTP, documentar limitación.
3. Verificación:
   ```powershell
   curl.exe -i http://localhost:4444/examenes
   curl.exe -i -X OPTIONS http://localhost:4444/examenes -H "Origin: http://localhost:3333" -H "Access-Control-Request-Method: GET"
   ```
4. Evidencias PNG/TXT: `EV3-08-headers-after.txt`.
5. No romper Swagger `/docs` ni el FE: probar login UI.

### DoD
- [ ] Headers presentes  
- [ ] CORS acotado  
- [ ] FE sigue operando  

---

## EV3-12 — JMeter: ramp hasta 5000 usuarios concurrentes (obligatorio)

### Objetivo
Prueba de concurrencia/estrés con **5000** usuarios virtuales, con métricas y gráficos para el informe.

### Precondiciones
- EV3-04 **Hecho**.  
- API estable; token de médico (o login sampler en el plan).  
- Máquina con recursos monitoreados (Administrador de tareas / `docker stats`).

### Diseño del plan `.jmx`

1. Crear `Evidencias/JMeter/EV3-12-Cuidarte_5000.jmx` (o carpeta `Ari/jmeter/`).
2. Thread Groups **escalonados** (mismo plan, TG distintos o ejecuciones sucesivas):

| Fase | VU | Ramp-up | Duración / loops | Propósito |
|------|----|---------|------------------|-----------|
| A | 100 | 30 s | 2–3 min | Humo carga |
| B | 500 | 60 s | 3 min | Estabilidad |
| C | 1000 | 90 s | 3–5 min | Escalamiento |
| D | 2500 | 120 s | 3–5 min | Pre-estrés |
| E | **5000** | 180–300 s | 3–5 min | Requisito EP5 |

3. Samplers mínimos:
   - `POST /auth/login` (o setUp Thread Group que guarde token).
   - `GET /examenes` (o endpoint de lectura frecuente) con Bearer.
   - (Opcional) `GET /pacientes` con menor peso.
4. Listeners: Backend Listener / Simple Data Writer → `.jtl`. Al final generar dashboard:
   ```text
   jmeter -g resultados.jtl -o Evidencias/JMeter/EV3-12-dashboard-5000
   ```
5. Ejecutar **no-GUI**:
   ```powershell
   jmeter -n -t EV3-12-Cuidarte_5000.jmx -l Evidencias/JMeter/EV3-12-faseE-5000.jtl -e -o Evidencias/JMeter/EV3-12-dashboard-5000
   ```
   (Ajustar path a tu instalación o imagen Docker `justb4/jmeter` como en EV2.)

### Métricas a registrar (tabla para Giannina)

| Fase | VU | Samples | Avg (ms) | p90 | p95 | Error % | Throughput | CPU host | RAM | Notas |
|------|----|---------|----------|-----|-----|---------|------------|----------|-----|-------|
| A | 100 | | | | | | | | | |
| … | | | | | | | | | | |
| E | 5000 | | | | | | | | | |

Comparar avg/p95 contra **300 ms** (NFR-PERF-1). Si el delay ya no está y aun así p95 ≫ 300 ms, documentar como residual de capacidad, no como INC-04.

### Si el hardware no aguanta 5000

1. Ejecutar igual la fase E y **guardar** errores de conexión / timeouts.  
2. Registrar techo estable (p. ej. 1500 VU con error % &lt; 1 %).  
3. En bitácora e informe:  
   - “Se intentó 5000 VU; el cuello de botella fue el host/Docker; evidencia en …”  
   - No ocultar el requisito; mostrar ambas corridas (máximo estable + intento 5000).

### Evidencias
- `.jmx`, `.jtl` por fase (o al menos C/D/E).  
- Dashboard HTML.  
- Capturas: summary report, `docker stats`, Administrador de tareas.  
- Prefijo `EV3-12-`.

### DoD
- [ ] Intento 5000 documentado  
- [ ] Dashboard + tabla KPI  
- [ ] Gráficos exportables para §5.1  

---

## EV3-13 — Retest CP-15 (John the Ripper) post-bcrypt

### Objetivo
Demostrar que INC-01 quedó cerrado: John debe ver **hashes**, no texto plano.

### Pasos

1. Esperar aviso de Nicolás (EV3-01 Hecho).
2. Extraer columna `contrasena` a `Evidencias/Logs/EV3-13-hashes.txt` (solo laboratorio).
3. Ejecutar John (Docker como en EV2 si aplica).
4. Resultados esperados:
   - Ya **no** aparece “No password hashes loaded” por texto plano.
   - Los valores se reconocen como bcrypt (`$2…`).
5. Evidencia: terminal + (opcional) `\d` / select redactado.
6. Conclusión bitácora: CP-15 **Aprobado** (o Fallido si aún hay plain).

### DoD
- [ ] Output John archivado  
- [ ] Estado CP-15 actualizado para Giannina  

---

## EV3-14 — ZAP autenticado (retest)

### Objetivo
Repetir DAST con sesión tras hardening INC-05.

### Pasos

1. Importar OpenAPI `/docs-json` o equivalente.
2. Reglas Bearer con token médico y paciente (como EP3).
3. Active scan acotado al laboratorio.
4. Exportar reporte HTML/XML a `Evidencias/` (o capturas si la exportación falla — en EV2 falló el export: **esta vez priorizar export**).
5. Registrar: High / Medium / Low counts.
6. Cruzar con curl de headers (EV3-08).

### DoD
- [ ] Evidencia ZAP con fecha  
- [ ] Comparación cualitativa vs EV2 (0 High se mantiene / mejora Medium)  

---

## EV3-16 — Wireshark bajo carga

### Objetivo
Complementar JMeter con evidencia de tráfico (retransmisiones, volumen, errores TCP).

### Pasos

1. Iniciar captura filtrada a puerto API antes de la fase D o E.
2. Correr JMeter.
3. Detener captura; guardar `EV3-16-carga.pcapng`.
4. Anotar: conversaciones, retransmissions, resets (Statistics → Conversations / I/O Graph).
5. PNG del I/O Graph → informe.
6. Coordinar con Skarlett si también captura TLS: no duplicar el mismo relato; tú enfocas **estrés**, ella **confidentiality en tránsito**.

### DoD
- [ ] pcap + 1–2 capturas de estadísticas  
- [ ] Párrafo KPI/red para Giannina  

---

## Handoff a Giannina (§5.1 rendimiento + seguridad dinámica)

Entregar:

1. Tabla de fases JMeter completa.  
2. Rutas a dashboards y pcap.  
3. Estado CP-04, CP-05, CP-15, CP-19 (si se corre), CP-21 si tocas disponibilidad.  
4. Tres bullets de remediación: INC-04, INC-05, INC-01 (verificación).  
5. Gráficos sugeridos: latencia vs VU; error % vs VU; before/after delay.

Plantilla bitácora: igual formato que Nicolás (`Fecha | Item | Herramienta | Resultado | Evidencia | INC | Notas`).

---

## Orden recomendado

| Día | Foco |
|-----|------|
| D1 | EV3-04 (+ sync Nicolás bcrypt) |
| D2 | EV3-08 headers; smoke FE |
| D3 | EV3-12 fases A–C |
| D4 | EV3-12 fases D–E + EV3-16 Wireshark |
| D5 | EV3-13 John + EV3-14 ZAP + handoff |
