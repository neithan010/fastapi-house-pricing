from fastapi import APIRouter, HTTPException, Query
from models import HouseFeatures, HousePrediction, HouseSaved
from typing import List

# Creamos el router. 
# prefix="/casas" significa que TODAS las rutas aquí empezarán con /casas
# tags=["Casas"] sirve para agruparlas bonito en la documentación azul
router = APIRouter(prefix="/casas", tags=["Casas"])

# Base de datos "falsa" de casa
db_casas = []

# Un simple contador para IDs de las casas.
id_counter = 1

# NOTA: Ya no ponemos "/casas/predict...", solo "/predict..." 
# porque el prefix ya lo agrega automático.
@router.post("/", response_model=HousePrediction)
def crear_casa(features: HouseFeatures):
    global id_counter

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

    # Le asignamos id a la casa
    features_dict = features.model_dump()
    features_dict["precio_estimado"] = int(precio_estimado)
    features_dict["id"] = id_counter

    # Guardamos en la "base de datos"
    db_casas.append(features_dict)

    # Actualizamos el ID
    id_counter += 1
    return {
        "input_features": features_dict,
        "prediccion_precio_clp": int(precio_estimado),
        "mensaje": "Predicción generada exitosamente"
    }

# Endpoint para listar todas las casas guardadas
@router.get("/", response_model=List[HouseSaved])
def listar_casas():
    return db_casas

#Endpoint para obtener una casa por ID
@router.get("/{casa_id}", response_model=HouseSaved)
def obtener_casa(casa_id: int):
    for casa in db_casas:
        if casa["id"] == casa_id:
            return casa
    raise HTTPException(status_code=404, detail="Casa no encontrada")

# Endpoint para eliminar una casa por ID
@router.delete("/{casa_id}", response_model=None)
def eliminar_casa(casa_id: int):
    global db_casas
    for index,casa in enumerate(db_casas):
        if casa["id"] == casa_id:
            db_casas.pop(index)
            return 
    raise HTTPException(status_code=404, detail="Casa no encontrada")

# Podemos agregar más endpoints exclusivos de casas aquí
@router.get("/ofertas/")
def ver_ofertas(comuna: str = Query("Santiago")):
    return {"mensaje": f"Buscando ofertas de casas en {comuna}"}