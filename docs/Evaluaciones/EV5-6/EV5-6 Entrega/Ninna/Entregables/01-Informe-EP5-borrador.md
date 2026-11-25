# EVALUACIÓN PARCIAL N° 5 (borrador de trabajo)

**Verificación de calidad, seguridad y cumplimiento normativo — ciclo de mitigación**

| Campo | Detalle |
|-------|---------|
| Caso | B · Sistema de exámenes médicos Cuidarte+ |
| Asignatura | ISY1102 · Seguridad y Calidad en el Desarrollo de Software |
| Carrera | Ingeniería en Informática |
| Sección | 001V · Sede Puente Alto |
| Docente | Jose Sergio Collio Huennun |
| Integrantes | Ari Araya · Nicolás Barra · Giannina Guerrero · Skarlett Tropan |
| Fecha borrador | 25 de noviembre de 2026 |
| Estado | Borrador Ninna: §1–§3 listos para pasar a Word; §4–§6 con huecos de handoff |

> Este Markdown es el texto base para pegar al formato docente (Arial 12/11, interlineado 1,5, justificado).  
> Las marcas `«Pendiente handoff»` no se inventan: se completan con bitácoras del equipo.

---

## 1. Introducción

### 1.1 Contexto del software

Cuidarte+ es una plataforma web para centros de salud (Caso B de la asignatura), desarrollada por CreaLab SpA. Permite que los médicos registren pacientes y exámenes, que los pacientes revisen y descarguen documentos clínicos, y que los administradores gestionen usuarios y revisen auditoría. La arquitectura es multicapa: una SPA en React consume una API REST en Express sobre PostgreSQL. En el laboratorio del grupo el sistema se ejecuta con Docker Compose: frontend en el puerto 3333, API en el 4444 (Swagger en `/docs`) y base de datos en el 15442.

Los datos tratados incluyen información de salud. En el marco chileno, la ficha clínica y los datos sensibles de salud están sujetos a la Ley 20.584, al DS 41 y a la Ley 19.628; la Ley 21.719 aparece como horizonte de vigencia (desde el 1 de diciembre de 2026).

### 1.2 Propósito de este informe

En las evaluaciones EP3 y EP4 el equipo diseñó, ejecutó y documentó pruebas funcionales, de seguridad, de rendimiento y de análisis estático. El dictamen de ese ciclo fue **No certificado**, con incidentes críticos y graves abiertos (entre ellos contraseñas en texto plano, secreto JWT expuesto, logout sin revocación de token, retraso artificial de 5 s y ruta `/roles` sin control de rol).

El presente informe corresponde al ciclo **MITIGAR** (EV5-6 / EP5): aplicar remediaciones acordadas, retestear con evidencia before/after, actualizar la matriz de trazabilidad de los 40 códigos del ERS B, incorporar pruebas obligatorias de Selenium y de estrés con JMeter hasta 5000 usuarios concurrentes, y emitir un dictamen actualizado.

### 1.3 Alcance y estructura

- **Dentro de alcance:** remediación mínima de INC-01, INC-02, INC-03, INC-04 e INC-07; ampliación recomendada (INC-05, 06, 13, 14); retest con Selenium, JMeter, ZAP, SonarQube, SQLMap, John the Ripper y Wireshark según rol; matriz 40/40; KPIs; propuesta de mejora con mitigaciones aplicadas.
- **Fuera de alcance o con reserva:** TLS productivo completo y alta disponibilidad multi-réplica si el entorno Docker local no lo permite; se documentan como limitación o plan fechado en la sección 6.

El documento sigue el formato oficial: criterios de calidad (sección 2), plan de pruebas (sección 3), diseño de casos (sección 4), ejecución (sección 5) y propuesta de mejora (sección 6).

---

## 2. Criterios de calidad

Los criterios unen tres objetivos: calidad de producto, seguridad de la información y cumplimiento normativo. Cada criterio debe ser medible con un caso de prueba, una herramienta o un control revisable.

### 2.1 Calidad de producto (ISO/IEC 25010:2023)

