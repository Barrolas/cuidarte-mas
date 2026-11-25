# Evaluación del avance Ninna/EV5-6 frente a la Guía unificada

**Fuente:** `docs/Contenido Academico/Guia-Unificada-Seguridad-y-Calidad.md` (copia de la PDF, 56 págs.).  
**Objeto evaluado:** carpeta `EV5-6 Entrega/Ninna/` al **2026-11-25** (matriz, inventario INC, KPIs, borrador informe, outline guion).  
**Alcance:** lo que ya está escrito; no el cierre del examen (handoffs pendientes).

Criterio de lectura de la guía:

| Bloque guía | Qué exige para este ciclo |
|-------------|---------------------------|
| U1 | Distinguir 25010 (producto) vs 27001 (controles) vs 29119 (proceso de prueba) |
| U2 | Plan, riesgos, casos, matriz, bitácora, informe de certificación, ética/norma |
| U3 | Mitigar + retest; Selenium; carga/estrés; SAST/DAST en pipeline; mejora continua |

---

## 1. Veredicto

El paquete cumple bien el rol de **integración y certificación documental** de la Unidad 2 (matriz, criterios, plan, dictamen provisional, trazabilidad).  
Queda **incompleto frente a la Unidad 3** porque aún faltan remediación P0 verificada, Selenium post-fix, JMeter 5000, Sonar/ZAP after y gráficos con datos reales. Eso es coherente con el cronograma (handoffs vie 27), no es un error de diseño del borrador.

**Nota de avance (solo documentación Ninna):** sólido como esqueleto académico; aún no es entregable final de EP5.

---

## 2. Tabla de cumplimiento (guía → evidencia Ninna)

| Criterio de la guía | ¿Qué dice la guía? | Estado en el avance | Evidencia | Brecha |
|---------------------|--------------------|---------------------|-----------|--------|
| 25010 vs 27001 | No intercambiar producto y SGSI | Cumple | Informe §2.1 y §2.2 separados | — |
| 29119 / plan | Alcance, riesgos, tipos, entrada/salida, herramientas | Cumple (borrador) | Informe §3 | Falta cronograma fechado en Word final |
| Estrategia por riesgo | Priorizar probabilidad × impacto | Cumple | §3.1 P0–P4 heredados | Podría explicitar 1 matriz riesgo 3×3 |
| Caso de prueba | ID, precondiciones, pasos, esperado, trazabilidad | Parcial | Remite a fichas EV2 | §4 aún no pega ≥5 fichas completas |
| Matriz de trazabilidad | REQ ↔ caso ↔ resultado ↔ INC; diseñado ≠ cubierto | Cumple diseño; parcial ejecución ciclo 3 | CSV/MD 40 filas con Resultado EV2 | Columna EV5-6 casi toda “Pendiente handoff” |
| Cobertura | Ejecutado ÷ total; normativos también con caso | Cumple EV2 (40/40 ejecutados) | Nota matriz (10/10/20) | Recalcular post-retest |
| Bitácora | Qué, resultado, quién, cuándo | Parcial (equipo) | Checklist handoff + bitácora Ari INC-04 | Falta consolidar §5.2 |
| Estático / Sonar | SAST; leer panel; no confiar solo en Quality Gate heredado | Pendiente | Hueco G6 + handoff Skarlett | Obligatorio para U3 / IE1 |
| DAST / pentest ético | Autorizado, alcance, evidencia, remediación, retest | Pendiente | Hueco ZAP Ari | Lab Docker = alcance OK |
| Selenium | Flujos repetibles; cuidado flaky | Pendiente post-fix | Baseline EV2 citada | Suite post-mitigación |
| Carga vs estrés | Esperado vs punto de quiebre; métricas JMeter | Parcial | INC-04 timing; G4/G5 vacíos | Falta ramp 5000 |
| Informe de certificación | Alcance, hallazgos, evidencias, limitaciones, decisión | Parcial | §1–3 + §6.4 provisional | Falta resumen ejecutivo 1–2 pág. formal; anexos firmados |
| No conformidad | Descripción + evidencia + cláusula/art. + mayor/menor | Parcial | Inventario INC | Falta formato “NC” con artículo en cada INC cerrado |
| Evidencia objetiva | Verificable, trazable, suficiente | Parcial | Paths Ari EV56-04 | Resto sin path |
| Ética / honestidad | No ocultar hallazgos; no inventar | Cumple | Dictamen “No certificado” con INC-01 abierto; huecos marcados | Mantener al congelar |
| CI/CD DevSecOps | SAST/DAST/secrets/quality gate en pipeline | Pendiente | §6.3 esquema | Diagrama con Skarlett (EV56-21) |
| Continuo U3 | Medir → priorizar → remediar → retest | Parcial | Cadena descrita; 1 INC medido AFTER | Cerrar ≥5 INC con retest |

