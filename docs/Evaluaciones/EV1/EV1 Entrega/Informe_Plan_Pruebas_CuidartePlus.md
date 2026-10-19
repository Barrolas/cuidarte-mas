# Informe de seguridad y calidad en el desarrollo de software

**Asignatura:** ISY1102 — Seguridad y Calidad en el Desarrollo de Software  
**Evaluación:** Evaluación Parcial Nº 1 (17%)  
**Título del encargo:** Diseñando un plan de pruebas seguro, legal y normativo  
**Caso:** Sistema de exámenes médicos Cuidarte+  
**Sección:** 001V  
**Docente:** Jose Sergio Collio Huennun  
**Fecha:** septiembre 2026  

### Integrantes

| Nombre | Rol en el encargo |
|--------|-------------------|
| Skarlett Tropan | Normativa, criterios de calidad, tipos de prueba, cobertura y ensamblaje |
| Nicolás Barra | Estrategia, recursos, cronograma y diseño técnico de casos de prueba |
| Ari Araya | Apoyo al plan de pruebas y revisión de casos |
| Giannina Guerrero | Apoyo normativo/cobertura y revisión del informe |

> Equipo de **4 integrantes**, autorizado por el docente.  
> **Formato AVA:** títulos Arial 12, cuerpo Arial 11, interlineado 1,5, texto justificado. Entrega: Word/PDF generado desde este contenido.

---

## Índice

1. Introducción  
2. Criterios de calidad, seguridad y cumplimiento normativo  
3. Tipos de pruebas y justificación  
4. Estrategia de pruebas y justificación  
5. Recursos necesarios  
6. Diseño de casos de prueba  
7. Análisis de cobertura, pertinencia y coherencia  
8. Conclusiones y recomendaciones  
9. Referencias  

---

## 1. Introducción

### 1.1 Contexto del software a evaluar

Cuidarte+ es una plataforma web orientada a centros de salud, desarrollada por CreaLab Spa, cuya finalidad es la gestión de pacientes, exámenes médicos y documentos clínicos. El sistema contempla cuatro perfiles de uso:

- **Médicos:** registran pacientes y exámenes médicos.  
- **Pacientes:** visualizan su información clínica y descargan documentos asociados.  
- **Administradores:** supervisan, auditan y administran usuarios y datos.  
- **Visitantes:** solo acceden al flujo de registro, sin acceso a información clínica.

Arquitectónicamente se implementa como aplicación multicapa: **frontend React (SPA)**, **backend Express/Node.js (API REST)** y **PostgreSQL**. Las comunicaciones deben usar TLS; las contraseñas, hashing bcrypt; la autenticación, JWT; y los documentos clínicos se conservan en storage interno con referencia en base de datos.

El sistema trata datos personales y **datos sensibles de salud** (alergias, enfermedades crónicas, diagnósticos, tratamientos, etc.). Un fallo de calidad, seguridad o cumplimiento compromete confidencialidad clínica, continuidad operativa y responsabilidad legal.

### 1.2 Propósito del plan de pruebas

Diseñar una estrategia integral que asegure, antes de producción, que Cuidarte+:

1. Cumple los requerimientos funcionales del ERS (RF-1 a RF-5).  
2. Satisface atributos no funcionales (seguridad, rendimiento, usabilidad, disponibilidad, compatibilidad).  
3. Se alinea con el marco legal chileno de datos personales, ciberseguridad, documentos electrónicos y accesibilidad.

El plan adopta el enfoque **QA + Seguridad + Cumplimiento**, evitando tratar la norma como fase aislada al final.

### 1.3 Objetivos

- Definir criterios de calidad, seguridad y cumplimiento trazables a códigos del ERS.  
- Clasificar y justificar tipos de prueba aplicables.  
- Establecer estrategia, herramientas, criterios de entrada/salida, recursos y cronograma.  
- Diseñar al menos cinco casos representativos (aquí: CP-01 a CP-06).  
- Evaluar cobertura, brechas y coherencia frente a ERS y leyes (IE5).

