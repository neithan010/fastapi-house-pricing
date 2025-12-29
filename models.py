from pydantic import BaseModel
from typing import Optional

# Aquí definimos CÓMO se ven los datos de una casa
class HouseFeatures(BaseModel):
    metros_cuadrados: float
    habitaciones: int
    tiene_patio: bool
    sector: Optional[str] = "centro"

class HousePrediction(BaseModel):
    input_features: HouseFeatures
    prediccion_precio_clp: int
    mensaje: str