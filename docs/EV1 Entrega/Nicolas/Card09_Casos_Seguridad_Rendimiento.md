# Card 9 — Casos de seguridad y rendimiento (Nicolás)

**Casos:** CP-04, CP-05  
**Rúbrica:** IE3 (20%) — card crítica  
**API base:** `http://localhost:4444`

---

## CP-04 — Control de acceso RBAC e inyección en entradas

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-04 |
| **6.2 Descripción** | Verificar que un paciente no puede ejecutar operaciones privilegiadas ni modificar datos ajenos, y que entradas maliciosas (SQLi/XSS) son rechazadas o saneadas. |
| **6.3 Requerimiento asociado** | **NFR-SEG-4**; **RB-1**; **NFR-SEG-5** |
| **6.4 Datos de entrada** | Token JWT de `paciente.qa`. Intentos: `GET/DELETE /usuarios`, `DELETE /examenes/:id` ajeno. SQLi en login: `nombre_usuario="' OR 1=1 --"`, `password="x"`. XSS: observación/campo texto `<script>alert(1)</script>` (si el rol pudiera escribir; o verificar renderizado donde aplique). |
| **6.5 Resultado esperado** | Accesos indebidos → HTTP **401/403** (o equivalente denegado). SQLi **no** autentica. XSS **no** se ejecuta (escapado/saneado). Paciente solo lee **sus** exámenes (`/examenes/paciente/:paciente_id` propio). |
| **6.6 Criterios de aceptación** | RBAC efectivo en backend; validación/saneamiento de entrada; sin hallazgos críticos de inyección en checklist de seguridad. |
| **6.7 Tipo de prueba** | **No funcional — Seguridad** |

**Precondiciones**

- Usuarios `paciente.qa`, `medico.qa`, `admin.qa` creados.
- Al menos un examen de otro paciente (para probar acceso cruzado).
- Postman con variables `token_paciente`, `token_medico`.

**Pasos (RBAC)**

1. `POST /autenticacion/login` como `paciente.qa` → guardar token.
2. Con el token del paciente, invocar `GET /usuarios` y/o `DELETE /usuarios/:id`.
3. Intentar `DELETE /examenes/:id` de un examen ajeno.
4. Verificar denegación (401/403) y que no hubo borrado.
5. Como control positivo: con token de médico, `GET /examenes/paciente/:id` de un paciente registrado debe permitirse (RB-3).

**Pasos (NFR-SEG-5 — inyección)**

6. `POST /autenticacion/login` con payload SQLi en `nombre_usuario`.
7. Verificar 401 / error de validación; **no** emitir JWT.
8. Enviar cadena XSS en un campo de texto persistente (si hay flujo permitido) o validar que el frontend no ejecuta HTML crudo al mostrar datos.
9. Registrar evidencias (status, body, captura ZAP opcional).

**Criterios medibles**

| Métrica | Esperado |
|---------|----------|
| HTTP en acceso indebido | 401 o 403 |
| JWT tras SQLi | Ausente |
| Ejecución de `alert` XSS | No ocurre |

**Ejecución exploratoria (sep 2026) — evidencia CP-04**

| Prueba | Resultado | Hallazgo |
|--------|-----------|----------|
| Paciente `GET /usuarios` | HTTP **403** | RBAC OK (NFR-SEG-4) |
| Login SQLi `' OR 1=1 --` | HTTP **401**, sin JWT | SQLi no autentica |
| Password en claro / seed `medico/medico` | Login 200 + JWT | **HALL-02** (falla NFR-SEG-2) |
| ZAP baseline sin auth | 0 FAIL, WARN headers | **HALL-05** |
| `JWT_SECRET \|\| "inseguro"` | Código + riesgo sesión | **HALL-03** |

Detalle: [`../Informe_Hallazgos_CuidartePlus.md`](../Informe_Hallazgos_CuidartePlus.md).

---

## CP-05 — Tiempo de respuesta CRUD bajo carga normal

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-05 |
| **6.2 Descripción** | Medir latencia de operaciones CRUD simples (pacientes/exámenes) bajo carga normal y contrastarla con el umbral del ERS. |
| **6.3 Requerimiento asociado** | **NFR-PERF-1** |
| **6.4 Datos de entrada** | Script k6/JMeter: **20** usuarios virtuales; mix `GET/POST` sobre `/pacientes` y `/examenes` durante **5 minutos**; ambiente QA local. Token de `medico.qa` o `admin.qa`. |
| **6.5 Resultado esperado** | Tiempo de respuesta de operaciones CRUD simples **&lt; 300 ms** bajo carga normal (usar p95 o media acordada; documentar la métrica elegida). |
| **6.6 Criterios de aceptación** | La prueba de carga cumple NFR-PERF-1; se adjunta resumen de latencias (tabla o gráfico). |
| **6.7 Tipo de prueba** | **No funcional — Rendimiento** |

**Precondiciones**

- Ambiente estable (idealmente sin `delayMiddleware` artificial en rutas bajo medición, o documentar si el delay de desarrollo distorsiona el umbral).
- Dataset sintético precargado.
- Herramienta k6 o JMeter instalada.

> **Nota técnica del repo:** algunas rutas (`/examenes`, `/pacientes` GET) usan `delayMiddleware(5000)` en desarrollo. Para este caso de plan, se declara el umbral del ERS (&lt; 300 ms) y se indica que la medición formal debe ejecutarse con el delay deshabilitado o en build de QA sin latencia artificial.

**Pasos**

1. Preparar script con requests autenticados CRUD.
2. Ejecutar prueba 5 minutos / 20 VUs.
3. Exportar p50, p95, p99 y tasa de error.
4. Comparar p95 (o métrica definida) contra **300 ms**.
5. Si no cumple: registrar defecto de rendimiento con evidencia.

**Artefacto JMeter:** [`../Anexos/jmeter/CuidartePlus_CP05.jmx`](../Anexos/jmeter/CuidartePlus_CP05.jmx) · informe [`../Anexos/jmeter/Informe_JMeter_CP05.md`](../Anexos/jmeter/Informe_JMeter_CP05.md)

**Resultado ejecutado (con `delayMiddleware` activo)**

| Operación | p50 | p95 | p99 | ¿Cumple &lt;300 ms? |
|-----------|-----|-----|-----|---------------------|
| POST Login | 8–10 | ~14 | ~93 | **Sí** |
| GET /pacientes | ~5007 | ~5010 | ~5010 | **No** → **HALL-04** |
| GET /examenes | ~5006 | ~5008 | ~5016 | **No** → **HALL-04** |

Totales: 220 samples · 0% error · TG-B 50 VUs sin fallos HTTP.

---

## Resumen Card 9

| ID | ERS | Tipo | Prioridad |
|----|-----|------|-----------|
| CP-04 | NFR-SEG-4 + RB-1 + NFR-SEG-5 (+ evid. NFR-SEG-2) | Seguridad | P0 |
| CP-05 | NFR-PERF-1 (+ smoke NFR-PERF-3) | Rendimiento | P3 |

**Checklist**

- [x] Criterios medibles (HTTP, ms, rol)
- [x] Sub-caso SQLi/XSS en CP-04
- [x] Datos anonimizados / sintéticos
- [x] Advertencia sobre delay artificial del código
- [x] Ejecución JMeter + anexo de resultados
- [x] Referencia a HALL-02…05 en hallazgos EV1