| Característica 25010 | Criterio en Cuidarte+ | Cómo se mide |
|----------------------|----------------------|--------------|
| Adecuación funcional | Login, CRUD clínico, auditoría y roles según ERS B | CP funcionales / API / Selenium |
| Eficiencia de desempeño | Respuestas bajo umbral (NFR-PERF-1: 300 ms en condiciones de laboratorio acordadas); capacidad bajo carga | JMeter (ramp hasta 5000 VU); timing API |
| Seguridad | Autenticación, autorización, secretos, entradas, configuración | ZAP, SQLMap, John, Postman/curl, revisión de código |
| Fiabilidad / disponibilidad | Continuidad básica del laboratorio | CP-21; documentación de limitación si aplica |
| Capacidad de interacción | Mensajes claros; sin fugas técnicas al usuario | CP-06, CP-17, CP-20 |
| Mantenibilidad | Defectos detectables por SAST; código sin olores críticos nuevos | SonarQube before/after |
| Compatibilidad | Chrome/Edge (mínimo); otros navegadores según evidencia | CP-22 |

### 2.2 Seguridad (controles alineados a ISO/IEC 27001 — enfoque)

| Control | Criterio | Evidencia esperada |
|---------|----------|-------------------|
| Cifrado de autenticadores | Contraseñas con hash (bcrypt); sin texto plano en BD | INC-01 + John/psql |
| Gestión de secretos | JWT solo en variables de entorno; no en README/código | INC-02 |
| Gestión de sesión | Logout invalida el token | INC-03 / CP-07 |
| Control de acceso | Endpoints sensibles exigen JWT y rol | INC-07, RB-1, CP-04/08 |
| Registro (auditoría) | Acciones relevantes (p. ej. descarga) quedan trazadas | INC-13 / RF-5.1 |
| Manejo de errores | Respuestas genéricas; sin `err.message` al cliente | INC-06 / CP-17 |
| Comunicación | Preferir TLS; si el lab es HTTP, declarar limitación | CP-14 / Wireshark |

### 2.3 Cumplimiento normativo (resumen)

| Norma | Qué exige (lectura de laboratorio) | Relación con Cuidarte+ |
|-------|------------------------------------|------------------------|
| Ley 20.584 | Acceso a ficha clínica según derechos del paciente | RBAC, datos de exámenes/documentos |
| DS 41 | Seguridad de la ficha (integridad, transmisión, registro) | Auditoría, TLS/limitación, control de acceso |
| Ley 19.628 | Protección de datos personales / sensibles | INC-01, secretos, errores |
| Ley 21.719 | Horizonte (vigencia 01-12-2026): deber de seguridad reforzado | Se cita como proyección, no como única base vigente al 25-11-2026 |

«Pendiente handoff Skarlett»: insertar tabla normativa detallada (artículos ↔ INC/CP) cuando llegue EV56 handoff.

### 2.4 Criterios transversales de aceptación del ciclo

1. Ambiente Docker reproducible (FE 3333 / API 4444).  
2. Al menos cinco incidentes mitigados y retesteados, con ≥1 crítico (INC-01).  
3. Suite Selenium ejecutada y archivada.  
4. Intento documentado de JMeter a 5000 VU (con ramp previo).  
5. Cero defectos críticos abiertos para aspirar a **Certificado con reservas**; si INC-01 sigue abierto, el dictamen permanece **No certificado**.

---

## 3. Plan de pruebas

### 3.1 Estrategia

Estrategia **mixta basada en riesgos**, con *shift-left* en lo ya detectado en EV2:

1. Mitigar primero los INC P0 (autenticación, secretos, sesión, rendimiento artificial, RBAC).  
2. Retestear con evidencia before/after.  
3. Automatizar regresión UI (Selenium obligatorio).  
4. Medir desempeño sin el delay artificial y escalar carga.  
5. Complementar con SAST (Sonar) y DAST (ZAP) autenticado.  

Priorización heredada: P0 autenticación/acceso/documentos clínicos; P1 auditoría y configuración; P2 CRUD; P3 rendimiento/disponibilidad; P4 usabilidad/compatibilidad.

### 3.2 Tipos de prueba

