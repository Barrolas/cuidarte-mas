# HANDOFF — Skarlett → Ninna (viernes 27-nov-2026)

**De:** Skarlett Tropan  
**Para:** Giannina Guerrero (Ninna)  
**Zona horaria:** America/Santiago (UTC-3)  
**Base de esta rama de docs:** `origin/main` `d5829ed3041642df0714fcb8b65b270364ed5d7a` (el paquete de Ninna **solo está en `main`**, no en `dev`).  
**Código y evidencia EV56-20:** `origin/dev` `5707693e2f7e9826d645800e89792533329e1b99`. EV56-20 se copió desde `origin/dev` **sin modificar** los blobs.

Regla que respeté: no invento números. Toda cifra tiene path y fecha.

Las rutas de abajo son relativas a `docs/Evaluaciones/EV5-6/EV5-6 Entrega/Skarlett/`.

---

## 1. Lo que pediste en el checklist (viernes 27)

### 1.1 Sonar backend/frontend post-fix (capturas + métricas)

**Entregado**, con una reserva explícita.

- Documento: [`Entregables/EV56-18-Retest-CP17-y-Sonar.md`](./Entregables/EV56-18-Retest-CP17-y-Sonar.md)  
- Capturas y JSON: [`Evidencias/EV56-18/`](./Evidencias/EV56-18/README.md)

Corrida del **27-nov-2026 ~22:00 America/Santiago** sobre `origin/dev` `5707693` (ya tiene INC-04, INC-05 e INC-06). Motor: SonarQube Community 26.11.0.134175.

**Este no es el scan final post INC-01, INC-02 e INC-07:** esos merges de Nicolás **aún no están** en `dev` (lo confirmé en el código). Cuando entren, hay que volver a escanear antes de congelar G6 el sábado 28, si alcanzan.

Valores para **G6** (plantilla `Ninna/Planillas/EV56-22-KPIs.md`):

| Métrica | Backend EV2 (20-oct) | Backend EV5-6 (27-nov, `5707693`) | Frontend EV2 (20-oct) | Frontend EV5-6 (27-nov, `5707693`) |
|---------|----------------------|-----------------------------------|------------------------|------------------------------------|
| Bugs | 0 | 0 | 14 | 14 |
| Vulnerabilities | 4 | 2 | 0 | 0 |
| Security Hotspots | 0 | 0 | 0 | 0 |
| Code smells | 2 | 2 | 3 | 3 |
| Security rating | E | E | A | A |
| Fecha | Capturas EV2 Skarlett | 27-nov-2026 ~22:00 America/Santiago | Ídem EV2 | Ídem 27-nov |

Lectura corta: el backend bajó de 4 a 2 vulnerabilidades (salieron las de CORS/Express ligadas a INC-05). Sigue **E** por el secreto en `db.js:6` (BLOCKER) y el límite de `multer` en `documentos.js:13` (MAJOR). El frontend no cambió. Quality Gate Passed en instancia fresca, **sin** condiciones de New Code; eso no certifica seguridad. Cobertura 0,0 % en ambos. Duplicación backend 25,1 % (era 25,8 %); frontend 7,8 %. LoC backend 2165; frontend 7877.

Fuente EV2: `docs/Evaluaciones/EV2/EV2 Contexto/Entregables/capturas-sonar/`.

### 1.2 CP-14 / 16 / 17 / 18 (resultado o limitación fechada)

