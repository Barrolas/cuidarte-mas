# 02 — Setup Postman (desde cero)

Objetivo: hacer un **login** a la API y guardar el **token**.

---

## 2.1 Instalar Postman

1. Entra a https://www.postman.com/downloads/  
2. Descarga **Postman for Windows** e instálalo.  
3. Ábrelo. Puedes crear cuenta gratis o usar “Skip” / continuar sin cuenta según la versión.

---

## 2.2 Importar la colección del curso

1. En Postman: **Import** (botón arriba a la izquierda).  
2. Arrastra o elige el archivo:

`docs/Evaluaciones/EV2/EV2 Entrega/Nicolas/postman/CuidartePlus_Nicolas_EP3.postman_collection.json`

3. Debe aparecer la colección **CuidartePlus Nicolás EP3**.

---

## 2.3 Crear un Environment (variables)

Así no escribes el token a mano cada vez.

1. Izquierda: **Environments** → **+** Create.  
2. Nombre: `Cuidarte Local`.  
3. Agrega variables:

| Variable | Initial value | Current value |
|----------|---------------|---------------|
| `baseUrl` | `http://localhost:4444` | igual |
| `token` | (vacío) | (vacío) |

4. Guarda y **selecciona** ese environment en el selector arriba a la derecha (debe decir `Cuidarte Local`, no “No Environment”).

---

## 2.4 Primer request: Login médico

1. Abre la colección → carpeta **01 Auth** → request **Login medico**.  
2. Verifica:
   - Método: `POST`  
   - URL: `{{baseUrl}}/autenticacion/login`  
   - Body → raw → JSON:

```json
{
  "nombre_usuario": "medico",
  "password": "medico"
}
```

3. Pulsa **Send**.

### Qué debes ver

- Status **200 OK**  
- En el Body un JSON con un campo tipo `token` (texto largo).

### Guardar el token (automático)

El request de la colección incluye un script *Tests* que guarda `token` en el environment. Si no:

1. Copia el valor de `token` del JSON.  
2. Environments → `Cuidarte Local` → pega en `token` → Save.

---

## 2.5 Segundo request: usar el token

1. Abre **02 Pacientes** → **GET Pacientes**.  
2. En Headers debe existir:

`Authorization` = `Bearer {{token}}`

3. **Send**.  
4. Esperado: **200** y una lista (array) de pacientes (puede estar vacía o con datos del dump).

Si sale **401**: el token no está o el environment no está seleccionado. Repite login.

---

## 2.6 Alternativa sin Postman: Swagger

1. Abre http://localhost:4444/docs  
2. Busca `POST /autenticacion/login` → Try it out → Execute con `medico`/`medico`.  
3. Copia el token.  
4. Arriba en Swagger suele haber **Authorize**: pega `Bearer TU_TOKEN` (o solo el token, según la UI).  
5. Prueba `GET /pacientes`.

Úsalo si Postman te complica; la evidencia puede ser captura de Swagger.

---

## 2.7 Cómo guardar evidencia

1. En Postman, con la respuesta visible: captura de pantalla (Win+Shift+S).  
2. Guarda en:

`docs/Evaluaciones/EV2/EV2 Entrega/Nicolas/Evidencias/CP-01/postman-login-medico-200.png`

Incluye en la foto: URL, status y un trozo del body (puedes tapar el token largo si quieres, pero deja visible que existe).

---

## Listo → siguiente

[`03_Setup_Selenium.md`](./03_Setup_Selenium.md)