| Tipo | Propósito en este ciclo | Herramienta |
|------|-------------------------|-------------|
| Funcional / reglas de negocio | Confirmar flujos tras el fix | Selenium, Postman/Swagger |
| Seguridad — autenticación | Hash, política de clave, sesión | John, curl, CP-01/07/15 |
| Seguridad — autorización | Roles e IDOR | curl/Swagger, CP-04/08 |
| Seguridad — entradas | Inyección en login | SQLMap |
| Seguridad — configuración | Headers, CORS, errores | curl, ZAP, CP-17 |
| Análisis estático | Defectos y hotspots en código | SonarQube |
| Rendimiento / estrés | Latencia y error % hasta 5000 VU | JMeter |
| Tráfico de red | Visibilidad HTTP/TLS en lab | Wireshark |
| Configuración / cumplimiento | TLS, cifrado en reposo, respaldo | Revisión + CP-14/16/18 |

### 3.3 Criterios de aceptación (ejemplos)

| Ámbito | Criterio |
|--------|----------|
| API autenticada | 401 sin token; 403 rol insuficiente; 2xx rol correcto |
| Logout | Tras logout, el token previo no autoriza (401) |
| Contraseñas | BD sin texto plano; John carga hashes |
| Desempeño 1 VU post-delay | GET clínicos ≪ 300 ms en lab (baseline Ari ~30 ms) |
| Estrés | Ramp documentado; intento 5000 VU con `.jtl` |
| Selenium | Report HTML/JSON; casos críticos en verde o con INC residual declarado |
| Secretos | Sin JWT en README ni código fuente versionado |

### 3.4 Herramientas y recursos

| Recurso | Detalle |
|---------|---------|
| Entorno | Docker Compose; usuarios semilla `admin`/`medico`/`paciente` |
| Roles | Nicolás (auth/RBAC/Selenium/SQLMap); Ari (delay/JMeter/ZAP/John); Skarlett (Sonar/errores/TLS/norma); Giannina/Ninna (matriz/informe/dictamen) |
| Evidencias | Prefijo `EV56-<ID>-` bajo `EV5-6 Entrega/*/Evidencias/` |

---

## 4. Diseño de casos de prueba

Se reutilizan el catálogo y las fichas de la EP3 (23 casos → 40 códigos ERS B). En este ciclo MITIGAR, los casos ligados a INC-01…07, 05, 06, 13 y 14 se marcan como **Retest ciclo EV5-6**. El resultado de ejecución EV5-6 se completa con handoff (viernes 27); no se inventa.

### 4.1 Matriz de trazabilidad

La matriz 40/40 con columnas Resultado EV2 y Resultado EV5-6 está en:

- Trabajo: `Planillas/EV56-22-Matriz-40-ERS-ciclo3.csv`
- Word: `EV5-6 Contexto/02-Matriz-trazabilidad-40-ERS.docx`

### 4.2 Catálogo de casos (reuso EP3)

