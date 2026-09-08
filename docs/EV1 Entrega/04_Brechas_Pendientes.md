# Brechas pendientes — EV1 (post-merge)

Tras comparar Word Skarlett + paquete Nicolás y unificar el Markdown.

## Ya cerrado en el merge de contenido

| Brecha | Quién | Estado |
|--------|-------|--------|
| Intro sin propósito/objetivos/alcance/estructura (Card 2) | Skarlett | **Cerrado** en `Informe_Plan_Pruebas_CuidartePlus.md` §1.2–1.5 |
| Casos sin rutas reales de API | Nicolás | **Cerrado** (CP usan `/autenticacion`, `/examenes`, etc.) |
| Aviso `delayMiddleware` en PERF | Nicolás | **Cerrado** en CP-05 |
| Merge rama `sk` → `main` local | Equipo | **Hecho** (Word en el repo) |
| Comparación CP | Equipo | **Hecho** en `03_Comparacion_Casos_Skarlett_Nicolas.md` |
| Validación API autenticada (RBAC, SQLi, password plano) | Nicolás | **Hecho** → HALL-02…03 + evidencia CP-04 |
| Bug “Ver Documento” documentado | Nicolás | **Hecho** → HALL-01 (sin fix de código en EV1) |
| JMeter CP-05 + resultados | Nicolás | **Hecho** → `Anexos/jmeter/` + HALL-04 |
| Anexo unificado de hallazgos MD/PDF | Nicolás | **Hecho** → `Informe_Hallazgos_CuidartePlus.*` |
| §6.8 hallazgos + matriz actualizada en informe | Nicolás | **Hecho** |

## Pendiente antes de AVA

| # | Tarea | Responsable | Prioridad |
|---|-------|-------------|-----------|
| 1 | Decidir si se agrega CP-07 logout (RF-1.2) en este entregable o como brecha documentada | Equipo | Media |
| 2 | Checklist TLS / backups (NFR-SEG-1 / 7) como anexo operativo | Nicolás | Media |
| 3 | Estudiar cuestionario individual (`02_Resumen_Estudio_Cuestionario_AVA.md`) | Cada uno | Alta día prueba |

**Cerrado:** 4 integrantes autorizados por docente; Word final generado desde Markdown unificado.

## Qué NO falta para la rúbrica del informe (si se entrega el Markdown unificado / Word actualizado)

- IE1 normativa: cubierta  
- IE2 tipos: cubierta  
- IE3 no funcionales CP-04/05/06 + evidencia JMeter/ZAP/hallazgos: cubierta  
- IE4 plan completo: cubierta (tras completar §1.2–1.5)  
- IE5 cobertura/brechas: cubierta (+ HALL-01…05 trazados)  

Portada con 4 integrantes autorizados; Word alineado al Markdown unificado (incluye hallazgos y anexos).
