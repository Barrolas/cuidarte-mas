# 00 — Análisis del encargo EP5 (EV3) — Cuidarte+

**Asignatura:** ISY1102 Seguridad y calidad en el desarrollo de software  
**Sección:** 001V  
**Integrantes:** Ari Araya · Nicolás Barra · Giannina Guerrero · Skarlett Tropan  
**Fuentes:**  
- [`../EV3 Contexto/EP5_ISY1102_Estudiante_Formato_Informe.pdf`](../EV3%20Contexto/EP5_ISY1102_Estudiante_Formato_Informe.pdf) (rúbrica / formato **preliminar**)  
- [`../EV3 Contexto/Guia-Unificada-Seguridad-y-Calidad.pdf`](../EV3%20Contexto/Guia-Unificada-Seguridad-y-Calidad.pdf)  
- Dictamen y hallazgos EV2 (EP3/EP4): **No certificado** (INC-01, INC-02, INC-07 + P0 fallidos)

> **Nota:** la rúbrica oficial se entregará próximamente. No debería diferir mucho; se espera más detalle sobre logs, métricas y evidencias. Donde el formato preliminar no precise un artefacto, este análisis deja **reserva explícita** marcada como *pendiente rúbrica oficial*.

---

## 1. Qué pide el encargo (lectura del formato)

El entregable EP5 es un **informe de seguridad y calidad** con esta estructura:

| § | Título | Qué debe demostrar el equipo |
|---|--------|------------------------------|
| 1 | Introducción | Contexto Cuidarte+, propósito del plan, estructura del informe |
| 2 | Criterios de calidad | Usabilidad, rendimiento, estabilidad, confiabilidad, mantenibilidad; seguridad (datos, acceso, errores, integridad); normativas |
| 3 | Plan de pruebas | Estrategia, tipos, criterios de aceptación, herramientas y recursos |
| 4 | Diseño de casos | Fichas CP (ID, req, descripción, precondiciones, pasos, esperado, aceptación, datos) |
| 5 | Ejecución | Resumen, detalle caso a caso, criticidad de incidentes |
| 6 | Propuesta de mejora | Remediación concreta por defecto (ID, impacto, propuesta) |

EP6 (presentación) se apoya en este informe y en evidencias nuevas del ciclo 3; su guion se prepara **después** de tener retest.

---

## 2. Delta respecto de EV2 (lo que cambia el trabajo)

| Dimensión | EV2 (EP3/EP4) | EV3 (EP5/EP6) |
|-----------|---------------|---------------|
| Objetivo | Detectar, evidenciar, dictaminar | **Aplicar** remediaciones del dictamen + **retest** |
| Dictamen de partida | No certificado | Meta: **Certificado con reservas** (si se cierran P0 acordados) |
| Selenium | Suite profesional (plus) | **Obligatorio** |
| JMeter | ~70 VU; delay 5 s (INC-04) | **5000 usuarios concurrentes** (tras quitar delay) |
| Tráfico de red | No formalizado | **Wireshark** donde aporte evidencia |
| Informe | Tablas + capturas | Tablas + capturas + **gráficos y KPIs** |
| Código | En general no se “arreglaba” en el ciclo de prueba | **Sí se remedia** en branch, luego se retestea |

---

## 3. Alcance de remediación (acordado)

### 3.1 Prioridad P0 (código + retest)

| INC | Defecto EV2 | Remediación esperada | Dueño primario |
|-----|-------------|----------------------|----------------|
| INC-01 | Contraseñas en texto plano | bcrypt + política ≥12 | Nicolás (código) / Ari (John retest) |
| INC-02 | Secreto JWT en repo | Solo env; rotar; limpiar README | Nicolás |
| INC-03 | Logout no revoca JWT | Endpoint logout + invalidación | Nicolás |
| INC-04 | `delayMiddleware(5000)` | Eliminar delay artificial | Ari |
| INC-07 | `/roles` sin token | JWT + rol admin | Nicolás |
| INC-13 | Descarga sin auditoría | Evento de descarga en `auditoria` | Nicolás |
| INC-14 | `POST /auditoria` abierto | Restringir a admin / política clara | Nicolás |

### 3.2 Prioridad P1 (hardening viable en Docker)

| INC / CP | Acción | Dueño |
|----------|--------|-------|
| INC-05 | CORS acotado + cabeceras de seguridad | Ari (código/verificación) / Skarlett (lectura norma) |
| INC-06 | No exponer `err.message` al cliente | Skarlett (código/revisión) / Nicolás si toca rutas compartidas |
| CP-14 | Intento TLS o evidencia Wireshark HTTP en claro + limitación declarada | Skarlett |
| CP-16 | Cifrado en reposo si es viable; si no, plan fechado | Skarlett |

### 3.3 Prioridad P2 (no bloquean el primer cierre del informe)

INC-09, INC-10, INC-11, INC-15, INC-16, INC-17 y afines: quedan en backlog con dueño; se documentan en §6 como pendientes con fecha.

---

## 4. Mapa a estándares (qué citar y dónde)

| Estándar / norma | Uso en el informe | Sección típica |
|------------------|-------------------|----------------|
| ISO/IEC **25010** | Características de calidad del producto (seguridad, desempeño, fiabilidad, usabilidad, mantenibilidad) | §2, criterios de aceptación §3.3 |
| ISO/IEC **27001** (enfoque controles) | Gestión de secretos, acceso, registro, criptografía | §2 seguridad, §6 remediación |
| ISO/IEC/IEEE **29119** | Proceso y documentación de pruebas | §3–§5 |
| Ley **20.584** | Acceso a ficha clínica / roles | Dictamen, INC-07, RBAC |
| Ley **19.628** | Deber de cuidado de datos personales | INC-01, secretos, errores |
| **DS 41** | Seguridad de la ficha clínica (transmisión, integridad, auditoría) | TLS, auditoría, respaldos |
| Ley **21.719** | Horizonte (vigencia dic-2026); no sustituye 20.584/DS 41 hoy | §2 / dictamen |

