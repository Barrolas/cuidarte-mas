# Informe de seguridad y calidad en el desarrollo de software

**Asignatura:** ISY1102 — Seguridad y Calidad en el Desarrollo de Software  
**Evaluación:** Evaluación Parcial Nº 1 (17%)  
**Título del encargo:** Diseñando un plan de pruebas seguro, legal y normativo  
**Caso:** Sistema de exámenes médicos Cuidarte+  
**Sección:** [Completar]  
**Docente:** [Completar]  
**Fecha:** septiembre 2026  

### Integrantes

| Nombre | Rol en el encargo |
|--------|-------------------|
| Skarlett [Apellido] | Normativa, criterios de calidad, tipos de prueba, cobertura y ensamblaje |
| Nicolás [Apellido] | Estrategia, recursos, cronograma y diseño de casos de prueba |

> **Nota formal:** Completar apellidos, sección y docente antes de exportar a Word/PDF para AVA. Formato requerido: títulos Arial 12, cuerpo Arial 11, interlineado 1,5, texto justificado.

---

## Índice

1. [Introducción](#1-introducción)
2. [Criterios de calidad, seguridad y cumplimiento normativo](#2-criterios-de-calidad-seguridad-y-cumplimiento-normativo)
3. [Tipos de pruebas y justificación](#3-tipos-de-pruebas-y-justificación)
4. [Estrategia de pruebas y justificación](#4-estrategia-de-pruebas-y-justificación)
5. [Recursos necesarios](#5-recursos-necesarios)
6. [Diseño de casos de prueba](#6-diseño-de-casos-de-prueba)
7. [Análisis de cobertura, pertinencia y coherencia](#7-análisis-de-cobertura-pertinencia-y-coherencia)
8. [Conclusiones y recomendaciones](#8-conclusiones-y-recomendaciones)
9. [Referencias](#9-referencias)

---

## 1. Introducción

### 1.1 Contexto del software a evaluar

Cuidarte+ es una plataforma web orientada a centros de salud, desarrollada por CreaLab Spa, cuya finalidad es la gestión de pacientes, exámenes médicos y documentos clínicos. El sistema permite que:

- los **médicos** registren pacientes y exámenes médicos;
- los **pacientes** visualicen su información clínica y descarguen documentos asociados;
- los **administradores** supervisen, auditen y administren usuarios y datos;
- los **visitantes** solo accedan al flujo de registro, sin acceso a datos clínicos.

Arquitectónicamente, Cuidarte+ se implementa como aplicación multicapa: **Frontend React** (SPA), **Backend Express/Node.js** (API REST) y **PostgreSQL**. Las comunicaciones deben utilizar TLS; las contraseñas se almacenan con hashing bcrypt; la autenticación se basa en JWT; y los documentos clínicos se guardan en storage interno con referencia en base de datos.

Dado que el sistema trata **datos de carácter personal y datos sensibles de salud**, cualquier fallo de calidad, seguridad o cumplimiento normativo puede afectar la confidencialidad clínica, la continuidad del servicio y la responsabilidad legal de la organización.

### 1.2 Propósito del plan de pruebas

El presente plan de pruebas tiene por objeto diseñar una estrategia integral que asegure, antes de la puesta en producción, que Cuidarte+:

1. **Cumple los requerimientos funcionales** definidos en el ERS (RF-1 a RF-5).
2. **Satisface atributos de calidad no funcionales** (seguridad, rendimiento, usabilidad, disponibilidad y compatibilidad).
3. **Se alinea con el marco legal y normativo chileno** aplicable a protección de datos personales, ciberseguridad, documentos electrónicos y accesibilidad web.

No se trata solo de verificar que “el sistema funciona”, sino de garantizar que sea **confiable, seguro, usable y legalmente defendible** (enfoque QA + Seguridad + Cumplimiento).

### 1.3 Objetivos del plan

- Definir criterios de calidad, seguridad y cumplimiento asociados a códigos del ERS.
- Clasificar y justificar los tipos de prueba aplicables al caso.
- Establecer estrategia, etapas, herramientas, criterios de entrada/salida, recursos y cronograma.
- Diseñar al menos cinco casos de prueba representativos, trazables a RF/NFR.
- Evaluar cobertura, pertinencia y coherencia del plan frente a requerimientos y normas.

### 1.4 Alcance

**Incluye (in-scope):**

- Autenticación y sesión (RF-1).
- Gestión de usuarios/pacientes y roles (RF-2, RB-1 a RB-3).
- Gestión de exámenes y documentos clínicos (RF-3, RF-4).
- Auditoría de acciones críticas (RF-5).
- Seguridad (NFR-SEG), rendimiento (NFR-PERF), usabilidad/accesibilidad (NFR-USAB) y compatibilidad (NFR-COMPAT).

**Excluye (out-of-scope) en esta EV1:**

- Ejecución real de pruebas de penetración certificadas.
- Certificación formal WCAG o auditoría legal externa.
- Pruebas de infraestructura de nube productiva (el ERS considera despliegue con Docker/stack local de referencia).

### 1.5 Estructura del informe

El informe sigue la estructura del Ítem I del encargo: introducción; criterios de calidad, seguridad y normativa; tipos de prueba; estrategia; recursos; diseño de casos; y un análisis de cobertura que responde al indicador IE5 de la rúbrica.

---

## 2. Criterios de calidad, seguridad y cumplimiento normativo

### 2.1 Criterios de calidad (ISO/IEC 25010 aplicado a Cuidarte+)

| Atributo | Criterio de calidad | Requerimiento ERS | Evidencia esperada en pruebas |
|----------|---------------------|-------------------|-------------------------------|
| Usabilidad | Tipografía legible, contraste adecuado, controles grandes para adultos mayores; flujos claros | NFR-USAB-1, NFR-USAB-2, NFR-USAB-3, NFR-USAB-4 | Pruebas con usuarios representativos; Lighthouse/accesibilidad básica |
| Rendimiento | CRUD < 300 ms; página principal < 2 s; soporte ~200 usuarios concurrentes | NFR-PERF-1, NFR-PERF-2, NFR-PERF-3 | Pruebas de carga (k6/JMeter) |
| Fiabilidad / disponibilidad | Disponibilidad objetivo 99,5% mensual; ventanas de mantenimiento controladas | NFR-DIS-1, NFR-DIS-2 | Monitoreo, pruebas de recuperación |
| Mantenibilidad | Código testeable, endpoints documentados, validación server-side | Interfaces backend ERS §3.1.2 | Cobertura de endpoints críticos / Swagger |
| Compatibilidad | Últimas 2 versiones de Chrome, Firefox, Safari, Edge; responsive móvil/tablet | NFR-COMPAT-1, NFR-COMPAT-2 | Matriz de navegadores/dispositivos |

### 2.2 Criterios de seguridad

| ID ERS | Criterio | Qué se verifica |
|--------|----------|-----------------|
| NFR-SEG-1 | TLS obligatorio | Tráfico HTTP rechazado o forzado a HTTPS |
| NFR-SEG-2 | Hashing bcrypt | Contraseñas no almacenadas en texto plano |
| NFR-SEG-3 | Cifrado en reposo de datos sensibles | Documentos/datos clínicos protegidos en storage/BD |
| NFR-SEG-4 | Control de acceso por rol (RBAC) | Paciente no escribe; admin CRUD; médico según RB-3 |
| NFR-SEG-5 | Protección CSRF, XSS, SQL Injection | Entradas validadas/saneadas; payloads maliciosos rechazados |
| NFR-SEG-6 | Logs seguros | Eventos relevantes sin filtrar secretos |
| NFR-SEG-7 | Respaldo y recuperación | Política de backup verificable |
| NFR-SEG-8 | Cumplimiento normativo de datos personales | Trazabilidad, minimización, acceso restringido |
| NFR-SEG-9 | Sesión JWT | Token de corta vigencia; logout/revocación (RF-1.2) |

**Reglas de negocio asociadas:**

- **RB-1:** paciente solo lectura.
- **RB-2:** administrador con CRUD completo.
- **RB-3:** médico puede ver información clínica de cualquier paciente registrado.

### 2.3 Cumplimiento normativo y legal (Chile)

Cuidarte+ procesa datos personales y sensibles de salud; por ello el plan integra las siguientes normas, priorizadas según las notas del equipo y el NFR-SEG-8:

| Norma / estándar | Aspecto relevante | Aplicación en Cuidarte+ | Traducción a prueba |
|------------------|-------------------|-------------------------|---------------------|
| **Ley 19.628** (Protección de la vida privada) | Tratamiento de datos personales; Arts. 22 (responsabilidad civil) y 23 (indemnización) | Titularidad, finalidad, secreto y derechos del paciente | Verificar acceso restringido por rol; no exposición indebida de ficha clínica |
| **Ley 21.719** (Protección de datos personales) | Art. 35: sanciones leves/graves/gravísimas (hasta 5.000 / 10.000 / 20.000 UTM) | Responsable del tratamiento de datos clínicos | Casos de autorización, minimización y registro de incidentes de acceso |
| **Ley 21.663** (Ley Marco de Ciberseguridad) | Arts. 36–40: infracciones y multas; deberes de prevención/reporte | Plataforma con redes/sistemas que tratan información sensible | Pruebas de detección/reporte de incidentes, hardening y controles de seguridad |
| **DTO 181 / Ley 19.799** | Documentos electrónicos y firma electrónica; seguridad de usuarios | Documentos clínicos digitales | Integridad y control de acceso a PDF/DOC/JPG almacenados |
| **NCh27002.Of2009** | Código de práctica para gestión de seguridad de la información | Políticas, controles y gestión de riesgos | Checklist de controles (acceso, logs, respaldos) |
| **Manual de Accesibilidad Web** | Accesibilidad para personas mayores y diversidad funcional | NFR-USAB y criterios de UI del ERS | Contraste, tamaño de controles, navegación por teclado |
| **Ley 21.459** (Delitos informáticos) | Tipificación de accesos indebidos y ataques | Disuasión y evidencia forense vía auditoría | RF-5.1 + pruebas de acceso no autorizado |
| **Política Nacional de Ciberseguridad** | Cultura de prevención y resiliencia | Marco orientador institucional | Criterios de priorización por riesgo en la estrategia |

### 2.4 Matriz criterio → ERS → norma

| Criterio transversal | Códigos ERS | Norma / estándar de respaldo |
|----------------------|-------------|------------------------------|
| Confidencialidad clínica | NFR-SEG-3, NFR-SEG-4, RB-1 | Ley 19.628; Ley 21.719 |
| Autenticación robusta | RF-1.1, RF-1.2, NFR-SEG-2, NFR-SEG-9 | Ley 21.663; NCh27002 |
| Integridad de documentos | RF-4.3, RF-4.4, NFR-SEG-3 | DTO 181; Ley 19.799 |
| Trazabilidad / accountability | RF-5.1, NFR-SEG-6 | Ley 21.719; Ley 21.459 |
| Disponibilidad del servicio | NFR-DIS-1, NFR-PERF-3 | Ley 21.663 (resiliencia) |
| Accesibilidad e inclusión | NFR-USAB-1 a 4, NFR-COMPAT-2 | Manual Accesibilidad Web |

---

## 3. Tipos de pruebas y justificación

### 3.1 Diferencia entre pruebas funcionales y no funcionales

| Dimensión | Pruebas funcionales | Pruebas no funcionales |
|-----------|---------------------|------------------------|
| Pregunta central | ¿El sistema hace lo que debe? | ¿El sistema lo hace bien (seguro, rápido, usable, compatible)? |
| Base | RF-1 a RF-5, reglas de negocio | NFR-SEG, NFR-PERF, NFR-USAB, NFR-DIS, NFR-COMPAT |
| Ejemplo Cuidarte+ | Médico registra un examen | Respuesta CRUD < 300 ms; paciente no puede eliminar usuarios |

Ambas son indispensables: un flujo funcional correcto que filtre datos clínicos por un fallo de autorización constituye un **incumplimiento de seguridad y de ley de datos**, no solo un “bug”.

### 3.2 Catálogo de tipos de prueba para Cuidarte+

| Tipo de prueba | Propósito | RF/NFR que cubre | Ejemplo en Cuidarte+ |
|----------------|-----------|------------------|----------------------|
| **Funcionales** | Verificar comportamientos esperados de negocio | RF-1 a RF-5 | Login, CRUD de exámenes, descarga de documentos |
| **Integración / API** | Validar contratos entre React, Express y PostgreSQL | Interfaces §3.1.2, RF-1 a RF-4 | Endpoint `/auth/login` + persistencia de sesión |
| **Seguridad** | Detectar vulnerabilidades y fallas de control de acceso | NFR-SEG-1 a 9, RB-1 a RB-3 | Paciente llama API de admin → 403; payload SQLi rechazado |
| **Usabilidad / accesibilidad** | Asegurar uso por adultos mayores y claridad de flujos | NFR-USAB-1 a 4 | Contraste, botones táctiles, flujo paciente → exámenes |
| **Rendimiento / carga** | Cumplir umbrales de tiempo y concurrencia | NFR-PERF-1 a 3 | CRUD < 300 ms; 200 usuarios concurrentes |
| **Compatibilidad** | Verificar navegadores y responsive | NFR-COMPAT-1, NFR-COMPAT-2 | Chrome/Firefox/Safari/Edge; móvil/tablet |
| **Auditoría / cumplimiento** | Verificar trazas y controles legales | RF-5.1, NFR-SEG-6, NFR-SEG-8 | Log tras eliminación de usuario o descarga de documento |
| **Humo (smoke)** | Validar estabilidad mínima tras despliegue | RF críticos | Login + listar pacientes + ver examen |
| **Regresión** | Evitar que cambios rompan funciones previas | RF/NFR ya aceptados | Re-ejecutar suite tras fix de seguridad |

### 3.3 Justificación de la selección

Se priorizan seguridad, auditoría y usabilidad porque Cuidarte+ maneja **datos sensibles de salud** y se orienta a usuarios mayores. El rendimiento se incluye porque el ERS fija umbrales cuantitativos. La compatibilidad es necesaria por el carácter multi-dispositivo del producto. Las pruebas de cumplimiento normativo no se dejan “para el final”: se traducen a casos técnicos ejecutables (por ejemplo, RBAC y logs).

---

## 4. Estrategia de pruebas y justificación

### 4.1 Enfoque general: mixto

Se adopta un **enfoque mixto**:

- **Automatizado:** pruebas unitarias/API, checks de seguridad básicos (DAST ligero), rendimiento y smoke.
- **Manual:** usabilidad con adultos mayores, exploración de flujos clínicos, revisión de mensajes de error y criterios de accesibilidad visual.

**Justificación:** automatizar reduce costo de regresión en auth/API; lo manual es indispensable para usabilidad clínica y validación de experiencia de adultos mayores (criterio de aceptación del ERS §3.1.1).

### 4.2 Etapas del proceso (alineadas a STLC / pirámide de pruebas)

| Fase | Descripción | RF/NFR principales | Herramientas |
|------|-------------|--------------------|--------------|
| 1. Análisis y diseño | Revisar ERS, riesgos y diseñar casos | Todos | ERS, matriz de trazabilidad |
| 2. Unitarias | Validaciones, hashing, helpers de auth | NFR-SEG-2, NFR-SEG-9 | Jest |
| 3. Integración API | Contratos REST, códigos HTTP, JWT | RF-1 a RF-5, NFR-SEG-4 | Postman / Swagger |
| 4. Sistema / E2E UI | Flujos por rol en React | RF-2 a RF-4, NFR-USAB-2 | Pruebas manuales + checklist |
| 5. Seguridad | RBAC, XSS/SQLi, TLS, sesión | NFR-SEG-1 a 9 | OWASP ZAP, Postman |
| 6. Rendimiento | Carga y tiempos de respuesta | NFR-PERF-1 a 3 | k6 / JMeter |
| 7. Usabilidad / accesibilidad | Adultos mayores, contraste, responsive | NFR-USAB, NFR-COMPAT | Lighthouse, sesiones UAT |
| 8. Cierre | Informe de defectos, cobertura, DoD | IE5 | Matriz de trazabilidad |

### 4.3 Priorización por riesgo

| Prioridad | Área de riesgo | Motivo |
|-----------|----------------|--------|
| P0 | Autenticación, RBAC, documentos clínicos | Impacto legal y filtración de datos de salud |
| P1 | Auditoría y logs | Evidencia ante incidentes (Ley 21.719 / 21.663) |
| P2 | CRUD de exámenes y pacientes | Núcleo funcional del negocio |
| P3 | Rendimiento bajo carga | SLA del ERS |
| P4 | Usabilidad / compatibilidad | Adopción por adultos mayores y multi-dispositivo |

### 4.4 Criterios de entrada y salida

**Criterios de entrada (Ready for Testing):**

- ERS estable (versión de referencia del caso semestral).
- Ambiente de pruebas levantado (Docker: frontend, backend, PostgreSQL).
- Usuarios de prueba por rol (Admin, Médico, Paciente) con datos anonimizados.
- Casos de prueba diseñados y revisados.

**Criterios de salida (Definition of Done del ciclo de pruebas):**

- 100% de casos P0/P1 ejecutados.
- Sin hallazgos críticos abiertos de seguridad (NFR-SEG).
- Umbrales NFR-PERF-1 cumplidos en ambiente de prueba.
- Matriz de trazabilidad actualizada y brechas documentadas.
- Informe de resultados disponible para stakeholders.

### 4.5 Criterios de aceptación transversales

Un caso se considera **aprobado** si:

1. El resultado observado coincide con el resultado esperado documentado.
2. Se respeta la regla de negocio aplicable (RB-1/RB-2/RB-3).
3. No se exponen datos clínicos a roles no autorizados.
4. Ante fallo de seguridad o cumplimiento, el caso se marca **fallido** aunque la UI “parezca correcta”.

---

## 5. Recursos necesarios

### 5.1 Recursos humanos

| Rol | Responsabilidad |
|-----|-----------------|
| Analista / Tester | Diseño y ejecución de casos; registro de defectos |
| Desarrollador Backend | Soporte API, datos de prueba, corrección de hallazgos |
| Desarrollador Frontend | Soporte UI, responsive y accesibilidad |
| Responsable de seguridad | Checklist OWASP, revisión RBAC y logs |
| Usuario representativo (adulto mayor) | Sesiones de usabilidad (mín. 5 según ERS §3.1.1) |
| Coordinador del plan (dupla Skarlett/Nicolás) | Trazabilidad, normativa y entrega formal |

### 5.2 Recursos técnicos

| Recurso | Uso |
|---------|-----|
| Node.js 18+/20, React 19, Express, PostgreSQL 15 | Stack del producto |
| Docker Compose | Entorno reproducible (postgres, backend, frontend) |
| Postman / Swagger | Pruebas de API e integración |
| Jest | Pruebas unitarias |
| OWASP ZAP | DAST básico (XSS, headers, paths) |
| Lighthouse | Accesibilidad y performance frontend |
| k6 o JMeter | Carga y umbrales NFR-PERF |
| Navegadores Chrome, Firefox, Edge, Safari (si disponible) | Compatibilidad |
| Datos anonimizados / sintéticos | Cumplir minimización (sin RUT/datos reales de pacientes) |

### 5.3 Entorno de prueba

| Ambiente | Propósito |
|----------|-----------|
| Local (Docker) | Desarrollo y smoke diario |
| QA / staging | Ejecución formal de la suite; TLS habilitado; roles de prueba |

**Cuentas de prueba sugeridas (ficticias):**

- `admin.qa` — rol Administrador  
- `medico.qa` — rol Médico  
- `paciente.qa` — rol Paciente  

Contraseñas de prueba cumplen política ERS (≥12 caracteres, mayúscula, minúscula, número y símbolo), por ejemplo: `PruebaSegura#2026`.

### 5.4 Cronograma tentativo (3 semanas de ciclo de pruebas)

| Semana | Actividades | Entregables |
|--------|-------------|-------------|
| Semana 1 | Análisis ERS, riesgos, diseño de casos P0/P1; preparar ambiente | Casos CP-01 a CP-06; entorno QA operativo |
| Semana 2 | Ejecución funcional, integración API, seguridad y auditoría | Bitácora de defectos; resultados CP-01 a CP-04 |
| Semana 3 | Rendimiento, usabilidad/compatibilidad, regresión y cierre | Resultados CP-05/CP-06; matriz de cobertura; informe final |

### 5.5 Estimación de esfuerzo (orientativa)

| Tipo de prueba | Esfuerzo relativo |
|----------------|-------------------|
| Funcional + auditoría | 30% |
| Seguridad | 25% |
| Rendimiento | 15% |
| Usabilidad / compatibilidad | 20% |
| Coordinación, trazabilidad y reporte | 10% |

---

## 6. Diseño de casos de prueba

Cada caso incluye los campos exigidos por el encargo (6.1 a 6.7) y se enriquece con precondiciones y pasos para facilitar su ejecución.

---

### CP-01 — Autenticación exitosa y rechazo de credenciales inválidas

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-01 |
| **6.2 Descripción** | Verificar que un usuario válido obtiene sesión JWT y que credenciales inválidas son rechazadas sin exponer información sensible. |
| **6.3 Requerimiento asociado** | RF-1.1 (Autenticación con nombre_usuario y contraseña); apoyo NFR-SEG-9 |
| **6.4 Datos de entrada** | Usuario válido: `medico.qa` / `PruebaSegura#2026`. Usuario inválido: `medico.qa` / `ClaveIncorrecta#1` |
| **6.5 Resultado esperado** | Login válido: HTTP 200 y token JWT. Login inválido: HTTP 401, sin token y mensaje genérico de error. |
| **6.6 Criterios de aceptación** | Login exitoso genera token de sesión (JWT). Fallo no revela si el usuario existe. No se registran contraseñas en logs. |
| **6.7 Tipo de prueba** | Funcional / Seguridad |

**Precondiciones:** backend y BD levantados; usuario `medico.qa` creado.  
**Pasos:**  
1. POST `/auth/login` con credenciales válidas.  
2. Verificar presencia de JWT.  
3. POST `/auth/login` con contraseña inválida.  
4. Verificar 401 y ausencia de token.

---

### CP-02 — Médico registra examen médico a un paciente

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-02 |
| **6.2 Descripción** | Validar que un médico autenticado puede crear un examen asociado a un paciente existente, con validación de campos obligatorios. |
| **6.3 Requerimiento asociado** | RF-3.1; RB-3 |
| **6.4 Datos de entrada** | Paciente ID de prueba; tipo de examen: “Hemograma”; fecha; observaciones: “Control rutinario”; documento opcional PDF ≤ límite permitido |
| **6.5 Resultado esperado** | Examen creado (HTTP 201); visible para el médico; asociado al paciente correcto. |
| **6.6 Criterios de aceptación** | CRUD de examen funciona; validación de ingreso correcta; el médico puede ver la información clínica del paciente (RB-3). |
| **6.7 Tipo de prueba** | Funcional |

**Precondiciones:** sesión de médico válida; paciente de prueba existente.  
**Pasos:**  
1. Iniciar sesión como médico.  
2. Seleccionar paciente.  
3. Registrar examen con datos válidos.  
4. Confirmar persistencia en listado/detalle.  
5. Intentar guardar sin campos obligatorios y verificar rechazo.

---

### CP-03 — Auditoría de acción crítica (eliminación)

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-03 |
| **6.2 Descripción** | Comprobar que la eliminación lógica de un examen (o eliminación de usuario por admin) genera registro de auditoría con actor, acción, fecha y recurso afectado. |
| **6.3 Requerimiento asociado** | RF-5.1; apoyo NFR-SEG-6 |
| **6.4 Datos de entrada** | Examen ID previamente creado en CP-02; usuario actor `medico.qa` (o `admin.qa` si se prueba baja de usuario) |
| **6.5 Resultado esperado** | Tras confirmar eliminación, existe un log de auditoría con acción “DELETE/ELIMINACION”, usuario, timestamp y referencia al recurso. |
| **6.6 Criterios de aceptación** | Registros de auditoría generados en cada acción crítica; la UI solicita confirmación antes de eliminar (criterio RF-3). |
| **6.7 Tipo de prueba** | Funcional / Auditoría (cumplimiento) |

**Precondiciones:** examen existente; rol autorizado.  
**Pasos:**  
1. Ejecutar eliminación con confirmación.  
2. Consultar módulo/tabla de auditoría.  
3. Verificar campos mínimos del evento.  
4. Verificar que no se audita la contraseña ni tokens.

---

### CP-04 — Control de acceso RBAC e inyección en entradas

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-04 |
| **6.2 Descripción** | Verificar que un paciente no puede ejecutar operaciones de administración ni modificar datos ajenos, y que entradas maliciosas (SQLi/XSS) son rechazadas o saneadas. |
| **6.3 Requerimiento asociado** | NFR-SEG-4; RB-1; NFR-SEG-5 |
| **6.4 Datos de entrada** | Token de `paciente.qa`. Intento: GET/DELETE de endpoint admin/usuarios. Payload login usuario: `' OR 1=1 --`. Campo observación examen: `<script>alert(1)</script>` (vía rol no autorizado o intento de escritura). |
| **6.5 Resultado esperado** | Accesos indebidos: HTTP 401/403. SQLi no autentica ni altera consultas. XSS no se ejecuta (escapa/sanea). Paciente mantiene solo lectura de **sus** exámenes. |
| **6.6 Criterios de aceptación** | RBAC efectivo en backend; validación/saneamiento de entrada; sin hallazgos críticos de inyección en checklist de seguridad. |
| **6.7 Tipo de prueba** | No funcional — Seguridad |

**Precondiciones:** usuarios paciente, médico y admin disponibles; endpoints protegidos.  
**Pasos:**  
1. Autenticarse como paciente.  
2. Invocar endpoint de administración.  
3. Intentar editar/eliminar examen o usuario.  
4. Enviar payloads SQLi/XSS en login u otros inputs.  
5. Registrar códigos HTTP y comportamiento de la UI.

---

### CP-05 — Tiempo de respuesta CRUD bajo carga normal

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-05 |
| **6.2 Descripción** | Medir el tiempo de respuesta de operaciones CRUD simples de pacientes/exámenes bajo carga normal y contrastarlo con el umbral del ERS. |
| **6.3 Requerimiento asociado** | NFR-PERF-1 |
| **6.4 Datos de entrada** | Script k6/JMeter: 20 usuarios virtuales; operaciones GET/POST de exámenes/pacientes durante 5 minutos; ambiente QA. |
| **6.5 Resultado esperado** | Percentil de respuesta de operaciones CRUD simples < 300 ms bajo carga normal. |
| **6.6 Criterios de aceptación** | Prueba de carga cumple el umbral NFR-PERF-1; se adjunta gráfico/resumen de latencias. |
| **6.7 Tipo de prueba** | No funcional — Rendimiento |

**Precondiciones:** ambiente QA estable; dataset sintético cargado.  
**Pasos:**  
1. Preparar colección de requests CRUD.  
2. Ejecutar prueba de carga.  
3. Comparar p95/p99 o media según métrica acordada con umbral 300 ms.  
4. Documentar desviaciones.

---

### CP-06 — Usabilidad para adulto mayor y compatibilidad responsive

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-06 |
| **6.2 Descripción** | Evaluar que un paciente adulto mayor pueda completar el flujo de acceso a su información (paciente → exámenes → descarga) en móvil/tablet, con tipografía legible, contraste adecuado y controles táctiles suficientes. |
| **6.3 Requerimiento asociado** | NFR-USAB-1; NFR-USAB-2; NFR-USAB-4; NFR-COMPAT-2 |
| **6.4 Datos de entrada** | Dispositivo móvil (viewport 375px) y tablet; usuario `paciente.qa`; checklist de contraste/tamaño mínimo de controles; sesión de usabilidad guiada. |
| **6.5 Resultado esperado** | Flujo completado sin bloqueos mayores; UI responsive; textos legibles; botones alcanzables; mensajes de error comprensibles. |
| **6.6 Criterios de aceptación** | Prueba con usuario representativo sin bloqueos mayores; cumplimiento básico de accesibilidad; score de usabilidad mínimo aceptable (checklist del equipo). |
| **6.7 Tipo de prueba** | No funcional — Usabilidad / Compatibilidad |

**Precondiciones:** frontend desplegado; cuenta paciente con al menos un examen y documento.  
**Pasos:**  
1. Abrir aplicación en móvil.  
2. Iniciar sesión como paciente.  
3. Navegar paciente → listado de exámenes → detalle → descarga.  
4. Verificar contraste, tamaño de fuente (≥12px) y controles.  
5. Repetir smoke en tablet y navegador alternativo.

---

## 7. Análisis de cobertura, pertinencia y coherencia

### 7.1 Matriz de trazabilidad

| Requerimiento / regla | Tipo de prueba | Caso(s) | Cobertura |
|-----------------------|----------------|---------|-----------|
| RF-1.1 | Funcional / Seguridad | CP-01 | Cubierto |
| RF-1.2 | Seguridad (sesión) | CP-01 (apoyo logout/revocación pendiente ampliación) | Parcial |
| RF-3.1 | Funcional | CP-02 | Cubierto |
| RB-3 | Funcional | CP-02 | Cubierto |
| RF-5.1 | Auditoría | CP-03 | Cubierto |
| NFR-SEG-4 + RB-1 | Seguridad | CP-04 | Cubierto |
| NFR-SEG-5 | Seguridad | CP-04 | Cubierto |
| NFR-PERF-1 | Rendimiento | CP-05 | Cubierto |
| NFR-USAB-1/2/4 | Usabilidad | CP-06 | Cubierto |
| NFR-COMPAT-2 | Compatibilidad | CP-06 | Cubierto |
| NFR-SEG-8 (normativo) | Cumplimiento vía RBAC + auditoría | CP-03, CP-04 | Cubierto (indirecto) |

### 7.2 Brechas identificadas y priorización

| Brecha | Justificación de postergación / siguiente iteración | Prioridad |
|--------|-----------------------------------------------------|-----------|
| RF-2.x (CRUD completo de usuarios por admin) | Cubierto conceptualmente por RBAC; se recomienda CP-07 en ciclo 2 | Media |
| RF-4.2 descarga de documentos (tiempo ≤10 s) | Parcialmente en CP-06; medir tiempo explícito en ciclo 2 | Media |
| NFR-PERF-2 / NFR-PERF-3 | Solo se midió NFR-PERF-1 en CP-05 por foco del encargo | Media |
| NFR-SEG-1 TLS y NFR-SEG-7 backups | Verificables por checklist de entorno; no son casos UI | Alta (checklist operativo) |
| NFR-DIS-1 disponibilidad 99,5% | Requiere monitoreo prolongado; fuera de alcance EV1 | Baja en EV1 |

La priorización privilegia **riesgo legal y clínico** (auth, RBAC, auditoría, documentos) sobre métricas de largo plazo.

### 7.3 Coherencia estrategia ↔ recursos ↔ cronograma

- La **estrategia mixta** se sostiene con herramientas disponibles en taller (Postman, Docker, Lighthouse, k6) y pruebas manuales de usabilidad.  
- El **cronograma de 3 semanas** concentra P0/P1 en la semana 2, coherente con la priorización por riesgo.  
- Los **casos CP-01 a CP-06** materializan tipos funcionales y no funcionales exigidos por IE2/IE3.  
- La **sección normativa** conecta NFR-SEG-8 con leyes chilenas concretas, evitando menciones genéricas.

### 7.4 Evaluación frente a la rúbrica

| Indicador | Evidencia en este informe |
|-----------|---------------------------|
| IE1 (15%) | §2 criterios + marco legal chileno aplicado al dominio clínico |
| IE2 (20%) | §3 clasificación y justificación de tipos |
| IE3 (20%) | CP-04, CP-05, CP-06 (no funcionales con criterios medibles) |
| IE4 (25%) | §1, §4, §5: intro, estrategia, recursos, cronograma, vínculo ERS/normas |
| IE5 (20%) | §7 matriz, brechas, coherencia y recomendaciones |

---

## 8. Conclusiones y recomendaciones

El plan de pruebas de Cuidarte+ integra calidad, seguridad y cumplimiento normativo desde el diseño, alineado al ERS del caso semestral y a la EV1. Con seis casos representativos se cubren autenticación, funcionalidad clínica, auditoría, RBAC/seguridad de entradas, rendimiento y usabilidad/compatibilidad.

**Recomendaciones:**

1. Ampliar la suite con CP de logout/revocación JWT (RF-1.2) y CRUD admin (RF-2.5–RF-2.7).  
2. Formalizar checklist TLS/backups (NFR-SEG-1, NFR-SEG-7) en cada despliegue QA.  
3. Ejecutar al menos una sesión UAT con 5 adultos mayores documentando hallazgos.  
4. Mantener datos de prueba sintéticos para reducir riesgo legal durante las pruebas.  
5. Antes de producción, complementar con DAST más profundo y revisión de dependencias (SCA).

---

## 9. Referencias

1. EP1_ISY1102_Estudiante.pdf — Instrucciones y pauta de evaluación EV1.  
2. EP1_ISY1102_Estudiante_ERS_B.pdf — Especificación de requerimientos de software Cuidarte+.  
3. EP1_ISY1102_Estudiante_Formato_Informe.docx — Plantilla de informe.  
4. Ley 19.628 — Sobre protección de la vida privada.  
5. Ley 21.719 — Protección de datos personales.  
6. Ley 21.663 — Ley Marco de Ciberseguridad.  
7. Ley 21.459 — Delitos informáticos.  
8. Decreto 181 / Ley 19.799 — Documentos electrónicos y firma electrónica.  
9. NCh27002.Of2009 — Código de práctica para la gestión de seguridad de la información.  
10. Manual de Accesibilidad Web (Gobierno de Chile / referentes del curso).  
11. Política Nacional de Ciberseguridad.  
12. ISO/IEC 25010 (modelo de calidad) y OWASP Top 10 (referencia de seguridad web).

---

## Anexo A — Checklist de entrega AVA

- [ ] Completar apellidos, sección y nombre del docente en portada  
- [ ] Exportar este Markdown a Word o PDF  
- [ ] Aplicar Arial 12 (títulos), Arial 11 (cuerpo), interlineado 1,5, texto justificado  
- [ ] Revisar ortografía y lenguaje formal técnico  
- [ ] Verificar que existen ≥5 casos con campos 6.1–6.7  
- [ ] Subir a AVA el día del cuestionario  
- [ ] Rendir cuestionario individual (sin IA, un intento)

## Anexo B — Distribución de trabajo ejecutada

| Responsable | Aporte en este documento |
|-------------|--------------------------|
| Skarlett | §§1–3, §7–8, portada, anexos de entrega |
| Nicolás | §§4–6 (estrategia, recursos, cronograma, CP-01 a CP-06) |
| Ambos | Revisión cruzada de coherencia técnica y normativa |
