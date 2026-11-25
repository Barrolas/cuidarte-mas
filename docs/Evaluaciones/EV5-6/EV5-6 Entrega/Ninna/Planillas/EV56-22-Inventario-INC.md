# Inventario de incidentes — ciclo mitigación (EV5-6)

Fuente baseline: informe EP3/EP4 y bitácoras EV2.  
Actualización: **2026-11-25**. No inventar cierres sin evidencia de retest.

Estados: `Abierto` · `En remediación` · `Verificado (retest)` · `Residual / reserva`

---

## 1. Mínimo de examen (P0)

| INC | Severidad | Defecto | Dueño fix | Retest | Estado 2026-11-25 | Evidencia |
|-----|-----------|---------|-----------|--------|-------------------|-----------|
| INC-01 | Crítico | Contraseñas en texto plano | Nicolás (bcrypt) / Ari (John) | CP-15, John, login | Abierto | EV2: hashes.txt / John sin hashes |
| INC-02 | Grave | JWT_SECRET en repo | Nicolás | Login + revisión repo | Abierto | EV2: `.env` / README |
| INC-03 | Grave | Logout no revoca JWT | Nicolás | CP-07 | Abierto | EV2 bitácora CP-07 |
| INC-04 | Grave | `delayMiddleware(5000)` | Ari | Timing API + humo FE; luego JMeter | **En remediación / medido AFTER** | `Ari/Evidencias/EV56-04/` — before ~5,03 s → after ~0,03 s |
| INC-07 | Grave | `/roles` sin JWT+admin | Nicolás | curl/Swagger 401/403/2xx | Abierto | EV2: esperado; parcial en CP-08 |

## 2. Ampliación recomendada

| INC | Severidad | Defecto | Dueño | Estado | Nota |
|-----|-----------|---------|-------|--------|------|
| INC-05 | Moderado/Grave* | CORS abierto + cabeceras | Ari | Abierto | Bloquea ZAP “after” limpio |
| INC-06 | Grave | Fuga `err.message` | Skarlett | Abierto | Confirmado en código EV2 |
| INC-13 | Grave | Descarga sin auditoría | Nicolás | Abierto | CP-03 / RF-4.2 / RF-5.1 |
| INC-14 | Grave | `POST /auditoria` abierto | Nicolás | Abierto | CP-03 |

\*Severidad según Tabla 6.2 EV2; confirmar en §5.3 del informe final.

## 3. Otros INC residuales (P2 / reserva §6)

Documentar en §6 con dueño y fecha; no bloquean el mínimo si el dictamen declara reserva.

| INC | Tema breve | Estado |
|-----|------------|--------|
| INC-09 | Borrado / baja lógica | Abierto |
| INC-10 | Política de clave / registro | Abierto / parcial |
| INC-15 | Rechazo DOC/PPT incompleto o UI | Abierto |
| INC-16 | Documentos en bytea / cifrado reposo | Abierto |
| INC-17 | Disponibilidad / réplica | Abierto |

## 4. Contadores (actualizar el sábado 28)

| Métrica | Valor ahora | Meta salida |
|---------|-------------|-------------|
| INC P0 mínimo (01,02,03,04,07) | 1 en remediación (04); 4 abiertos | ≥5 Verificados |
| Críticos abiertos | 1 (INC-01) | 0 para Certificado con reservas |
| % P0 mitigados con retest | 0 % Verificado (04 medido, falta merge/equipo) | 100 % del mínimo |

## 5. Regla de dictamen (resumen alto valor)

- ≥1 crítico abierto → **No certificado**.  
- P0 cerrados + reservas explícitas (TLS, techo 5000 VU, etc.) → **Certificado con reservas**.  
- El dictamen debe coincidir con la matriz y con §6.
