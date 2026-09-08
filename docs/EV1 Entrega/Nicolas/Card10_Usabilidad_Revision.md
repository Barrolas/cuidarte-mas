# Card 10 — Usabilidad/compatibilidad + revisión (Nicolás)

**Caso:** CP-06  
**Extras:** revisión técnica + insumos de trazabilidad para Skarlett (Card 5)  
**Rúbrica:** IE3 + apoyo IE5

---

## CP-06 — Usabilidad adulto mayor y compatibilidad responsive

| Campo | Contenido |
|-------|-----------|
| **6.1 ID** | CP-06 |
| **6.2 Descripción** | Evaluar que un paciente adulto mayor complete el flujo paciente → exámenes → descarga de documento en móvil/tablet, con tipografía legible, contraste adecuado y controles táctiles suficientes. |
| **6.3 Requerimiento asociado** | **NFR-USAB-1**, **NFR-USAB-2**, **NFR-USAB-4**, **NFR-COMPAT-2** |
| **6.4 Datos de entrada** | Viewport móvil 375px y tablet ~768px; usuario `paciente.qa`; checklist de contraste/tamaño; sesión UAT guiada (idealmente ≥1 adulto mayor representativo en esta EV1; meta ERS: 5 usuarios). |
| **6.5 Resultado esperado** | Flujo sin bloqueos mayores; layout responsive; textos ≥12px legibles; botones alcanzables; errores comprensibles. |
| **6.6 Criterios de aceptación** | Sin bloqueos mayores en UAT; cumplimiento básico de accesibilidad; score mínimo aceptable según checklist del equipo (Lighthouse Accessibility ≥ 80 como meta interna). |
| **6.7 Tipo de prueba** | **No funcional — Usabilidad / Compatibilidad** |

**Precondiciones**

- Frontend en `http://localhost:3333`.
- Paciente con ≥1 examen y ≥1 documento asociado.
- Chrome DevTools (modo dispositivo) o dispositivo real.

**Pasos**

1. Abrir la app en viewport móvil (375px).
2. Iniciar sesión como `paciente.qa`.
3. Navegar: acceso a paciente → listado de exámenes → detalle → descarga documento.
4. Verificar contraste, tamaño de fuente (≥12px) y área táctil de botones.
5. Repetir smoke en tablet y en un segundo navegador (Firefox o Edge).
6. (Opcional) Ejecutar Lighthouse → Accessibility y anotar puntaje.

**Checklist rápido UAT**

| Ítem | Sí/No |
|------|-------|
| Login comprensible | |
| Exámenes visibles sin confusión | |
| Descarga funciona | |
| No hay texto cortado en móvil | |
| Botones usables con dedo | |
| Mensajes de error claros | |

---

## Revisión técnica cruzada (secciones de Skarlett)

| Sección Skarlett | Qué validó Nicolás | Resultado |
|------------------|--------------------|-----------|
| §2 Criterios + normas | NFR-SEG-1…9 y leyes citadas son coherentes con casos CP-04/CP-03 | OK — mantener vínculo NFR-SEG-8 ↔ 19.628/21.719 |
| §3 Tipos de prueba | Catálogo cubre los tipos usados en CP-01…CP-06 | OK — seguridad/rendimiento/usabilidad presentes |
| Estrategia (§4 de Nicolás) vs tipos | Cada tipo tiene fase y herramienta | OK |

---

## Insumos para matriz de trazabilidad (entregar a Skarlett — Card 5)

| Requerimiento / regla | Tipo de prueba | Caso | Prioridad | Cobertura |
|-----------------------|----------------|------|-----------|-----------|
| RF-1.1 | Funcional / Seguridad | CP-01 | P0 | Cubierto |
| RF-1.2 (logout/revocación) | Seguridad sesión | — | P0 | **Brecha** → recomendar CP-07 en ciclo 2 |
| RF-3.1 | Funcional | CP-02 | P2 | Cubierto |
| RB-3 | Funcional | CP-02 | P2 | Cubierto |
| RF-5.1 | Auditoría | CP-03 | P1 | Cubierto |
| NFR-SEG-4 + RB-1 | Seguridad | CP-04 | P0 | Cubierto |
| NFR-SEG-5 | Seguridad | CP-04 | P0 | Cubierto |
| NFR-PERF-1 | Rendimiento | CP-05 | P3 | Cubierto |
| NFR-PERF-2 / PERF-3 | Rendimiento | — | P3 | **Brecha** documentada |
| NFR-USAB-1/2/4 | Usabilidad | CP-06 | P4 | Cubierto |
| NFR-COMPAT-2 | Compatibilidad | CP-06 | P4 | Cubierto |
| NFR-SEG-8 (normativo) | Cumplimiento vía RBAC + auditoría | CP-03, CP-04 | P0/P1 | Cubierto (indirecto) |
| RF-2.5–2.7 (admin usuarios) | Funcional | — | P2 | **Brecha** → CP-08 sugerido |
| RF-4.2 (descarga ≤10 s) | Funcional / perf. docs | Parcial en CP-06 | P2 | **Parcial** |
| NFR-SEG-1 TLS / NFR-SEG-7 backups | Checklist entorno | — | P0/P1 | Checklist operativo (no caso UI) |

### Mensaje corto para Skarlett (Card 5)

> Cobertura EV1: 6 casos cubren auth, examen, auditoría, RBAC+inyección, rendimiento CRUD y usabilidad/responsive. Brechas conscientes: logout JWT (RF-1.2), CRUD admin completo (RF-2.x), PERF-2/3, medición explícita de descarga ≤10 s. Priorizamos P0/P1 por riesgo clínico-legal.

---

## Verificación de cobertura mínima del encargo

| Requisito del encargo | ¿Cumple? |
|-----------------------|----------|
| ≥5 casos | Sí (6) |
| Campos 6.1–6.7 | Sí |
| Códigos ERS explícitos | Sí |
| ≥2–3 no funcionales | Sí (CP-04, CP-05, CP-06) |
| RF + NFR-SEG + NFR-PERF + NFR-USAB + RF-5 | Sí |

---

**Checklist Card 10**

- [x] CP-06 completo
- [x] Cobertura RF / NFR-SEG / NFR-PERF / NFR-USAB / RF-5
- [x] Revisión cruzada secciones Skarlett
- [x] Insumos matriz para Card 5
