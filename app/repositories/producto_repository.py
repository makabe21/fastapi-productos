from app.models.producto import Producto

def get_all(db):
    return db.query(Producto).all()

def get_by_id(db, producto_id):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def create(db, producto):
    nuevo = Producto(**producto.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update(db, producto_id, data):
    producto = get_by_id(db, producto_id)
    if producto:
        producto.nombre = data.nombre
        producto.descripcion = data.descripcion
        producto.precio = data.precio
        producto.stock = data.stock
        db.commit()
        db.refresh(producto)
    return producto

def delete(db, producto_id):
    producto = get_by_id(db, producto_id)
    if producto:
        db.delete(producto)
        db.commit()
    return producto