### 1.4 Alcance

**Incluye:** autenticación y sesión (RF-1); roles y reglas RB-1/2/3; exámenes y documentos (RF-3, RF-4); auditoría (RF-5); NFR-SEG, NFR-PERF, NFR-USAB, NFR-COMPAT.

**Excluye en esta EV1:** pentest certificado, certificación WCAG formal, auditoría legal externa, medición prolongada de disponibilidad 99,5%.

### 1.5 Estructura del informe

El documento sigue el Ítem I del encargo y la plantilla institucional: introducción; criterios y normativa; tipos de prueba; estrategia; recursos; casos; análisis de cobertura; conclusiones y referencias.

---

## 2. Criterios de calidad, seguridad y cumplimiento normativo

Los criterios se derivan de ISO/IEC 25010, del ERS y del marco legal chileno aplicable a datos de salud.

### 2.1 Criterios de calidad

| Atributo | Criterio | Requerimiento ERS | Evidencia |
|----------|----------|-------------------|-----------|
| Usabilidad | Tipografía legible, contraste, controles amplios, flujos claros | NFR-USAB-1 a 4 | UAT adultos mayores; Lighthouse |
| Rendimiento | CRUD &lt; 300 ms; home &lt; 2 s; ~200 concurrentes | NFR-PERF-1 a 3 | k6 / JMeter |
| Fiabilidad / disponibilidad | 99,5% mensual; ventanas de mantenimiento | NFR-DIS-1, NFR-DIS-2 | Monitoreo / recuperación |
| Mantenibilidad | Código testeable, endpoints documentados, validación server-side | ERS §3.1.2 | Swagger `/docs` |
| Compatibilidad | Últimas 2 versiones Chrome/Firefox/Safari/Edge; responsive | NFR-COMPAT-1, 2 | Matriz navegadores/dispositivos |

### 2.2 Criterios de seguridad

| ID ERS | Criterio | Qué se verifica |
|--------|----------|-----------------|
| NFR-SEG-1 | TLS obligatorio | HTTP rechazado o forzado a HTTPS |
| NFR-SEG-2 | Hashing bcrypt | Contraseñas no en texto plano |
| NFR-SEG-3 | Cifrado en reposo | Documentos/datos clínicos protegidos |
| NFR-SEG-4 | RBAC en backend | Paciente no escribe; admin CRUD; médico según RB-3 |
| NFR-SEG-5 | CSRF, XSS, SQLi | Entradas validadas/saneadas |
| NFR-SEG-6 | Logs seguros | Eventos sin filtrar secretos |
| NFR-SEG-7 | Respaldo y recuperación | Política verificable |
| NFR-SEG-8 | Cumplimiento datos personales | Trazabilidad, minimización, acceso restringido |
| NFR-SEG-9 | Sesión JWT | Token de corta vigencia; logout/revocación (RF-1.2) |

**Reglas de negocio:** RB-1 paciente solo lectura; RB-2 admin CRUD completo; RB-3 médico puede ver clínica de pacientes registrados.

### 2.3 Cumplimiento normativo y legal

| Norma | Aspecto relevante | Aplicación en Cuidarte+ | Traducción a prueba |
|-------|-------------------|-------------------------|---------------------|
| Ley 19.628 | Tratamiento de datos; arts. 22 (resp. civil) y 23 (indemnización) | Ficha clínica y derechos del titular | RBAC; no exposición indebida |
| Ley 21.719 | Principios y art. 35 (≤5.000 / 10.000 / 20.000 UTM) | Responsable del tratamiento clínico | Autorización, minimización, incidentes |
| Ley 21.663 | Riesgos, reporte; arts. 36–40 (hasta 40.000 UTM si operador vital) | Servicio de salud / sistemas críticos | Controles, hardening, reporte |
| DTO 181 / Ley 19.799 | Documentos electrónicos; remite a NCh27002 | Informes de exámenes digitales | Integridad y control de acceso a docs |
| NCh27002.Of2009 | Controles de seguridad de la información | Políticas y gestión de riesgos | Checklist acceso, crypto, logs, backups |
| Ley 21.459 | Delitos informáticos | Accesos ilícitos / integridad | Acceso no autorizado + RF-5.1 |
| Ley 17.336 arts. 78–79 | Propiedad intelectual / software | Dependencias del stack | SCA / licencias |
| Manual Accesibilidad Web | Perceptibilidad y operabilidad | Portal paciente / adultos mayores | Contraste, teclado, tamaño controles |
| Política Nacional de Ciberseguridad | Resiliencia y cultura | Marco orientador | Priorización por riesgo |

