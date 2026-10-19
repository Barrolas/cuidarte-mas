# Resumen de estudio — Cuestionario AVA (EV1)

**Asignatura:** ISY1102 — Seguridad y Calidad en el Desarrollo de Software  
**Uso:** preparación **individual** del cuestionario (20 alternativas + 5 desarrollo)  
**Reglas del día:** 1 intento · **sin IA** · **sin recursos externos**

> Estudia este resumen **antes**. El día del cuestionario solo usas lo que memorices.

---

## 1. Indicadores de Logro (IL 1.1 – 1.5)

| IL | Idea clave (memorizar) | Pregunta típica |
|----|------------------------|-----------------|
| **IL 1.1** | La **calidad** aporta al éxito del producto; el **cumplimiento legal/normativo** es parte esencial del desarrollo, no un “extra” al final. | ¿Por qué calidad + seguridad + ley van juntas? |
| **IL 1.2** | Diferenciar **funcionales** (¿hace lo pedido?) vs **no funcionales** (¿lo hace bien: seguro, rápido, usable…?) e integrar criterios legales. | Clasificar un caso como funcional o no funcional |
| **IL 1.3** | Identificar **usabilidad**, **rendimiento** y **compatibilidad**; impactan calidad, accesibilidad, confiabilidad y ética. | ¿Qué prueba usas para adultos mayores / carga / navegadores? |
| **IL 1.4** | Un **plan de pruebas** incluye estrategia, objetivos, recursos y **cronograma**, coherente con requerimientos y normas. | Elementos mínimos de un plan |
| **IL 1.5** | Evaluar **consistencia y cobertura**: ¿el plan cubre RF/NFR y marcos legales? ¿hay brechas? | Matriz de trazabilidad / análisis de cobertura |

**Frase puente para desarrollo:**  
*“En Cuidarte+ la calidad no basta: hay datos clínicos (Ley 19.628 / 21.719), riesgos cibernéticos (Ley 21.663) y deber de trazabilidad; por eso el plan integra QA + seguridad + cumplimiento.”*

---

## 2. Tipos de prueba (mapa rápido)

### 2.1 Funcional vs no funcional

| | **Funcional** | **No funcional** |
|---|---------------|------------------|
| Pregunta | ¿El sistema hace lo que el ERS pide? | ¿Lo hace con calidad (seguro, rápido, usable…)? |
| Base | RF-1…RF-5, reglas de negocio | NFR-SEG, NFR-PERF, NFR-USAB, NFR-COMPAT, NFR-DIS |
| Ejemplo Cuidarte+ | Médico crea un examen (RF-3.1) | CRUD < 300 ms (NFR-PERF-1); paciente no puede borrar usuarios (RBAC) |

### 2.2 Catálogo que suelen preguntar

| Tipo | Propósito en una frase | Ejemplo Cuidarte+ |
|------|------------------------|-------------------|
| **Funcional** | Verificar requisitos de negocio | Login, CRUD exámenes |
| **Integración / API** | Capas React ↔ Express ↔ PostgreSQL | Endpoint login + JWT |
| **Seguridad** | Resistir ataques y fallas de acceso | RBAC, XSS, SQLi, TLS |
| **Usabilidad** | Facilidad de uso (incl. adultos mayores) | Contraste, botones grandes |
| **Accesibilidad** | Uso por diversidad funcional | Teclado, ARIA, tipografía |
| **Rendimiento / carga** | Tiempos y concurrencia | < 300 ms; ~200 usuarios |
| **Compatibilidad** | Navegadores y dispositivos | Chrome/Firefox/Safari/Edge; móvil |
| **Auditoría / cumplimiento** | Trazas y privacidad | Log al eliminar examen |
| **Humo (smoke)** | ¿Arranca lo crítico? | Login + listar pacientes |
| **Regresión** | Un fix no rompe lo anterior | Re-ejecutar suite tras parche |

### 2.3 Elementos de un plan de pruebas (IL 1.4)

