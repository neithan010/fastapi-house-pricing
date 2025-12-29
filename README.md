
# API de Tasación de Propiedades (FastAPI)

API RESTful desarrollada con **Python** y **FastAPI** para simular la tasación de propiedades inmobiliarias mediante un modelo de lógica de negocio.

## Características

* Endpoint POST para predicción de precios.
* Validación de datos estricta con **Pydantic**.
* Manejo de errores HTTP (400 Bad Request) para inputs inválidos.
* Documentación automática con Swagger UI.

## Cómo correrlo

1. Instalar dependencias: `pip install -r requirements.txt`
2. Ejecutar servidor: `uvicorn main:app --reload`