La Ley 21.180 (transformación digital del Estado) **no es directamente exigible** mientras Cuidarte+ opere como prestador privado; se declara solo como criterio de interoperabilidad futura (FONASA, Registro Civil, etc.).

### 2.4 Matriz criterio → ERS → norma

| Criterio transversal | Códigos ERS | Norma de respaldo |
|----------------------|-------------|-------------------|
| Confidencialidad clínica | NFR-SEG-3, NFR-SEG-4, RB-1 | 19.628; 21.719 |
| Autenticación robusta | RF-1.1, RF-1.2, NFR-SEG-2, NFR-SEG-9 | 21.663; NCh27002 |
| Integridad documental | RF-4.3, RF-4.4, NFR-SEG-3 | DTO 181; 19.799 |
| Trazabilidad | RF-5.1, NFR-SEG-6 | 21.719; 21.459 |
| Disponibilidad | NFR-DIS-1, NFR-PERF-3 | 21.663 |
| Accesibilidad | NFR-USAB-1…4, NFR-COMPAT-2 | Manual Accesibilidad |

---

## 3. Tipos de pruebas y justificación

### 3.1 Funcional vs no funcional

| | Funcional | No funcional |
|---|-----------|--------------|
| Pregunta | ¿Hace lo pedido? | ¿Lo hace bien (seguro, rápido, usable…)? |
| Base | RF-1…RF-5, RB | NFR-SEG, PERF, USAB, DIS, COMPAT |
| Ejemplo | Médico crea examen | CRUD &lt; 300 ms; paciente no borra usuarios |

### 3.2 Catálogo

| Tipo | Propósito | RF/NFR | Ejemplo Cuidarte+ |
|------|-----------|--------|-------------------|
| Funcional | Verificar negocio | RF-1…RF-5 | Login, CRUD exámenes |
| Integración / API | Contratos React↔Express↔PG | §3.1.2 | `POST /autenticacion/login` |
| Seguridad | Resistir ataques / fallas de acceso | NFR-SEG, RB | RBAC, XSS, SQLi |
| Usabilidad / accesibilidad | Adultos mayores y claridad | NFR-USAB | Contraste, flujo paciente→exámenes |
| Rendimiento | Umbrales de tiempo/carga | NFR-PERF | &lt; 300 ms |
| Compatibilidad | Navegadores y dispositivos | NFR-COMPAT | Móvil/tablet |
| Auditoría / cumplimiento | Trazas legales | RF-5.1, NFR-SEG-6/8 | Log al eliminar |
| Humo | Estabilidad mínima | RF críticos | Login + listar |
| Regresión | No romper lo aceptado | Suite previa | Tras fix de seguridad |

---

## 4. Estrategia de pruebas y justificación

### 4.1 Enfoque mixto

- **Automatizado:** unitarias, API (Postman), smoke, carga (k6), DAST ligero (ZAP).  
- **Manual:** E2E por rol, UAT adulto mayor, revisión visual de accesibilidad.

### 4.2 Etapas

| Fase | RF/NFR | Herramientas |
|------|--------|--------------|
| Análisis y diseño | Todos | ERS, matriz |
| Unitarias | NFR-SEG-2, 9 | Jest |
| Integración API | RF-1…5, NFR-SEG-4 | Postman, Swagger `http://localhost:4444/docs` |
| E2E UI | RF-2…4, NFR-USAB-2 | Checklist manual |
| Seguridad | NFR-SEG-1…9 | ZAP, Postman |
| Rendimiento | NFR-PERF | k6/JMeter |
| Usabilidad / compatibilidad | NFR-USAB, COMPAT | Lighthouse, UAT |
| Cierre | IE5 | Matriz + informe |