1. Introducción / contexto y propósito  
2. Criterios de calidad, seguridad y normativa  
3. Tipos de prueba y justificación  
4. **Estrategia** (manual / automático / mixto)  
5. **Recursos** (humanos, técnicos, entorno)  
6. **Cronograma**  
7. Casos de prueba (≥5) con: ID, descripción, código ERS, datos, resultado esperado, criterio de aceptación, tipo  
8. (Buena práctica) Matriz de cobertura / brechas (IL 1.5)

**Criterios de entrada:** ambiente listo, ERS estable, datos de prueba, casos diseñados.  
**Criterios de salida (DoD):** P0/P1 ejecutados, sin críticos de seguridad abiertos, cobertura documentada.

---

## 3. OWASP básico (Top riesgos web / API)

Memoriza el **qué es** y un **control**:

| Riesgo | Qué es | Control típico |
|--------|--------|----------------|
| **Injection (SQLi)** | Entrada maliciosa altera consultas | Validar/parametrizar queries |
| **XSS** | Script malicioso en la página | Escapar/sanear salida; CSP |
| **Broken Access Control** | Usuario hace lo que no debería | RBAC en **backend**; denegar por defecto |
| **Broken Authentication** | Fallas de login/sesión | bcrypt, JWT corto, logout/revocación |
| **Security Misconfiguration** | Defaults inseguros, TLS ausente | Hardening, HTTPS obligatorio |
| **Sensitive Data Exposure** | Datos clínicos sin protección | Cifrado en tránsito (TLS) y en reposo |
| **CSRF** | Acción no deseada con sesión ajena | Tokens CSRF / SameSite |
| **Logging & Monitoring fallidos** | No hay evidencia del incidente | Logs de acciones críticas (auditoría) |

**SAST vs DAST (una línea cada uno):**
- **SAST:** analiza **código** (caja blanca).  
- **DAST:** prueba la app **en ejecución** (caja negra), ej. OWASP ZAP.  
- **SCA:** revisa **librerías** de terceros vulnerables.

**Shift-left:** incorporar seguridad **desde el diseño**, no solo al final.

---

## 4. Cuidarte+ — anclas del ERS (útil en desarrollo)

### Roles / reglas de negocio
- **Admin (RB-2):** CRUD completo.  
- **Médico (RB-3):** gestiona pacientes/exámenes; puede ver clínica de pacientes registrados.  
- **Paciente (RB-1):** **solo lectura** de lo suyo.  
- **Visitante:** solo registro.

### Stack
React (frontend) + Express/Node (API) + PostgreSQL · JWT · bcrypt · TLS · documentos en storage interno.

### NFR que más caen
- **SEG:** TLS, bcrypt, cifrado reposo, RBAC, CSRF/XSS/SQLi, logs, backups, datos personales, JWT.  
- **PERF:** CRUD < **300 ms**; home < **2 s**; ~**200** concurrentes.  
- **USAB:** tipografía/contraste/controles grandes; flujo paciente → exámenes.  
- **COMPAT:** últimas 2 versiones de navegadores modernos; responsive.

---

## 5. Normativas chilenas (carpeta `Normativas/`)

### 5.1 Tabla “una frase + dato clave”

| Norma | Para qué sirve en el curso | Dato clave para memorizar |
|-------|----------------------------|---------------------------|
| **Ley 19.628** Protección vida privada | Tratamiento de datos personales | Arts. **22** responsabilidad civil · **23** indemnización |
| **Ley 21.719** Protección datos personales | Marco moderno + sanciones a responsables | Art. **35**: leves ≤**5.000** UTM · graves ≤**10.000** · gravísimas ≤**20.000** |
| **Ley 21.663** Marco de ciberseguridad | Institucionalidad, deberes, incidentes | Art. **40**: leves ≤5.000 (≤10.000 si operador vital) · graves ≤10.000 (≤20.000) · gravísimas ≤20.000 (≤**40.000** vital). Arts. **36**/38 infracciones (también vía Código Penal) |
| **Ley 21.459** Delitos informáticos | Accesos indebidos, ataques, tipificación penal | Relacionar con auditoría y accesos no autorizados |
| **Ley 21.180** Transformación digital del Estado | Digitalización de procedimientos estatales | Contexto de Estado digital (menos central en Cuidarte+ privado, pero del set del curso) |
| **DTO 181** (+ Ley 19.799) | Documentos y firma electrónica | Título IV derechos usuarios · seguridad; remite a **NCh27002** |
| **NCh27002.Of2009** | Código de práctica de seguridad de la información | Controles de gestión (acceso, backups, políticas) |
| **Ley 17.336** Propiedad intelectual | Software/obras protegidas | Arts. **78–79** sanciones |
| **Manual Accesibilidad Web** | Accesibilidad e inclusión | Apoya NFR-USAB (contraste, tamaño, teclado) |
| **Política Nacional de Ciberseguridad** | Orientación país | Prevención, resiliencia, cultura de ciberseguridad |

