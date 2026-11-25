# Cronograma EV5-6 — hasta domingo 29 (grabación)

**Hoy de referencia:** martes 24 de noviembre de 2026  
**Hito duro:** domingo **29** — ensayo + grabación de la presentación  
**Hito previo:** sábado **28** — **guion cerrado** (el 29 no se inventa texto nuevo)

Tablero: [`00_Backlog_Equipo.md`](./00_Backlog_Equipo.md)  
Análisis: [`00_Analisis_Encargo_Final.md`](./00_Analisis_Encargo_Final.md)

---

## 1. Prioridades

| Prioridad | Qué | Por qué |
|-----------|-----|---------|
| **P0** | Mitigar ≥5 INC con ≥1 crítico (INC-01, 02, 03, 04, 07) | Mínimo del examen |
| **P0** | Selenium post-fix (Nicolás) | Obligatorio |
| **P0** | JMeter → 5000 VU (Ari) | Obligatorio; bloqueado hasta quitar delay |
| **P0** | ZAP + Sonar + SQLMap (evidencias) | Rúbrica IE1 / IE5 |
| **P0** | Informe borrador + **guion listo antes del 29** | Sin guion no graban |
| **P1** | INC-13/14/05/06, lockout, Wireshark, TLS | Calidad extra; si aprieta, después del P0 |
| **P1** | PPT/video pulido | Día 29; guion ya cerrado |

---

## 2. Dependencias entre integrantes

```text
TODOS: baseline Docker
        │
   ┌────┴────────────────────────┐
   │                             │
Nicolás: JWT → bcrypt → logout   Ari: QUITAR DELAY (lo antes posible)
         → /roles                │
   │                             └─► JMeter 100→5000 → Wireshark carga
   │         bcrypt listo ───────► Ari: John + lockout
   │         headers Ari ────────► Ari: ZAP after
   │
Skarlett: errores ──► CP-17     (en paralelo desde día 1)
          Sonar (cuando haya merges P0)
          TLS/limitación + diagrama CI/CD con Ninna
   │
   └─ handoffs ──► Ninna: planillas → informe → dictamen
                              │
                              └─► GUION (listo ≤ sábado 28)
                                  PPT/ensayo domingo 29 → grabación
```

**Reglas duras**

1. Ari **no** corre 5000 VU hasta tener INC-04 (delay) fuera.  
2. Nicolás **no** cierra Selenium “final” hasta INC-01…05 mitigados.  
3. Ninna puede armar esqueleto desde ya; **congela números** solo con handoffs de Selenium + JMeter + Sonar (vie–sáb).

| Integrante | Puede empezar ya | Espera a | Desbloquea a |
|------------|------------------|----------|--------------|
| **Nicolás** | Baseline, JWT, bcrypt, logout, roles, Wireshark sesión | Selenium final tras sus P0 | Ari (John/lockout), Ninna (Selenium) |
| **Ari** | **Quitar delay YA**, headers, ZAP “antes” | bcrypt de Nico para John/lockout; delay para JMeter | Ninna (JMeter/ZAP), Nico (suite estable) |
| **Skarlett** | Errores INC-06, TLS/limitación, borrador diagrama | Merges P0 para Sonar “después” | Ninna (norma/Sonar/diagrama) |
| **Ninna** | Esqueleto informe, planillas, outline guion | Handoffs reales vie–sáb | Equipo el 29 (texto para grabar) |

---

## 3. Calendario día a día (24 → 29)

| Día | Meta del día | Nicolás | Ari | Skarlett | Ninna |
|-----|--------------|---------|-----|----------|-------|
| **Mar 24** | Baseline + arranque P0 | Docker + capturas “antes”; JWT; bcrypt | **Quitar delay**; timing before/after | Inventario `catch`; TLS plan | Esqueleto Word + planillas |
| **Mié 25** | Mitigación mínima cerrada | Logout + `/roles` (+ audit si alcanza) | Headers; ZAP before; ramp JMeter 100–1000 | INC-06 + CP-17 | Meter INC mitigados en planillas |
| **Jue 26** | Pruebas obligatorias | Selenium post-fix + SQLMap | JMeter 2500→**5000**; John; ZAP after | Sonar post-fix | Borrador §5 con huecos |
| **Vie 27** | Handoffs + informe | Wireshark sesión; **handoff final** | Wireshark carga; **handoff KPIs** | Tabla normativa + diagrama; **handoff** | §1–6 casi completo; **outline guion** |
| **Sáb 28** | Congelar + **guion listo** | Buffer flaky Selenium; frases de su parte | Frases JMeter/ZAP | Frases Sonar/norma | Dictamen + **guion completo** por voz |
| **Dom 29** | Ensayo + grabación | Ensaya su bloque | Ensaya su bloque | Ensaya su bloque | PPT final; dirige ensayo; **graban** |

### Hitos de guion / grabación

| Cuándo | Qué |
|--------|-----|
| Vie 27 | Outline del guion (láminas + quién habla) |
| **Sáb 28 EOD** | **Guion cerrado y repartido** |
| Dom 29 AM | Ensayo cronometrado (~10 min + margen preguntas) |
| Dom 29 | Grabación del video |

---

## 4. Orden técnico de desarrollo

1. Baseline (todos)  
2. **En paralelo:** Ari delay · Nico JWT/bcrypt · Skarlett errores  
3. Nico logout + `/roles` → quedan ≥5 INC con el delay  
4. Ari JMeter 5000 · Nico Selenium · Ari ZAP/John · Skarlett Sonar  
5. Si hay tiempo: audit 13/14, lockout, Wireshark, TLS  
6. Ninna planillas → informe → dictamen → **guion** → PPT → video  

---

## 5. Corte de alcance (si el viernes 27 no cierran P0)

**Mantener sí o sí**

- INC-01, 02, 03, 04, 07  
- Selenium + intento JMeter 5000  
- ZAP **o** Sonar (ideal ambos)  
- Informe corto + guion  

**Dejar como reserva / §6 planificado**

- TLS completo  
- INC-13 / 14  
- Lockout perfecto  
- Wireshark de carga  

---

## 6. Checklist de handoff a Ninna (viernes 27)

- [ ] Nicolás: bitácora INC auth + Selenium (pass rate) + SQLMap + path evidencias  
- [ ] Ari: tabla JMeter por fase + ZAP + John + headers (+ fuerza bruta si hubo)  
- [ ] Skarlett: Sonar delta + CP-14/16/17/18 + tabla normativa + diagrama CI/CD  
- [ ] Ninna confirma recepción y congela números el sábado  

---

## 7. Voces sugeridas para el guion (domingo 29)

| Quién | Bloque (~2–2,5 min) |
|-------|---------------------|
| Ninna | Marco, trazabilidad, dictamen |
| Nicolás | Mitigaciones auth/RBAC + Selenium |
| Ari | Delay/JMeter 5000 + ZAP/John |
| Skarlett | Sonar + norma/TLS + mantenimiento |

Backlogs: [Nicolás](./Nicolas/BACKLOG.md) · [Ari](./Ari/BACKLOG.md) · [Skarlett](./Skarlett/BACKLOG.md) · [Ninna](./Ninna/BACKLOG.md)
