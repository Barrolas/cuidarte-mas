# EV1 Cuidarte+ — Tablero de cards (Trello)

**Asignatura:** ISY1102 — Seguridad y Calidad en el Desarrollo de Software  
**Encargo:** Diseñando un plan de pruebas seguro, legal y normativo (17%)  
**Equipo:** Skarlett (normativo / redacción) · Nicolás (técnico)

---

## Resumen de asignación

| Card | Título | Responsable | Rúbrica |
|------|--------|-------------|---------|
| 1 | Portada, formato y ensamblaje final | Skarlett | IE4 |
| 2 | Introducción y contexto del plan | Skarlett | IE1, IE4 |
| 3 | Criterios de calidad, seguridad y normativa | Skarlett | IE1, IE4 |
| 4 | Tipos de pruebas y justificación | Skarlett | IE2 |
| 5 | Análisis de cobertura y coherencia | Skarlett | IE5 |
| 6 | Estrategia de pruebas | Nicolás | IE4 |
| 7 | Recursos y cronograma | Nicolás | IE4 |
| 8 | Casos funcionales + auditoría (CP-01 a CP-03) | Nicolás | IE2, IE3 |
| 9 | Casos seguridad y rendimiento (CP-04, CP-05) | Nicolás | IE3 |
| 10 | Caso usabilidad/compatibilidad + revisión (CP-06) | Nicolás | IE3, IE5 |

**Entregable unificado:** [Informe_Plan_Pruebas_CuidartePlus.md](./Informe_Plan_Pruebas_CuidartePlus.md)

---

## Card 1 — Portada, formato y ensamblaje final

**Asignada a:** Skarlett  
**Etiquetas:** `Formal` `Entrega` `IE4`  
**Estado:** Completada en el informe

**Checklist:**
- [x] Portada con integrantes, carrera, sección, docente y fecha
- [x] Estructura alineada a plantilla e Ítem I del encargo
- [x] Unificación de títulos y numeración
- [x] Verificación de las 6 secciones obligatorias
- [ ] Exportar a Word/PDF (Arial 12/11, interlineado 1,5) y subir a AVA el día del cuestionario

---

## Card 2 — Introducción y contexto del plan

**Asignada a:** Skarlett  
**Etiquetas:** `Sección 1` `IE1` `IE4`

**Checklist:**
- [x] Describir Cuidarte+ (alcance, actores, stack)
- [x] Propósito del plan (calidad + seguridad + legal)
- [x] Objetivos y alcance de las pruebas
- [x] Estructura del informe
- [x] Vinculación con códigos RF/NFR del ERS

---

## Card 3 — Criterios de calidad, seguridad y normativa

**Asignada a:** Skarlett  
**Etiquetas:** `Sección 2` `IE1` `IE4` `Legal`  
**Prioridad:** Crítica para Skarlett

**Checklist:**
- [x] Matriz criterio → ERS → norma/estándar
- [x] Calidad: usabilidad, rendimiento, disponibilidad, mantenibilidad
- [x] Seguridad: TLS, bcrypt, RBAC, JWT, CSRF/XSS/SQLi, logs, backups
- [x] Legal: Ley 19.628, 21.719, 21.663, DTO 181 / NCh27002
- [x] Accesibilidad: Manual Accesibilidad Web
- [x] Justificación del dominio clínico

---

## Card 4 — Tipos de pruebas y justificación

**Asignada a:** Skarlett  
**Etiquetas:** `Sección 3` `IE2`

**Checklist:**
- [x] Clasificar funcionales, no funcionales, seguridad, usabilidad, rendimiento, compatibilidad, integración, humo/regresión
- [x] Propósito + RF/NFR + ejemplo Cuidarte+ por tipo
- [x] Distinción explícita funcional vs no funcional
- [x] Accesibilidad y cumplimiento normativo como categorías
- [x] Revisión técnica cruzada (contenido unificado en el informe)

---

## Card 5 — Análisis de cobertura y coherencia

