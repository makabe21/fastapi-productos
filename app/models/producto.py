from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    descripcion = Column(String(255))
    precio = Column(Float)
    stock = Column(Integer)