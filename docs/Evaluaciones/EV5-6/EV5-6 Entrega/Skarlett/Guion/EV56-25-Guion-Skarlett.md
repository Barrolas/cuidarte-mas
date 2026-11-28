# EV56-25 — Guion de Skarlett Tropan (láminas 9 y 10 del outline EP6)

**Alineado a:** [`../Ninna/Guion/EV56-25-Outline-EP6.md`](../../Ninna/Guion/EV56-25-Outline-EP6.md)  
**Grabación objetivo:** domingo 29-nov-2026  
**Duración de esta voz:** ~2:00 a 2:30 minutos (el total del equipo va en ≤ 10 min)  
**Cifras:** corte 27-nov-2026, America/Santiago. Si Nicolás mergea INC-01, 02 y 07 y se vuelve a correr Sonar **antes** de congelar el sábado 28, actualizar solo la frase de vulnerabilidades del backend y el rating.

Cada voz lleva al menos una captura real. Aquí: dashboard Sonar del 27-nov (lámina 9) y el diagrama CI/CD (lámina 10). Si faltara una cifra de otro integrante, no inventarla.

---

## Lámina 9 — Sonar delta + errores INC-06 + norma  
**Quién habla:** Skarlett · **IE:** IE1 / IE3 · **Tiempo:** ~1:15 a 1:20

**En pantalla:** tabla G6 (EV2 vs EV5-6) + captura `Evidencias/EV56-18/2026-11-27_sonar-be-dev-final.png`. Si cabe, un recorte de `Evidencias/EV56-20/cp17-rama-final.png`.

«Gracias. En análisis estático corrimos SonarQube Community sobre backend y frontend, siempre en localhost. El 20 de octubre el backend tenía cuatro vulnerabilidades y calificación E en seguridad, y el frontend catorce bugs, sin vulnerabilidades. El 27 de noviembre, ya con INC-04, INC-05 e INC-06 en `dev`, el Quality Gate volvió a aparecer en verde, el backend bajó de cuatro a **dos** vulnerabilidades y el frontend no se movió: siguen los catorce bugs y seguridad A. La calificación de seguridad del backend **sigue en E**, porque todavía hay un secreto de base de datos en el código y un aviso en la carga de documentos. Todavía faltan los merges de Nicolás de INC-01, INC-02 e INC-07, así que este no es el scan final.

Un Quality Gate en verde no significa un producto seguro. Sonar no nos detectó la fuga de errores de INC-06 ni la lógica de las contraseñas en claro. INC-06, que el inventario marca como Grave, sí lo cerramos en runtime: antes, cinco endpoints devolvían al cliente el error de PostgreSQL; después, con un helper común, responden HTTP 500 genérico, el detalle `22P02` queda solo en el log del servidor, y el caso de RUT duplicado sale como 400 controlado. Esa evidencia está en EV56-20.

En la norma, cruzamos DS 41 artículo 8, Ley 19.628 artículo 11 y Ley 20.584. CP-14 sigue fallido con reserva: el laboratorio corre en HTTP, aunque un proxy autofirmado en el puerto 3443 sí levantó TLS 1.2 y 1.3 con HSTS; lo dejamos para el 15 de diciembre. CP-16 también falla: no hay `pgcrypto` y los documentos se bajan sin token. En CP-18 el `pg_dump` tardó 216 milisegundos, el restore 190 —406 milisegundos en total— y los conteos calzaron, pero no hay backup automático ni retención a 15 años; eso queda para el 20 de diciembre.»

---

## Lámina 10 — Diagrama CI/CD con controles de seguridad  
**Quién habla:** Skarlett, con apoyo de Ninna si hace falta · **IE:** IE3 · **Tiempo:** ~0:50 a 1:10

**En pantalla:** `Planillas/EV56-21-Diagrama-CICD-Controles.png`.

«Para no depender solo del examen, armamos una propuesta de pipeline con enfoque shift-left y fail fast. Hoy el repositorio no tiene GitHub Actions: Sonar, Selenium, ZAP y JMeter se corren a mano contra Docker. El diagrama es una propuesta de mantenimiento, no la foto de un CI que ya exista.

La idea es simple. En cada pull request se revisa que no viajen secretos, se hace lint y `npm audit`, y corre Sonar con el Quality Gate por defecto: en código nuevo pide cobertura de al menos 80 por ciento, duplicación de a lo más 3 por ciento y cero violaciones nuevas. Ojo: en una instancia nueva, sin periodo de código nuevo, el gate puede pasar aunque el backend esté en E; por eso no lo usamos como certificado. Después se despliega el laboratorio y entra Selenium. ZAP, en el equipo, hoy es manual, a cargo de Ari; en la propuesta queda como un paso nocturno, no como algo que ya esté automatizado. Si el gate, el audit crítico o Selenium fallan, el cambio no se promueve. Con eso le paso a Ninna los KPI y el dictamen.»

---

## Preguntas probables (ensayar en voz alta)

1. **¿Por qué dicen que el Quality Gate no basta, si en `dev` apareció Passed?**  
   «Porque el gate por defecto mira sobre todo el código nuevo. En una instancia fresca, el 25 y el 27 de noviembre, ni siquiera había condiciones de New Code y igual dio Passed, con el backend en E. El 25, en la rama del fix, el mismo gate dio ERROR con cero issues nuevos, solo por duplicación y por cobertura 0. Además Community no ve SQLi, XSS ni la fuga de `err.message`; por eso lo complementamos con CP-17, ZAP, SQLMap y Selenium.»

2. **En el diagrama, ¿qué pasa si falla un control? ¿ZAP ya corre en el pipeline?**  
   «Si falla el audit alto, el Quality Gate de código nuevo, Selenium o —cuando se automatice— una alerta alta de ZAP, se bloquea la promoción. ZAP hoy no está en el pipeline: lo corre Ari a mano. El diagrama lo deja como paso opcional nocturno, porque no vamos a mostrar un CI que no existe.»

3. **¿Cómo demostraron INC-06 sin perder trazabilidad?**  
   «Con cinco IDs no numéricos, antes y después. Antes, el cliente veía `invalid input syntax for type bigint`. Después, ve un 500 genérico y en `docker logs` queda el `22P02` con la ruta. El 27 de noviembre lo repetimos en la rama final, ya mergeada a `dev`.»

4. **¿Por qué CP-14, CP-16 y CP-18 no se aprueban, si probaron TLS y el `pg_dump`?**  
   «Porque no aprobamos con un parche que no está en el despliegue oficial. El proxy autofirmado funcionó, y el restore del 25 de noviembre quedó íntegro en 406 milisegundos, con 3 usuarios y 20 pacientes. Pero en `dev` no hay certificados integrados, `/files/documentos` sigue sin token y no hay backup automático ni retención de 15 años. Por eso van al plan, con dueño y fecha.»

5. **¿Qué números gobiernan el plan de mantenimiento?**  
   «Los que ya medimos y los objetivos. Medidos: cobertura 0 por ciento, restore de laboratorio en 190 milisegundos, dump en 216. Objetivos: RTO y RPO de a lo más 15 minutos para fichas clínicas, MTTR de a lo más 2 horas, y la línea de JMeter de 300 milisegundos en p95, que es de Ari, no mía. También la alerta en 3 horas de la Ley 21.663, que es una de las razones para dejar el error real en el log y no en la respuesta.»
