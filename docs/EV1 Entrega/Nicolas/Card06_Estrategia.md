# Card 6 — Estrategia de pruebas (Nicolás)

**Sección del informe:** 4. Estrategia de pruebas y justificación  
**Rúbrica:** IE4 (25%)  
**Estado:** Listo para pegar en Word

---

## 4. Estrategia de pruebas y justificación

### 4.1 Enfoque general: mixto

Para Cuidarte+ se adopta un **enfoque mixto** (manual + automatizado), porque el sistema combina:

- flujos de negocio verificables por API (login, CRUD de pacientes/exámenes, auditoría);
- controles de seguridad que deben validarse de forma objetiva (RBAC, inyección, sesión JWT);
- atributos de experiencia de usuario (usabilidad para adultos mayores y responsive) que requieren juicio humano.

| Enfoque | Qué se automatiza / ejecuta | Por qué |
|---------|-----------------------------|---------|
| **Automatizado** | Unitarias, colección API (Postman), smoke, carga (k6), DAST básico (ZAP) | Repetible, barato en regresión, medible (ms, HTTP) |
| **Manual** | E2E por rol en UI React, usabilidad con adulto mayor, revisión visual de accesibilidad | El ERS exige pruebas con usuarios mayores y flujos claros |

**Justificación:** automatizar solo no cubre NFR-USAB; probar solo a mano no garantiza umbrales NFR-PERF ni controles NFR-SEG de forma sistemática.

### 4.2 Etapas del proceso

| # | Etapa | Objetivo | RF / NFR | Herramientas |
|---|-------|----------|----------|--------------|
| 1 | Análisis y diseño | Riesgos, casos, datos sintéticos | Todos | ERS, matriz de trazabilidad |
| 2 | Unitarias | Validaciones y lógica aislada | NFR-SEG-2, NFR-SEG-9 | Jest |
| 3 | Integración API | Contratos REST reales del backend | RF-1…RF-5, NFR-SEG-4 | Postman, Swagger (`/docs`) |
| 4 | Sistema / E2E UI | Flujos Admin / Médico / Paciente | RF-2…RF-4, NFR-USAB-2 | Checklist manual + navegador |
| 5 | Seguridad | RBAC, XSS/SQLi, sesión, exposición | NFR-SEG-1…9, RB-1…3 | Postman, OWASP ZAP |
| 6 | Rendimiento | Latencia CRUD y concurrencia | NFR-PERF-1…3 | k6 / JMeter |
| 7 | Usabilidad / compatibilidad | Adulto mayor + móvil/tablet | NFR-USAB, NFR-COMPAT | Lighthouse, UAT |
| 8 | Cierre | Defectos, cobertura, DoD | IE5 | Informe + matriz |

**Endpoints de referencia del backend Cuidarte+ (ambiente local/Docker):**

| Recurso | Rutas base |
|---------|------------|
| Auth | `POST /autenticacion/login`, `POST /autenticacion/registro` |
| Usuarios | `/usuarios` |
| Pacientes | `/pacientes` |
| Exámenes | `/examenes` |
| Documentos | `/documentos` |
| Auditoría | `/auditoria` |
| API docs | `/docs`, `/openapi.json` |

Puerto expuesto típico según README del proyecto: **4444** (backend) / **3333** (frontend).

### 4.3 Priorización por riesgo

| Prioridad | Área | Motivo técnico-legal |
|-----------|------|----------------------|
| **P0** | Autenticación JWT, RBAC, documentos clínicos | Filtración de datos de salud (Ley 19.628 / 21.719) |
| **P1** | Auditoría y logs seguros | Evidencia ante incidentes (Ley 21.663 / RF-5.1) |
| **P2** | CRUD pacientes y exámenes | Núcleo funcional del negocio |
| **P3** | Rendimiento | Umbrales contractuales del ERS |
| **P4** | Usabilidad / compatibilidad | Adopción por adultos mayores y multi-dispositivo |

### 4.4 Criterios de entrada y salida

**Entrada (Ready for Testing):**

1. ERS de Cuidarte+ disponible y estable.
2. Stack levantado con Docker Compose (PostgreSQL + backend + frontend).
3. Usuarios de prueba por rol: `admin.qa`, `medico.qa`, `paciente.qa` (datos sintéticos).
4. Casos CP-01 a CP-06 diseñados y revisados.
5. Acceso a Swagger (`/docs`) para contratos de API.

**Salida (Definition of Done del ciclo):**

1. 100% de casos **P0/P1** ejecutados y documentados.
2. Sin hallazgos **críticos** abiertos de seguridad (NFR-SEG).
3. NFR-PERF-1 verificado en ambiente QA (CRUD < 300 ms bajo carga normal).
4. Matriz de trazabilidad actualizada (insumo a Skarlett — Card 5).
5. Bitácora de defectos entregada al equipo.

### 4.5 Criterios de aceptación transversales

Un caso se **aprueba** solo si:

1. El resultado observado = resultado esperado del caso.
2. Se respeta RB-1 / RB-2 / RB-3 según el actor.
3. No hay exposición de datos clínicos a roles no autorizados.
4. Un fallo de seguridad o cumplimiento **no** se considera “pasado” aunque la UI se vea correcta.

### 4.6 Criterios de entrada/salida por fase (detalle)

| Fase | Entrada | Salida |
|------|---------|--------|
| Unitarias | Código compilable / dependencias instaladas | Suite Jest verde en módulos críticos |
| API | Backend healthy + BD con seed | Colección Postman P0/P1 OK |
| E2E UI | Frontend apunta al API QA | Flujos por rol sin bloqueos |
| Seguridad | Tokens por rol disponibles | Checklist OWASP sin críticos |
| Rendimiento | Dataset sintético cargado | Informe latencias vs 300 ms |
| Usabilidad | Checklist accesibilidad | Acta UAT adulto mayor |

---

**Checklist Card 6**

- [x] Enfoque mixto justificado
- [x] Etapas con RF/NFR y herramientas
- [x] Priorización P0–P4
- [x] Entrada/salida globales y por fase
- [x] Endpoints reales del backend
