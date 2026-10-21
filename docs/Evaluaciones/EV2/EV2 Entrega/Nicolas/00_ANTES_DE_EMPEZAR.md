# 00 — Antes de empezar (mapa mental)

Lee esto completo una vez. No necesitas memorizarlo: vuelve aquí cuando te confundan los nombres.

---

## 1. Qué estás haciendo en la EP3

El equipo **diseñó** casos (CP-01…CP-23). A ti te toca **ejecutar** varios y dejar **evidencia** (capturas, respuestas HTTP) en una **bitácora**.

No “arreglas” el código ahora (salvo que el equipo lo pida). Si algo falla, lo documentas como **Falla** + incidente (`INC-xx` o `BUG-xxx`).

Las **recomendaciones** de buenas prácticas (lockout, formularios, etc.) se escriben para el **informe** más adelante; **no** son una ronda de pruebas ni requieren evidencia. Ver [`05_Buenas_Practicas_Observaciones.md`](./05_Buenas_Practicas_Observaciones.md). Mientras ejecutas, solo te preocupas del ERS + capturas del CP.

---

## 2. Piezas del sistema Cuidarte+

Imagina tres cajas:

```
[ Navegador / Selenium ]  -->  Frontend :3333  -->  API :4444  -->  Postgres :15442
     (lo que ves)              (pantallas)         (JSON/JWT)      (datos)
```

| Pieza | URL / puerto | Para qué sirve en tus pruebas |
|-------|--------------|-------------------------------|
| Frontend | http://localhost:3333 | Pantallas (login, pacientes, exámenes) — **Selenium** |
| API | http://localhost:4444 | Endpoints REST — **Postman** / Swagger http://localhost:4444/docs |
| Base de datos | localhost:15442 | Solo si revisas auditoría o documentos en BD |

Si el frontend o la API no abren, **no sigas** con los CP: primero arregla Docker ([01_Setup_Docker.md](./01_Setup_Docker.md)).

---

## 3. Qué es cada herramienta (en una frase)

| Herramienta | Qué es | Qué harás tú con ella |
|-------------|--------|------------------------|
| **Docker** | Empaqueta la app para que corra igual en tu PC | `docker compose up -d` y listo |
| **Postman** | App para llamar a la API sin programar | Login, GET/POST, ver código 200/401/403 |
| **Swagger** | Documentación interactiva de la API en el navegador | Alternativa a Postman para probar un endpoint |
| **Selenium** | Automatiza el navegador (clics, escribir, capturas) | Repetir flujos UI de forma trazable |
| **SQLMap** | Busca inyección SQL en un parámetro | Solo CP-04, contra login local |
| **Bitácora** | Tabla de resultados | La llenas tú y se la pasas a Giannina |

**Kali:** no la necesitas para empezar. Sirve más a Ari (ZAP, Burp, etc.).

---

## 4. Palabras que verás todo el tiempo

| Término | Significado simple |
|---------|-------------------|
| **JWT / token** | “Pase” que te da el login; lo mandas en otras peticiones como `Authorization: Bearer …` |
| **Endpoint** | Ruta de la API, ej. `POST /autenticacion/login` |
| **Status / código HTTP** | 200 = OK, 401 = no autenticado, 403 = no autorizado, 404 = no existe, 500 = error servidor |
| **RBAC** | Permisos por rol (admin / médico / paciente) |
| **P0 / P1 / P2** | Prioridad: primero lo crítico (auth, docs), después el resto |
| **INC-xx** | Incidente ya previsto en el análisis del equipo |
| **BUG-xxx** | Defecto nuevo que encuentres tú |

---

## 5. Cómo marcar un caso

| Resultado | Cuándo usarlo |
|-----------|----------------|
| **Aprobado** | Cumple lo esperado (UI y/o API según el CP) |
| **Falla** | No cumple (aunque “casi” funcione) |
| **Bloqueado** | No pudiste probarlo porque Docker/login estaba roto |
| **No ejecutado** | Aún no lo hiciste |

Regla del curso: si hay problema de **seguridad o cumplimiento**, es **Falla** aunque la pantalla se vea bien.

---

## 6. Orden de trabajo recomendado (días)

| Día | Qué hacer |
|-----|-----------|
| 0 | Leer este archivo + setup Docker + Postman + Selenium (guías 01–03) |
| 1 | Oleada P0: CP-01, CP-07, CP-08, CP-12 |
| 2 | Oleada P1: CP-03, CP-11, CP-13 |
| 3 | Oleada P2: CP-02, CP-09, CP-10 + SQLMap CP-04 |
| 4 | Revisar bitácora, subir evidencias al repo, avisar a Giannina |

Si un día no terminas, **no inventes resultados**: deja “No ejecutado” o “Bloqueado” con la causa.

---

## 7. Checklist antes del primer CP

- [ ] Leí este documento  
- [ ] Docker corre y abro http://localhost:3333 y http://localhost:4444  
- [ ] Login manual con `medico` / `medico` funciona en el navegador  
- [ ] Postman: un login me devolvió token (guía 02)  
- [ ] Selenium: el smoke de login pasó (guía 03)  
- [ ] Tengo abierta la bitácora para ir anotando  

Cuando todo eso esté en ✓, pasa a [`04_Playbook_Ejecucion_CP.md`](./04_Playbook_Ejecucion_CP.md).
