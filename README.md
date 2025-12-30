
# 🏠 FastAPI House Pricing API

Una API RESTful robusta diseñada para predecir precios de viviendas y gestionar un catálogo de propiedades. Este proyecto implementa las mejores prácticas de **DevOps** utilizando Docker para la contenedorización y GitHub Actions/Render para el despliegue continuo (CI/CD).

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker)
![Render](https://img.shields.io/badge/Deploy-Render-black?style=for-the-badge&logo=render)

## 🚀 Demo en Vivo

Puedes probar la API funcionando en la nube aquí:
👉 **[Ver Documentación Interactiva (Swagger UI)](https://[PON-TU-URL-DE-RENDER-AQUI].onrender.com/docs)**

---

## 🛠️ Tecnologías

* **Framework:** FastAPI
* **Lenguaje:** Python 3.11
* **Base de Datos:** SQLite (Persistencia local) / SQLAlchemy ORM
* **Validación de Datos:** Pydantic
* **Contenedorización:** Docker & Docker Compose
* **Servidor:** Uvicorn

---

## ⚙️ Instalación y Ejecución

Tienes dos formas de correr este proyecto: la forma "DevOps" (recomendada) y la forma tradicional.

### 🐳 Opción 1: Con Docker (Recomendada)

Olvídate de instalar Python o dependencias. Si tienes Docker, solo corre:

1. **Clonar el repositorio:**

   ```bash
   git clone [https://github.com/](https://github.com/)[TU-USUARIO]/fastapi-house-pricing.git
   cd fastapi-house-pricing
   ```
2. **Levantar el servicio:**

   ```bash
   docker-compose up -d --build
   ```
3. **¡Listo!**
   La API estará corriendo en: `http://localhost:8000/docs`

> **Nota sobre Persistencia:** Gracias a Docker Volumes, la base de datos `casas.db` persiste en tu máquina local aunque apagues o reinicies el contenedor.

---

### 🐍 Opción 2: Ejecución Manual (Local)

Si prefieres correrlo en tu entorno Python nativo:

1. **Crear entorno virtual:**

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```
2. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecutar servidor:**

   ```bash
   uvicorn main:app --reload
   ```

---

## 📂 Estructura del Proyecto

El proyecto sigue una arquitectura modular y limpia:

```text
/
├── docker/
│   └── Dockerfile       # Receta de construcción de la imagen
├── routers/             # Rutas divididas por módulos
├── models.py            # Modelos de Base de Datos (SQLAlchemy)
├── main.py              # Punto de entrada de la aplicación
├── docker-compose.yml   # Orquestación de contenedores
├── requirements.txt     # Dependencias
└── casas.db             # Base de datos SQLite (se genera automáticamente)
```
