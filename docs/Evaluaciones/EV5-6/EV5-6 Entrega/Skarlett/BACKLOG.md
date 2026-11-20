# BACKLOG — Skarlett Tropan (EV5-6)

**Rol:** SAST (SonarQube), errores/logs (CP-17), configuración TLS/backup, lectura normativa, apoyo diagrama CI/CD con controles de seguridad.  
**Tablero:** [`../00_Backlog_Equipo.md`](../00_Backlog_Equipo.md)  
**Análisis:** [`../00_Analisis_Encargo_Final.md`](../00_Analisis_Encargo_Final.md)

Estándares: **25010**, **27001**, Leyes **19.628**, **20.584**, **DS 41**.

---

## Checklist

- [ ] EV56-09 INC-06 sin fuga de errores  
- [ ] EV56-20 CP-17 retest  
- [ ] EV56-18 Sonar post-fix  
- [ ] EV56-19 CP-14 / 16 / 18  
- [ ] EV56-21 Diagrama CI/CD + controles (con Ninna)  
- [ ] Tabla normativa → estado  
- [ ] Handoff a Ninna  

---

## EV56-09 — INC-06 no exponer `err.message`

1. Inventario de `catch` / `glosa: err.message` en routers.  
2. Log interno en servidor; respuesta al cliente genérica en 500.  
3. Priorizar auth, documentos, auditoría, roles.  
4. Coordinar merges con Nicolás el mismo día.  
5. Guardar sample diff / captura.

**DoD:** catch críticos sin fuga; lista de archivos en bitácora.

---

## EV56-20 — Retest CP-17

1. Tras EV56-09, provocar error controlado en laboratorio.  
2. Verificar cuerpo HTTP sin SQL/stack/`err.message`.  
3. 401/403 genéricos.  
4. Si no hay 500 reproducible: declarar limitación + evidencia de código/grep.  
5. Actualizar veredicto CP-17.

**DoD:** bitácora ciclo final + cruce INC-06.

---

## EV56-18 — SonarQube post-mitigación

1. Analizar cuando P0/P1 relevantes estén en la branch.  
2. Capturar Quality Gate, bugs, vulnerabilidades, security rating BE/FE.  
3. Tabla delta vs Sonar EV2 (20-oct).  
4. Recordar: Quality Gate Passed ≠ producto seguro (mismo matiz EP4).

**DoD:** capturas + tabla delta para §5/§6.

---

## EV56-19 — CP-14 TLS / CP-16 reposo / CP-18 backup

### TLS (CP-14)
1. Intento TLS en Docker (cert autofirmado) **o**  
2. Wireshark HTTP en claro + limitación declarada + plan fechado en §6.  
3. No aprobar CP-14 sin TLS real.

### Reposo (CP-16) y backup (CP-18)
1. Retestar o documentar residual.  
2. Propuestas §6 con dueño/fecha si no hay fix completo.

**DoD:** resultado explícito por CP.

---

## EV56-21 — Diagrama CI/CD con controles de seguridad (IE3)

1. Con Ninna, dibujar pipeline (build → test → SAST/DAST → deploy lab).  
2. Marcar controles: Sonar, Selenium, ZAP, secretos en env, no deploy si Quality Gate falla (aunque sea aspiracional).  
3. Alinear con criterios normativos (acceso, registro, criptografía).  
4. Entregar figura lista para el informe.

**DoD:** diagrama claro + leyenda de controles.

---

## Tabla normativa (handoff clave)

Completar y pasar a Ninna:

| Hallazgo / INC | Evidencia ciclo final | Control 27001 / 25010 | Deber legal | Estado post-fix |
|----------------|----------------------|------------------------|-------------|------------------|
| INC-01 | John (Ari) + bcrypt (Nico) | Autenticación | 19.628 art. 11 | |
| INC-02 | Grep JWT | Secretos | 19.628 / 20.584 | |
| INC-06 | CP-17 | Logging seguro | 19.628 art. 11 | |
| INC-07 | Postman Nico | Control de acceso | 20.584 art. 13 | |
| CP-14 | Wireshark/TLS | Cifrado tránsito | DS 41 art. 8 | |
| Sonar | EV56-18 | SAST | DS 41 / 19.628 | |

---

## Handoff a Ninna

1. Tabla normativa.  
2. Estados CP-14, 16, 17, 18.  
3. Delta Sonar.  
4. Diagrama CI/CD.  
5. Recomendaciones §6 residuales con fecha.

---

## Orden sugerido

| Bloque | Foco |
|--------|------|
| 1 | EV56-09 |
| 2 | EV56-20 |
| 3 | EV56-19 |
| 4 | EV56-18 (cuando haya merges) |
| 5 | EV56-21 + handoff |
