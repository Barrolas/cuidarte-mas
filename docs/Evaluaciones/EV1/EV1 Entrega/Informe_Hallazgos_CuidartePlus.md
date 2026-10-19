# Informe de hallazgos — Cuidarte+ (EV1)

**Asignatura:** ISY1102 · Evaluación Parcial 1  
**Ejecutor:** Nicolás Barra  
**Fecha:** 7–8 septiembre 2026  
**Alcance:** Documentación de defectos reales (sin corrección de código en esta entrega)  
**Ambiente:** Docker Compose local (FE `:3333`, API `:4444`, PostgreSQL `:15442`)

---

## 1. Por qué el baseline ZAP “casi no encontró nada grave”

El escaneo OWASP ZAP previo fue **baseline no autenticado**. Solo alcanzó la superficie pública (SPA nginx y raíz JSON de la API). **No** recorrió flujos con JWT (médico/paciente), ni subida/descarga de documentos clínicos.

Por eso el resultado fue: **0 FAIL** + WARN de headers (CSP, clickjacking, `X-Content-Type-Options`, etc.). Eso **no** implica que Cuidarte+ esté seguro: implica que el DAST sin sesión no llega al núcleo del ERS.

Evidencia ZAP ya generada: carpeta [`Anexos/`](./Anexos/) (PDF/MD FE y API) e [`Informe_OWASP_ZAP_CuidartePlus.md`](./Informe_OWASP_ZAP_CuidartePlus.md).

---

## 2. Resumen de hallazgos

| ID | Severidad | Tipo | Título corto | ERS / CP |
|----|-----------|------|--------------|----------|
| **HALL-01** | Alta (funcional) | Funcional / usabilidad | “Ver Documento” no visualiza el adjunto de forma usable | RF-4.2, RF-4.3, NFR-USAB-2 · CP-02/CP-06 |
| **HALL-02** | Crítica (seguridad) | Seguridad | Contraseñas en texto plano (sin bcrypt) | NFR-SEG-2 · CP-01/CP-04 |
| **HALL-03** | Alta | Seguridad | `JWT_SECRET` por defecto `"inseguro"` | NFR-SEG-9 · CP-01 |
| **HALL-04** | Alta (calidad/perf.) | Rendimiento | `delayMiddleware(5000)` falsea NFR-PERF-1 | NFR-PERF-1 · CP-05 |
| **HALL-05** | Media | Hardening | Headers de seguridad ausentes / CORS amplio (ZAP) | NFR-SEG-5 · CP-04 |

---

## 3. Fichas detalladas

### HALL-01 — Ver Documento (médico / formulario de examen)

| Campo | Detalle |
|-------|---------|
| **Descripción** | Tras subir un documento a un examen, al pulsar **“Ver Documento”** en la UI de edición (`ExamenForm`) el usuario no obtiene una visualización/descarga clara del adjunto; se reporta apertura del **cargador de archivos** (selector de ficheros), comportamiento incorrecto. |
| **Ubicación código** | [`FRONTEND/src/pages/examenes/ExamenForm.jsx`](../../FRONTEND/src/pages/examenes/ExamenForm.jsx): botón “Ver Documento” (~L563–570) dentro de un `<form>` **sin `type="button"`**; dropzone (`react-dropzone`) adyacente (~L417–465); `handleDownloadDocument` fuerza nombre `documento-{id}.pdf` (~L167–180). |
| **Roles afectados** | Médico (confirmado en flujo de edición). Admin usa flujo similar en detalle. Paciente descarga desde `MisResultados` (otro handler). |
| **Resultado API** | `POST /documentos` → 201; `GET /documentos/:id` como médico → **200** `Content-Type: application/pdf`, `Content-Disposition: attachment` (API OK). El fallo es **de interfaz / UX**, no de ausencia total del endpoint. |
| **Esperado** | Abrir/descargar el documento ya asociado al examen. |
| **Observado** | Experiencia de “ver” rota / confusión con selector de archivos; descarga UI no alineada a RF-4. |
| **Recomendación** | `type="button"`; `e.preventDefault()`; abrir blob con MIME real en nueva pestaña; separar zona dropzone de acciones de visualización. |

### HALL-02 — Contraseñas en texto plano

