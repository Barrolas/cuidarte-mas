# EV56-18 / EV56-20 — Retest CP-17 y SonarQube

**Responsable:** Skarlett Tropan  
**Ambiente:** solo `localhost` (FE `:3333`, API `:4444`, Postgres `:15442`; SonarQube `:9000`).  
**Ética:** Ley 21.459; usuarios sintéticos de laboratorio; credenciales redactadas en las evidencias.

La carpeta [`../Evidencias/EV56-20/`](../Evidencias/EV56-20/README.md) se conserva **tal cual** (mismo contenido que en `origin/dev`).

---

## A. Retest CP-17 (INC-06)

### A.1 Antes / después del 25-nov-2026

| Prueba | Antes, `dev` `2d0abc7` | Después, `sk/inc-06-errores` `f8e2786` | Log interno |
|--------|------------------------|----------------------------------------|-------------|
| `GET /examenes/abc` (médico) | 500, `glosa` con `invalid input syntax for type bigint` | 500, `glosa`: `"Ocurrió un error interno en el servidor"` | `22P02` en el servidor |
| `POST /documentos` (`examen_medico_id=abc`) | Igual (cierra la captura que faltaba en EV2) | 500 genérico | `22P02` |
| `GET /roles/abc`, `GET /pacientes/abc`, `GET /tipo-examen/abc` | 500 con el mensaje de PostgreSQL | 500 genérico | `22P02` |
| `GET /examenes` sin token | — | 401 `"Token inválido"` | Sin fuga |
| `GET /auditoria` (médico) / `GET /examenes/paciente/999` (paciente) | — | 403 con mensaje de permiso, sin stack | Sin fuga |

Evidencia: [`../Evidencias/EV56-09/`](../Evidencias/EV56-09/README.md).

### A.2 Rama final — 27-nov-2026 20:06 America/Santiago (EV56-20)

**Commit probado:** `df6fd24d22145d3f7eaf5a66e3a1b9130fc1ea6d` (`origin/feature/skarlett-ep3`, ya con INC-04 e INC-05). Ese trabajo quedó mergeado en `origin/dev` `5707693` vía PR #7.

**Veredicto: CP-17 PASA para INC-06** (paso con observaciones).

- 5/5 errores internos → HTTP 500 `{"error":"<acción>","glosa":"Ocurrió un error interno en el servidor"}`, sin SQL ni stack en el cuerpo.
- Duplicado 23505 (`POST /pacientes` con RUT `11111111-1`) → HTTP 400 `"El RUT o email ya existe"`.
- 401/403 genéricos.
- `docker logs`: 5 entradas `invalid input syntax for type bigint`, `code: '22P02'`.
- Tras INC-05: ya no aparece `X-Powered-By`; CORS limitado a `http://localhost:3333`; `X-Content-Type-Options: nosniff`; `X-Frame-Options: DENY`.
- Tras INC-04: las mismas pruebas responden en milisegundos (antes ~5 s).

**Observaciones abiertas (no son INC-06):** INC-14 (Nicolás) e INC-11 (`npm audit`).

---

## B. SonarQube Community 26.11.0.134175

Evidencias: [`../Evidencias/EV56-18/`](../Evidencias/EV56-18/README.md).  
Fuente EV2 (20-oct-2026): `docs/Evaluaciones/EV2/EV2 Contexto/Entregables/capturas-sonar/`.

### B.1 Tabla delta (métricas clásicas pedidas en G6 + contexto)

