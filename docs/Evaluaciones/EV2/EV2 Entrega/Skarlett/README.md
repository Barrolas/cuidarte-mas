# Paquete EP3 — Skarlett Tropan

CP-06, CP-14, CP-16, CP-18, CP-20 y CP-22 ya están en la Tabla 24. Este paquete cierra lo que faltaba: CP-17, la revisión cruzada de §3.4 y §5.3, y el repaso de formato del informe.

**Caso:** gestión de log y manejo de errores sin fuga de información.  
**ERS:** NFR-SEG-6.  
**Resultado:** Fallido.  
**Fecha de cierre:** 27 de octubre de 2026.

## De dónde sale cada dato

En `origin` no hay una rama `dev`. El código de desarrollo que se revisó es el de `main` (`BACKEND/` y `FRONTEND/`).

| Fuente | Qué aporta a CP-17 |
|--------|--------------------|
| `main` — matriz `02-Matriz-trazabilidad-40-ERS.docx` | Ficha: SonarQube, Burp Suite y revisión manual. Responsables: Skarlett y Ari. Incidentes previstos: INC-06 e INC-14. |
| `main` — informe `Entregables/EP3-Informe-Cuidarte-Mas-avance.docx` §5.4 | SonarQube del 20 de octubre de 2026. La Tabla 24 deja CP-17 en «[Pendiente]». |
| `main` — `Entregables/capturas-sonar/` | Paneles Backend y Frontend (Community Build 26.10.0.133078, modo MQR). |
| `main` — `BACKEND/src` y `FRONTEND/src` | Revisión manual de logs, `catch` y `POST /auditoria`. |
| `main` — `EV2 Entrega/Nicolas/Bitacora_Ejecucion.md` | INC-14 ya ejecutado el 20 de octubre: médico `POST /auditoria` → 201. |
| `origin/feature/ari-ep3-qa-seguridad` (`785062d`) | Parte dinámica del 26 de octubre. Burp se sustituyó por Swagger Authorize y `curl.exe -i`. |

## Lectura

1. [`CP-17_Gestion_Log_y_Errores.md`](./CP-17_Gestion_Log_y_Errores.md) — ficha, evidencia y texto para pegar en el informe.
2. [`Bitacora_Ejecucion.md`](./Bitacora_Ejecucion.md) — fila para las tablas 21, 22 y 24.
3. [`Revision_Cruzada_3.4_y_5.3.md`](./Revision_Cruzada_3.4_y_5.3.md) — revisión de las secciones de Ari, con la severidad final y el texto para pegar.
4. [`Revision_Formato_Informe.md`](./Revision_Formato_Informe.md) — fuente, pendientes y qué falta para exportar el PDF.

El Word `EP3-Informe-Cuidarte-Mas-avance.docx` ya tiene la fila de CP-17 en Fallido, el párrafo de la sección 5, los resultados de INC-06, INC-11, INC-12, INC-14 e INC-16, y las capturas de Skarlett en el Anexo B. Siguen pendientes las filas de Nicolás, Ari y Giannina. INC-11 no se baja de Grave hasta adjuntar el `npm audit`.
