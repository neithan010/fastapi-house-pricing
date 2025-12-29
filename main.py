from fastapi import FastAPI
from routers import casas # <--- Importamos el router que creamos

app = FastAPI(
    title="API de Tasación Inmobiliaria",
    description="API profesional modularizada para predicción de precios",
    version="2.0.0"
)

# Aquí conectamos el router al sistema principal
app.include_router(casas.router)

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API Inmobiliaria. Ve a /docs para usarla."}