from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services import producto_service
from app.schemas.producto_schema import ProductoCreate

router = APIRouter(prefix="/productos")

# LISTAR PRODUCTOS
@router.get("/")
def listar(db: Session = Depends(get_db)):
    return producto_service.listar_productos(db)

# CREAR PRODUCTO
@router.post("/")
def crear(producto: ProductoCreate, db: Session = Depends(get_db)):
    return producto_service.crear_producto(db, producto)

# ACTUALIZAR PRODUCTO
@router.put("/{id}")
def actualizar(id: int, producto: ProductoCreate, db: Session = Depends(get_db)):
    return producto_service.actualizar_producto(db, id, producto)

# ELIMINAR PRODUCTO
@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    return producto_service.eliminar_producto(db, id)