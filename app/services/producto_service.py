from app.repositories import producto_repository as repo

def listar_productos(db):
    return repo.get_all(db)

def crear_producto(db, producto):
    return repo.create(db, producto)

def actualizar_producto(db, producto_id, producto):
    return repo.update(db, producto_id, producto)

def eliminar_producto(db, producto_id):
    return repo.delete(db, producto_id)