**Rutas base del backend:** `/autenticacion`, `/usuarios`, `/pacientes`, `/examenes`, `/documentos`, `/auditoria`, `/roles`, `/tipo-examen`.

### 4.3 Priorización por riesgo

P0 auth/RBAC/documentos → P1 auditoría → P2 CRUD clínico → P3 rendimiento → P4 usabilidad/compatibilidad.

### 4.4 Criterios de entrada / salida

**Entrada:** ERS estable; Docker up; usuarios `admin.qa` / `medico.qa` / `paciente.qa`; casos diseñados.  
**Salida:** 100% P0/P1 ejecutados; sin críticos de seguridad abiertos; NFR-PERF-1 verificado (sin delay artificial); matriz actualizada.

### 4.5 Aceptación transversal

Coincide resultado esperado; respeta RB; no expone datos clínicos indebidos; fallo de seguridad = caso fallido aunque la UI “se vea bien”.

---

## 5. Recursos necesarios

### 5.1 Humanos

Tester, dev backend, dev frontend, responsable seguridad, ≥5 adultos mayores (ERS §3.1.1), equipo de 4 integrantes (Ari Araya, Giannina Guerrero, Skarlett Tropan, Nicolás Barra).

### 5.2 Técnicos

Docker Compose; Node 18/20; React; Express; PostgreSQL 15; Postman; Swagger; Jest; OWASP ZAP; Lighthouse; k6/JMeter; Chrome/Firefox/Edge/Safari.

### 5.3 Entorno

| Ambiente | Acceso | Uso |
|----------|--------|-----|
| Local Docker | FE `:3333` · API `:4444` | Smoke / diseño |
| QA | Misma topología (+ TLS si hay proxy) | Suite formal |

Contraseña de prueba ejemplo: `PruebaSegura#2026` (cumple política ≥12 + complejidad). Solo datos sintéticos (minimización / Ley 21.719).

### 5.4 Cronograma (3 semanas)

| Semana | Foco | Entregable |
|--------|------|------------|
| 1 | Ambiente + diseño CP-01…06 | Casos + Postman base |
| 2 | Ejecución P0–P2 (CP-01…04) | Bitácora defectos |
| 3 | PERF/USAB + cierre (CP-05…06) | Matriz + informe |

### 5.5 Esfuerzo orientativo

Funcional+auditoría 30% · Seguridad 25% · Rendimiento 15% · Usabilidad 20% · Coordinación 10%.

---

## 6. Diseño de casos de prueba

API base de referencia: `http://localhost:4444`.

### CP-01 — Autenticación válida y rechazo de credenciales inválidas

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-01 |
| **6.2 Descripción** | Verificar que un usuario válido obtiene JWT y que credenciales inválidas se rechazan sin exponer información sensible. |
| **6.3 Requerimiento** | RF-1.1; NFR-SEG-9 |
| **6.4 Datos de entrada** | OK: `medico.qa` / `PruebaSegura#2026`. Fallo: misma usuaria + `ClaveIncorrecta#1` |
| **6.5 Resultado esperado** | 200 + `token` JWT; fallo 401 sin token y mensaje genérico |
| **6.6 Criterio de aceptación** | Login genera JWT; fallo no revela existencia de cuenta de forma explotable; password no en logs |
| **6.7 Tipo** | Funcional / Seguridad |

**Pasos:** `POST /autenticacion/login` válido → verificar token → login inválido → verificar 401.

### CP-02 — Registro de examen médico por profesional autorizado

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-02 |
| **6.2 Descripción** | Médico autenticado crea examen de paciente existente; el sistema valida campos obligatorios. |
| **6.3 Requerimiento** | RF-3.1; RB-3 |
| **6.4 Datos de entrada** | Token médico; `paciente_id`; `tipo_examen_id`; observaciones “Control rutinario”; PDF opcional |
| **6.5 Resultado esperado** | Examen persistido y asociado; visible en listado/detalle |
| **6.6 Criterio de aceptación** | CRUD válido; rechazo de payload incompleto; médico ve clínica del paciente (RB-3) |
| **6.7 Tipo** | Funcional |

