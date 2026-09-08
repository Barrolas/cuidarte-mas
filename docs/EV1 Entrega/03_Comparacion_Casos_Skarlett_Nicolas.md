# Comparación de casos: Skarlett (Word) vs Nicolás (Cards)

| Caso | Coincidencia ERS | Skarlett (Word) | Nicolás (paquete) | Decisión de merge |
|------|------------------|-----------------|-------------------|-------------------|
| **CP-01** | RF-1.1 + NFR-SEG-9 | Buena redacción; endpoint genérico (“POST autenticación”) | Misma idea + ruta real `POST /autenticacion/login` + HTTP 200/401 | **Unir:** texto Skarlett + endpoint Nicolás |
| **CP-02** | RF-3.1 + RB-3 | Incluye adjunto PDF en el flujo | Rutas `POST /examenes`, `GET /tipo-examen`, validación | **Unir:** ambos; explicitar API |
| **CP-03** | RF-5.1 + NFR-SEG-6 | Eliminación + auditoría UI | `DELETE /examenes/:id` + `GET /auditoria` | **Unir:** pasos API Nicolás |
| **CP-04** | NFR-SEG-4/5 + RB-1 | Completo a nivel conceptual | Payloads SQLi/XSS + métricas HTTP + control positivo RB-3 | **Preferir Nicolás** (más medible) + estilo Skarlett |
| **CP-05** | NFR-PERF-1 | p95 < 300 ms, 5 min | Igual + aviso `delayMiddleware(5000)` del repo | **Unir:** aviso técnico de Nicolás es crítico |
| **CP-06** | NFR-USAB + COMPAT-2 | Flujo paciente / responsive | Checklist UAT + meta Lighthouse | **Unir** |

## Conclusión comparación

- Misma cobertura de casos (CP-01…CP-06): **alineados**.
- Skarlett gana en **redacción formal** y plantilla institucional.
- Nicolás gana en **trazabilidad técnica al código** (rutas reales, delay artificial, métricas).
- El informe unificado debe quedarse con **Word/maqueta + normativa Skarlett** y **endpoints/avisos Nicolás**.
