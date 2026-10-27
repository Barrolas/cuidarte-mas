# Revisión cruzada — §3.4 y §5.3

**Revisora:** Skarlett Tropan  
**Fecha:** 27 de octubre de 2026  
**Documento revisado:** `docs/Evaluaciones/EV2/EV2 Contexto/Entregables/EP3-Informe-Cuidarte-Mas-avance.docx` (secciones 3.4 y 5.3)  
**Contraste:** rama `origin/feature/ari-ep3-qa-seguridad` (`785062d`), bitácora de Nicolás en `main`, ejecución de Skarlett del 20 de octubre y código de `main`.

La escala de la Tabla 25 se sostiene. El bloqueo de estas dos secciones es de actualización: §3.4 describe el plan, y §5.3 deja los resultados en «Pendiente» aunque ya hay ejecución.

## §3.4 Herramientas y entorno

Lo que puede quedar como está: el retiro de Jest y k6, los tres servicios de Compose (frontend `:3333`, API `:4444`, Postgres `:15442`), SonarQube en CP-16 y CP-17, y la limitación de que todo corre en Docker local.

Correcciones para Giannina antes del PDF:

| Dónde | Texto actual | Corrección |
|-------|----------------|------------|
| Tabla 9, datos de prueba | Cuentas `admin.qa`, `medico.qa`, `paciente.qa` | El dump tiene `admin`/`admin`, `medico`/`medico` y `paciente`/`paciente` (`BACKEND/sql/dump-cuidarteplus.sql`). Nicolás y Ari usaron esas tres. |
| Tabla 9, navegadores | Chrome, Firefox y Edge, dos últimas versiones; móvil 375 px | CP-22 (20 oct): Chrome 155.0.8059.81 y Edge 155.0.4283.45. Firefox y Safari no estaban instalados: bloqueado, no aprobado. La ventana móvil medida fue de 390 px. |
| Tabla 7, Selenium | CP-01, 02, 08 a 12 y 22 | Esos casos se ejecutaron a mano o con Postman. El smoke de Selenium no tiene salida. CP-22 no usó Selenium. |
| Tabla 7, Burp y Nikto | Burp en CP-04 y CP-17; Nikto en CP-04 y CP-14 | El 26 oct Ari no abrió esas herramientas. El mismo criterio se probó con Swagger Authorize y `curl.exe -i` / `-I`. Hay que decir el equivalente en la tabla, no dejar el nombre del plan como si se hubiera ejecutado. |
| Tabla 7, Lighthouse | CP-06 y CP-19 | Lighthouse se usó en el login (CP-06, accesibilidad 0,96). CP-19 no se ejecutó. |
| Tabla 7, JMeter | CP-05, CP-13 y CP-19 | El 26 oct se rehizo CP-05 con delay (220 muestras, promedio 2965 ms, máximo 5016 ms). Sin delay, el tiempo de descarga (CP-13) y los 200 usuarios (CP-19) siguen no ejecutados. |
| Párrafo de entorno, TLS | Las verificaciones de producción se informan con la limitación del despliegue | CP-14 ya tiene resultado: Fallido. nginx escucha el puerto 80, no hay certificado y PostgreSQL está con `ssl=off`. No dejarlo como «no se evalúa». |

El párrafo de Ari sobre contenedores `healthy` el 26 de octubre puede pegarse en Recursos técnicos. Su nota de `init-db.sh` con finales de línea Windows explica un bloqueo de ambiente (`relation "usuarios" does not exist`). Ese día el login respondió 200, así que no aplica a los resultados ya registrados.

## §5.3 Criticidad

En el Word ya quedaron escritos los resultados de INC-06, INC-11, INC-12, INC-14 e INC-16, que son los de los casos de Skarlett. INC-14 e INC-16 pasaron a Grave. El resto de la Tabla 26 sigue en «Pendiente». Abajo va la severidad que esta revisión sostiene para todos. Ari propone subir INC-09, y el informe ya lo tiene en Grave: ahí no hay cambio.

