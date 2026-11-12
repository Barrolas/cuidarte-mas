# BACKLOG — Skarlett Tropan (EV3 / EP5)

**Continuidad EV2:** SonarQube (SAST), configuración (TLS, cifrado, respaldos), CP-17 (errores/logs), lectura normativa de hallazgos.  
**Tablero:** [`../00_Backlog_Equipo.md`](../00_Backlog_Equipo.md)  
**Evidencias:** [`../Evidencias/Sonar`](../Evidencias/Sonar), [`Wireshark`](../Evidencias/Wireshark), [`Logs`](../Evidencias/Logs)

Estándares: **ISO/IEC 25010** (seguridad, mantenibilidad), **27001** (controles de config/criptografía/registro), Ley **19.628** art. 11, **DS 41** arts. 8–9 y 11–12, **20.584** donde aplique acceso.

---

## Checklist rápido

- [ ] EV3-09 INC-06 sin fuga de errores  
- [ ] EV3-20 CP-17 retest  
- [ ] EV3-17 Sonar post-fix  
- [ ] EV3-18 CP-14 TLS / Wireshark HTTP  
- [ ] EV3-19 CP-16 / CP-18  
- [ ] Tabla norma → estado  
- [ ] Handoff a Giannina  

---

## EV3-09 — INC-06 No exponer `err.message` al cliente

### Objetivo
Los `catch` no deben devolver mensajes internos de BD/stack al cliente (falla CP-17 en EV2).

### Pasos

1. Inventario: buscar en backend `glosa: err.message`, `err.message`, `console.error(err)` en routers.
2. Patrón de remediación:
   - Log completo **solo** en servidor (`console.error` o logger).
   - Respuesta al cliente: mensaje genérico (`"Error interno"`) + código 500.
   - No filtrar detalles en JSON de respuesta.
3. Priorizar las 8 rutas / ~34 catch reportados en EV2; cerrar al menos los de documentos, auth, auditoría, roles.
4. Coordinar con Nicolás si él toca los mismos archivos el mismo día (evitar conflictos de merge).
5. Evidencia de código: diff o captura de un `catch` corregido → `Evidencias/Logs/EV3-09-catch-sample.diff.txt`.

### DoD
- [ ] Catch críticos sin `err.message` al cliente  
- [ ] Lista de archivos tocados en bitácora  

---

## EV3-20 — Retest CP-17 (gestión de log y errores)

### Objetivo
Cerrar o actualizar el veredicto de CP-17 con evidencia dinámica + estática.

### Pasos

1. Tras EV3-09, forzar un error controlado en laboratorio (p. ej. payload inválido en `POST /documentos` o ID inexistente que dispare 500 **sin** corromper datos reales de demo).
2. Inspeccionar cuerpo HTTP: **no** debe contener SQL/stack/`err.message` crudo.
3. 401/403: mensajes genéricos (como en EV2 de Ari).
4. Documentar limitación si no se logra un 500 reproducible: la evidencia de código + grep cuenta, pero declararlo (como en EP3).
5. Actualizar ficha CP-17: resultado Aprobado / Parcial / Fallido.
6. Evidencias: `EV3-20-respuesta-error.png`, `EV3-20-grep-catch.txt`.

### DoD
- [ ] Bitácora CP-17 con fecha ciclo 3  
- [ ] Cruce con INC-06 e INC-14 (si aplica)  

---

## EV3-17 — SonarQube post-remediación

### Objetivo
Medir el código **después** de los fixes P0/P1 y comparar con el Sonar del 20-oct (EV2).

### Pasos

1. Esperar a que Nicolás/Ari/tú tengan merges locales en `feature/ev3-remediacion` (al menos P0 auth + delay + errores).
2. Ejecutar análisis Sonar backend y frontend (mismo procedimiento EV2).
3. Capturar:
   - Quality Gate  
   - Bugs / Vulnerabilities / Code smells / Security rating  
   - Nota sobre “código nuevo vs total” (mismo matiz EP4)
4. Guardar en `Evidencias/Sonar/EV3-17-backend.png`, `EV3-17-frontend.png` + export si existe.
5. Tabla comparativa:

| Métrica | EV2 (20-oct) | EV3 (fecha) | Delta |
|---------|--------------|-------------|-------|
| Vulnerabilidades BE | 4 | | |
| Security rating BE | E | | |
| Bugs FE | 14 | | |
| Hotspots | 0 | | |
| Cobertura | 0 % | | |