### 5.2 Cómo conectar norma → prueba (respuesta tipo desarrollo)

| Norma | Traducción a prueba |
|-------|---------------------|
| 19.628 / 21.719 | Paciente no ve fichas ajenas; consentimiento/finalidad; no filtrar datos en logs |
| 21.663 | Controles de prevención; reporte de incidentes; hardening; RBAC |
| DTO 181 / NCh27002 | Integridad/acceso a documentos clínicos; checklist de controles |
| Accesibilidad | Prueba con adulto mayor; contraste; responsive |
| 21.459 + RF-5.1 | Intento de acceso indebido deja traza de auditoría |

### 5.3 Truco de escalas de multa (no confundir)

- **21.719 Art. 35** (datos): 5k / 10k / 20k UTM.  
- **21.663 Art. 40** (ciber): misma base, pero **duplica techo** si es **operador de importancia vital** (hasta 10k / 20k / **40k**).

---

## 6. ISO 25010 (calidad) — atributos frecuentes

Funcionalidad · **Rendimiento** · **Usabilidad** · Fiabilidad · Seguridad · Mantenibilidad · Compatibilidad · Portabilidad.

En el cuestionario: “¿Qué atributo mide X?” → ubicar en esta lista.

---

## 7. Mini banco de autoevaluación (sin mirar)

1. Diferencia funcional vs no funcional con un ejemplo de Cuidarte+.  
2. Nombra 3 elementos obligatorios de un plan de pruebas.  
3. ¿Qué es Broken Access Control y cómo se prueba en Cuidarte+?  
4. ¿Qué leyes aplican a datos clínicos y qué artículos de sanción recordamos?  
5. ¿Qué umbral de rendimiento fija el ERS para CRUD?  
6. SAST vs DAST en una línea.  
7. ¿Para qué sirve la matriz de trazabilidad (IL 1.5)?  
8. Diferencia multas 21.719 vs 21.663 (operador vital).

**Respuestas breves:**  
1) Funcional = crea examen; NF = <300 ms o 403 a paciente admin.  
2) Estrategia, recursos, cronograma (+ objetivos/casos).  
3) Paciente llama API admin → 403; RBAC backend.  
4) 19.628 (22–23) y 21.719 (35: 5/10/20 mil UTM).  
5) < 300 ms.  
6) Código vs app en ejecución.  
7) Ver qué RF/NFR tienen caso y qué falta.  
8) 21.663 sube techos si es operador de importancia vital (hasta 40.000 UTM).

---

## 8. Checklist del día del cuestionario

- [ ] Repasé IL 1.1–1.5 en voz alta  
- [ ] Sé explicar funcional vs no funcional + 3 tipos NF  
- [ ] Memorice 4–5 riesgos OWASP con su control  
- [ ] Memorice tablas de leyes 19.628, 21.719, 21.663, DTO 181/NCh27002  
- [ ] Sé umbrales PERF y roles RB-1/2/3 de Cuidarte+  
- [ ] Entro al AVA **sin** apuntes ni IA · **un solo intento**

---

## Referencias de estudio (solo para preparar, no para el día del test)

- `docs/EV1 Contexto/EP1_ISY1102_Estudiante.pdf` — IL y estructura del encargo  
- `docs/EV1 Contexto/EP1_ISY1102_Estudiante_ERS_B.pdf` — RF/NFR Cuidarte+  
- `docs/EV1 Contexto/Normativas/` — textos legales  
- `docs/EV1 Entrega/Informe_Plan_Pruebas_CuidartePlus.md` — aplicación al caso  
