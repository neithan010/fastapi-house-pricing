from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Creamos la instancia de la aplicación (el "restaurante")
app = FastAPI()

# Definimos una ruta (un "item del menú")
# Cuando alguien vaya a la raiz "/" usando GET
@app.get("/")
def read_root():
    # Devolvemos un JSON (FastAPI lo convierte automático)
    return {"mensaje": "Hola Nicolás", "estado": "Aprendiendo FastAPI"}

# Otra ruta: /items/5
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "descripcion": "Este es un item dinámico"}

# 1. Definimos el "Modelo" (El contrato de datos)
# Esto le dice a la API: "Solo acepto JSONs que tengan esta forma"
class OperacionMatematica(BaseModel):
    numero_a: float
    numero_b: float
    tipo: str  # Ejemplo: "suma", "resta", "multiplicacion"

@app.get("/")
def home():
    return {"mensaje": "API de Calculadora activa"}

# 2. Creamos un endpoint POST (para recibir datos)
@app.post("/calcular/")
def calcular(datos: OperacionMatematica):
    # Fíjate cómo accedemos a los datos con punto (datos.numero_a)
    # ¡El autocompletado de tu IDE debería funcionar aquí!
    
    resultado = 0
    
    if datos.tipo == "suma":
        resultado = datos.numero_a + datos.numero_b
    elif datos.tipo == "resta":
        resultado = datos.numero_a - datos.numero_b
    elif datos.tipo == "multiplicacion":
        resultado = datos.numero_a * datos.numero_b
    else:
        return {"error": "Operación no soportada"}

    return {
        "operacion": datos.tipo,
        "inputs": [datos.numero_a, datos.numero_b],
        "resultado_final": resultado
    }

# Modelo de Input: Las características de la casa
class HouseFeatures(BaseModel):
    metros_cuadrados: float
    habitaciones: int
    tiene_patio: bool
    sector: Optional[str] = "centro" # Si no lo mandan, asume "centro"

@app.post("/predict_price/")
def predict_price(features: HouseFeatures):
    # 1. LÓGICA DE NEGOCIO (Aquí iría tu modelo.predict() de Scikit-Learn o TensorFlow)
    # Por ahora, simularemos un modelo lineal simple: y = mx + b
    if features.metros_cuadrados < 10:
        raise HTTPException(status_code=400, detail="Casa muy pequeña, no se puede tasar.")

    precio_base = 50_000_000 # 50 millones
    precio_por_metro = 1_200_000
    
    # Cálculo
    precio_estimado = precio_base + (features.metros_cuadrados * precio_por_metro)
    
    # Ajustes del modelo
    if features.tiene_patio:
        precio_estimado += 10_000_000 # Suma valor
        
    if features.habitaciones > 3:
        precio_estimado *= 1.10 # 10% extra por ser grande
        
    # 2. RESPUESTA
    return {
        "input_features": features,
        "prediccion_precio_clp": int(precio_estimado),
        "mensaje": "Predicción generada exitosamente por el modelo v1"
    }