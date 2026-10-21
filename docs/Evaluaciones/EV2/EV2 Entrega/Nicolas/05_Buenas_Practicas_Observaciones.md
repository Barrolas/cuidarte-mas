# 05 — Buenas prácticas → recomendaciones del informe

**Qué es esto:** texto listo para el apartado de **recomendaciones** de la EP3 (Giannina/Skarlett integran). Demuestra criterio de seguridad/UX.

**Qué no es:**
- No codeas.
- No es una oleada de pruebas extra.
- **No requiere carpetas de evidencia ni capturas** solo para OBS/REC.
- No cambia el resultado Aprobado/Falla de tus CP frente al ERS.

La **evidencia** sigue siendo solo de la ejecución ERS (capa A: login ok/fail, API 200/401, CRUD, etc.).

---

## 1. Dos capas (claras)

| Capa | Qué haces | Entregable |
|------|-----------|------------|
| **A — ERS** | Ejecutas el CP con Postman/UI/Selenium | Bitácora + capturas en `Evidencias/CP-XX/` |
| **B — Recomendaciones** | Anotas mejoras conocidas / vistas de paso | Tabla OBS/REC en bitácora o párrafo para el informe (**sin** fotos obligatorias) |

Si al hacer el login “normal” del CP-01 ya ves que puedes fallar muchas veces, puedes **mencionar** eso en la recomendación. No hace falta armar una secuencia `07…10-fallo-N.png` solo para eso.

---

## 2. Temas a mencionar en el informe (tu parte)

Úsalos como checklist mental al redactar; no como pasos de ejecución.

### Autenticación / seguridad
- Bloqueo o rate-limit tras ~3–5 intentos fallidos de login (mención docente / buena práctica).
- Mensajes genéricos ante fallo de login (no revelar si falló el usuario o la clave).
- Invalidación de JWT al cerrar sesión (ligado a INC-03 si aplica).
- No exponer stack traces en errores 401/500.

### Formularios / validación
- Validación **UI + API** (no solo front).
- Mensajes claros junto al campo (vacíos, formato RUT/correo, política de clave).
- Confirmación antes de borrar usuarios/exámenes/documentos.

### UX / usabilidad (flujos que tú ejecutas)
- Feedback visible: cargando / éxito / error comprensible.
- Empty states cuando no hay datos.
- Mensaje claro al rechazar formato de documento no permitido.

No duplicar el trabajo de Skarlett (contraste, Lighthouse, CP-06/20): ella ya cubre accesibilidad visual formal.

---

## 3. IDs sugeridos para pegar en el informe

| ID | ¿Exigido ERS? | Texto base (ajusta al redactar) |
|----|---------------|----------------------------------|
| **REC-01** | No | Implementar bloqueo temporal o rate-limit tras 3–5 intentos fallidos de autenticación, con mensaje claro al usuario y registro en auditoría. |
| **REC-02** | Parcial | Asegurar validación de entrada en backend alineada con el front (campos vacíos, formatos, política de clave). |
| **REC-03** | No | Mejorar mensajes de error de formularios (específicos por campo, lenguaje no técnico). |
| **REC-04** | No | Confirmación explícita y feedback de éxito/error en acciones críticas (alta/baja de usuarios, exámenes, documentos). |
| **REC-05** | Sí (si INC-03) | Invalidar el JWT en servidor al logout y limpiar el token en el cliente. |
| **REC-06** | No | Tras cerrar sesión, mostrar feedback breve (“Sesión cerrada”) al redirigir al login. |
| **REC-09** | No | Validar RUT chileno con dígito verificador (módulo 11), no solo máscara/formato. |
| **REC-10** | No | Teléfono: select país/prefijo + validación de largo según país. |

Puedes renombrar a OBS-xx si el informe distingue “observación” vs “recomendación”; el contenido es el mismo.

---

## 4. Cómo usarlo en la práctica

1. Ejecutas tus CP **solo** con lo del playbook capa A + evidencias normales.  
2. Al cerrar una oleada (o al final), copias/adaptas las REC de la tabla a la bitácora sección recomendaciones **o** se las pasas a Giannina en un párrafo.  
3. En la presentación EP4 puedes citar 1–2 recomendaciones (p. ej. lockout) como criterio de calidad, sin mostrar un montaje de capturas de “4 fallos”.

---

## 5. Qué entregas a Giannina

- Bitácora de CP (capa A) + evidencias.  
- Lista corta de **REC-01…** (texto) para el capítulo de recomendaciones del informe.