6. Interpretar: Quality Gate Passed **no** equivale a producto seguro (mensaje ya usado en EP4; reiterar con datos nuevos).

### DoD
- [ ] Capturas + tabla delta  
- [ ] Párrafo para §5 / §6  

---

## EV3-18 — CP-14 TLS + Wireshark

### Objetivo
Evidenciar confidencialidad en tránsito (DS 41 art. 8) o declarar limitación con prueba de HTTP en claro.

### Camino A — Intento TLS en Docker (preferible)

1. Añadir terminación TLS (nginx sidecar / certificados autofirmados mkcert u openssl).
2. Documentar pasos en bitácora (cómo regenerar certs).
3. Probar `https://localhost:...` (aceptar warning de autofirmado).
4. Wireshark: handshake TLS visible; payload no en claro.
5. Evidencias: config snippet + pcap + curl `-k -I`.

### Camino B — Limitación declarada (si A no entra en el sprint)

1. Wireshark en login HTTP: mostrar usuario/token en claro (redactar en informe público).
2. Archivo `EV3-18-http-claro.pcapng` + PNG.
3. §6: plan fechado “habilitar TLS en reverse proxy antes de cualquier exposición no local”.
4. Estado CP-14: **Fallido** o **Parcial** con justificación — no fingir Aprobado.

### DoD
- [ ] A o B completado con evidencia  
- [ ] Texto listo para Giannina  

---

## EV3-19 — CP-16 cifrado en reposo / CP-18 respaldos

### Objetivo
Retestar o planificar lo que EV2 dejó abierto en configuración.

### CP-16

1. Revisar PostgreSQL: ¿`ssl`, cifrado de volumen, datos clínicos en claro en disco?
2. Si no hay cifrado real en el stack estudiantil:
   - Documentar hallazgo residual.
   - Propuesta §6: volumen cifrado / TDE / al menos cifrar documentos sensibles.
3. Si implementan algo mínimo (p. ej. no servir uploads en ruta pública — ligado a INC-16): evidenciar.

### CP-18

1. Probar restore manual del volumen/dump (como EV2 si ya existía).
2. Verificar: ¿hay política de programación, retención, copia externa?  
   - Si no: CP-18 Parcial/Fallido + plan en §6.

### DoD
- [ ] Resultado explícito por CP  
- [ ] Propuestas fechadas si no hay fix completo  

---

## Tabla normativa (entregable clave para §2 / §6)

Completar y pasar a Giannina:

| Hallazgo / INC | Evidencia ciclo 3 | Control orientativo 27001 / 25010 | Deber legal | Estado post-fix |
|----------------|-------------------|-----------------------------------|-------------|------------------|
| INC-01 texto plano | John EV3-13 (Ari) | Autenticación / criptografía | 19.628 art. 11 | |
| INC-02 JWT en repo | Grep Nicolás | Gestión de secretos | 20.584 / 19.628 | |
| INC-06 errores | CP-17 | Logging seguro | 19.628 art. 11 | |
| INC-07 /roles | Postman Nicolás | Control de acceso | 20.584 art. 13 | |
| CP-14 sin TLS | Wireshark | Criptografía en tránsito | DS 41 art. 8 | |
| CP-16 reposo | Revisión config | Criptografía en reposo | DS 41 | |
| Sonar pwd PG en código | Sonar EV3-17 | Secretos en código | 19.628 / DS 41 art. 9 | |
| INC-13 descarga | Nicolás | Registro de eventos | DS 41 | |

---

## Handoff a Giannina

1. Tabla normativa llena.  
2. Estados CP-14, 16, 17, 18.  
3. Delta Sonar EV2→EV3.  
4. Tres recomendaciones §6 con dueño/fecha (TLS, cifrado reposo, backup policy) si siguen abiertas.  
5. Rutas de evidencias Sonar/Wireshark/Logs.

---

## Orden recomendado

| Día | Foco |
|-----|------|
| D1 | EV3-09 catch (en paralelo a auth de Nicolás) |
| D2 | EV3-20 CP-17 evidencia |
| D3 | EV3-18 TLS/Wireshark |
| D4 | EV3-17 Sonar (cuando P0 esté mergeado en la branch) |
| D5 | EV3-19 + tabla normativa + handoff |
