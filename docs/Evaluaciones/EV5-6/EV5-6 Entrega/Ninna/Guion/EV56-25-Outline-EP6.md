# Outline guion EP6 — defensa (~10 min + 5 preguntas)

**Fecha objetivo grabación:** domingo 29-11-2026  
**Guion cerrado:** sábado 28-11-2026  
**Estado:** outline (sin frases finales hasta congelar números)

Cada persona ~2–2,5 min. Cualquiera debe poder explicar cualquier lámina (nota individual).

---

## Mapa de láminas

| # | Lámina | Quién habla | Evidencia mínima | IE rúbrica |
|---|--------|-------------|------------------|------------|
| 1 | Portada · Caso B Cuidarte+ | Ninna | Logo / puertos Docker | — |
| 2 | Del dictamen EV2 “No certificado” al ciclo MITIGAR | Ninna | Inventario INC | IE9 |
| 3 | Estrategia por riesgo + cadena requisito→INC→retest→dictamen | Ninna | Matriz 40 | IE9 / trazabilidad |
| 4 | Mitigaciones auth: INC-01 bcrypt, INC-02 JWT, INC-03 logout | Nicolás | Before/after + Postman | IE1 |
| 5 | RBAC: INC-07 `/roles` + IDOR paciente | Nicolás | curl 401/403/2xx | IE1 |
| 6 | Selenium obligatorio: pass rate post-fix | Nicolás | report.html/json | IE5 |
| 7 | INC-04 delay + JMeter ramp a 5000 VU | Ari | EV56-04 + jtl | IE1 / perf |
| 8 | ZAP / John / fuerza bruta (lo que exista) | Ari | Reportes | IE1 |
| 9 | Sonar delta + errores INC-06 + norma | Skarlett | Capturas Sonar | IE1 / IE3 |
| 10 | Diagrama CI/CD con controles de seguridad | Skarlett (+ Ninna) | Diagrama | IE3 |
| 11 | KPIs G1–G6 (1 lámina resumen) | Ninna | Gráficos | IE9 |
| 12 | Dictamen + reservas + mantenimiento | Ninna | §6 | IE7 |
| 13 | Preguntas | Todos | — | — |

Si falta evidencia, **quitar la lámina** o marcarla “plan §6”; no mostrar capturas inventadas.

---

## Bloque Ninna (texto guía, no memorizar literal)

1. **Contexto:** Cuidarte+ maneja datos clínicos; por eso calidad, seguridad y norma se prueban juntas (25010 + 27001 + 20.584/DS 41/19.628).  
2. **EV2:** 40/40 en diseño; dictamen No certificado por críticos/graves.  
3. **Este ciclo:** mitigar ≥5 INC (≥1 crítico), Selenium, JMeter 5000, retest.  
4. **Trazabilidad:** cada requisito de la matriz tiene Resultado EV2 y Resultado EV5-6.  
5. **Dictamen:** se lee solo al final, alineado a INC-01 y P0 verificados.

## Preguntas probables (ensayar)

- ¿Por qué no certifican si el delay ya bajó a 30 ms? → Porque INC-01 crítico sigue abierto.  
- ¿Qué es Certificado con reservas? → P0 cerrados + limitaciones explícitas (TLS lab, techo HW).  
- ¿Dónde está la evidencia del requisito NFR-SEG-2? → Matriz → CP-15/CP-01 → INC-01 → path John.  
- ¿Qué hace Selenium en el pipeline? → Regresión UI post-merge; no reemplaza DAST/SAST.

---

## Checklist de ensayo (domingo AM)

- [ ] Cronómetro ≤ 10 min  
- [ ] Cada voz tiene 1 captura real  
- [ ] Números iguales a §5 del informe  
- [ ] Lista de reservas igual al dictamen  