---

## 3. Fortalezas (alineadas a la guía)

1. **Trazabilidad:** la matriz tiene las columnas que la guía pide (requisito, caso, riesgo, INC, resultado). Se declara que “diseñado no es cubierto”.
2. **Lenguaje de certificación:** el dictamen provisional no certifica con crítico abierto (regla explícita de la guía / material U2).
3. **Separación 25010 / 27001 / normas chilenas:** evita el error frecuente de mezclar atributos de producto con SGSI.
4. **Honestidad metodológica:** no se inventan Selenium/JMeter/Sonar; se marcan pendientes (principio ISTQB: las pruebas muestran presencia de defectos, no su ausencia).
5. **Puente U2 → U3:** el informe habla de mitigar + retest + before/after, no solo de descubrir (fase “Informe y remediación” del pentest / mejora continua).

---

## 4. Debilidades / riesgos académicos

| Riesgo | Por qué importa según la guía | Qué hacer |
|--------|-------------------------------|-----------|
| §4 sin fichas completas | Un informe de certificación necesita casos reproducibles | Pegar ≥5 fichas EP3 + marcar Retest |
| §5 sin gráficos | U2/U3 piden métricas e indicadores, no solo prosa | Completar G1–G6 el vie–sáb |
| NC sin artículo | “Omitir la cláusula no es simplificar” (guía 7.4) | Al cerrar cada INC: Ley/DS/OWASP + evidencia |
| Solo 1 mitigación medible (INC-04) | U3: toda remediación cierra con retest | No declarar “Certificado con reservas” antes de INC-01 |
| Word aún no es el formato docente 100 % | Aspectos formales EP5 | Revisar Arial/portada al pasar del borrador |
| Pipeline CI/CD solo narrado | IE3 / U3.2 | Diagrama SAST→gate→deploy→Selenium→DAST |

---

## 5. Puntaje orientativo por bloque de la guía

Escala: 0 no abordado · 1 iniciado · 2 parcial usable · 3 alineado (falta cierre) · 4 listo entrega.

| Bloque | Puntaje | Comentario |
|--------|---------|------------|
| Fundamentos U1 (calidad/seguridad/norma) | 3 | §2 bien planteado |
| Plan y riesgos U2 | 3 | §3 completo como borrador |
| Diseño de casos U2 | 1–2 | Diferido a EV2 |
| Matriz U2 | 3 | EV2 cargado; ciclo 3 pendiente |
| Ejecución / bitácora U2 | 1 | Solo INC-04 consolidado |
| Informe certificación U2 | 2 | Estructura §1–6; falta evidencias y ejecutivo |
| Ética y dictamen U2 | 3 | Dictamen coherente con INC-01 |
| Mitigación + retest U3 | 1–2 | Proceso definido; 1 fix medido |
| Automatización Selenium U3 | 1 | Baseline citada |
| Desempeño JMeter U3 | 1–2 | Timing 1 VU; falta estrés |
| DevSecOps / pipeline U3 | 1 | Texto §6.3; sin diagrama |

**Promedio aproximado del avance documental:** ~2,1 / 4 (esqueleto listo; cierre operativo pendiente del equipo).

---

## 6. Acciones priorizadas (para subir de 2 → 4)

1. **Viernes:** recibir handoffs (checklist ya escrito).  
2. Completar **no conformidades** INC-01…07 con artículo + evidencia + mayor/menor.  
3. Insertar **G1–G6** en §5.1 y recalcular cobertura post-retest.  
4. Pegar **≥5 casos** en §4 con marca Retest.  
5. Con Skarlett: **diagrama CI/CD** (SAST, secrets scan, quality gate, Selenium, DAST).  
6. Solo entonces actualizar dictamen; si INC-01 sigue abierto, mantener **No certificado**.

---

## 7. Conclusión

Desde la Guía unificada, el trabajo de Ninna está **bien orientado**: hace exactamente el eslabón de certificación (matriz, criterios, plan, dictamen honesto).  
Todavía **no demuestra** el ciclo completo de la Unidad 3 (remediar → retest → métricas → pipeline), porque ese cierre depende de Nicolás, Ari y Skarlett. El borrador Word ya existe para seguir editando sin perder formato.

Archivos relacionados:

- Guía MD: `docs/Contenido Academico/Guia-Unificada-Seguridad-y-Calidad.md`
- Informe DOCX: `Entregables/EP5-Informe-Cuidarte-Mas-borrador.docx`
- Informe MD: `Entregables/01-Informe-EP5-borrador.md`
