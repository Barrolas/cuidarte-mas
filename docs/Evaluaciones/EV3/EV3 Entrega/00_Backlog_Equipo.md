# 00 — Backlog de equipo EV3 / EP5

Tablero único. El detalle paso a paso está en el `BACKLOG.md` de cada integrante.

**Branch de trabajo:** `feature/ev3-remediacion`  
**Ambiente:** Docker FE `http://localhost:3333` · API `http://localhost:4444`  
**Análisis:** [`00_Analisis_Encargo_EP5.md`](./00_Analisis_Encargo_EP5.md)

Estados: `Pendiente` · `En curso` · `Bloqueado` · `Hecho` · `Verificado (retest)`

---

## 1. Épicas

| ID | Épica | Objetivo |
|----|-------|----------|
| E0 | Baseline y entorno | Docker + branch + baseline Selenium/Postman |
| E1 | Remediación P0 | Cerrar INC-01, 02, 03, 04, 07, 13, 14 |
| E2 | Hardening P1 | INC-05, 06 + intento TLS/CP-16 |
| E3 | Retest automatizado | Selenium obligatorio + SQLMap |
| E4 | Carga 5000 VU | JMeter escalonado hasta 5000 |
| E5 | Evidencia de red | Wireshark (sesión + carga ± TLS) |
| E6 | SAST y config | Sonar post-fix + CP-14/16/17/18 |
| E7 | Informe y dictamen | Matriz, KPIs, §1–6, prep EP6 |

---

## 2. Items del backlog (vista equipo)

| ID | Título | Prioridad | Dueño | Depende de | DoD (resumen) | Estado |
|----|--------|-----------|-------|------------|---------------|--------|
| EV3-00 | Branch + Docker + baseline | P0 | Todos (coord. Nicolás) | — | Branch creada; compose up; Selenium baseline archivada | Pendiente |
| EV3-01 | INC-01 bcrypt + política clave | P0 | Nicolás | EV3-00 | Login con hash; seeds migrados; Postman OK/401 | Pendiente |
| EV3-02 | INC-02 secreto JWT solo env | P0 | Nicolás | EV3-00 | Sin secreto en README/código; `.env.example` | Pendiente |
| EV3-03 | INC-03 logout revoca token | P0 | Nicolás | EV3-02 | Post-logout GET API → 401 | Pendiente |
| EV3-04 | INC-04 quitar delay 5 s | P0 | Ari | EV3-00 | Sin `delayMiddleware(5000)`; humo <1 s | Pendiente |
| EV3-05 | INC-07 `/roles` con JWT+admin | P0 | Nicolás | EV3-02 | Sin token 401; médico 403; admin 2xx | Pendiente |
| EV3-06 | INC-14 restringir POST auditoría | P0 | Nicolás | EV3-02 | Médico no crea auditoría arbitraria | Pendiente |
| EV3-07 | INC-13 auditar descargas | P0 | Nicolás | EV3-00 | Evento descarga visible en GET `/auditoria` | Pendiente |
| EV3-08 | INC-05 CORS + headers | P1 | Ari | EV3-00 | curl muestra headers; CORS no `*` abierto | Pendiente |
| EV3-09 | INC-06 sin fuga `err.message` | P1 | Skarlett | EV3-00 | catch genéricos; evidencia curl | Pendiente |
| EV3-10 | Suite Selenium obligatoria + extensión | P0 | Nicolás | EV3-01…07 | report.html/json; casos logout/RBAC/audit | Pendiente |
| EV3-11 | SQLMap retest login | P1 | Nicolás | EV3-01 | Output + conclusión (inyección / no) | Pendiente |
| EV3-12 | JMeter ramp → 5000 VU | P0 | Ari | EV3-04 | `.jtl` + dashboard + intento 5000 documentado | Pendiente |
| EV3-13 | John retest CP-15 | P0 | Ari | EV3-01 | Hashes cargan / no texto plano | Pendiente |
| EV3-14 | ZAP autenticado retest | P1 | Ari | EV3-08 | Capturas/reporte; 0 High objetivo | Pendiente |
| EV3-15 | Wireshark sesión (login/API) | P0 | Nicolás | EV3-00 | `.pcapng` + PNG anotada | Pendiente |
| EV3-16 | Wireshark bajo carga | P1 | Ari | EV3-12 | Captura durante stress + notas | Pendiente |
| EV3-17 | SonarQube post-fix | P0 | Skarlett | EV3-01…09 | Capturas BE/FE + métricas | Pendiente |
| EV3-18 | CP-14 TLS / Wireshark HTTP | P1 | Skarlett | EV3-00 | Intento TLS o limitación + pcap | Pendiente |
| EV3-19 | CP-16 / CP-18 retest o plan | P1 | Skarlett | EV3-00 | Resultado o plan fechado en §6 | Pendiente |
| EV3-20 | CP-17 retest mensajes error | P0 | Skarlett | EV3-09 | Bitácora + evidencia | Pendiente |
| EV3-21 | Matriz 40 ERS ciclo 3 | P0 | Giannina | EV3-10,12,17 | Matriz actualizada | Pendiente |
| EV3-22 | KPIs y gráficos §5.1 | P0 | Giannina | handoffs | 6 gráficos mínimos del análisis | Pendiente |
| EV3-23 | Informe EP5 §1–6 | P0 | Giannina | EV3-21,22 | Word/PDF según formato | Pendiente |
| EV3-24 | Dictamen actualizado | P0 | Giannina | EV3-23 | Meta: Certificado con reservas | Pendiente |
| EV3-25 | Prep guion EP6 | P1 | Giannina | EV3-24 | Borrador guion + evidencias clave | Pendiente |

