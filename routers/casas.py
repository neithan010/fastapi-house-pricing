from fastapi import APIRouter, HTTPException, Query
from models import HouseFeatures, HousePrediction 

# Creamos el router. 
# prefix="/casas" significa que TODAS las rutas aquí empezarán con /casas
# tags=["Casas"] sirve para agruparlas bonito en la documentación azul
router = APIRouter(prefix="/casas", tags=["Casas"])

# NOTA: Ya no ponemos "/casas/predict...", solo "/predict..." 
# porque el prefix ya lo agrega automático.
@router.post("/predict_price/", response_model=HousePrediction)
def predict_price(features: HouseFeatures):
    
    # Validacion
    if features.metros_cuadrados < 10:
        raise HTTPException(status_code=400, detail="Casa muy pequeña, no se puede tasar.")

    # Lógica de Tasación (Tu algoritmo)
    precio_base = 50_000_000
    precio_por_metro = 1_200_000
    
    precio_estimado = precio_base + (features.metros_cuadrados * precio_por_metro)
    
    if features.tiene_patio:
        precio_estimado += 10_000_000
        
    if features.habitaciones > 3:
        precio_estimado *= 1.10

    return {
        "input_features": features,
        "prediccion_precio_clp": int(precio_estimado),
        "mensaje": "Predicción generada exitosamente"
    }

# Podemos agregar más endpoints exclusivos de casas aquí
@router.get("/ofertas/")
def ver_ofertas(comuna: str = Query("Santiago")):
    return {"mensaje": f"Buscando ofertas de casas en {comuna}"}