**Asignada a:** Skarlett  
**Etiquetas:** `Sección cierre` `IE5`

**Checklist:**
- [x] Matriz de trazabilidad RF/NFR → tipo → ID de caso
- [x] Brechas y priorización justificada
- [x] Coherencia estrategia ↔ recursos ↔ cronograma
- [x] Conclusión de cobertura ERS + marco legal
- [x] Recomendaciones de mejora

---

## Card 6 — Estrategia de pruebas

**Asignada a:** Nicolás  
**Etiquetas:** `Sección 4` `IE4` `Técnico`

**Checklist:**
- [x] Enfoque mixto (manual + automatizado) justificado
- [x] Etapas: unitarias, integración API, E2E, seguridad, carga, usabilidad
- [x] Priorización por riesgo (datos clínicos, auth, documentos)
- [x] Criterios de entrada/salida por fase
- [x] Herramientas: Postman/Swagger, Jest, OWASP ZAP, Lighthouse, k6
- [x] Vínculo de cada fase a RF/NFR

---

## Card 7 — Recursos y cronograma

**Asignada a:** Nicolás  
**Etiquetas:** `Sección 5` `IE4` `Técnico`

**Checklist:**
- [x] Recursos humanos
- [x] Recursos técnicos (Docker, BD de prueba, datos anonimizados)
- [x] Entorno staging con TLS y roles de prueba
- [x] Cronograma por fases
- [x] Estimación de esfuerzo

---

## Card 8 — Casos funcionales + auditoría (CP-01 a CP-03)

**Asignada a:** Nicolás  
**Etiquetas:** `Sección 6` `IE3` `Funcional`

| ID | ERS | Tipo |
|----|-----|------|
| CP-01 | RF-1.1 | Funcional / seguridad |
| CP-02 | RF-3.1 + RB-3 | Funcional |
| CP-03 | RF-5.1 | Funcional / auditoría |

**Checklist:**
- [x] Plantilla completa 6.1–6.7 por caso

---

## Card 9 — Casos seguridad y rendimiento (CP-04, CP-05)

**Asignada a:** Nicolás  
**Etiquetas:** `Sección 6` `IE3` `No funcional`  
**Prioridad:** Crítica para Nicolás

| ID | ERS | Tipo |
|----|-----|------|
| CP-04 | NFR-SEG-4 + RB-1 (+ NFR-SEG-5) | Seguridad / RBAC |
| CP-05 | NFR-PERF-1 | Rendimiento |

**Checklist:**
- [x] Criterios medibles (HTTP, tiempo, rol)
- [x] Sub-caso inyección / XSS (NFR-SEG-5) en CP-04
- [x] Datos de prueba anonimizados

---

## Card 10 — Caso usabilidad/compatibilidad + revisión (CP-06)

**Asignada a:** Nicolás  
**Etiquetas:** `Sección 6` `IE3` `IE5` `Técnico`

| ID | ERS | Tipo |
|----|-----|------|
| CP-06 | NFR-USAB-1 + NFR-COMPAT-2 | Usabilidad / compatibilidad |

**Checklist:**
- [x] Plantilla 6.1–6.7 de CP-06
- [x] Cobertura RF, NFR-SEG, NFR-PERF, NFR-USAB y RF-5
- [x] Revisión técnica de secciones normativas
- [x] Insumos para matriz de trazabilidad (Card 5)

---

## Bonus — Cuestionario AVA (individual)

**Material de estudio:** [02_Resumen_Estudio_Cuestionario_AVA.md](./02_Resumen_Estudio_Cuestionario_AVA.md)

- [ ] Repasar IL 1.1–1.5, tipos de prueba, OWASP básico (usar resumen §1–3)
- [ ] Revisar normas en `docs/EV1 Contexto/Normativas/` (usar resumen §5)
- [ ] Completar mini autoevaluación del resumen (§7)
- [ ] Rendir cuestionario sin IA ni recursos externos (1 intento)
