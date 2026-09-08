# Anexo — OWASP ZAP en el plan de pruebas Cuidarte+

## ¿Lo exige la rúbrica?

**No de forma obligatoria.**

La EV1 evalúa el **diseño** de un plan de pruebas (IE1–IE5): criterios, tipos, estrategia, recursos, ≥5 casos y cobertura. No pide ejecutar herramientas ni adjuntar reportes de escaneo.

| Indicador | ¿ZAP aporta? | Cómo |
|-----------|--------------|------|
| IE2 | Sí (opcional) | Tipifica pruebas de **seguridad** (DAST) |
| IE3 | Sí (opcional) | Evidencia de caso no funcional de seguridad (refuerza CP-04 / NFR-SEG-5) |
| IE4 | Sí (opcional) | Justifica ZAP como **herramienta** de la estrategia |
| IE1 / IE5 | Indirecto | Relaciona hallazgos con NFR-SEG y normas (21.663, 21.719) |

**Conclusión:** un informe ZAP es un **plus de evidencia**, no un requisito. Si el tiempo aprieta, basta nombrar ZAP en estrategia/recursos (ya está). Si puedes ejecutarlo, súbelo como anexo al Word.

---

## Encaje con Cuidarte+

| Objetivo ZAP | NFR / caso | Qué buscar |
|--------------|------------|------------|
| DAST baseline sobre API/FE | NFR-SEG-5, CP-04 | XSS, headers, paths sensibles |
| Spider + active selectivo | NFR-SEG-4 | Acceso a rutas admin sin rol |
| TLS / HTTPS (si hay proxy) | NFR-SEG-1 | Tráfico en claro |
| Info disclosure | NFR-SEG-6 / 8 | Stack traces, datos en respuestas |

**Targets sugeridos (Docker levantado):**

- Frontend: `http://localhost:3333`
- Backend / Swagger: `http://localhost:4444` y `http://localhost:4444/docs`

> No apuntes ZAP a datos reales de pacientes. Usa cuentas `*.qa` y dataset sintético.

---

## Cómo generar el reporte (cuando Docker esté up)

1. Inicia Cuidarte+: `docker-compose up -d` en la raíz del repo.  
2. Abre **OWASP ZAP** (instalación en `C:\Program Files\ZAP\`).  
3. Modo recomendado para la EV1: **Automated Scan** o **Baseline** (rápido, menos agresivo).  
4. URL: primero `http://localhost:3333`; luego, si aplica, API `http://localhost:4444`.  
5. Exporta: **Report → Generate HTML/PDF Report** (o JSON).  
6. Guarda el archivo en:

`docs/EV1 Entrega/Anexos/OWASP_ZAP_CuidartePlus_<fecha>.html` (o `.pdf`)

---

## Plantilla para el informe (pegar en Word como Anexo B)

### B.1 Objetivo
Ejecutar un análisis dinámico (DAST) con OWASP ZAP sobre el ambiente local de Cuidarte+, para complementar el caso **CP-04** (NFR-SEG-4 / NFR-SEG-5).

### B.2 Alcance del escaneo
- Ambiente: local Docker  
- URLs: …  
- Tipo de escaneo: Baseline / Automated (pasivo + activo limitado)  
- Autenticación usada: [ninguna / token de paciente.qa / …]  
- Fecha: …

### B.3 Resumen de hallazgos

| Severidad | Cantidad | Ejemplos (título alerta) | ¿Relacionado a NFR? |
|-----------|----------|--------------------------|---------------------|
| High | | | |
| Medium | | | |
| Low | | | |
| Informational | | | |

### B.4 Interpretación para Cuidarte+
- Hallazgos **High/Medium** de inyección o XSS → fallan criterios de CP-04 / NFR-SEG-5.  
- Missing security headers → mejora de hardening (NFR-SEG / NCh27002), no siempre bloqueante del encargo.  
- Falsos positivos: documentar cuáles y por qué se descartan.

### B.5 Conclusión del anexo
El uso de ZAP materializa la herramienta declarada en la estrategia de pruebas y aporta evidencia objetiva de pruebas no funcionales de seguridad, alineada a IE3 e IE4, sin reemplazar el diseño de casos del plan.

---

## Bitácora de ejecución (llenar)

| Campo | Valor |
|-------|-------|
| Ejecutado por | Nicolás Barra |
| Fecha | 2026-09-07 |
| Versión ZAP | ghcr.io/zaproxy/zaproxy:stable (baseline) |
| Target | FE `localhost:3333` + API `localhost:4444` |
| Archivo reporte | Ver carpeta `Anexos/` + `Informe_OWASP_ZAP_CuidartePlus.md` |
| High abiertos | 0 FAIL · solo WARN headers |
| ¿Se adjunta al Word AVA? | Sí (recomendado: PDF resumen + interpretativo MD) |
