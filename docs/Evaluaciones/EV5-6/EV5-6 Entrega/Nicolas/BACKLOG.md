# BACKLOG — Nicolás Barra (EV5-6)

**Rol:** Auth, sesión JWT, RBAC, auditoría, Selenium obligatorio, SQLMap, Wireshark sesión.  
**Tablero:** [`../00_Backlog_Equipo.md`](../00_Backlog_Equipo.md)  
**Análisis:** [`../00_Analisis_Encargo_Final.md`](../00_Analisis_Encargo_Final.md)  
**Suite base:** `docs/Evaluaciones/EV3/EV3 Entrega/Nicolas/selenium_suite/` · branch `feature/nicolas-ev3`

Estándares: ISO/IEC **25010**, **27001** (secretos/acceso/registro), **29119**; Leyes **20.584**, **19.628**, **DS 41**.

---

## Checklist

- [ ] EV56-00 Baseline  
- [ ] EV56-01 INC-01 bcrypt  
- [ ] EV56-02 INC-02 JWT env  
- [ ] EV56-03 INC-03 logout revoca  
- [ ] EV56-05 INC-07 `/roles`  
- [ ] EV56-06 INC-14 POST auditoría  
- [ ] EV56-07 INC-13 descarga auditada  
- [ ] EV56-11 Selenium post-mitigación  
- [ ] EV56-12 SQLMap retest  
- [ ] EV56-16 Wireshark sesión  
- [ ] Apoyo EV56-10 lockout (si toca código)  
- [ ] Handoff a Ninna  

---

## EV56-00 — Baseline

1. `git fetch` y trabajar en tu branch de remediación (p.ej. `feature/nicolas-ev3`).  
2. `docker compose up -d --build` → FE `:3333` / API `:4444`.  
3. Smoke login con seeds actuales; anotar si la clave sigue en texto plano.  
4. Guardar 2–3 capturas “antes” (login OK, token post-logout si aún falla, `/roles` sin auth si aplica).  
5. Abrir bitácora personal (crear `Bitacora_Ejecucion.md` en esta carpeta).

**DoD:** ambiente usable + evidencias pre-fix referenciadas en bitácora.

---

## EV56-01 — INC-01 bcrypt (crítico)

1. Localizar login/registro/seeds en `BACKEND` (`auth.js`, usuarios).  
2. Hash con bcrypt (cost ≥10) al crear/actualizar; `compare` en login.  
3. Rechazar claves &lt; 12 caracteres.  
4. Migrar seeds (hashes); documentar claves de laboratorio en bitácora de equipo (no en README público).  
5. Evidencia Postman: login 200, login inválido 401, valor en DB no legible.  
6. Avisar a **Ari** (John EV56-14).

**DoD:** INC-01 *Verificado*; norma 19.628 art. 11 citada en bitácora.

---

## EV56-02 — INC-02 JWT solo env

1. Buscar secreto hardcodeado / README.  
2. Usar `process.env.JWT_SECRET`; fallar si falta.  
3. `.env.example` + `.env` en `.gitignore`; rotar valor.  
4. Actualizar compose/env del contenedor.  
5. Evidencia: grep limpio + login OK.

**DoD:** sin secreto real en git.

---

## EV56-03 — INC-03 logout revoca token

1. Endpoint logout + denylist (jti/hash) hasta `exp`.  
2. Middleware auth consulta denylist.  
3. FE limpia storage al cerrar sesión.  
4. Retest CP-07: token guardado → logout → `GET /examenes` → **401**.  
5. Evidencias antes/después.

**DoD:** UI + API coherentes; caso Selenium alineado (EV56-11).

---

## EV56-05 — INC-07 proteger `/roles`

1. Middleware JWT + rol admin en mutaciones de roles.  
2. Postman: sin token 401; médico 403; admin 2xx.  
3. Evidencias `EV56-05-*.png`.

**DoD:** matriz negativa/positiva archivada.

---

## EV56-06 — INC-14 restringir POST auditoría

1. Quitar POST público o limitar a admin / solo escritura interna.  
2. Retest: médico + POST inventado → 401/403 (no 201).

**DoD:** 201 arbitrario eliminado.

---

## EV56-07 — INC-13 auditar descargas

1. En handler de descarga, registrar evento (p.ej. `DOCUMENTOS_DESCARGAR`).  
2. Descargar PDF de prueba → `GET /auditoria` muestra el evento.  
3. Evidencias UI + API.

**DoD:** evento reproducible sin romper RBAC paciente.

---

## EV56-11 — Selenium obligatorio (post-mitigación)

1. Usar/actualizar suite en EV3 o copiar a esta carpeta `selenium_suite/`.  
2. Mantener casos AUTH/RBAC/PAC/EXA/RES.  
3. Añadir/ajustar: logout-revocado, RBAC roles, humo tres roles post-bcrypt.  
4. Ejecutar headless; archivar `report.html`, `report.json`, capturas, log.  
5. Anotar pass rate y duración para Ninna (KPI).

**DoD:** suite verde o fallos residuales documentados; HTML autocontenido.

Comando típico:

```powershell
cd "...\selenium_suite"
.\.venv\Scripts\Activate.ps1
$env:SELENIUM_HEADLESS="1"
pytest -v --html=..\..\Evidencias\Selenium\EV56-11-report.html --self-contained-html
```

(Ajusta la ruta de evidencias a donde el equipo las guarde.)

---

## EV56-12 — SQLMap retest

1. Solo contra login de laboratorio Docker.  
2. Guardar output completo.  
3. Conclusión: injectable / no; payloads manuales si aplica.

**DoD:** log + párrafo para §5 del informe.

---

## EV56-16 — Wireshark sesión

1. Capturar loopback/puertos 3333–4444.  
2. Reproducir login + una API con Bearer.  
3. Si no hay TLS: anotar tráfico en claro (apoyo CP-14).  
4. Exportar `.pcapng` + PNG (redactar secretos en lo publicado).

**DoD:** anexo usable en defensa.

---

## Apoyo EV56-10 (lockout)

Si Ari define la prueba de fuerza bruta y hace falta código (rate-limit / bloqueo temporal):

1. Acordar umbral (p.ej. N fallos → 429/bloqueo).  
2. Implementar en auth.  
3. Retest conjunto con Ari.

---

## Handoff a Ninna

Entregar:

1. Bitácora con fechas y paths.  
2. Tabla INC: ID · estado · evidencia · CP.  
3. Números Selenium (total/passed/failed/duración).  
4. Texto corto §5.2 de tus CP.  
5. Una frase de remediación por INC cerrado para §6.

---

## Orden sugerido

| Bloque | Foco |
|--------|------|
| 1 | EV56-00 + 02 + 01 |
| 2 | EV56-03 + 05 + 06 |
| 3 | EV56-07 + 16 |
| 4 | EV56-11 + 12 |
| 5 | Handoff + buffer flaky |