**Pasos:** login médico → `GET /pacientes` / `GET /tipo-examen` → `POST /examenes` → verificar con `GET /examenes/:id` o `/examenes/paciente/:id` → reintentar sin obligatorios.

### CP-03 — Auditoría ante acción crítica

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-03 |
| **6.2 Descripción** | La eliminación de examen/usuario genera registro de auditoría (actor, acción, fecha, recurso). |
| **6.3 Requerimiento** | RF-5.1; NFR-SEG-6 |
| **6.4 Datos de entrada** | Examen de CP-02; actor `medico.qa` o `admin.qa` |
| **6.5 Resultado esperado** | Evento en auditoría tras delete |
| **6.6 Criterio de aceptación** | Traza completa; confirmación previa en UI; sin secretos en logs |
| **6.7 Tipo** | Funcional / Auditoría |

**Pasos:** `DELETE /examenes/:id` (o `/usuarios/:id`) → `GET /auditoria` → verificar campos → sin password/JWT en log.

### CP-04 — Control de acceso por rol y resistencia a inyección

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-04 |
| **6.2 Descripción** | Paciente no ejecuta operaciones privilegiadas ni altera datos ajenos; SQLi/XSS rechazados o saneados. |
| **6.3 Requerimiento** | NFR-SEG-4; NFR-SEG-5; RB-1 |
| **6.4 Datos de entrada** | Token `paciente.qa`; intentos `GET/DELETE /usuarios`; SQLi `' OR 1=1 --`; XSS `<script>alert(1)</script>` |
| **6.5 Resultado esperado** | 401/403 en acceso indebido; sin JWT tras SQLi; sin ejecución XSS |
| **6.6 Criterio de aceptación** | RBAC efectivo; saneamiento; sin críticos de inyección |
| **6.7 Tipo** | **No funcional — Seguridad** |

**Pasos:** login paciente → endpoints admin → delete examen ajeno → payloads maliciosos → control positivo: médico lee paciente (RB-3).

> **Ejecución exploratoria (sep 2026):** paciente → `GET /usuarios` → **403**; login SQLi → **401** (sin JWT). ZAP baseline (sin auth) → HALL-05. Hallazgos de diseño: **HALL-02** (password en claro / NFR-SEG-2) y **HALL-03** (JWT débil). Ver [`Informe_Hallazgos_CuidartePlus.md`](./Informe_Hallazgos_CuidartePlus.md).

### CP-05 — Tiempo de respuesta CRUD bajo carga normal

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-05 |
| **6.2 Descripción** | Medir latencia CRUD pacientes/exámenes bajo carga normal vs umbral ERS. |
| **6.3 Requerimiento** | NFR-PERF-1 |
| **6.4 Datos de entrada** | JMeter: [`Anexos/jmeter/CuidartePlus_CP05.jmx`](./Anexos/jmeter/CuidartePlus_CP05.jmx) — TG-A 20 VUs; TG-B 50 VUs (smoke concurrencia) |
| **6.5 Resultado esperado** | p95 (o métrica acordada) &lt; 300 ms |
| **6.6 Criterio de aceptación** | Umbral cumplido + resumen de latencias |
| **6.7 Tipo** | **No funcional — Rendimiento** |

> **Aviso técnico del repo:** varias rutas usan `delayMiddleware(5000)` en desarrollo. La medición formal de NFR-PERF-1 debe ejecutarse **sin** ese delay artificial; de lo contrario el umbral de 300 ms queda falseado.

> **Resultado ejecutado (con delay activo):** 220 samples, 0% error; Login p95 ≈ 14 ms (**cumple**); GET pacientes/exámenes p95 ≈ **5008–5011 ms** (**no cumple** NFR-PERF-1) → **HALL-04**. Detalle: [`Anexos/jmeter/Informe_JMeter_CP05.md`](./Anexos/jmeter/Informe_JMeter_CP05.md).

