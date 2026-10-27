# Paquete Ari Araya — QA de seguridad y rendimiento (EP3)

Material para integrar en el informe EP3 y para que **Nicolás** complete §5.2 / Tablas 21 y 22.

**No codear el producto.** Documentar ejecución, criticidad y evidencias.

## Orden de lectura

1. [`HANDOFF_PARA_NICOLAS.md`](./HANDOFF_PARA_NICOLAS.md) — filas listas para la bitácora 5.2  
2. [`Bitacora_Ejecucion.md`](./Bitacora_Ejecucion.md) — detalle por caso  
3. [`CP-21_Disponibilidad.md`](./CP-21_Disponibilidad.md) — caso que faltaba ejecutar (solo Docker)  
4. [`03_4_Entorno_y_Herramientas.md`](./03_4_Entorno_y_Herramientas.md) — pegar/adaptar en §3.4  
5. [`05_3_Criticidad_Incidentes.md`](./05_3_Criticidad_Incidentes.md) — §5.3 + decisión INC-09 Grave  

## Casos a cargo de Ari

| Caso | Estado en este paquete |
|------|------------------------|
| CP-04 | Parcial: baseline ZAP EV1 + SQLMap de Nicolás. ZAP autenticado / Burp / Nikto ciclo 2: no ejecutado |
| CP-05 | Falla con delay (JMeter EV1). Sin delay: no ejecutado |
| CP-13 (tiempo) | No ejecutado (formatos: Nicolás) |
| CP-15 | Falla (código + dump; John no aplica si no hay hash) |
| CP-17 | Confirmado por código (`glosa`); Burp ciclo 2: no ejecutado |
| CP-19 | No ejecutado |
| CP-21 | **Ejecutado** (revisión Docker, 2026-10-26) → Falla documental |

## Capturas / anexo ciclo 2

- ZAP GUI (sep 2026): rama `feature/owasp-zap-ataque` y anexos EV1 en `docs/Evaluaciones/EV1/EV1 Entrega/Anexos/`  
- JMeter EV1: `docs/Evaluaciones/EV1/EV1 Entrega/Anexos/jmeter/`  
- CP-21: evidencia documental en `Evidencias/CP-21/` (agregar captura de `docker compose ps` cuando Docker esté up)

## Cuentas (dump)

`admin`/`admin` · `medico`/`medico` · `paciente`/`paciente`

Si el login dice que no existe `usuarios`, el dump no cargó (`init-db.sh` con CRLF). Ver nota en la bitácora.
