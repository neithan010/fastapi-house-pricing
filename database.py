from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. La URL de la Base de Datos
# Esto creará un archivo 'casas.db' en tu carpeta
SQLALCHEMY_DATABASE_URL = "sqlite:///./casas.db"

# 2. El Motor (Engine)
# "check_same_thread": False es necesario SOLO para SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. La Sesión (SessionLocal)
# Esta es la fábrica de conexiones. Cada petición tendrá su propia sesión.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. La Clase Base
# Todos nuestros modelos de tablas heredarán de aquí
Base = declarative_base()   

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()