| Caso | Nombre | Códigos ERS | Herramienta | Ejecuta | Retest EV5-6 |
|------|--------|-------------|-------------|---------|--------------|
| CP-01 | Autenticación válida y rechazo de credenciales inválidas | RF-1.1, NFR-SEG-2, NFR-SEG-9 | UI, Postman/Swagger, Selenium | Nicolás | Sí (post bcrypt / JWT) |
| CP-02 | Registro de examen médico | RF-3.1, RB-3 | UI, Postman, Selenium | Nicolás | Sí (post INC-04) |
| CP-03 | Auditoría ante acciones críticas | RF-5.1, NFR-SEG-8 | Postman, BD auditoría | Nicolás | Sí (INC-13/14) |
| CP-04 | Control de acceso por rol e inyección | NFR-SEG-4, NFR-SEG-5, RB-1 | ZAP, SQLMap, Swagger | Ari / Nicolás | Sí (INC-05/07) |
| CP-05 | Tiempo CRUD bajo carga + estrés | NFR-PERF-1 (+ ramp 5000) | JMeter | Ari | Sí (INC-04; 5000 pendiente) |
| CP-06 | Usabilidad adulto mayor / responsivo | NFR-USAB-1/2/4, NFR-COMPAT-2 | Checklist, Lighthouse | Skarlett | Según alcance |
| CP-07 | Cierre de sesión y revocación de token | RF-1.2, NFR-SEG-9 | Postman, Selenium | Nicolás | Sí (INC-03) |
| CP-08 | Administración de usuarios (admin) | RF-2.5–2.7, NFR-SEG-4, RB-2 | UI, Postman, Selenium | Nicolás | Sí (INC-07) |
| CP-09…CP-13 | Registro, pacientes, exámenes, documentos | RF-2.*, RF-3.*, RF-4.* | UI / Postman / Selenium | Nicolás (+ Ari tiempo) | Selectivo |
| CP-14 | TLS frontend y API | NFR-SEG-1 | Revisión nginx / compose | Skarlett | Resultado o reserva |
| CP-15 | Hash de contraseñas / John | NFR-SEG-2 | BD + John the Ripper | Ari | Sí (INC-01) |
| CP-16 | Cifrado en reposo | NFR-SEG-3 | Esquema / uploads / Sonar | Skarlett | Resultado o reserva |
| CP-17 | Logs y errores sin fuga | NFR-SEG-6 | Sonar, Swagger | Skarlett / Ari | Sí (INC-06) |
| CP-18 | Respaldo / restauración | NFR-SEG-7 | pg_dump | Skarlett | Resultado o reserva |
| CP-19 | Perf página / 200 VU | NFR-PERF-2/3 | Lighthouse, JMeter | Ari | Tras INC-04 |
| CP-20…CP-22 | Usabilidad mensajes / disponibilidad / browsers | NFR-USAB-3, NFR-DIS-*, NFR-COMPAT-1 | Manual / doc | Varios | Según alcance |
| CP-23 | Cumplimiento normativo | NFR-SEG-8 | Checklist normativo | Giannina | Con tabla Skarlett |
| SEL-suite | Regresión UI Selenium post-mitigación | RF/RB críticos | Selenium report.html/json | Nicolás | **Obligatorio** |

### 4.3 Casos detallados (mínimo representativo + obligatorios)

Formato alineado al formato oficial EP5 (ID · Nombre · Requerimiento · Descripción · Precondiciones · Pasos · Resultado esperado · Criterio · Datos · Tipo). Fuente de diseño: fichas EP3. Columna adicional de este ciclo: **Retest EV5-6**.

#### Tabla. Ficha CP-01 (auth + hashes)

| Campo | Contenido |
|-------|-----------|
| ID / Nombre | CP-01 · Autenticación válida y rechazo de credenciales inválidas |
| Requerimiento | RF-1.1; NFR-SEG-2; NFR-SEG-9 |
| Descripción | Verificar que un usuario válido obtiene JWT; credenciales inválidas se rechazan sin filtrar si el usuario existe; post-mitigación las contraseñas no están en texto plano. |
| Precondiciones | Docker FE 3333 / API 4444. Usuario de prueba (p. ej. médico). |
| Pasos | 1. POST `/autenticacion/login` válido. 2. Verificar 200 + JWT. 3. Login inválido → 401. 4. (EV5-6) Confirmar hashes en BD / John carga hashes (con CP-15). |
| Resultado esperado | Login válido 200; rechazos 401; BD sin texto plano tras INC-01. |
| Criterio de aceptación | Token solo con credenciales válidas; NFR-SEG-2 cumplido en retest. |
| Datos de prueba | Credenciales semilla del laboratorio; variantes inválidas. |
| Tipo | Funcional y seguridad |
| Retest EV5-6 | Pendiente handoff Nicolás/Ari (post bcrypt) |
| Resultado EV2 | Aprobado en login; INC-01 abierto en almacenamiento (CP-15) |

#### Tabla. Ficha CP-15 (John / hashes)