| Campo | Detalle |
|-------|---------|
| **Descripción** | El login compara `user.contrasena !== password` en claro; el registro inserta la contraseña sin hash bcrypt. |
| **Evidencia código** | [`BACKEND/src/routes/auth.js`](../../BACKEND/src/routes/auth.js) L21, L110. Dump seed: `admin/admin`, `medico/medico`, `paciente/paciente` en [`dump-cuidarteplus.sql`](../../BACKEND/sql/dump-cuidarteplus.sql). |
| **Evidencia dinámica** | Login `medico/medico` → HTTP 200 + JWT (septiembre 2026). |
| **ERS** | Viola **NFR-SEG-2** (hashing bcrypt). |
| **Recomendación** | bcrypt/argon2 al persistir y al verificar; migrar hashes existentes. |

### HALL-03 — Secreto JWT débil por defecto

| Campo | Detalle |
|-------|---------|
| **Descripción** | Varias rutas usan `process.env.JWT_SECRET \|\| "inseguro"`. |
| **Evidencia** | `auth.js`, `documentos.js`, `examenes.js`, `pacientes.js`, `users.js`, `audit.js`, `roles.js`. |
| **ERS** | Debilita **NFR-SEG-9**. |
| **Recomendación** | Exigir secreto fuerte en entorno; fallar al arrancar si falta. |

### HALL-04 — Delay artificial de 5 s

| Campo | Detalle |
|-------|---------|
| **Descripción** | Middleware añade ~5000 ms a GET/POST de pacientes, exámenes y documentos. |
| **Evidencia código** | [`BACKEND/src/middleware/delay.js`](../../BACKEND/src/middleware/delay.js); uso en `examenes.js`, `pacientes.js`, `documentos.js`. |
| **Evidencia JMeter** | p95 GET Examenes/Pacientes ≈ **5008–5011 ms**; Login p95 ≈ **14 ms**; 0% errores; ver [`Anexos/jmeter/Informe_JMeter_CP05.md`](./Anexos/jmeter/Informe_JMeter_CP05.md). |
| **ERS** | **NFR-PERF-1** (&lt; 300 ms) **no se cumple** con el delay activo. |
| **Recomendación** | Desactivar delay en QA/producción; medir PERF solo sin latencia artificial. |

### HALL-05 — Hardening (ZAP)

| Campo | Detalle |
|-------|---------|
| **Descripción** | Ausencia de CSP, anti-clickjacking, `X-Content-Type-Options`; API filtra `X-Powered-By`; CORS permisivo. |
| **Evidencia** | PDFs ZAP FE/API en `Anexos/`. |
| **ERS** | **NFR-SEG-5** / buenas prácticas NCh27002. |

### Controles que SÍ funcionaron (parcial)

| Prueba | Resultado |
|--------|-----------|
| SQLi trivial en login (`' OR 1=1 --`) | HTTP **401** Credenciales inválidas (parametrización SQL del login) |
| Paciente `GET /usuarios` | HTTP **403** (RBAC admin-only) — corrida previa documentada |
| Descarga API documento por médico | HTTP **200** con PDF |

---

## 4. Trazabilidad a casos de prueba del plan

| Hallazgo | Caso(s) | Efecto en cobertura |
|----------|---------|---------------------|
| HALL-01 | CP-02, CP-06 | RF-4 marcado como **fallido en UI** pese a API OK |
| HALL-02 | CP-01, CP-04 | Evidencia objetiva de incumplimiento NFR-SEG-2 |
| HALL-03 | CP-01 | Riesgo de sesión |
| HALL-04 | CP-05 | NFR-PERF-1 **no cumplido** en ambiente actual |
| HALL-05 | CP-04 | Complementa DAST baseline |

---

## 5. JMeter y rúbrica

JMeter **sí corresponde** a IE3 (prueba no funcional de rendimiento) e IE4 (herramienta de la estrategia + CP-05).  
Resultado: script ejecutable + JTL + HTML report + este informe.

---

## 6. Recomendaciones prioritarias (sin implementar aquí)

1. Corregir UX de “Ver Documento” (HALL-01).  
2. Implementar bcrypt (HALL-02) y secreto JWT obligatorio (HALL-03).  
3. Quitar `delayMiddleware` fuera de demos (HALL-04).  
4. Headers de seguridad en nginx/Express (HALL-05).  
5. Ampliar pruebas autenticadas (IDOR documento ajeno, logout RF-1.2).

---

## 7. Conclusión

Cuidarte+ presenta **defectos reales de seguridad y calidad** alineados al ERS. El baseline ZAP sin sesión solo mostró hardening superficial; la combinación **prueba manual + revisión de código + API autenticada + JMeter** sí evidencia incumplimientos relevantes para la EV1 (IE3/IE5).
