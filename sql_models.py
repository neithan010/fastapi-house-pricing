from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base # Importamos la Base que creamos recién

# Esta clase ES LA TABLA en la base de datos
class CasaDB(Base):
    __tablename__ = "casas" # El nombre real de la tabla en SQL

    id = Column(Integer, primary_key=True, index=True) # Llave primaria
    metros_cuadrados = Column(Float)
    habitaciones = Column(Integer)
    tiene_patio = Column(Boolean)
    sector = Column(String)
    precio_estimado = Column(Integer)