| Campo | Contenido |
|-------|-----------|
| ID / Nombre | CP-15 · Almacenamiento de contraseñas y resistencia a crackeo |
| Requerimiento | NFR-SEG-2 |
| Descripción | Comprobar que las contraseñas en BD usan hash seguro (bcrypt) y que John the Ripper opera sobre hashes, no sobre texto plano. |
| Precondiciones | Acceso a BD de prueba; John instalado; baseline EV2: texto plano. |
| Pasos | 1. Consultar columna de contraseñas. 2. Exportar hashes si existen. 3. Ejecutar John. 4. Contrastar before (EV2) vs after (EV5-6). |
| Resultado esperado | Hashes bcrypt; John no ve texto plano. |
| Criterio de aceptación | NFR-SEG-2 cumplido; evidencia before/after archivada. |
| Datos de prueba | Usuarios semilla del laboratorio. |
| Tipo | Seguridad |
| Retest EV5-6 | Pendiente handoff Ari (bloqueado por INC-01) |
| Resultado EV2 | Fallido (INC-01) |

#### Tabla. Ficha CP-07 (logout)

| Campo | Contenido |
|-------|-----------|
| ID / Nombre | CP-07 · Cierre de sesión y revocación del token |
| Requerimiento | RF-1.2; NFR-SEG-9 |
| Descripción | Al cerrar sesión, el JWT previo deja de autorizar llamadas a la API. |
| Precondiciones | Docker arriba; usuario médico; al menos un recurso autenticado. |
| Pasos | 1. Login y guardar token. 2. GET autenticado → 200. 3. Logout. 4. Reutilizar token → 401. |
| Resultado esperado | 401 con el token post-logout. |
| Criterio de aceptación | Logout invalida sesión en servidor (no solo UI). |
| Datos de prueba | Token JWT del paso 1. |
| Tipo | Seguridad de sesión |
| Retest EV5-6 | Pendiente handoff Nicolás (INC-03) |
| Resultado EV2 | Fallido (INC-03) |

#### Tabla. Ficha CP-04 / CP-08 (RBAC e `/roles`)

| Campo | Contenido |
|-------|-----------|
| ID / Nombre | CP-04 · Control de acceso por rol; CP-08 · Administración de usuarios |
| Requerimiento | NFR-SEG-4, NFR-SEG-5, RB-1, RF-2.5–2.7, RB-2 |
| Descripción | Paciente no administra ni ve datos ajenos; médico no usa `/usuarios` ni `/roles` de admin; admin completa CRUD de usuarios; `/roles` exige JWT+admin. |
| Precondiciones | Tokens de los tres roles. |
| Pasos | 1. Paciente: escrituras / datos ajenos → 403. 2. Médico: `/usuarios`, `/roles` → 401/403. 3. Admin: listar/editar/eliminar → 2xx. 4. Sin token → 401. |
| Resultado esperado | Matriz 401/403/2xx según rol; sin inyección crítica. |
| Criterio de aceptación | Control efectivo en backend (INC-07 cerrado). |
| Datos de prueba | Tokens paciente / médico / admin; payloads SQLMap/ZAP según bitácora. |
| Tipo | Seguridad / funcional RBAC |
| Retest EV5-6 | Pendiente handoff Nicolás/Ari |
| Resultado EV2 | Parcial (403 en varios flujos; `/roles` sin prueba dinámica completa) |

#### Tabla. Ficha CP-05 + estrés 5000 VU

| Campo | Contenido |
|-------|-----------|
| ID / Nombre | CP-05 · Tiempo CRUD + ramp JMeter hasta 5000 VU |
| Requerimiento | NFR-PERF-1 (300 ms); estrés obligatorio del examen |
| Descripción | Medir latencia CRUD sin delay artificial y documentar ramp 100→1000→2500→5000 VU. |
| Precondiciones | INC-04 mitigado (delay fuera de rutas). Ambiente estable. |
| Pasos | 1. Humo 1 VU (timing API). 2. Planes JMeter por fase. 3. Archivar `.jtl` / dashboard. 4. Si HW no alcanza 5000, declarar techo. |
| Resultado esperado | 1 VU ≪ 300 ms; fases documentadas; intento 5000 con evidencia. |
| Criterio de aceptación | Evidencia before/after delay + tablas por VU. |
| Datos de prueba | GET/POST pacientes y exámenes; usuarios virtuales por fase. |
| Tipo | Rendimiento / estrés |
| Retest EV5-6 | **Parcial hecho:** after delay ~0,03 s (Ari EV56-04). JMeter 5000 pendiente. |
| Resultado EV2 | Fallido (INC-04, ~5 s) |

