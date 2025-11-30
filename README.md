# Gestor de Usuarios — Microservicio (FastAPI + PostgreSQL)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)

API REST diseñada para la gestión de usuarios, roles y autenticación de empleados dentro de la arquitectura de microservicios. Implementada con **FastAPI** para alto rendimiento y **PostgreSQL** para persistencia relacional robusta.

---

## 📋 Tabla de contenidos

- [Características](#características)
- [Tecnologías](#tecnologías)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación y ejecución (desarrollo)](#instalación-y-ejecución-desarrollo)
- [Configuración](#configuración)
- [Base de datos (Docker)](#base-de-datos-docker)
- [Documentación de la API](#documentación-de-la-api)

---

## ✨ Características

* ✅ **CRUD Completo** de usuarios (Crear, Leer, Actualizar).
* 🛡️ **Gestión de roles** (Operario, Admin, Gerente).
* 📄 **Documentación automática** interactiva con OpenAPI/Swagger.
* ⚡ **Alto rendimiento** gracias al motor asíncrono de FastAPI (Uvicorn).
* 🗄️ **ORM Moderno** usando SQLModel.

## 🛠 Tecnologías

* **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web moderno y rápido.
* **[SQLModel](https://sqlmodel.tiangolo.com/)**: ORM que combina la potencia de SQLAlchemy con la validación de Pydantic.
* **[PostgreSQL](https://www.postgresql.org/)**: Base de datos relacional.
* **[Uvicorn](https://www.uvicorn.org/)**: Servidor ASGI de alto rendimiento.
* **[Docker](https://www.docker.com/)**: Contenedorización de la base de datos.

## 📂 Estructura del proyecto

Raíz del servicio `microservicio-usuarios`:

```text
.
├── main.py              # Punto de entrada (endpoints)
├── database.py          # Configuración y conexión a BD
├── models.py            # Modelos de datos (Tablas SQL)
├── requirements.txt     # Dependencias del proyecto
├── .env.example         # Plantilla de variables de entorno
└── README.md            # Documentación del proyecto

📋 Requisitos
Python 3.10 o superior

PostgreSQL (local o en contenedor Docker)

Pip y Virtualenv

🚀 Instalación y ejecución (desarrollo)
Sigue estos pasos para correr el proyecto localmente:

1. Clonar el repositorio:

Bash

git clone <URL_DE_TU_REPO>
cd microservicio-usuarios
2. Crear y activar un entorno virtual:

PowerShell

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\activate
Bash

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Instalar dependencias:

Bash

pip install -r requirements.txt
4. Configurar variables de entorno:

Crea un archivo llamado .env en la raíz (puedes copiar el ejemplo):

Bash

# Windows
copy .env.example .env
5. Iniciar el servidor:

Bash

uvicorn main:app --reload --port 8001
El servidor quedará disponible en: http://localhost:8001

⚙️ Configuración
Asegúrate de que tu archivo .env tenga las credenciales correctas.

Nota: Si usas la configuración de Docker de este proyecto, el puerto puede ser 5433 o 5432 dependiendo de tu docker-compose.

Ini, TOML

DB_USER=admin
DB_PASSWORD=password123
DB_HOST=127.0.0.1
DB_PORT=5433
DB_NAME=empleados_db
🐳 Base de datos (Docker)
Si prefieres levantar la base de datos con Docker rápidamente sin instalar PostgreSQL en tu sistema:

Bash

docker run -d --name postgres_db \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=password123 \
  -e POSTGRES_DB=empleados_db \
  -p 5433:5432 postgres:15
Esto levantará PostgreSQL accesible en el puerto 5433 de tu máquina local.

📚 Documentación de la API
FastAPI genera documentación interactiva automáticamente. Una vez corriendo el servidor, visita:

Swagger UI: http://localhost:8001/docs

ReDoc: http://localhost:8001/redoc

Ejemplo de uso (Crear Usuario)
Puedes usar curl o la interfaz de Swagger:

Bash

curl -X POST "http://localhost:8001/usuarios/" \
  -H "Content-Type: application/json" \
  -d '{"username": "S-01", "email": "vendedor@test.com", "rol": "operario"}'