| Proyecto | Métrica | EV2 (20-oct-2026) | `dev` `2d0abc7` (25-nov) | `origin/dev` `5707693` (27-nov ~22:00 America/Santiago) |
|----------|---------|-------------------|---------------------------|---------------------------------------------------------|
| Backend | Quality Gate | Passed (New Code) | Passed (`OK`, instancia fresca, `conditions: []`) | Passed (`OK`, instancia fresca, `conditions: []`) |
| Backend | Bugs | 0 | 0 | 0 |
| Backend | Vulnerabilities | 4 | 4 | **2** |
| Backend | Security rating | E | E (`5.0`) | E (`5.0`) |
| Backend | Security Hotspots | 0 | 0 | 0 |
| Backend | Code smells | 2 | 2 | 2 |
| Backend | Reliability (issues / rating SQ) | 2 / C | 2 / C (`3.0`) | 2 / C (`3.0`) |
| Backend | Maintainability | 2 / A | 2 / A | 2 / A |
| Backend | Cobertura | 0,0 % (~2,3 k LoC) | 0,0 % (2256 LoC) | 0,0 % (**2165** LoC) |
| Backend | Duplicación | 25,8 % | 25,8 % | **25,1 %** |
| Frontend | Quality Gate | Passed | Passed | Passed |
| Frontend | Bugs | 14 | 14 | 14 |
| Frontend | Vulnerabilities | 0 | 0 | 0 |
| Frontend | Security rating | A | A (`1.0`) | A (`1.0`) |
| Frontend | Security Hotspots | 0 | 0 | 0 |
| Frontend | Code smells | 3 | 3 | 3 |
| Frontend | Reliability (issues / rating SQ) | 17 (14 bugs) / C | 17 / C | 17 / C |
| Frontend | Maintainability | 3 / A | 3 / A | 3 / A |
| Frontend | Cobertura | 0,0 % (~7,9 k LoC) | 0,0 % (7877 LoC) | 0,0 % (7877 LoC) |
| Frontend | Duplicación | 7,8 % | 7,8 % | 7,8 % |

El 27-nov el Quality Gate del frontend y del backend quedó Passed porque la instancia era nueva y **no había periodo de New Code**. Eso no contradice que el backend siga en Security **E**.

### B.2 Qué cambió en el backend el 27-nov (2 vulnerabilidades que quedan)

Tras los merges de **INC-04, INC-05 e INC-06** ya presentes en `5707693`, Sonar dejó de reportar las dos vulnerabilidades de CORS / versión de Express vistas el 25-nov. Permanecen:

1. **BLOCKER** — `BACKEND/src/db.js:6`: secreto de PostgreSQL en el código (regla `secrets:S6698`).
2. **MAJOR** — `BACKEND/src/routes/documentos.js:13`: límite de tamaño de `multer` (regla `javascript:S5693`).

Los 2 code smells siguen siendo `parseInt` en `users.js` (líneas 176 y 331).

Frontend: **sin cambio** respecto de EV2 (14 bugs, 0 vulnerabilidades).

### B.3 Quality Gate observado en ramas con New Code (25-nov, no es el scan de `5707693`)

En `sk/inc-06-errores` (`f8e2786`) el Quality Gate de *New Code* del backend dio **ERROR** con 0 violaciones nuevas, por `new_duplicated_lines_density = 30,56 %` (umbral 3 %). Tras el helper (`46e0f25`) siguió en **ERROR** por dos condiciones: duplicación nueva **16,42 %** y `new_coverage = 0,0 %` (umbral 80 %, 48 líneas nuevas sin tests). Es honesto: la duplicación venía de bloques ya repetidos y no hay pruebas unitarias (cobertura global 0 %).

Umbrales reales del gate por defecto: ver [`../Planillas/EV56-21-Diagrama-CICD-Controles.md`](../Planillas/EV56-21-Diagrama-CICD-Controles.md).

### B.4 El scan “final” sigue pendiente

El análisis del 27-nov sobre `5707693` **no** es el Sonar final del ciclo. En `origin/dev` todavía no están los merges de Nicolás de **INC-01, INC-02 e INC-07** (confirmado en código: comparación de contraseña en claro, fallback de `JWT_SECRET` en 7 rutas, `/roles` sin exigir token). Cuando esos cambios entren a `dev`, hay que volver a escanear backend y frontend, actualizar G6 y estas capturas.

**Lectura para el informe:** un Quality Gate Passed no significa producto seguro. Sonar Community no detectó INC-06 (se demostró con CP-17) ni la lógica de INC-01 / INC-07.