| Caso | Resultado EV5-6 sugerido | Fecha de la evidencia | Limitación / plan | Path |
|------|--------------------------|----------------------|-------------------|------|
| **CP-17** | **Paso con observaciones** | 27-nov-2026 20:06 America/Santiago (`df6fd24`, mergeado en `5707693`) | INC-06 verificado. Observación: INC-14 (Nicolás) e INC-11 | [`Evidencias/EV56-20/`](./Evidencias/EV56-20/README.md) (intacta). Antes 25-nov: [`Evidencias/EV56-09/`](./Evidencias/EV56-09/README.md) |
| **CP-14** | **Fallido con reserva** | 25-nov-2026 (`dev` `2d0abc7`) | HTTP en `:3333`/`:4444`, sin HSTS; HTTPS error 35; Postgres `ssl=off`. Proxy `:3443` sí hizo TLS+HSTS, pero no está en el compose oficial. **15-dic-2026** | [`Evidencias/EV56-19/`](./Evidencias/EV56-19/README.md) · [`Entregables/EV56-19-CP-14-16-18.md`](./Entregables/EV56-19-CP-14-16-18.md) |
| **CP-16** | **Fallido** | 25-nov-2026 (`2d0abc7`); en `5707693` la ruta sigue en `app.js:63` | Sin `pgcrypto`; `/files/documentos` sin token → 200 (INC-16). **15-dic-2026** | Ídem EV56-19 |
| **CP-18** | **Fallido / Parcial con reserva** | 25-nov-2026 13:04 America/Santiago | `pg_dump` 216 ms / 23.198 B; restore 190 ms (406 ms total); conteos 3/20/0/0/7/3 idénticos. Sin cron, retención 15 años ni copia externa. **20-dic-2026** | Ídem EV56-19 |

CP-14/16/18 no se reejecutaron el 27-nov; lo declaré en el documento. No hay evidencia nueva de **CP-06, CP-20 ni CP-22**: dejar `PENDIENTE_RETEST` / «sin retest en este ciclo».

### 1.3 Tabla normativa artículo ↔ INC/CP

**Entregada:** [`Entregables/EV56-Tabla-Normativa.md`](./Entregables/EV56-Tabla-Normativa.md).

Para pegar en el informe **§2.3**, en el hueco «Pendiente handoff Skarlett».

### 1.4 Diagrama CI/CD con controles de seguridad (borrador OK)

**Entregado**, como **propuesta IE7** (el CI no está automatizado).

- Texto + respuestas al “Qué falta”: [`Planillas/EV56-21-Diagrama-CICD-Controles.md`](./Planillas/EV56-21-Diagrama-CICD-Controles.md)  
- PNG: [`Planillas/EV56-21-Diagrama-CICD-Controles.png`](./Planillas/EV56-21-Diagrama-CICD-Controles.png)  
- YAML de propuesta (no activo, sin secretos en claro): [`Planillas/EV56-21-security.yml`](./Planillas/EV56-21-security.yml)

---

## 2. “Qué falta que complete Skarlett” (borrador EV56-21)

| Pedido | Respuesta |
|--------|-----------|
| Herramientas exactas del equipo | GitHub (`Barrolas/cuidarte-mas`). **No hay** `.github/workflows/` ni runner. Laboratorio: Docker Compose. Sonar, Selenium, ZAP y JMeter se ejecutan **a mano**. |
| Umbrales del Quality Gate que ya usan | Gate **por defecto** (“Sonar way”). Con New Code (25-nov, rama del fix): `new_coverage` ≥ 80 %, `new_duplicated_lines_density` ≤ 3 %, `new_violations` ≤ 0. En instancia fresca (25-nov `dev` y 27-nov `5707693`): `conditions: []` y Passed, aunque el backend esté en E. |
| ¿ZAP va en el pipeline o solo manual? | **Solo manual** (Ari). En la propuesta aparece como paso nocturno opcional. No hay captura de pipeline con ZAP. |
| PNG/SVG para el PPT | PNG en `Planillas/EV56-21-Diagrama-CICD-Controles.png`. |

---

## 3. Sugerencias para la matriz (`Resultado_EV56` + `Evidencia_path`) y el registro

Insumos editables: [`Planillas/EV56-22-Matriz-Trazabilidad-Skarlett.xlsx`](./Planillas/EV56-22-Matriz-Trazabilidad-Skarlett.xlsx) y [`Planillas/EV56-22-Registro-Casos-Skarlett.xlsx`](./Planillas/EV56-22-Registro-Casos-Skarlett.xlsx). Tú actualizas el CSV/Excel oficial.

