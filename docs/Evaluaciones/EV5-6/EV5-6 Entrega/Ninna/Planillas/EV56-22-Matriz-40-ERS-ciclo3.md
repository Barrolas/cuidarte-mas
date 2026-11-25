# Matriz de trazabilidad 40 ERS — ciclo EV5-6

Fuente EV2: `02-Matriz-trazabilidad-40-ERS.docx` (cierre 27-10-2026).  
Archivo de trabajo: `EV56-22-Matriz-40-ERS-ciclo3.csv`.  
Actualizado: 2026-11-25.

| Código | Caso | Riesgo | Ejecuta | INC | Resultado EV2 (resumen) | Resultado EV5-6 |
|--------|------|--------|---------|-----|-------------------------|-----------------|
| RF-1.1 | CP-01 | P0 | Nicolás | INC-01, INC-02 | Aprobado. Bitácora CP-01 | Pendiente handoff |
| RF-1.2 | CP-07 | P0 | Nicolás | INC-03 | Fallido, INC-03. Bitácora CP-07 | Pendiente handoff |
| RF-2.1 | CP-09 | P2 | Nicolás | INC-10 | Parcial: alta vía administrador; /registro público sin probar. Bitácora CP-09 | Pendiente handoff |
| RF-2.2 | CP-10 | P2 | Nicolás | Ninguno | Parcial: se probó la edición, no el alta del paciente. Bitácora CP-10 | Pendiente handoff |
| RF-2.3 | CP-10 | P2 | Nicolás | Ninguno | Aprobado. Bitácora CP-10 | Pendiente handoff |
| RF-2.4 | CP-10 | P0 | Nicolás | OC-01 | Aprobado. Bitácora CP-10 | Pendiente handoff |
| RF-2.5 | CP-08 | P0 | Nicolás | Ninguno | Aprobado. Bitácora CP-08 | Pendiente handoff |
| RF-2.6 | CP-08 | P0 | Nicolás | INC-07 | Parcial: sin evidencia de edición de rol; INC-07 sin probar. Bitácora CP-08 | Pendiente handoff |
| RF-2.7 | CP-08 | P0 | Nicolás | INC-09 | Parcial: se vio la confirmación; baja lógica sin verificar (INC-09). Bitácora... | Pendiente handoff |
| RF-3.1 | CP-02 | P2 | Nicolás | INC-04 | Aprobado. Bitácora CP-02 | En curso: delay retirado 2026-11-25 (Ari EV56-04, evidenc... |
| RF-3.2 | CP-11 | P2 | Nicolás | Ninguno | Aprobado. Bitácora CP-11 | Pendiente handoff |
| RF-3.3 | CP-11 | P1 | Nicolás | INC-09 | Parcial: el médico no tiene opción de eliminar; INC-09 sin probar. Bitácora C... | Pendiente handoff |
| RF-4.1 | CP-12 | P0 | Nicolás | Ninguno | Aprobado. Bitácora CP-12 | Pendiente handoff |
| RF-4.2 | CP-13 | P0 | Nicolás (flujo) y Ari (tiempo) | INC-12, INC-13 | Parcial: la descarga funciona pero no se audita (INC-13); el tiempo de 10 s n... | Pendiente handoff |
| RF-4.3 | CP-13 | P2 | Nicolás | INC-15 | Fallido, INC-15. Bitácora CP-13 | Pendiente handoff |
| RF-4.4 | CP-13 | P1 | Nicolás | INC-16 | Fallido, INC-16. Bitácora CP-13 y Tabla 24 CP-16 | Pendiente handoff |
| RF-5.1 | CP-03 | P1 | Nicolás | INC-13, INC-14 | Fallido, INC-13 e INC-14. Bitácora CP-03 | Pendiente handoff |
| NFR-SEG-1 | CP-14 | P0 | Skarlett | Ninguno | Fallido. Tabla 24 CP-14 | Pendiente handoff |
| NFR-SEG-2 | CP-15 y CP-01 | P0 | Ari | INC-01, INC-10 | Fallido, INC-01. Contraseñas en texto plano y John the Ripper sin hashes que ... | Pendiente handoff |
| NFR-SEG-3 | CP-16 | P0 | Skarlett | Ninguno | Fallido, INC-16. Tabla 24 CP-16 | Pendiente handoff |
| NFR-SEG-4 | CP-04 y CP-08 | P0 | Ari | INC-07 | Parcial: el paciente recibe 403 al escribir o pedir datos ajenos y el médico ... | Pendiente handoff |
| NFR-SEG-5 | CP-04 | P0 | Ari (ZAP y curl) y Nicolás (SQLMap) | INC-05, INC-08 | Parcial: SQLMap sin inyección y ZAP autenticado sin alertas altas; CORS abier... | Pendiente handoff |
| NFR-SEG-6 | CP-17 | P1 | Skarlett (SonarQube) y Ari | INC-06, INC-14 | Fallido, INC-06 confirmado en el código (34 bloques catch con err.message) e ... | Pendiente handoff |
| NFR-SEG-7 | CP-18 | P1 | Skarlett | Ninguno | Fallido. Tabla 24 CP-18 | Pendiente handoff |
| NFR-SEG-8 | CP-23 (con CP-03 y CP-04) | P0 | Giannina | INC de seguridad | Fallido: DS 41 arts. 8 y 9 y Ley 20.584 art. 13 no se cumplen. Tabla 24 CP-23 | Pendiente handoff |
| NFR-SEG-9 | CP-01 y CP-07 | P0 | Nicolás y Ari | INC-02, INC-03, INC-08 | Fallido, INC-03. Bitácora CP-07 | Pendiente handoff |
| NFR-PERF-1 | CP-05 | P3 | Ari | INC-04 | Fallido, INC-04. Con el retraso las consultas tardan 5 s; sin retraso no se m... | En curso: delay retirado 2026-11-25 (Ari EV56-04, evidenc... |
| NFR-PERF-2 | CP-19 | P3 | Ari (Skarlett apoya con Lighthouse) | Ninguno | Fallido (27 oct 2026, Ari). Lighthouse Performance 43; JMeter CP19_200u.jmx: ... | Pendiente handoff |
| NFR-PERF-3 | CP-19 | P3 | Ari | INC-04 | Fallido (27 oct 2026, Ari). Lighthouse Performance 43; JMeter CP19_200u.jmx: ... | En curso: delay retirado 2026-11-25 (Ari EV56-04, evidenc... |
| NFR-USAB-1 | CP-06 | P4 | Skarlett | Ninguno | Fallido. Tabla 24 CP-06 | Pendiente handoff |
| NFR-USAB-2 | CP-06 | P4 | Skarlett | INC-12 | Parcial: INC-12 no se reejecutó, sin documentos. Tabla 24 CP-06 | Pendiente handoff |
| NFR-USAB-3 | CP-20 | P4 | Skarlett | INC-06 | Fallido. INC-06 no se reprodujo en el login, pero está confirmado en el códig... | Pendiente handoff |
| NFR-USAB-4 | CP-06 | P4 | Skarlett | Ninguno | Fallido. Tabla 24 CP-06 | Pendiente handoff |
| NFR-DIS-1 | CP-21 | P3 | Ari | INC-17 | Fallido, INC-17. Una sola réplica y sin medición del 99,5 %. Tabla 24 CP-21 | Pendiente handoff |
| NFR-DIS-2 | CP-21 | P3 | Ari | INC-17 | Fallido, INC-17. Sin ventana de mantenimiento ni respaldo automático. Tabla 2... | Pendiente handoff |
| NFR-COMPAT-1 | CP-22 | P4 | Skarlett | Ninguno | Parcial: Chrome y Edge aprobados; Firefox y Safari sin probar. Tabla 24 CP-22 | Pendiente handoff |
| NFR-COMPAT-2 | CP-06 | P4 | Skarlett | Ninguno | Fallido. Tabla 24 CP-06 | Pendiente handoff |
| RB-1 | CP-04 | P0 | Ari | Ninguno | Aprobado: con token de paciente las escrituras y los datos ajenos responden 4... | Pendiente handoff |
| RB-2 | CP-08 | P0 | Nicolás | INC-07, OC-01 | Aprobado. Bitácora CP-08 | Pendiente handoff |
| RB-3 | CP-10 y CP-02 | P0 | Nicolás | OC-01 | Aprobado; OC-01 se analiza en la sección 6. Bitácora CP-10 y CP-02 | Pendiente handoff |

## Contadores EV2
- Aprobado: 10 · Parcial: 10 · Fallido: 20 · Sin resultado: 0
- Cobertura de diseño: 40/40

## Nota INC-04
Filas ligadas a CP-05 / INC-04: delay medido AFTER por Ari (2026-11-25). No marcar Verificado formal hasta handoff de cierre de equipo.
