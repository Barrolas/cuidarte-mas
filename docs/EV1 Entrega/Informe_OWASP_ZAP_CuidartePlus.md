# Anexo B — Informe OWASP ZAP (Cuidarte+)

**Asignatura:** ISY1102 · EV1  
**Ejecutado por:** Nicolás Barra  
**Fecha:** 7 de septiembre de 2026  
**Herramienta:** OWASP ZAP (imagen `ghcr.io/zaproxy/zaproxy:stable`) · `zap-baseline.py`  
**Ambiente:** Docker local Cuidarte+ (FE `:3333`, API `:4444`)  
**Tipo de escaneo:** Baseline (pasivo + reglas baseline; no pentest autenticado profundo)

> Este anexo es **evidencia complementaria** (IE3/IE4). No reemplaza el diseño de casos del plan.  
> **Resultado global:** 0 FAIL · solo WARN / INFO de hardening (headers). Ningún High crítico de inyección/XSS en este baseline.

---

## 1. Alcance

| Target | URL | Reporte PDF | Reporte MD | HTML / JSON |
|--------|-----|-------------|------------|-------------|
| Frontend (nginx/React) | `http://localhost:3333` | [OWASP_ZAP_FE_CuidartePlus.pdf](./Anexos/OWASP_ZAP_FE_CuidartePlus.pdf) | [OWASP_ZAP_FE_CuidartePlus.md](./Anexos/OWASP_ZAP_FE_CuidartePlus.md) | `.html` / `.json` |
| Backend (Express API) | `http://localhost:4444` | [OWASP_ZAP_API_CuidartePlus.pdf](./Anexos/OWASP_ZAP_API_CuidartePlus.pdf) | [OWASP_ZAP_API_CuidartePlus.md](./Anexos/OWASP_ZAP_API_CuidartePlus.md) | `.html` / `.json` |

**No incluido en este corrido:** escaneo autenticado con JWT de `paciente.qa`/`medico.qa`, active scan agresivo, ni fuzzing de todos los endpoints OpenAPI. Eso puede ampliarse en un ciclo posterior ligado a CP-04.

---

## 2. Resumen ejecutivo

| Target | FAIL | WARN | PASS (reglas) | Lectura para EV1 |
|--------|------|------|---------------|------------------|
| Frontend `:3333` | 0 | 10 tipos | 57 | Faltan headers de seguridad (CSP, clickjacking, X-Content-Type-Options, etc.) |
| API `:4444` | 0 | 6 tipos | 61 | Falta X-Content-Type-Options; filtra `X-Powered-By`; CORS amplio (Cross-Domain Misconfiguration) |

**Relación con casos del plan:** refuerza **CP-04** / **NFR-SEG-5** (superficie de ataque y hardening) y **NFR-SEG-1** (TLS aún no forzado en local HTTP — esperado en ambiente de desarrollo).

---

## 3. Hallazgos Frontend (`:3333`)

| Severidad ZAP | Alerta | Inst. | Relación NFR / plan | Interpretación |
|---------------|--------|------:|---------------------|----------------|
| Medium | Content Security Policy (CSP) Header Not Set | 3 | NFR-SEG-5 / hardening | Mitigar XSS con CSP en nginx |
| Medium | Missing Anti-clickjacking Header | 2 | NFR-SEG-5 | Agregar `X-Frame-Options` o CSP `frame-ancestors` |
| Medium | Sub Resource Integrity Attribute Missing | 5 | Hardening FE | SRI en scripts/estilos externos si aplica |
| Low | X-Content-Type-Options Header Missing | 5 | NFR-SEG-5 | `nosniff` |
| Low | Server Leaks Version Information (`Server`) | 5 | NFR-SEG-6 | Ocultar banner nginx |
| Low | Permissions Policy / COOP / COEP / CORP missing | varios | Hardening | Headers modernos de aislamiento |
| Low | Timestamp Disclosure - Unix | 1 | Info leak menor | Revisar asset JS |
| Informational | Modern Web Application / Cacheable Content | — | Informativo | SPA: baseline limitado sin auth |

---

## 4. Hallazgos API (`:4444`)

| Severidad ZAP | Alerta | Inst. | Relación NFR / plan | Interpretación |
|---------------|--------|------:|---------------------|----------------|
| Medium | CSP: Failure to Define Directive… | 2 | Menor en API JSON | Más relevante en respuestas HTML/404 |
| Medium | Cross-Domain Misconfiguration | 3 | NFR-SEG-4/5, CORS | Revisar `cors()` abierto; restringir orígenes en prod |
| Low | X-Powered-By information leak | 3 | NFR-SEG-6 | Deshabilitar header Express |
| Low | X-Content-Type-Options Missing | 1 | Hardening | `nosniff` en respuestas |
| Low | Permissions Policy Not Set | 2 | Hardening | Opcional en API |
| Informational | Storable and Cacheable Content | 3 | Informativo | Cuidado con cache de datos clínicos en proxies |

---

## 5. Conclusión para la rúbrica

1. El baseline **no encontró FAIL** de inyección/XSS en las URLs alcanzadas sin autenticación.  
2. Sí evidencia **deuda de hardening** (headers), coherente con una estrategia DevSecOps y con **NCh27002** / **Ley 21.663** (controles preventivos).  
3. Para cerrar el círculo con **CP-04**, el siguiente paso recomendado es un escaneo **autenticado** (token paciente intentando `/usuarios`) + prueba manual Postman ya diseñada.  
4. En producción debe medirse además **TLS** (NFR-SEG-1); este ambiente local usa HTTP.

**Veredicto EV1:** anexo válido como evidencia de herramienta DAST declarada en la estrategia; hallazgos Medium/Low de configuración, sin bloqueo crítico del diseño del plan.

---

## 6. Cómo reproducir

```powershell
docker-compose up -d
# desde docs/EV1 Entrega/Anexos montado en /zap/wrk:
docker run --rm --add-host=host.docker.internal:host-gateway `
  -v "${PWD}:/zap/wrk:rw" -t ghcr.io/zaproxy/zaproxy:stable `
  zap-baseline.py -t http://host.docker.internal:3333 `
  -r OWASP_ZAP_FE_CuidartePlus.html -w OWASP_ZAP_FE_CuidartePlus.md -J OWASP_ZAP_FE_CuidartePlus.json -I
```

PDF generados con Microsoft Edge headless (`--print-to-pdf`) a partir de los HTML de ZAP.
