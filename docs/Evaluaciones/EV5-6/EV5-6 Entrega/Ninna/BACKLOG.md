# BACKLOG — Ninna / Giannina Guerrero (EV5-6)

**Rol:** Matriz de trazabilidad, planillas de métricas, informe §1–6 (formato tesis/docente), KPIs/gráficos, dictamen, integración de evidencias; luego guion/PPT/video de defensa.  
**Tablero:** [`../00_Backlog_Equipo.md`](../00_Backlog_Equipo.md)  
**Análisis:** [`../00_Analisis_Encargo_Final.md`](../00_Analisis_Encargo_Final.md)  
**Formato:** [`../../EP5_ISY1102_Estudiante_Formato_Informe.docx`](../../EP5_ISY1102_Estudiante_Formato_Informe.docx) (contenido §1–6)

Estándares a hilvanar: **25010**, **27001**, **29119**; Leyes **20.584**, **19.628**, **DS 41**.

---

## Checklist

- [ ] EV56-22 Planillas (registro CP, matriz, métricas, inventario INC)  
- [ ] EV56-21 Apoyo diagrama CI/CD (con Skarlett)  
- [ ] EV56-23 Informe EP5 §1–6 + KPIs  
- [ ] EV56-24 Dictamen post-mitigación  
- [ ] EV56-25 Guion + PPT + video (después del cierre operativo)  
- [ ] Integración handoffs N/A/S  

---

## EV56-22 — Planillas (tú las llenas; insumos del equipo)

Usar plantillas en `docs/Evaluaciones/EV5-6/` (ojo: algunos archivos están mal etiquetados; ver análisis §7).

### A) Registro / seguimiento de casos
Fuente: `Planilla_Consolidado_Avance_Metricas_Ejecucion_Casos_Prueba.xlsx`

1. Una fila por CP (reuso EV2 + nuevos: SEG fuerza bruta, estrés 5000, Selenium).  
2. Estados: VALIDO / FALLIDO / PASO CON OBSERVACIONES.  
3. Columnas de **CORRECCIONES REALIZADAS** + fecha (ciclo mitigación).  
4. Realizado por / visado por según dueño.

### B) Matriz de trazabilidad
Fuente usable: plantilla `3.4.2` (XLSX mal nombrado como docx) + matriz EV2.

1. Filas RF / RNF / RB del ERS B.  
2. Columnas CP ampliados.  
3. Marcar cobertura post-mitigación.

### C) Dashboard de métricas
Fuente: archivo llamado `EP6_...Presentación.pdf` que en realidad es XLSX de avance.

1. Totales, % avance planificado/real, incidencias, corregidos.  
2. Actualizar con handoffs reales (no inventar).

### D) Inventario INC
Tabla propia: INC · severidad · dueño · before/after · estado Verificado/Abierto.

**DoD:** Excel/PDF anexables al informe sin celdas huérfanas críticas.

---

## EV56-23 — Informe EP5 (§1–6)

### Esqueleto

1. **§1 Introducción** — Cuidarte+, propósito (mitigar + asegurar), estructura.  
2. **§2 Criterios** — 25010 + seguridad + normas; tabla normativa de Skarlett.  
3. **§3 Plan** — estrategia mixta MITIGAR; Selenium/JMeter/ZAP/Sonar/Wireshark; entrada/salida.  
4. **§4 Diseño** — fichas CP (reuso + nuevos).  
5. **§5 Ejecución** — resumen con **gráficos**; detalle; criticidad.  
6. **§6 Mejora** — mitigaciones **aplicadas** + residuales con dueño/fecha + mantenimiento + diagrama CI/CD.

### KPIs / gráficos mínimos

- CP Aprobado/Parcial/Fallido/No ejecutado (antes vs después)  
- INC abiertos vs cerrados por severidad  
- Selenium pass rate / duración  
- JMeter: avg/p95/error % vs VU (+ línea 300 ms)  
- Sonar: vulnerabilidades/bugs antes vs después  
- % INC P0 mitigados  

### Formales
Arial 12/11, interlineado 1,5, justificado, portada con 4 nombres, evidencias legibles.

**DoD:** borrador revisado por pares (hechos: Nico/Ari/Skarlett) antes del PDF final.

---

## EV56-24 — Dictamen

Meta: **Certificado con reservas** si:

1. INC-01, 02, 07 verificados.  
2. Mitigación mínima (≥5) cerrada con retest.  
3. P0 de sesión/estrés documentados; TLS/cifrado con reserva explícita si no hay fix total.  
4. Sin críticos abiertos.

Si falla algún P0 crítico → mantener **No certificado** con lista exacta.

**DoD:** sello + reservas trazables a evidencias.

---

## EV56-25 — Defensa (después del operativo)

1. Outline de láminas (continuidad de voces EV4):  
   - Ninna: marco + dictamen  
   - Nicolás: mitigaciones auth/RBAC + Selenium  
   - Ari: JMeter 5000 + ZAP/John  
   - Skarlett: Sonar + norma/TLS  
2. Guion corto por persona (~2–2,5 min).  
3. PPT + video; solo capturas que existan.  
4. Ensayo: cada uno debe poder explicar **cualquier** lámina (nota individual).

**DoD:** material listo 48 h antes de la defensa.

---

## Ritual de handoffs

| Desde | Qué pedís |
|-------|-----------|
| Nicolás | Bitácora INC auth + Selenium + SQLMap + Wireshark sesión |
| Ari | Tabla JMeter + ZAP + John + headers + fuerza bruta |
| Skarlett | Sonar delta + CP-14/16/17/18 + tabla normativa + diagrama |
| Freeze -48 h | Solo redacción; no cambiar números |

---

## Orden sugerido

| Bloque | Foco |
|--------|------|
| 1 | Plantilla Word + sheet KPIs vacío + matriz estructura |
| 2 | Incorporar primeras mitigaciones (delay, bcrypt) |
| 3 | Gráficos cuando existan Selenium final + JMeter |
| 4 | §5–§6 + dictamen |
| 5 | Revisión cruzada + PDF |
| 6 | Guion/PPT/video |
