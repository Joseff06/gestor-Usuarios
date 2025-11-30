# Gestor de Usuarios — Microservicio (FastAPI + PostgreSQL)

API para la gestión de usuarios, roles y autenticación de empleados. Implementada con `FastAPI` y `PostgreSQL` para ofrecer rendimiento y persistencia relacional.

## Tabla de contenidos

- [Características](#caracter%C3%ADsticas)
- [Tecnologías](#tecnolog%C3%ADas)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación y ejecución (desarrollo)](#instalaci%C3%B3n-y-ejecuci%C3%B3n-desarrollo)
- [Configuración](#configuraci%C3%B3n)
- [Base de datos (Docker)](#base-de-datos-docker)
- [Documentación de la API](#documentaci%C3%B3n-de-la-api)
- [Despliegue sugerido](#despliegue-sugerido)
- [Contribuir](#contribuir)
- [Licencia y Contacto](#licencia-y-contacto)

---

## Características

- CRUD de usuarios.
- Gestión de roles.
- Endpoints documentados con OpenAPI/Swagger.

## Tecnologías

- `FastAPI` (API)
- `SQLModel` / SQLAlchemy (modelos y ORM)
- `PostgreSQL` (base de datos)
- `uvicorn` (ASGI server)

## Estructura del proyecto

Raíz del servicio `microservicio-usuarios`:

```
main.py            # Punto de entrada (endpoints)
database.py        # Conexión y utilidades de BD
models.py          # Modelos de datos
requirements.txt   # Dependencias
.env.example       # Variables de entorno de ejemplo
README             # Documentación (este archivo)
```

## Requisitos

- `Python 3.10+`
- `PostgreSQL` (local o en contenedor Docker)
- `pip` y `virtualenv` (recomendado)

## Instalación y ejecución (desarrollo)

1. Clonar el repositorio y entrar en el directorio del servicio:

```powershell
git clone <URL_DEL_REPO>
cd microservicio-usuarios
```

2. Crear y activar un entorno virtual:

```powershell
python -m venv venv
.\n+venv\Scripts\activate
```

3. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

4. Crear el archivo de configuración a partir del ejemplo:

```powershell
copy .env.example .env
```

Editar `.
.env` y ajustar las variables para tu entorno (ver sección "Configuración").

5. Iniciar el servidor en modo desarrollo:

```powershell
uvicorn main:app --reload --port 8001
```

El servidor quedará disponible en `http://localhost:8001`.

## Configuración

Usar el archivo `.env` (basado en `.env.example`) para variables principales, por ejemplo:

```
DB_USER=admin
DB_PASSWORD=password123
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=empleados_db
```

Asegúrate de que el `DB_HOST` y `DB_PORT` apuntan a tu instancia de PostgreSQL.

## Base de datos (Docker)

Si no quieres instalar PostgreSQL localmente, puedes levantar un contenedor Docker rápido:

```powershell
docker run -d --name postgres_db -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=password123 -e POSTGRES_DB=empleados_db -p 5432:5432 postgres:15
```

Luego actualiza las variables en `.env` para que apunten a `DB_HOST=127.0.0.1` y `DB_PORT=5432`.

## Documentación de la API

FastAPI expone documentación interactiva OpenAPI en:

- Swagger UI: `http://localhost:8001/docs`
- ReDoc: `http://localhost:8001/redoc`

Ejemplo de petición para crear un usuario (cURL):

```bash
curl -X POST "http://localhost:8001/usuarios/" \
  -H "Content-Type: application/json" \
  -d '{"username":"S-01","email":"vendedor@test.com","rol":"operario"}'
```