---

## 3. Dependencias (orden de ejecución)

```text
EV3-00 Baseline
   ├─► EV3-04 Delay ──► EV3-12 JMeter 5000 ──► EV3-16 Wireshark carga
   ├─► EV3-01 bcrypt ─┬─► EV3-13 John
   │                  └─► EV3-11 SQLMap
   ├─► EV3-02 JWT ──► EV3-03 Logout ──┐
   │              └─► EV3-05 /roles ──┼─► EV3-10 Selenium ──► handoff Giannina
   │              └─► EV3-06 Audit POST┘
   ├─► EV3-07 Audit download ─────────┘
   ├─► EV3-08 Headers ──► EV3-14 ZAP
   ├─► EV3-09 Errores ──► EV3-20 CP-17
   ├─► EV3-15 Wireshark sesión
   └─► EV3-18 TLS · EV3-19 CP-16/18
            └─► EV3-17 Sonar ──► EV3-21…25 Informe
```

**Regla:** no empezar JMeter 5000 sin EV3-04. No cerrar Selenium “post-fix” sin EV3-01…07 en *Hecho*.

---

## 4. Definition of Done transversal (cualquier item de código)

1. Cambio en branch `feature/ev3-remediacion` (no direct a `main`).  
2. Evidencia de fallo **antes** (si aplica, referenciar EV2) y de éxito **después**.  
3. Archivos en `Evidencias/<herramienta>/` con prefijo `EV3-<ID>-`.  
4. Fila actualizada en bitácora del dueño.  
5. Ping a Giannina cuando el item pase a *Verificado (retest)*.  
6. Alineación explícita a 25010 / 27001 / ley cuando el item sea de seguridad (una línea en bitácora basta).

---

## 5. Handoffs hacia el informe

| Desde | Hacia Giannina | Artefacto |
|-------|----------------|-----------|
| Nicolás | §5.2 CP funcionales/API + Selenium + INC auth | `Nicolas/Bitacora_Ejecucion.md` + evidencias |
| Ari | §5.1 KPIs perf + CP-04/05/15 | `Ari/Bitacora_Ejecucion.md` + JMeter/ZAP |
| Skarlett | §2/§6 norma + Sonar + CP-14/16/17/18 | `Skarlett/Bitacora_Ejecucion.md` + tabla norma |
| Todos | §5.3 criticidad | Lista INC cerrado/abierto unificada |

---

## 6. Playbooks por persona

- [Nicolás](./Nicolas/BACKLOG.md)  
- [Ari](./Ari/BACKLOG.md)  
- [Skarlett](./Skarlett/BACKLOG.md)  
- [Giannina](./Giannina/BACKLOG.md)  

---

## 7. Pendiente rúbrica oficial

Cuando llegue la rúbrica formal, actualizar este tablero con filas `EV3-Rxx` (logs, métricas de contenedor, anexos obligatorios) **sin borrar** lo ya hecho; solo ampliar DoD.
