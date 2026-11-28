# Plan de mantenimiento continuo (IE7 / IE8) — insumo Skarlett

**Responsable:** Skarlett Tropan  
**Uso:** informe §6.2 (residuales con dueño y fecha) y §6.3 (mantenimiento + CI/CD)  
**Corte:** 27-nov-2026, America/Santiago

Este plan no inventa un CI que no existe. El laboratorio actual es Docker Compose local. El pipeline propuesto está en [`../Planillas/EV56-21-Diagrama-CICD-Controles.md`](../Planillas/EV56-21-Diagrama-CICD-Controles.md).

## 1. Tipos de mantenimiento

| Tipo | Acción | Frecuencia propuesta | Evidencia / métrica |
|------|--------|----------------------|---------------------|
| Preventivo | `npm audit` en backend y frontend (INC-11) | Semanal | Salida del audit sin CVE high abiertas, o ticket con fecha |
| Preventivo | Scan SonarQube Community (BE + FE) con el Quality Gate por defecto | Cada PR, cuando exista CI; mientras tanto, al cerrar un INC de código | Capturas + JSON en `Evidencias/EV56-18/` |
| Preventivo | Prueba de restore de `pg_dump` (CP-18) | Mensual | Conteos idénticos; tiempo de restore (hoy 190 ms en lab, 25-nov) |
| Correctivo | Cerrar residuales de la tabla §6.2 con retest | Según fecha objetivo | Path `EV56-` en bitácora |
| Adaptativo | Integrar TLS en el compose/Nginx oficial (CP-14) | 15-dic-2026 | HTTPS + HSTS en `:3333`/`:4444` o equivalente |
| Evolutivo | Subir cobertura unitaria desde el **0,0 %** actual | 30-dic-2026 (meta intermedia, no medida aún) | Columna Coverage de Sonar |
| Evolutivo | Activar el workflow propuesto (`EV56-21-security.yml`) tras revisión del equipo | Próximo ciclo, si el equipo lo aprueba | Presence de `.github/workflows/` |

## 2. Métricas de resiliencia (objetivo, no medidas en producción)

Tratándose de fichas clínicas:

- **RTO** objetivo ≤ 15 minutos (restaurar contenedor y base desde un respaldo). En el laboratorio, el restore manual del 25-nov tardó 190 ms, pero no hay procedimiento automático ni ambiente de producción.
- **RPO** objetivo ≤ 15 minutos. Hoy no hay respaldos incrementales ni copia externa: el RPO real depende de cuándo alguien ejecute un `pg_dump` a mano.
- **MTTR** objetivo ≤ 2 horas para incidentes de laboratorio.
- Alerta a CSIRT en **3 horas** (Ley 21.663 art. 9): exige logs internos útiles. INC-06 ya deja el detalle en el servidor y un mensaje genérico al cliente.
- Conservación de la ficha **15 años** (DS 41 arts. 11 y 12): no cumplido; falta política de retención.

## 3. Residuales con dueño y fecha (insumo §6.2)

| Brecha residual | Caso / INC | Acción comprometida | Responsable | Fecha objetivo | Sustento |
|-----------------|------------|---------------------|-------------|----------------|----------|
| TLS oficial + HSTS + `ssl` en Postgres | CP-14 | Integrar certificado (aunque sea de lab) en Nginx/compose; no dejar el proxy `:3443` como arreglo paralelo | DevOps / equipo | **15-dic-2026** | DS 41 art. 8 |
| Cifrado en reposo y `/files/documentos` sin token | CP-16 / INC-16 | JWT+RBAC en la ruta estática; plan de `pgcrypto` o volumen cifrado | Backend + DBA | **15-dic-2026** | Ley 19.628 art. 11; Ley 20.584 art. 13; DS 41 art. 8 |
| Backup automático, copia externa, retención 15 años | CP-18 | Cron diario de `pg_dump` cifrado, restore mensual y política de retención | DBA / infra | **20-dic-2026** | DS 41 arts. 8, 11 y 12 |
| Secreto de Postgres en `db.js:6` y fallback JWT | Sonar / INC-02 | Quitar secretos del código; solo variables de entorno | Nicolás (INC-02) + quien toque `db.js` | Con el merge de INC-02 (pendiente) | Ley 19.628 art. 11; 27001 A.5.17 |
| Contraseñas en claro | INC-01 | bcrypt + retest John | Nicolás / Ari | Pendiente merge P0 | Ley 19.628 art. 11; Ley 20.584 art. 12 |
| `/roles` abierto | INC-07 | JWT + rol admin y retest 401/403/2xx | Nicolás | Pendiente merge P0 | Ley 20.584 art. 13 |
| `POST /auditoria` abierto | INC-14 | Restringir a sistema/admin (observación de CP-17) | Nicolás | Tras P0 | DS 41 art. 9 |
| Dependencias sin audit formal | INC-11 | `npm audit` en BE y FE | QA / DevOps | **05-dic-2026** | 27001 A.8.8 |
| Cobertura 0,0 % | Sonar EV56-18 | Pruebas unitarias en el gate (hoy el umbral de *New Code* es 80 % y por eso una rama con código nuevo puede fallar el Quality Gate) | Backend / Frontend | **30-dic-2026** | ISO 25010 Mantenibilidad |

**INC-06 no es residual:** quedó verificado el 27-nov y mergeado en `origin/dev`.

## 4. Qué no se retesteó en este paquete

CP-06, CP-20 y CP-22 (usabilidad / compatibilidad, dueña Skarlett en la matriz) **no tienen evidencia nueva** en EV5-6. No se propone un resultado inventado: dejar `PENDIENTE_RETEST` o «sin retest en este ciclo».
