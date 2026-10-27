# Bitácora de ejecución — Nicolás Barra (EP3)

**Ambiente:** Docker local FE `:3333` / API `:4444`  
**Datos:** sintéticos (`admin`/`medico`/`paciente` u otros `*.qa`)  
**Instrucción:** una fila por ejecución. No dejes vacío el Resultado si ya corriste el caso.

Estados: `Aprobado` | `Falla` | `Bloqueado` | `No ejecutado`

---

## Resumen por caso

| Fecha | CP | Capa (UI/API/ambas) | Resultado | Evidencia (ruta) | INC / BUG | Notas |
|-------|----|---------------------|-----------|------------------|-----------|-------|
| 2026-10-20 | CP-01 | ambas | Aprobado | Evidencias/CP-01/01…05 + selenium-* | | UI ok/fail + API 200/401 |
| 2026-10-27 | CP-01 (Selenium smoke) | UI auto | Aprobado | Evidencias/CP-01/selenium-login-medico.png + selenium-smoke-output.txt | | `test_smoke_login.py` → /home; captura + log terminal |
| 2026-10-27 | Suite Selenium (8 flujos) | UI auto | Aprobado | Evidencias/Selenium/01…08 + suite-output.txt | | Login +/-; pacientes; exámenes; RBAC usuarios; Mis Resultados; logout UI. `test_suite_flujos.py` 8/8 OK |
| 2026-10-20 | CP-07 | ambas | Falla | Evidencias/CP-07/01…03 | INC-03 | Logout redirige a login pero el mismo JWT sigue dando 200 en GET /examenes |
| 2026-10-20 | CP-08 | ambas | Aprobado | Evidencias/CP-08/01…03 | | Admin lista usuarios + confirmación borrar; médico GET /usuarios → 403. Columna Rol N/A (nota UI) |
| 2026-10-20 | CP-12 | ambas | Aprobado | Evidencias/CP-12/01…03 | | Paciente ve solo sus exámenes (UI + GET /examenes filtrado paciente_id 1) |
| 2026-10-20 | CP-03 | ambas | Falla | Evidencias/CP-03/01…05 | INC-13, INC-14 | Subida sí audita (DOCUMENTOS_CREAR); descarga no aparece en auditoría; POST /auditoria con médico → 201 |
| 2026-10-20 | CP-11 | ambas | Aprobado | Evidencias/CP-11/01…02 | | Edit UI + API reflejan cambios. En lista médico solo lápiz (sin eliminar examen); docs solo borra admin (visto en CP-03) |
| 2026-10-20 | CP-13 | UI | Aprobado* | Evidencias/CP-13/01…05 | INC-15; INC-16 parcial | PDF/JPG/PNG OK; DOCX/PPTX rechazo silencioso. Tiempo ≤10s: Ari. Storage: ver nota INC-16 |
| 2026-10-20 | CP-02 | ambas | Aprobado | Evidencias/CP-02/01…02 | | UI lista con Glicemia/Javiera + API id 3. Toast antes que lista → REC-08 |
| 2026-10-20 | CP-09 | UI | Aprobado | Evidencias/CP-09/01…05 | | Alta paciente vía admin (rol Paciente) + login ok. Clave corta rechazada (≥8). Nota: no usó /registro público |
| 2026-10-20 | CP-10 | ambas | Aprobado | Evidencias/CP-10/00…03 | | Lista + edición Elva (API antes/después). REC-09/10 RUT DV y teléfono país/prefijo. Nota: contacto_emergencia_telefono=”Tek” sin validar |
| 2026-10-20 | CP-04 (SQLMap) | API | Aprobado* | Evidencias/CP-04/ | | SQLMap: no injectable. Payloads manuales OR 1=1 → 401. Ari: ZAP/Burp/Nikto |

---

## Checklist incidentes a confirmar (handoff)

| ID | Descripción corta | ¿Confirmado? (Sí/No/Parcial) | Evidencia |
|----|-------------------|------------------------------|-----------|
| INC-13 | Descarga sin auditoría | Sí | CP-03: hay DOCUMENTOS_CREAR; no hay log de descarga |
| INC-14 | POST /auditoria abierto | Sí | CP-03: médico POST → 201 crea registro inventado |
| INC-15 | DOC/PPT rechazados | Sí | CP-13: DOCX/PPTX no entran; sin toast (REC-07) |
| INC-16 | Documentos en bytea / storage | Parcial | API guarda en memoria→BD (bytea); sin carpeta uploads local típica |
| INC-03 | Sin logout que invalide JWT | Sí | CP-07: token post-logout sigue 200 |

---

## Bugs nuevos (si aparecen)

| ID | CP | Severidad (tú) | Descripción | Evidencia |
|----|----|----------------|-------------|-----------|
| BUG-001 | | | | |

---

## Recomendaciones para el informe (texto; sin evidencia obligatoria)

Borrador para el capítulo de recomendaciones EP3. No son casos de prueba ni requieren capturas.  
Detalle en [`05_Buenas_Practicas_Observaciones.md`](./05_Buenas_Practicas_Observaciones.md).

| ID | ¿Exigido ERS? | Recomendación (pegar/adaptar al informe) | Prioridad |
|----|---------------|------------------------------------------|-----------|
| REC-01 | No | Bloqueo / rate-limit tras 3–5 intentos fallidos de login + mensaje claro + auditoría | Alta |
| REC-02 | Parcial | Validación de entrada alineada UI + API | Media |
| REC-03 | No | Mensajes de error de formularios claros y por campo | Media |
| REC-04 | No | Confirmación y feedback en acciones críticas (alta/baja) | Media |
| REC-05 | Si INC-03 | Invalidar JWT al logout + limpiar token en cliente | Alta |
| REC-06 | No | Tras cerrar sesión, mostrar feedback breve (“Sesión cerrada”) antes o al llegar al login | Baja |
| REC-07 | No | Al rechazar formato (DOCX/PPT), mostrar toast de error; no ignorar el archivo en silencio | Media |
| REC-08 | No | Tras crear examen, refrescar la lista a la vez que el toast de éxito (evitar desfase) | Baja |
| REC-09 | No | Validar RUT chileno con dígito verificador (módulo 11 / “matemática” del DV), no solo formato visual | Alta |
| REC-10 | No | Teléfono: selector de país/prefijo + validación de largo según país (p. ej. Chile +56 y 9 dígitos móviles) | Media |

---

## Firmas de pasada

| Oleada | Fecha inicio | Fecha fin | Comentario |
|--------|--------------|-----------|------------|
| Setup (Docker/Postman/Selenium) | 2026-10-20 | 2026-10-27 | Docker + Postman OK; Selenium smoke + suite 8 flujos (8/8) 2026-10-27 |
| P0 | 2026-10-20 | 2026-10-20 | CP-01 Aprobado; CP-07 Falla INC-03; CP-08 Aprobado; CP-12 Aprobado |
| P1 | 2026-10-20 | 2026-10-20 | CP-03 Falla INC-13/14; CP-11 Aprobado; CP-13 Aprobado* INC-15 |
| P2 + SQLMap | 2026-10-20 | 2026-10-20 | CP-02/09/10 Aprobado; CP-04 SQLMap sin inyección + payloads 401 |

Cuando completes: avisar a **Giannina** para integrar §5 del informe EP3.
