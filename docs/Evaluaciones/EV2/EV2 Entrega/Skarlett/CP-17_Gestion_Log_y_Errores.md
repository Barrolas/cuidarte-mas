# CP-17 — Gestión de log y manejo de errores sin fuga de información

**Ejecutor del cierre:** Skarlett Tropan  
**Ejecutor de la parte dinámica:** Ari Araya  
**Fecha de cierre:** 27 de octubre de 2026  
**ERS:** NFR-SEG-6 — eventos relevantes registrados sin secretos; errores sin detalles internos.  
**Técnica (matriz):** SonarQube, Burp Suite y revisión manual.  
**Prioridad:** P1. Tipo: seguridad y cumplimiento.  
**Resultado:** **Fallido.**

El criterio se observa en tres sitios: el código que escribe el log, el cuerpo de error que recibe el cliente y quién puede insertar en `auditoria`. SonarQube cubre el primero solo en parte. La parte de Burp está en la rama `feature/ari-ep3-qa-seguridad`. La revisión manual se hizo sobre el código de `main`.

## 1. SonarQube (main, 20 de octubre de 2026)

Community Build 26.10.0.133078, modo MQR, Overall Code. Capturas en `docs/Evaluaciones/EV2/EV2 Contexto/Entregables/capturas-sonar/`. El informe ya las lee en la sección 5.4; aquí solo queda lo que toca a NFR-SEG-6.

| Proyecto | Security | Security Hotspots | Qué importa para CP-17 |
|----------|----------|-------------------|------------------------|
| Cuidarte+ Backend | 4 issues, nota E | 0 | No marcó los `catch` que devuelven `err.message`. Sí marcó, en `src/app.js`, «This framework implicitly discloses version information by default» (Security, Low): Express anuncia su versión. |
| Cuidarte+ Frontend | 0 issues, nota A | 0 | No marcó `console.error` ni el token en `localStorage`. |

El Quality Gate está Passed en los dos proyectos porque la puerta mira el código nuevo. El aviso del propio panel dice que esta edición no busca inyección SQL ni XSS, y que el análisis de dependencias se omitió. Un panel en verde no demuestra NFR-SEG-6.

El Blocker de `BACKEND/src/db.js` (contraseña de PostgreSQL en el código) ya está leído en la sección 5.4. Es un secreto en el fuente, no un evento de log, y se mantiene en esa sección.

## 2. Revisión manual del código (main, 27 de octubre de 2026)

### 2.1 Log de acceso y de errores

`BACKEND/src/app.js` registra cada request con el formato de desarrollo de Morgan y no define un logger de aplicación:

```21:23:BACKEND/src/app.js
app.use(cors());
app.use(express.json());
app.use(morgan("dev"));
```

Ese formato escribe método, URL, estado y tiempo en la salida estándar del contenedor. No escribe el cuerpo ni el header `Authorization`. Una credencial que viaje en la query string sí quedaría en el log. No hay niveles, retención ni redacción de secretos.

En los `catch`, el objeto de error completo va al mismo log y, a la vez, su mensaje sale al cliente. El patrón se repite en las ocho rutas: `auth.js`, `users.js`, `pacientes.js`, `examenes.js`, `documentos.js`, `audit.js`, `roles.js` y `tipo-examen.js`. Son **34** bloques. Ejemplo en la subida de documentos, que es el 500 que Ari vio el 26 de octubre:

```111:116:BACKEND/src/routes/documentos.js
  } catch (err) {
    console.error(err);
    res.status(500).json({
      error: "Error al subir documentos",
      glosa: err.message || err.toString(),
    });
  }
```

`err.message` de PostgreSQL puede incluir el texto SQL. `err.toString()` cubre el caso en que no haya `message`. Los dos salen en el JSON.

En el navegador, `FRONTEND/src/context/AuthContext.jsx` hace `console.error("Error al decodificar JWT:", error)`. Eso queda en la consola del cliente, no en el log del servidor. El mismo archivo guarda el token en `localStorage`; ese hallazgo ya está en la Tabla 28 del informe (INC-08) y no se reabre aquí.

### 2.2 Escritura de auditoría (INC-14)

`GET /auditoria` comprueba el rol y responde 403 si no es admin. `POST /auditoria` solo comprueba que el token sea válido y luego inserta `accion` y `detalles` tal como llegan:

```19:34:BACKEND/src/routes/audit.js
router.post("/", async (req, res) => {
  const { accion, detalles } = req.body;
  try {
    const authUser = getUserFromAuthHeader(req);
    if (!authUser) {
      return res.status(401).json({
        error: "No autorizado",
        glosa: "Token inválido",
      });
    }
    const actionText = detalles ? `${accion}: ${detalles}` : accion;
    const result = await pool.query(
      "INSERT INTO auditoria (usuario_id, accion) VALUES ($1, $2) RETURNING *",
      [authUser?.usuarioId || null, actionText]
    );
```

Nicolás ya lo ejecutó el 20 de octubre de 2026 (CP-03): con token de médico, `POST /auditoria` respondió **201** y creó un registro inventado. Evidencia en `docs/Evaluaciones/EV2/EV2 Entrega/Nicolas/Bitacora_Ejecucion.md` y en `Evidencias/CP-03/`. El log de auditoría no es íntegro: cualquier sesión puede escribirlo. El mismo `catch` de esta ruta también devuelve `glosa: err.message`.