#### Tabla. Ficha SEL-suite (Selenium obligatorio)

| Campo | Contenido |
|-------|-----------|
| ID / Nombre | SEL-suite · Regresión UI post-mitigación |
| Requerimiento | Flujos críticos RF/RB (login, roles, pacientes, exámenes) |
| Descripción | Ejecutar suite Selenium tras mitigaciones P0; archivar `report.html` y `report.json` con pass rate. |
| Precondiciones | Mitigación mínima 01–05 en código desplegado en lab. |
| Pasos | 1. Levantar Docker. 2. Correr suite. 3. Guardar reportes bajo `Nicolas/Evidencias/`. 4. Anotar fallos → INC residual. |
| Resultado esperado | Pass rate informado; fallos trazados a INC. |
| Criterio de aceptación | Reportes archivados; no se sustituye DAST/SAST. |
| Datos de prueba | Usuarios semilla; baseline EV2 11/11 solo como referencia. |
| Tipo | Automatización UI |
| Retest EV5-6 | Pendiente handoff Nicolás |
| Resultado EV2 | Baseline 11/11 (no sustituye post-fix) |

---

## 5. Ejecución

### 5.1 Resumen y KPIs

Plantilla y contadores: `../Planillas/EV56-22-KPIs.md`.

**Hecho al 25-11-2026 (parcial):**

- EV56-04 / INC-04: delay retirado en rutas; before ~5,03 s → after ~0,03 s; humo FE OK (Ari).  
- Matriz EV2 cargada: 10 aprobados, 10 parciales, 20 fallidos.

**Pendiente handoff:** Selenium post-fix, JMeter 5000, Sonar delta, ZAP after, John post-bcrypt, SQLMap retest, Wireshark.

### 5.2 Detalle por caso

«Pendiente»: pegar tabla del formato (Caso · Descripción · Resultado · Evidencia · Tipo) desde bitácoras Nicolás/Ari/Skarlett.

### 5.3 Criticidad de incidentes

Ver `../Planillas/EV56-22-Inventario-INC.md`.  
Escala: Crítico / Grave / Moderado / Leve (formato EP3).

---

## 6. Propuesta de mejora

Presenta acciones concretas de remediación (formato EP5: ID · impacto · propuesta) y el plan de residuales. Los estados «Verificado» solo se marcan con evidencia de retest.

### 6.1 Mitigaciones del ciclo (mínimo de examen)

#### INC-04 · Delay artificial 5 s

| Campo | Contenido |
|-------|-----------|
| ID / nombre | INC-04 / NFR-PERF-1 · `delayMiddleware(5000)` |
| Impacto | Grave — invalida mediciones de desempeño; CRUD ~5 s |
| Propuesta de remediación | Quitar `delayMiddleware` de rutas `pacientes`, `examenes`, `documentos` |
| Retest | Timing API + humo FE; luego JMeter ramp |
| Estado 25-11-2026 | **Medido AFTER** (Ari). Before ~5,03 s → after ~0,03 s. Paths: `Ari/Evidencias/EV56-04/`. Pendiente cierre/merge de equipo y JMeter 5000 |

#### INC-01 · Contraseñas en texto plano

| Campo | Contenido |
|-------|-----------|
| ID / nombre | INC-01 / NFR-SEG-2 · almacenamiento de autenticadores |
| Impacto | **Crítico** — exposición total de cuentas |
| Propuesta de remediación | Hash bcrypt al registrar/actualizar; migrar semillas; política de clave |
| Retest | CP-15 (John) + CP-01 login |
| Estado | **Abierto** — pendiente handoff Nicolás/Ari |

#### INC-02 · JWT_SECRET en repositorio

| Campo | Contenido |
|-------|-----------|
| ID / nombre | INC-02 / NFR-SEG-9 · secreto de sesión |
| Impacto | Grave — compromiso de sesiones |
| Propuesta de remediación | Secreto solo en variables de entorno; limpiar README/código versionado |
| Retest | Revisión repo + login |
| Estado | **Abierto** — pendiente Nicolás |

