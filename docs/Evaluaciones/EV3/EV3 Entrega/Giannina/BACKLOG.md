# BACKLOG — Giannina Guerrero (EV3 / EP5)

**Continuidad EV2:** matriz de trazabilidad 40 ERS, marco normativo, dictamen, integración del informe, guion de presentación.  
**Tablero:** [`../00_Backlog_Equipo.md`](../00_Backlog_Equipo.md)  
**Formato:** [`../../EV3 Contexto/EP5_ISY1102_Estudiante_Formato_Informe.pdf`](../../EV3%20Contexto/EP5_ISY1102_Estudiante_Formato_Informe.pdf)  
**Análisis:** [`../00_Analisis_Encargo_EP5.md`](../00_Analisis_Encargo_EP5.md)

Estándares a hilvanar en el relato: **25010** (producto), **27001** (controles de información), **29119** (proceso de prueba), Leyes **20.584**, **19.628**, **DS 41**, horizonte **21.719**.

---

## Checklist rápido

- [ ] EV3-21 Matriz 40 ERS ciclo 3  
- [ ] EV3-22 KPIs y gráficos §5.1  
- [ ] EV3-23 Informe EP5 §1–6  
- [ ] EV3-24 Dictamen actualizado  
- [ ] EV3-25 Prep guion EP6  
- [ ] Integración handoffs N/A/S  

---

## EV3-21 — Matriz de trazabilidad 40 ERS (ciclo 3)

### Objetivo
Actualizar la matriz EV2 con resultados **post-remediación** y responsables.

### Pasos

1. Partir de la matriz EP3/EP4 (Word/PDF en `EV2 Contexto` / entregables Giannina).
2. Columnas mínimas: Código ERS · Descripción · CP · Tipo · Riesgo · Módulo · Ejecuta · INC · **Resultado EV2** · **Resultado EV3** · Evidencia path.
3. Incorporar handoffs:
   - Nicolás: CP funcionales/API/Selenium.
   - Ari: CP-04, 05, 15 (+ 19/21 si hay).
   - Skarlett: CP-14, 16, 17, 18.
4. Marcar los 2 CP de rendimiento que en EV2 dependían de CP-19: actualizar si Ari corre algo; si no, mantener “sin ejecutar” con justificación.
5. Exportar PDF/DOCX a `EV3 Entrega/Giannina/` o carpeta Entregables cuando exista.

### DoD
- [ ] 40 códigos con fila ciclo 3  
- [ ] Sin celdas “Pendiente” huérfanas sin dueño  

---

## EV3-22 — KPIs y gráficos (§5.1)

### Objetivo
Ilustrar resultados (requisito de equipo para EP5).

### Gráficos mínimos (obligatorios del análisis)

| # | Gráfico | Datos de entrada | Dueño del dato |
|---|---------|------------------|----------------|
| G1 | CP Aprobado/Parcial/Fallido/No ejecutado EV2 vs EV3 | Matriz | Giannina + handoffs |
| G2 | Incidentes abiertos vs cerrados por severidad | Tabla INC unificada | Todos |
| G3 | Selenium pass rate y duración | report.json Nicolás | Nicolás |
| G4 | JMeter: latencia (avg/p95) vs VU + línea 300 ms | Tabla Ari | Ari |
| G5 | JMeter: error % vs VU (incluir punto 5000) | Tabla Ari | Ari |
| G6 | Sonar vulnerabilidades/bugs antes vs después | Tabla Skarlett | Skarlett |

### Pasos

1. Crear hoja `EV3-22-KPIs.xlsx` (o Google Sheet) con pestañas raw + charts.
2. Insertar gráficos en el Word del informe (no solo enlaces).
3. Cada gráfico: título, fuente (“evidencia … fecha …”), una frase de lectura.
4. *Pendiente rúbrica oficial:* añadir métricas/logs que pida el documento formal.

### DoD
- [ ] 6 gráficos en el borrador §5.1  
- [ ] Archivo de datos reproducible  

### Plantilla de tarjeta KPI (copiar al informe)

```
KPI: <nombre>
Valor EV2 → Valor EV3
Umbral / meta: <...>
Interpretación (1–2 oraciones):
Evidencia: <ruta>
```

---

## EV3-23 — Informe EP5 (§1–6)

### Objetivo
Redactar el entregable según formato preliminar, enriquecido con remediación + retest + KPIs.

### Esqueleto operativo

#### §1 Introducción
- Contexto Cuidarte+ (React / Express / PostgreSQL, Docker local).  
- Por qué el plan: datos clínicos, dictamen EV2 No certificado.  
- Qué incluye este informe: remediación ciclo 3, Selenium, JMeter 5000, Wireshark, dictamen actualizado.  
- Estructura §2–§6.

#### §2 Criterios de calidad
- Tabla 25010: característica → criterio Cuidarte+ → cómo se mide (CP/herramienta).  
- Seguridad: acceso, secretos, errores, integridad, tránsito (enlace DS 41).  
- Normativa: 20.584, 19.628, DS 41; 21.719 como horizonte.  
- Incluir tabla normativa de Skarlett (resumida).

