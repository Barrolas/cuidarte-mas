# 01 — Setup Docker (paso a paso)

Objetivo: tener Cuidarte+ corriendo en tu PC.

---

## 1.1 ¿Tienes Docker Desktop?

1. Abre el menú Inicio de Windows y busca **Docker Desktop**.  
2. Si no está instalado: descarga desde https://www.docker.com/products/docker-desktop/ e instálalo (reinicia si pide).  
3. Ábrelo y espera a que diga que el motor está **Running** (icono de ballena en la bandeja).

**Comprobar en PowerShell:**

```powershell
docker version
docker compose version
```

Si alguno falla, Docker no está listo: no sigas.

---

## 1.2 Ir a la carpeta del proyecto

Abre PowerShell y ejecuta (ajusta si tu ruta es distinta):

```powershell
cd "E:\CODE\LEARNING\DUOC - INGENIERIA EN INFORMATICA\Seg. y Calidad del Software\cuidarte-mas"
```

Verifica que ves carpetas `BACKEND`, `FRONTEND`, `docker-compose.yml`:

```powershell
dir
```

---

## 1.3 Levantar los contenedores

```powershell
docker compose up -d --build
```

- La **primera vez** puede tardar varios minutos (descarga imágenes y compila).  
- `-d` = en segundo plano.  
- `--build` = reconstruye si cambió el código.

Cuando termine sin error rojo grave:

```powershell
docker compose ps
```

Debes ver algo como:

- `cuidarteplus-postgres-ev` … healthy / running  
- `cuidarteplus-backend-ev` … running  
- `cuidarteplus-frontend-ev` … running  

---

## 1.4 Probar en el navegador

1. Abre Chrome o Edge.  
2. Ve a http://localhost:3333 → debe aparecer **Iniciar Sesión**.  
3. Ve a http://localhost:4444 → suele mostrar un JSON o mensaje de la API.  
4. Ve a http://localhost:4444/docs → documentación Swagger.

### Login manual de humo

1. En http://localhost:3333 escribe usuario `medico` y contraseña `medico`.  
2. Pulsa **Entrar**.  
3. Debes llegar a `/home` (o el home de la app) sin error.

Si falla el login: espera 30 s (el backend a veces arranca lento) y reintenta. Si sigue fallando:

```powershell
docker compose logs --tail=50 cuidarteplus-backend-ev
```

Copia el error para depurar (o pregunta en el equipo).

---

## 1.5 Parar / volver a subir

Parar (cuando termines el día):

```powershell
docker compose down
```

Volver a subir (días siguientes, sin rebuild si no cambió código):

```powershell
docker compose up -d
```

---

## 1.6 Si la base de datos está vacía

El compose monta un dump al **primer** arranque del volumen. Si recreaste volúmenes y no hay usuarios:

```powershell
docker compose down -v
docker compose up -d --build
```

`-v` **borra** los datos locales del Postgres del proyecto. Solo úsalo en ambiente de prueba.

---

## Listo → siguiente

[`02_Setup_Postman.md`](./02_Setup_Postman.md)