#### INC-03 · Logout sin revocación

| Campo | Contenido |
|-------|-----------|
| ID / nombre | INC-03 / RF-1.2 · sesión post-logout |
| Impacto | Grave — sesión usable en equipo compartido |
| Propuesta de remediación | Endpoint logout + blacklist/rotación de token |
| Retest | CP-07 |
| Estado | **Abierto** — pendiente Nicolás |

#### INC-07 · `/roles` sin control de rol

| Campo | Contenido |
|-------|-----------|
| ID / nombre | INC-07 / NFR-SEG-4 · autorización en `/roles` |
| Impacto | Grave — escalada de privilegios |
| Propuesta de remediación | Exigir JWT + rol administrador en la ruta |
| Retest | curl/Swagger 401/403/2xx (CP-04/08) |
| Estado | **Abierto** — pendiente Nicolás |

### 6.2 Residuales y plan (reserva §6 / ampliación)

| INC / tema | Impacto | Dueño | Fecha objetivo | Estado |
|------------|---------|-------|----------------|--------|
| INC-05 CORS + cabeceras | Moderado/Grave | Ari | Antes de ZAP after | Abierto |
| INC-06 fuga `err.message` | Grave | Skarlett | Con CP-17 | Abierto |
| INC-13 descarga sin auditoría | Grave | Nicolás | Tras P0 | Abierto |
| INC-14 POST `/auditoria` abierto | Grave | Nicolás | Tras P0 | Abierto |
| INC-09 baja lógica | Grave | Nicolás | Reserva si no alcanza | Abierto |
| INC-10 política de clave / registro | Moderado | Nicolás | Con INC-01 | Parcial |
| INC-15 formatos DOC/PPT | Moderado | Nicolás | Reserva | Abierto |
| INC-16 cifrado reposo / bytea | Grave | Skarlett | Reserva + plan | Abierto |
| INC-17 disponibilidad / réplica | Grave | Ari | Reserva | Abierto |
| CP-14 TLS laboratorio | P0 config | Skarlett | Resultado o limitación fechada | Pendiente |
| Lockout anti fuerza bruta | P1 | Ari (+ Nico) | Tras INC-01 | Pendiente |
| Wireshark sesión / carga | P1 | Nico / Ari | Según tiempo | Pendiente |

### 6.3 Mantenimiento continuo (IE7) y CI/CD

Objetivo: que los controles de calidad y seguridad no dependan solo del examen puntual.

Flujo propuesto (borrador Ninna para completar con Skarlett — EV56-21):

1. Commit / PR  
2. Build  
3. Pruebas unitarias  
4. SonarQube Quality Gate (SAST)  
5. Build imagen Docker  
6. Deploy a laboratorio  
7. Selenium (regresión UI)  
8. (Opcional / nocturno) ZAP autenticado  

Diagrama editable: `Planillas/EV56-21-Diagrama-CICD-borrador.md`.

Relación normativa de proceso: ISO/IEC/IEEE **29119** (proceso de pruebas) y controles alineados a **27001** (acceso, registro, desarrollo seguro).

### 6.4 Dictamen (borrador — no definitivo)

**Dictamen provisional al 25-11-2026: No certificado.**

Fundamento: INC-01 (crítico) sigue abierto; INC-02, 03 y 07 sin retest verificado. INC-04 muestra mejora medible de desempeño, pero no basta para certificar mientras exista un crítico abierto.

Meta del equipo al cierre: **Certificado con reservas**, si se verifican INC-01, 02, 03, 04 y 07 y se declaran reservas explícitas (p. ej. TLS de laboratorio, techo de hardware en 5000 VU, cifrado en reposo).

---

## Anexos (índice)

- A. Matriz 40 ERS ciclo 3 (CSV)  
- B. Inventario INC  
- C. KPIs G1–G6  
- D. Evidencias por integrante (paths)  
- E. Outline guion EP6
- F. Diagrama CI/CD borrador (EV56-21)  

---

*Elaborado como avance de integración por Giannina Guerrero (Ninna). Congelar números el sábado 28-11-2026 tras handoffs del viernes 27.*
