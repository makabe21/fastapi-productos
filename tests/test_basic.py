from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_productos():
    response = client.get("/productos/")
    assert response.status_code == 200

def test_create_producto():
    producto = {
        "nombre": "Laptop",
        "descripcion": "Dell",
        "precio": 5000,
        "stock": 10
    }

    response = client.post("/productos/", json=producto)
    assert response.status_code == 200

def test_update_producto():
    producto = {
        "nombre": "Laptop Pro",
        "descripcion": "Dell X",
        "precio": 6000,
        "stock": 5
    }

    response = client.put("/productos/1", json=producto)
    assert response.status_code == 200

def test_delete_producto():
    response = client.delete("/productos/1")
    assert response.status_code == 200