#### §3 Plan de pruebas
- 3.1 Estrategia mixta; priorización P0–P4; entrada/salida (ver análisis).  
- 3.2 Tipos: funcional, API, seguridad dinámica/estática, rendimiento, usabilidad (si aplica), configuración.  
- 3.3 Aceptación transversal: códigos HTTP, RBAC, umbrales perf, “sin secreto en repo”, etc.  
- 3.4 Herramientas + recursos humanos/técnicos/entorno (Selenium **obligatorio**, JMeter 5000, Wireshark).

#### §4 Diseño de casos
- Reusar fichas EV2; marcar **Retest ciclo 3** en los afectados por INC.  
- Añadir/ajustar casos Selenium y el de concurrencia 5000.

#### §5 Ejecución
- 5.1 Resumen + **gráficos G1–G6**.  
- 5.2 Detalle por CP (tabla del formato: Caso, Descripción, Resultado, Evidencia, Tipo).  
- 5.3 Criticidad: escala Crítico/Grave/Moderado/Leve; lista INC con estado *Verificado* o residual.

#### §6 Propuesta de mejora
- Por cada INC P0: remediación **aplicada** + evidencia de retest.  
- Por cada residual P1/P2: propuesta técnica + impacto + dueño + fecha.  
- Formato del PDF docente: ID · Nombre · Impacto · PROPUESTA DE REMEDIACIÓN.

### Pasos de integración

1. Congelar fecha de corte de evidencias.  
2. Pegar capturas con pie: herramienta, fecha, autor, INC/CP.  
3. Revisión cruzada: Skarlett (formato/norma), Nicolás (hechos API/Selenium), Ari (números JMeter).  
4. Exportar PDF final a carpeta de entregables cuando el equipo la defina.  
5. No inventar resultados: si 5000 VU falló por hardware, decirlo.

### DoD
- [ ] §1–§6 completos  
- [ ] Gráficos insertados  
- [ ] Portada con 4 integrantes + sección  

---

## EV3-24 — Dictamen actualizado

### Objetivo
Sustituir el dictamen EP4 “No certificado” por el veredicto ciclo 3.

### Criterio (el mismo del equipo en EP4, ahora con fixes)

Meta **Certificado con reservas** si:
1. INC-01, INC-02, INC-07 **Verificados**.  
2. P0 de sesión/TLS/cifrado: CP-07 aprobado; CP-14 y CP-16 al menos con plan/limitación explícita si no hay fix total (declarar reservas).  
3. INC-04 e INC-13 fechados/cerrados (dictamen EP4 los pedía en el camino).  
4. Sin críticos abiertos.

Si algún P0 crítico sigue abierto → mantener **No certificado** con lista exacta.

### Pasos

1. Tabla de decisión: INC → evidencia retest → pasa/no.  
2. Redactar sello + 3 reservas (si aplica).  
3. Alinear §6 con las reservas.  
4. Frase legal: obligaciones del centro vs capacidad del software (mismo enfoque EP4).

### DoD
- [ ] Dictamen explícito en §5 o §6  
- [ ] Trazable a evidencias  

---

## EV3-25 — Preparación guion EP6

### Objetivo
Borrador de presentación basado en evidencias **nuevas** (no solo repetir EP4).

### Pasos

1. Estructura sugerida (ajustar a tiempo oficial cuando salga rúbrica EP6):
   - Portada / objetivo  
   - Qué se remedió (INC-01/02/03/04/07/13/14)  
   - Selenium obligatorio (pass rate)  
   - JMeter 5000 (gráfico + honestidad de techo)  
   - Wireshark / TLS  
   - Sonar delta  
   - Dictamen y reservas  
2. Asignar láminas con continuidad de voces EV2:
   - Giannina: marco y dictamen  
   - Nicolás: remediación auth/RBAC + Selenium  
   - Ari: JMeter 5000 + DAST/John  
   - Skarlett: Sonar + TLS/norma  
3. Marcar “clic en captura” solo donde exista archivo en `Evidencias/`.  
4. No escribir guion final hasta tener reportes reales; este item es **plantilla + checklist**.

### DoD
- [ ] Outline EP6 en Markdown/DOCX  
- [ ] Lista de evidencias por lámina  

---

## Ritual de integración (cómo recibir handoffs)

| Cuándo | Qué pedís | Check |
|--------|-----------|-------|
| Tras P0 código | Tabla INC de Nicolás | Paths existen |
| Tras JMeter | Tabla fases + dashboard Ari | G4/G5 armables |
| Tras Sonar/TLS | Tabla normativa Skarlett | §2/§6 |
| Freeze -48 h | “No más cambios de números” | Solo redacción |

Si falta un handoff: sección del informe en *pendiente de evidencia* — no rellenar con supuestos.

---

## Orden recomendado

| Día | Foco |
|-----|------|
| D1–D2 | Plantilla Word EP5 + matriz vacía ciclo 3 + sheet KPIs |
| D3 | Incorporar primeras evidencias (delay, bcrypt) |
| D4 | Gráficos cuando existan Selenium final + JMeter |
| D5 | §5–§6 + dictamen borrador |
| D6 | Revisión cruzada + PDF + outline EP6 |

---

## Handoff checklist (entrada)

- [ ] Nicolás: bitácora + Selenium report + INC auth  
- [ ] Ari: JMeter 5000 + John + headers/ZAP  
- [ ] Skarlett: Sonar delta + CP-14/16/17/18 + tabla norma  
- [ ] Rúbrica oficial (cuando llegue): diff contra este BACKLOG → issues `EV3-Rxx`