| ID | Severidad que sostengo | Resultado para la columna | Comentario a Ari |
|----|------------------------|---------------------------|------------------|
| INC-01 | Crítico | Confirmado. CP-15 (26 oct): columna `contrasena` en texto; John no cargó hashes. CP-16: la misma columna `text`. | De acuerdo. Mientras siga abierto, el dictamen es No certificado. |
| INC-02 | Grave | Confirmado en código. Fallback `"inseguro"` en siete rutas. Compose usa además `your-secret-key-change-in-production`. SonarQube no marcó el fallback; sí marcó la contraseña de Postgres en `db.js` (Blocker), ya leída en §5.4. | De acuerdo con Grave. Completar la frase con el fallback del Compose. |
| INC-03 | Grave | Confirmado. CP-07 (Nicolás, 20 oct): el JWT sigue en 200 después del logout. Ari midió vigencia de 2 h. | De acuerdo. |
| INC-04 | Grave | Confirmado con el retraso de 5 s (JMeter 26 oct y la línea base de la EV1). Sin delay: no ejecutado. | De acuerdo. No cerrar la parte sin delay. |
| INC-05 | Moderado | Confirmado en cabeceras (curl 26 oct y CP-14 sin HSTS). ZAP autenticado: 0 High. El límite de intentos de login no se probó. | De acuerdo. No afirmar el límite de login. |
| INC-06 | Moderado | Confirmado en código (34 `catch` con `glosa: err.message`). El CP-20 no lo cubre: el 401 del login es genérico. El 500 de `POST /documentos` no tiene el cuerpo archivado. | De acuerdo con no darlo por cerrado en el cable. La severidad Moderado calza: el mensaje interno sale cuando ya hay un 500. |
| INC-07 | Grave | Confirmado por lectura de `roles.js`. No está en la bitácora de Nicolás. | La frase del informe se queda corta. POST, GET, PUT y DELETE no exigen token: el usuario se lee solo para la auditoría, con `authUser?.nombreUsuario`. |
| INC-08 | Moderado | Confirmado por lectura de `FRONTEND/src/context/AuthContext.jsx` (`localStorage`). SonarQube no lo marcó (0 vulnerabilidades en el frontend). | Ari dejó esta fila en blanco. Se mantiene Moderado. |
| INC-09 | Grave | Confirmado en código: `DELETE FROM usuarios` (`users.js`) y `DELETE FROM examen_medico` (`examenes.js`, con rol admin). Nicolás no lo registró en CP-08 ni en CP-11. | De acuerdo con Grave por la conservación de la ficha (Ley 20.584 art. 13 y DS 41). Observación aparte: el DELETE de usuarios borra antes de mirar el token. Si se ejecuta, el impacto de este incidente sube. |
| INC-10 | Moderado | Parcial. El registro exige 6 caracteres (`FRONTEND/src/validations/auth.js`); el ERS pide 12. La semilla `admin`/`admin` ya está dentro de INC-01. | No subir INC-10 a Grave. Eso cuenta dos veces la misma semilla. |
| INC-11 | Grave | No ejecutado. SonarQube omitió dependencias y en este equipo no hay `npm`. | No bajarlo a Moderado sin la tabla del audit (cuántas altas, críticas y si son de producción). |
| INC-12 | Moderado | No confirmado. CP-06: 0 documentos de prueba; el código descarga el archivo. | De acuerdo con dejar la severidad propuesta y el resultado en no confirmado. |
| INC-13 | Grave | Confirmado. CP-03 (Nicolás): hay `DOCUMENTOS_CREAR` y no hay evento de descarga. | De acuerdo. |
| INC-14 | Grave | Confirmado. CP-03 (Nicolás): médico `POST /auditoria` → 201. El GET sí exige admin. | Sube de Moderado a Grave. Un registro clínico que cualquiera con sesión puede escribir no es un endurecimiento menor (DS 41 art. 9). |
| INC-15 | Moderado | Confirmado. CP-13 (Nicolás): DOCX y PPTX no entran. | Sube de Leve a Moderado. El ERS pide esos formatos; no es un defecto de texto. |
| INC-16 | Grave | Confirmado. CP-16: sin `pgcrypto`, documento en `bytea`, y un archivo de prueba en `/files/documentos` respondió 200 sin token. Se borró al terminar. CP-13 (Nicolás) coincide en el almacenamiento. | Sube de Moderado a Grave por la ruta pública. El `bytea` sin cifrado sigue siendo el hallazgo de CP-16. |
| INC-17 | Moderado | Falla documental de CP-21 (Ari, 26 oct). No está en la Tabla 26. | Agregar la fila. No reabrir un BUG-001 para el mismo hecho. |

Controles que sí respondieron el 26 de octubre y deben verse en §5.2, no como incidentes: sin token, 401; paciente sobre recurso ajeno, 403; médico en sus rutas, 200.

Dictamen, alineado con el párrafo que ya está bajo la Tabla 26: con INC-01 abierto el resultado es **No certificado**.

## Texto breve para el informe

En §3.4, después de la Tabla 7: la ejecución del 26 de octubre usó ZAP 2.17 autenticado, John en Docker, JMeter 5.5 en Docker y `curl` como equivalente de Burp y de Nikto. Selenium no tiene salida de ejecución. Lighthouse cubre el CP-06 y no el CP-19.

En §5.3, reemplazar el pendiente de Ari por: la severidad final es la de la tabla de esta revisión. INC-14 e INC-16 pasan a Grave, INC-15 pasa a Moderado, INC-10 se mantiene en Moderado e INC-11 se mantiene en Grave hasta adjuntar el `npm audit`. Se agrega INC-17 (Moderado, CP-21).
