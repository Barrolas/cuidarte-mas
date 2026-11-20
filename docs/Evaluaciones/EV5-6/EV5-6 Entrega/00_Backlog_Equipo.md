# 00 — Backlog de equipo EV5-6 (examen final)

Tablero único. El detalle paso a paso está en el `BACKLOG.md` de cada integrante.

**Análisis:** [`00_Analisis_Encargo_Final.md`](./00_Analisis_Encargo_Final.md)  
**Ambiente:** Docker FE `http://localhost:3333` · API `http://localhost:4444`  
**Branches de trabajo:** p.ej. `feature/nicolas-ev3` (Nicolás); coordinar branch común de remediación si el equipo lo define.

Estados: `Pendiente` · `En curso` · `Bloqueado` · `Hecho` · `Verificado (retest)`

---

## 1. Épicas

| ID | Épica | Objetivo |
|----|-------|----------|
| E0 | Baseline | Docker + evidencias “antes” |
| E1 | Mitigación mínima (≥5) | INC-01, 02, 03, 04, 07 |
| E2 | Mitigación ampliada | INC-13, 14, 05, 06 + lockout |
| E3 | Automatización UI | Selenium obligatorio + reportes |
| E4 | Estrés 5000 VU | JMeter escalonado |
| E5 | Seguridad dinámica/estática | ZAP, SQLMap, Sonar, John, Wireshark |
| E6 | Documentación y defensa | Planillas, informe, dictamen, guion/PPT/video |

---

## 2. Items EV56 (vista equipo)

| ID | Título | Prioridad | Dueño | Depende de | DoD (resumen) |
|----|--------|-----------|-------|------------|---------------|
| EV56-00 | Baseline Docker + capturas pre-fix | P0 | Todos (coord. Nicolás) | — | Ambiente up; evidencias “antes” de INC clave |
| EV56-01 | INC-01 bcrypt + política clave | P0 | Nicolás | EV56-00 | Login con hash; DB sin texto plano |
| EV56-02 | INC-02 JWT solo env | P0 | Nicolás | EV56-00 | Sin secreto en repo; login OK |
| EV56-03 | INC-03 logout revoca token | P0 | Nicolás | EV56-02 | Post-logout API → 401 |
| EV56-04 | INC-04 quitar delay 5 s | P0 | Ari | EV56-00 | Timing ≪ 5 s |
| EV56-05 | INC-07 `/roles` JWT+admin | P0 | Nicolás | EV56-02 | 401/403/2xx según rol |
| EV56-06 | INC-14 restringir POST auditoría | P1 | Nicolás | EV56-02 | Médico no crea auditoría arbitraria |
| EV56-07 | INC-13 auditar descargas | P1 | Nicolás | EV56-00 | Evento descarga en auditoría |
| EV56-08 | INC-05 CORS + headers | P1 | Ari | EV56-00 | Headers presentes; CORS acotado |
| EV56-09 | INC-06 sin fuga err.message | P1 | Skarlett | EV56-00 | Respuestas 500 genéricas |
| EV56-10 | Lockout / anti fuerza bruta | P1 | Ari (+ Nico código) | EV56-01 | Evidencia before/after intentos |
| EV56-11 | Suite Selenium post-mitigación | P0 | Nicolás | EV56-01…05 | report.html/json + capturas |
| EV56-12 | SQLMap retest login | P0 | Nicolás | EV56-01 | Output + conclusión |
| EV56-13 | JMeter ramp → 5000 VU | P0 | Ari | EV56-04 | `.jtl` + dashboard + intento 5000 |
| EV56-14 | John retest CP-15 | P0 | Ari | EV56-01 | Hashes bcrypt / no plain |
| EV56-15 | ZAP autenticado before/after | P0 | Ari | EV56-08 | Reporte + ≥1 hallazgo mitigado |
| EV56-16 | Wireshark sesión | P1 | Nicolás | EV56-00 | `.pcapng` + PNG anotada |
| EV56-17 | Wireshark bajo carga | P1 | Ari | EV56-13 | Captura durante stress |
| EV56-18 | SonarQube post-fix | P0 | Skarlett | EV56-01…09 | Capturas + delta EV2 |
| EV56-19 | TLS/config CP-14/16/18 | P1 | Skarlett | EV56-00 | Resultado o limitación + plan |
| EV56-20 | CP-17 retest errores | P0 | Skarlett | EV56-09 | Bitácora + evidencia |
| EV56-21 | Diagrama CI/CD + controles seguridad | P0 | Skarlett + Ninna | — | Diagrama en informe (IE3) |
| EV56-22 | Planillas CP + métricas + matriz | P0 | Ninna (insumos todos) | handoffs | Excel llenos |
| EV56-23 | Informe EP5 §1–6 + KPIs | P0 | Ninna | EV56-11,13,18,22 | Word/PDF formato docente |
| EV56-24 | Dictamen post-mitigación | P0 | Ninna | EV56-23 | Meta: Certificado con reservas |
| EV56-25 | Guion + PPT + video defensa | P1 | Ninna (voces todos) | EV56-24 | Material EP6 |

---

## 3. Dependencias

```text
EV56-00 Baseline
  ├─ EV56-04 Delay ──► EV56-13 JMeter 5000 ──► EV56-17 Wireshark carga
  ├─ EV56-01 bcrypt ─┬─► EV56-14 John
  │                  ├─► EV56-12 SQLMap
  │                  └─► EV56-10 Lockout
  ├─ EV56-02 JWT ──► EV56-03 Logout ─┐
  │              ├─► EV56-05 /roles ─┼─► EV56-11 Selenium ──► Ninna
  │              └─► EV56-06 Audit ──┘
  ├─ EV56-07 Download audit ─────────┘
  ├─ EV56-08 Headers ──► EV56-15 ZAP
  ├─ EV56-09 Errores ──► EV56-20 CP-17
  ├─ EV56-16 Wireshark sesión
  └─ EV56-18 Sonar / EV56-19 TLS ──► EV56-21…25 Informe y defensa
```

**Regla:** no JMeter 5000 sin EV56-04. No Selenium “cierre” sin mitigación mínima 01–05 en *Hecho/Verificado*.

---

## 4. DoD transversal (cualquier ítem operativo)

1. Evidencia **antes** (si aplica) y **después**.  
2. Bitácora personal actualizada.  
3. Ping a Ninna con paths de evidencia + estado INC/CP.  
4. Una línea de norma/estándar (25010 / 27001 / ley) cuando sea de seguridad.  
5. No merge a `main` hasta retest acordado por el equipo.

---

## 5. Playbooks

- [Nicolás](./Nicolas/BACKLOG.md)  
- [Ari](./Ari/BACKLOG.md)  
- [Skarlett](./Skarlett/BACKLOG.md)  
- [Ninna](./Ninna/BACKLOG.md)  