### CP-06 — Usabilidad adulto mayor y compatibilidad responsive

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-06 |
| **6.2 Descripción** | Paciente adulto mayor completa paciente → exámenes → descarga en móvil/tablet con UI legible y táctil. |
| **6.3 Requerimiento** | NFR-USAB-1, 2, 4; NFR-COMPAT-2 |
| **6.4 Datos de entrada** | Viewport 375px y tablet; `paciente.qa`; checklist contraste/tamaño |
| **6.5 Resultado esperado** | Sin bloqueos mayores; responsive; controles usables |
| **6.6 Criterio de aceptación** | UAT sin bloqueos; accesibilidad básica; meta interna Lighthouse Accessibility ≥ 80 |
| **6.7 Tipo** | **No funcional — Usabilidad / Compatibilidad** |

**Pasos:** FE `:3333` móvil → login paciente → flujo completo → verificar UI → repetir tablet/otro navegador.

### 6.8 Hallazgos de ejecución exploratoria

Además del diseño de CP-01…CP-06, se ejecutó una batería exploratoria (UI, API autenticada, ZAP baseline, JMeter). Resumen:

| ID | Severidad | Hallazgo | ERS / CP |
|----|-----------|----------|----------|
| HALL-01 | Alta | UI “Ver Documento” no visualiza adjunto de forma usable (API download OK) | RF-4.x, NFR-USAB-2 · CP-02/06 |
| HALL-02 | Crítica | Contraseñas en texto plano (sin bcrypt) | NFR-SEG-2 · CP-01/04 |
| HALL-03 | Alta | `JWT_SECRET` por defecto `"inseguro"` | NFR-SEG-9 · CP-01 |
| HALL-04 | Alta | `delayMiddleware(5000)` → p95 ~5 s en JMeter | NFR-PERF-1 · CP-05 |
| HALL-05 | Media | Headers / hardening (ZAP sin auth) | NFR-SEG-5 · CP-04 |

**Por qué ZAP no mostró fallos graves:** el baseline fue **sin autenticación**; no entra a flujos clínicos con JWT ni a documentos. Los defectos de seguridad/calidad se evidencian con revisión de código + Postman/curl + JMeter.

Detalle completo: [`Informe_Hallazgos_CuidartePlus.md`](./Informe_Hallazgos_CuidartePlus.md) · PDF [`Anexos/Informe_Hallazgos_CuidartePlus.pdf`](./Anexos/Informe_Hallazgos_CuidartePlus.pdf).

---

## 7. Análisis de cobertura, pertinencia y coherencia

### 7.1 Matriz de trazabilidad

| Requerimiento | Tipo | Caso | Cobertura |
|---------------|------|------|-----------|
| RF-1.1 | Funcional/Seguridad | CP-01 | Cubierto |
| RF-1.2 | Sesión | — / parcial CP-01 | **Brecha** (ampliar logout) |
| RF-3.1 + RB-3 | Funcional | CP-02 | Cubierto |
| RF-4.2 / RF-4.3 | Funcional / docs | CP-02, CP-06 | **Fallido en UI** (HALL-01; API OK) |
| RF-5.1 | Auditoría | CP-03 | Cubierto |
| NFR-SEG-2 | Seguridad | CP-01, CP-04 | **Incumplido** (HALL-02) |
| NFR-SEG-4 + RB-1 | Seguridad | CP-04 | Cubierto (403 paciente) |
| NFR-SEG-5 | Seguridad | CP-04 | Cubierto (+ HALL-05 ZAP) |
| NFR-PERF-1 | Rendimiento | CP-05 | **No cumple con delay** (HALL-04 / JMeter) |
| NFR-USAB-1/2/4 | Usabilidad | CP-06 | Cubierto (+ HALL-01) |
| NFR-COMPAT-2 | Compatibilidad | CP-06 | Cubierto |
| NFR-SEG-8 | Cumplimiento | CP-03, CP-04 | Cubierto (indirecto) |