El valor por defecto `JWT_SECRET || "inseguro"` está en las siete rutas que firman o verifican el token (`auth`, `users`, `pacientes`, `examenes`, `documentos`, `audit`, `roles`). La Tabla 28 ya lo relaciona con la Ley 19.628 y el DS 41. SonarQube no lo marcó.

## 3. Parte dinámica de Ari (rama `feature/ari-ep3-qa-seguridad`, 26 de octubre de 2026)

Commit `785062d`. Bitácora: `docs/Evaluaciones/EV2/EV2 Entrega/Ari/Bitacora_Ejecucion.md` en esa rama. Evidencia canónica: `Evidencias/EV2_Ari_Pruebas_Seguridad_Rendimiento.docx` (figuras 12–13 y 17–28). Burp Suite no se abrió: el mismo criterio se probó con Swagger Authorize y `curl.exe -i`, igual que en CP-14.

| Prueba | Resultado de Ari | Lectura para NFR-SEG-6 |
|--------|------------------|------------------------|
| Sin token, `GET /examenes` | 401, glosa «Token inválido» | Mensaje genérico. Cumple. |
| Paciente sobre recurso ajeno (GET, DELETE, POST examen, `GET /examenes/paciente/2`) | 403, o 200 con lista vacía en el id propio | Mensajes genéricos. Cumple la parte de control de acceso. |
| Médico sobre sus rutas | 200 | Control positivo. |
| `POST /documentos` con token de médico y de paciente | 500. Multer corre antes del rol. El cuerpo no se guardó. | No demuestra ni descarta el texto de `err.message` en el cable. INC-06 queda abierto en runtime. |

Ari pidió no cerrar INC-06 solo con ese 500. La revisión del fuente sí lo confirma: el `catch` de `documentos.js` está escrito para enviar `err.message`. Falta la captura del cuerpo para la evidencia dinámica.

En CP-20 (20 de octubre, Skarlett) el login inválido respondió «Credenciales inválidas» y HTTP 401. Ese recorrido no pasa por un `catch` 500, así que no contradice INC-06.

## 4. Resultado frente al criterio

| Condición de NFR-SEG-6 | Observación | Juicio |
|------------------------|-------------|--------|
| Eventos relevantes, sin secretos | Morgan en formato `dev` y `console.error(err)`, sin redacción. La auditoría de descarga ya falló en CP-03 (INC-13, Nicolás). | No cumple |
| Errores sin detalles internos | 34 respuestas 500 incluyen `err.message`. SonarQube no las vio. El 500 de documentos no tiene body archivado. | No cumple (INC-06) |
| El log no lo escribe cualquiera | `POST /auditoria` con médico → 201 | No cumple (INC-14) |
| Mensajes de acceso (401/403) | Genéricos en la pasada de Ari | Cumple esa parte |

El caso queda **Fallido**. La parte de mensajes 401/403 no compensa la fuga del `catch` ni la escritura abierta de la auditoría.

## 5. Texto para el informe (Tabla 24 y relato)

Sustituir la fila pendiente de CP-17.

| Campo | Texto |
|-------|--------|
| Caso | CP-17. Gestión de log y manejo de errores sin fuga de información |
| Resultado | Fallido |
| Evidencia | 27 oct 2026. SonarQube (20 oct) : 0 Security Hotspots; no marcó la fuga y sí la versión de Express en `app.js` (Low). Revisión manual: 34 `catch` con `glosa: err.message` y `console.error(err)`; `morgan("dev")`. Ari (26 oct, curl equivalente a Burp): 401/403 genéricos; `POST /documentos` → 500 sin cuerpo guardado. Nicolás (20 oct): `POST /auditoria` con médico → 201. |
| Incidentes | INC-06 confirmado en código; falta la captura del cuerpo 500. INC-14 confirmado. INC-11 no ejecutado. |
| Fecha y ejecutor | 27 oct 2026. Skarlett Tropan (estático) y Ari Araya (dinámico). |

Párrafo para la sección 5, a continuación de CP-22:

CP-17 falla frente a NFR-SEG-6. El 20 de octubre SonarQube Community Build no marcó ningún Security Hotspot y no detectó los mensajes internos que el backend devuelve al cliente; el informe ya deja constancia de eso en la sección 5.4. La revisión del código de `main`, el 27 de octubre, encontró el mismo patrón en 34 bloques `catch` de ocho rutas: `console.error(err)` y `glosa: err.message`. El log de acceso es `morgan("dev")`, sin redacción. Ari, el 26 de octubre, probó la parte de Burp con Swagger y `curl`: los 401 y 403 usan mensajes genéricos, y `POST /documentos` respondió 500 sin que se guardara el cuerpo, así que la fuga no quedó fotografiada en el cable aunque el `catch` de `documentos.js` la escribe. Nicolás confirmó el 20 de octubre que un médico puede insertar en `auditoria` (HTTP 201): es INC-14. INC-11, las dependencias, sigue sin `npm audit`.

## 6. Qué queda fuera de este cierre

- INC-11. Hace falta `npm audit` en `BACKEND` y `FRONTEND`. Este equipo no tiene `npm` en el PATH, y el escáner declaró que omitió las dependencias.
- Captura del cuerpo del HTTP 500 de `POST /documentos`, para cerrar la evidencia dinámica de INC-06. La pide la bitácora de Ari (figuras 12 y 13 del Word, que muestran el 500 sin cuerpo).
- La fila de la Tabla 24 y el párrafo de la sección 5 ya están en `EP3-Informe-Cuidarte-Mas-avance.docx` (27 de octubre de 2026).