**Regla de oro (guía unificada):** no intercambiar 25010 (producto) con 27001 (SGSI). En el texto: *25010 mide el producto; 27001 orienta controles de información*.

---

## 5. Herramientas obligatorias y de apoyo

| Herramienta | Obligatoriedad ciclo 3 | Para qué | Evidencia mínima |
|-------------|------------------------|----------|------------------|
| **Selenium** (pytest + POM) | Obligatoria | Regresión UI post-remediación | `report.html`, `report.json`, capturas, log |
| **JMeter** | Obligatoria (5000 VU) | Concurrencia / estrés | `.jmx`, `.jtl`, dashboard HTML, gráficos KPI |
| **Wireshark** | Requerida donde aporte | Tráfico login/API/TLS | `.pcapng` + capturas anotadas |
| Postman / curl | Apoyo | API, RBAC, auditoría | Colección + PNG/JSON |
| SQLMap | Apoyo (retest) | Inyección login | Output + conclusión |
| OWASP ZAP | Apoyo | DAST autenticado | Reporte / capturas |
| John the Ripper | Apoyo | Retest INC-01 | Output post-bcrypt |
| SonarQube | Apoyo | SAST post-fix | Resumen backend/frontend |
| Docker | Base | FE :3333 / API :4444 | `compose` up estable |

*Pendiente rúbrica oficial:* lista exacta de logs de aplicación, métricas de contenedor y formato de anexos.

---

## 6. KPIs y gráficos mínimos (§5.1)

1. **Resultado de CP** — barras: Aprobado / Parcial / Fallido / No ejecutado (EV2 vs EV3).  
2. **Incidentes** — abiertos vs cerrados por severidad (Crítico / Grave / Moderado / Leve).  
3. **Selenium** — pass rate %, duración total, flaky count.  
4. **JMeter 5000** — avg, p90, p95, error %, throughput; línea del umbral 300 ms (NFR-PERF-1).  
5. **Sonar** — vulnerabilidades / bugs / rating seguridad antes vs después.  
6. **Cobertura de remediación P0** — checklist % INC cerrados con retest.

---

## 7. Continuidad de roles (igual criterio EV2)

| Integrante | Continuidad temática | Entregables ciclo 3 |
|------------|----------------------|---------------------|
| **Nicolás** | Auth, sesión, RBAC, auditoría, documentos, Selenium, SQLMap | Código P0 auth/RBAC/audit + suite Selenium + Wireshark sesión + bitácora |
| **Ari** | DAST, rendimiento, hashes, headers | INC-04 + JMeter 5000 + ZAP/John/curl + Wireshark carga + KPIs perf |
| **Skarlett** | SAST, config, TLS, errores, norma técnica | Sonar post-fix + CP-14/16/17/18 + tabla norma→estado |
| **Giannina** | Matriz, norma, dictamen, integración informe | Matriz 40 ERS + informe §1–6 con gráficos + dictamen + prep EP6 |

Detalle operativo: [`00_Backlog_Equipo.md`](./00_Backlog_Equipo.md) y `*/BACKLOG.md` de cada integrante.

---

## 8. Criterios de entrada / salida del ciclo 3

### Entrada
- Ambiente Docker reproducible.  
- Branch de remediación acordada (`feature/ev3-remediacion` o equivalente).  
- Baseline EV2 disponible (informe, bitácoras, suite Selenium 11/11).  
- Formato EP5 preliminar leído por el equipo.

### Salida (Definition of Done del ciclo documentación+retest)
- INC P0 con estado *Corregido* o *Verificado* y evidencia de retest.  
- Suite Selenium obligatoria ejecutada y archivada.  
- Corrida JMeter con intento documentado a **5000** VU (y ramp previo).  
- Al menos una evidencia Wireshark pertinente (sesión y/o carga y/o TLS).  
- Informe EP5 con §1–6, KPIs/gráficos y §6 de remediaciones hechas/pendientes.  
- *Pendiente rúbrica oficial:* anexar lo que la rúbrica formal exija de más (logs/métricas).

---

## 9. Riesgos y mitigaciones

| Riesgo | Impacto | Mitigación |
|--------|---------|------------|
| Hardware no sostiene 5000 VU | No cumplir literalmente el requisito | Ramp 100→5000; documentar techo; evidencia del intento a 5000; corrida estable al máximo alcanzable |
| Rúbrica oficial llega tarde | Retrabajo de anexos | Reservar carpetas `Evidencias/Logs` y métricas desde el día 1 |
| Remediación rompe UI | Selenium flaky | Baseline → fix → retest; no merge a main sin verde |
| TLS real en Docker local | CP-14 incompleto | Autofirmado o Wireshark HTTP + limitación declarada en §6 |
| Alcance creep (cerrar todos los INC) | No llegar a EP5 | P2 explícito; no bloquea dictamen “con reservas” |

---

## 10. Índice de carpeta EV3 Entrega

```
EV3 Entrega/
  00_Analisis_Encargo_EP5.md          ← este archivo
  00_Backlog_Equipo.md
  Nicolas/BACKLOG.md
  Ari/BACKLOG.md
  Skarlett/BACKLOG.md
  Giannina/BACKLOG.md
  Evidencias/
    Selenium/  JMeter/  Wireshark/  Sonar/  Postman/  Logs/
```

Siguiente lectura operativa: [`00_Backlog_Equipo.md`](./00_Backlog_Equipo.md).
