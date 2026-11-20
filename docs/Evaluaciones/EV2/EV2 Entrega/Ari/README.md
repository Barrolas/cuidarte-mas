# Paquete Ari Araya — QA de seguridad y rendimiento (EP3)

Handoff **definitivo** para Nicolás (§5.2 / Tablas 21 y 22) y Giannina (informe).  
Ejecución del **26 de octubre de 2026**. **No codear el producto.**

## Orden de lectura

1. [`HANDOFF_PARA_NICOLAS.md`](./HANDOFF_PARA_NICOLAS.md) — filas listas para la bitácora 5.2  
2. [`Bitacora_Ejecucion.md`](./Bitacora_Ejecucion.md) — detalle por caso  
3. [`Evidencias/EV2_Ari_Pruebas_Seguridad_Rendimiento.docx`](./Evidencias/EV2_Ari_Pruebas_Seguridad_Rendimiento.docx) — capturas y tablas del 26-10  
4. [`CP-21_Disponibilidad.md`](./CP-21_Disponibilidad.md) — NFR-DIS-1/2  
5. [`03_4_Entorno_y_Herramientas.md`](./03_4_Entorno_y_Herramientas.md) — pegar/adaptar en §3.4  
6. [`05_3_Criticidad_Incidentes.md`](./05_3_Criticidad_Incidentes.md) — §5.3 + INC-09 Grave  

## Casos a cargo de Ari

| Caso | Estado definitivo |
|------|-------------------|
| CP-04 | **Parcial.** ZAP auth 0 High (sin reporte HTML). Cabeceras **Falla** (INC-05). RBAC/IDOR **Aprobado** (Swagger y PowerShell). SQLMap = Nicolás |
| CP-05 | **Falla** con delay (rehecho 26-10: 220 samples, avg 2965 ms, max 5016 ms). Sin delay: no ejecutado |
| CP-13 (tiempo) | No ejecutado (0 documentos en el dump) |
| CP-15 | **Falla** (psql + John: *No password hashes loaded*) → INC-01 Crítico |
| CP-17 | RBAC/IDOR **Aprobado**. INC-06 (`glosa`) **no demostrado** en el cuerpo del 500 |
| CP-19 | **Falla** (27-10). Lighthouse Performance 43; JMeter 520 muestras, p95 5024 ms, pico 52 hilos |
| CP-21 | **Falla** documental → INC-17. El Word lo dejó [Pendiente]; este markdown **sí** lo cierra |

No bloquean el cierre: reporte ZAP HTML, JMeter sin delay, CP-13 tiempo. Burp y Nikto no se usaron.

## Cuentas (dump)

`admin`/`admin` · `medico`/`medico` · `paciente`/`paciente`

Si el login dice que no existe `usuarios`, el dump no cargó (`init-db.sh` con CRLF). El 26-10 el login respondió 200.
