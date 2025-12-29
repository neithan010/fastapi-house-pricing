from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from database import get_db
from sql_models import CasaDB
from models import HouseFeatures, HousePrediction, HouseSaved
from typing import List

# Creamos el router. 
# prefix="/casas" significa que TODAS las rutas aquí empezarán con /casas
# tags=["Casas"] sirve para agruparlas bonito en la documentación azul
router = APIRouter(prefix="/casas", tags=["Casas"])

# NOTA: Ya no ponemos "/casas/predict...", solo "/predict..." 
# porque el prefix ya lo agrega automático.
@router.post("/", response_model=HousePrediction)
def crear_casa(features: HouseFeatures, db: Session = Depends(get_db)):

    # Validacion metros cuadrados
    if features.metros_cuadrados < 10:
        raise HTTPException(status_code=400, detail="Casa muy pequeña, no se puede tasar.")

    # Lógica de Tasación (Tu algoritmo)
    precio_base = 50_000_000
    precio_por_metro = 1_200_000
    
    # Cálculo simple del precio estimado
    precio_estimado = precio_base + (features.metros_cuadrados * precio_por_metro)
    
    # Ajustes según características
    if features.tiene_patio:
        precio_estimado += 10_000_000
    if features.habitaciones > 3:
        precio_estimado *= 1.10

    # Agregamos la casa a la nueva base de datos db
    copy_casa = features.model_dump()
    copy_casa['precio_estimado'] = int(precio_estimado)

    nueva_casa_db = CasaDB(**copy_casa)
    db.add(nueva_casa_db)
    db.commit()

    # Hacemos un refresh para obtener el ID asignado
    db.refresh(nueva_casa_db)

    return {
        "input_features": copy_casa,
        "prediccion_precio_clp": copy_casa['precio_estimado'],
        "mensaje": "Predicción generada exitosamente con ID: " + str(nueva_casa_db.id)
    }

# Endpoint para listar todas las casas guardadas
@router.get("/", response_model=List[HouseSaved])
def listar_casas(db: Session = Depends(get_db)):
    casas_db = db.query(CasaDB).all()
    return casas_db

# Endpoint para obtener una casa por ID
@router.get("/{casa_id}", response_model=HouseSaved)
def obtener_casa(casa_id: int, db: Session = Depends(get_db)):
    casa = db.query(CasaDB).filter(CasaDB.id == casa_id).first()
    if not casa:
        raise HTTPException(status_code=404, detail="Casa no encontrada")
    return casa

# Endpoint para eliminar una casa por ID
@router.delete("/{casa_id}", response_model=None)
def eliminar_casa(casa_id: int, db: Session = Depends(get_db)):
    casa = db.query(CasaDB).filter(CasaDB.id == casa_id).first()
    if not casa:
        raise HTTPException(status_code=404, detail="Casa no encontrada")
    db.delete(casa)
    db.commit()

    return

# Podemos agregar más endpoints exclusivos de casas aquí
@router.get("/ofertas/")
def ver_ofertas(comuna: str = Query("Santiago")):
    return {"mensaje": f"Buscando ofertas de casas en {comuna}"}