| Codigo_ERS | Caso | Resultado_EV56 sugerido | Evidencia_path | Estado_EV56 sugerido en el registro |
|------------|------|-------------------------|----------------|--------------------------------------|
| NFR-SEG-1 | CP-14 | Fallido con reserva. HTTP en el lab; proxy autofirmado `:3443` no oficial. Plan 15-dic-2026. | `Skarlett/Evidencias/EV56-19/` | FALLIDO (con reserva fechada) |
| NFR-SEG-3 | CP-16 | Fallido (INC-16). Sin pgcrypto; documentos sin token. Plan 15-dic-2026. | `Skarlett/Evidencias/EV56-19/` | FALLIDO |
| NFR-SEG-6 | CP-17 | Paso con observaciones. INC-06 verificado en `origin/dev`. Pendiente INC-14 e INC-11. | `Skarlett/Evidencias/EV56-20/` | PASO CON OBSERVACIONES |
| NFR-SEG-7 | CP-18 | Fallido / Parcial con reserva. Restore manual OK (216 ms / 190 ms, conteos idénticos). Sin política automática. Plan 20-dic-2026. | `Skarlett/Evidencias/EV56-19/` | FALLIDO / PARCIAL CON RESERVA |
| NFR-USAB-1/2/4, NFR-COMPAT-2 | CP-06 | Sin retest en este ciclo (no hay evidencia nueva). | — | PENDIENTE_RETEST |
| NFR-USAB-3 | CP-20 | Sin retest de usabilidad en UI. El backend ahora responde 500 genéricos (ver CP-17), pero eso no sustituye el caso de usabilidad. | `Skarlett/Evidencias/EV56-20/` solo como contexto de errores | PENDIENTE_RETEST |
| NFR-COMPAT-1 | CP-22 | Sin retest en este ciclo. | — | PENDIENTE_RETEST |

---

## 4. Insumos para el informe

### §2.3 Cumplimiento normativo

Reemplazar «Pendiente handoff Skarlett» por la tabla de [`Entregables/EV56-Tabla-Normativa.md`](./Entregables/EV56-Tabla-Normativa.md).

### §6.2 Residuales (filas que me tocan)

| INC / tema | Impacto | Dueño | Fecha objetivo | Estado que propongo |
|------------|---------|-------|----------------|---------------------|
| INC-06 fuga `err.message` | Grave | Skarlett | — | **Verificado (retest)** — ya no es residual. Path: `Skarlett/Evidencias/EV56-20/` |
| INC-16 cifrado reposo / `/files/documentos` | Grave | Skarlett / backend | 15-dic-2026 | Residual / reserva. Path: `Skarlett/Evidencias/EV56-19/` |
| CP-14 TLS laboratorio | P0 config | Equipo / DevOps | 15-dic-2026 | Fallido con reserva. Path: `Skarlett/Evidencias/EV56-19/` |
| CP-18 backup automático y 15 años | P1 | DBA / infra | 20-dic-2026 | Fallido / Parcial con reserva. Path: `Skarlett/Evidencias/EV56-19/` |

Detalle y otras filas de apoyo (INC-11, cobertura 0 %, secreto en `db.js`): [`Entregables/EV56-Plan-Mantenimiento.md`](./Entregables/EV56-Plan-Mantenimiento.md).

### §6.3 Mantenimiento y CI/CD

Sustituir el flujo borrador por el de [`Planillas/EV56-21-Diagrama-CICD-Controles.md`](./Planillas/EV56-21-Diagrama-CICD-Controles.md) e insertar el PNG. Dejar explícito que **hoy no hay CI automatizado**.

### Inventario INC-06

Pasar de Abierto a **Verificado (retest)**. Severidad **Grave** (como en tu inventario; no «Moderado»). Evidencia: `Skarlett/Evidencias/EV56-20/`.

---

## 5. Guion (láminas 9 y 10)

Frases listas, en español hablado, con tiempos: [`Guion/EV56-25-Guion-Skarlett.md`](./Guion/EV56-25-Guion-Skarlett.md).

---

## 6. Qué queda pendiente (no lo cierro yo)

1. **Re-scan Sonar** cuando Nicolás mergee **INC-01, INC-02 e INC-07**, y actualizar G6 si eso ocurre antes del congelamiento del sábado 28.  
2. Retest y bitácoras de Nicolás (INC-01, 02, 03, 07, 14; Selenium; SQLMap) y de Ari (JMeter 5000, ZAP, John post-bcrypt).  
3. CP-06, CP-20 y CP-22 sin evidencia nueva.  
4. Activar o no el `security.yml` (decisión de equipo; yo no hice push).  
5. Wireshark de CP-14, si el equipo lo considera complemento (no está en este paquete).

No hice push de esta rama. El commit de docs queda para que el equipo lo suba cuando corresponda.