### 7.2 Brechas y priorización

| Brecha | Acción | Prioridad |
|--------|--------|-----------|
| RF-1.2 logout/revocación | CP-07 ciclo 2 | Alta |
| RF-2.5–2.7 CRUD admin | CP-08 ciclo 2 | Media |
| RF-4.2 descarga / Ver Documento (HALL-01) | Fix UI ciclo 2 | Alta |
| NFR-SEG-2 password plano (HALL-02) | bcrypt + migración | Crítica |
| NFR-PERF-1 con delay (HALL-04) | Quitar delay; re-medir JMeter | Alta |
| NFR-PERF-2/3 | Extender JMeter hacia 200 VUs | Media |
| NFR-SEG-1 TLS / NFR-SEG-7 backups | Checklist operativo por despliegue | Alta |
| NFR-DIS-1 99,5% | Fuera de alcance EV1 | Baja EV1 |

### 7.3 Coherencia

Estrategia mixta ↔ herramientas de taller ↔ cronograma 3 semanas ↔ seis casos que materializan funcionales y no funcionales. Normativa de §2 conecta con NFR-SEG-8 y con criterios de aceptación de CP-03/CP-04. Los hallazgos HALL-01…05 refuerzan IE3/IE5 con evidencia ejecutada (no solo diseño).

### 7.4 Rúbrica

| IE | Evidencia |
|----|-----------|
| IE1 | §2 marco legal + datos clínicos |
| IE2 | §3 tipos y distinción F/NF |
| IE3 | CP-04, CP-05, CP-06 + JMeter + ZAP + §6.8 hallazgos |
| IE4 | §1, §4, §5 plan completo + justificación herramientas |
| IE5 | §7 matriz y brechas (+ HALL trazados) |

---

## 8. Conclusiones y recomendaciones

El plan unifica el aporte normativo-formal y técnico del equipo de cuatro integrantes (autorizado por el docente). Con CP-01…CP-06 se cubre autenticación, clínica, auditoría, seguridad, rendimiento y usabilidad. La ejecución exploratoria confirma defectos reales (HALL-01…05) que el baseline ZAP sin sesión no alcanza.

**Recomendaciones**

1. Completar CP de logout JWT (RF-1.2) y CRUD admin (RF-2.x).  
2. Medir PERF con `delayMiddleware` desactivado y re-ejecutar el `.jmx` de CP-05.  
3. Ejecutar UAT con 5 adultos mayores (ERS).  
4. Corregir “Ver Documento” (HALL-01), bcrypt (HALL-02) y secreto JWT (HALL-03) en ciclo 2 — **fuera del alcance de fixes de esta EV1**.  
5. Checklist TLS/backups en cada despliegue QA.

---

## 9. Referencias

1. EP1_ISY1102_Estudiante.pdf — instrucciones y rúbrica.  
2. EP1_ISY1102_Estudiante_ERS_B.pdf — ERS Cuidarte+.  
3. EV1_Informe_Plan_Pruebas_Cuidarte_Mas.docx — maqueta Word (rama `sk`).  
4. Leyes 19.628, 21.719, 21.663, 21.459, 17.336; DTO 181; NCh27002; Manual Accesibilidad; Política Nacional de Ciberseguridad.  
5. ISO/IEC 25010; OWASP Top 10.  

---

## Anexo — Estado de consolidación

| Origen | Qué se incorporó |
|--------|------------------|
| Rama `sk` (Skarlett) | Word institucional; redacción normativa; estructura formal; CP narrativos |
| Paquete Nicolás | Endpoints reales; delayMiddleware; métricas; insumos trazabilidad |
| Gaps cerrados aquí | §1.2–1.5 propósito/objetivos/alcance/estructura; portada con sección/docente |
| Ejecución sep 2026 | §6.8 HALL-01…05; JMeter CP-05; ZAP anexos; `Informe_Hallazgos_CuidartePlus` |
