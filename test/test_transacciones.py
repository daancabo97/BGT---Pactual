# backend/tests/test_transacciones.py
from fastapi.testclient import TestClient
from app.main import app
from bson import ObjectId


client = TestClient(app)


CLIENTE_ID = str(ObjectId()) 
PRODUCTO_ID = str(ObjectId())  


def test_crear_cliente():
    cliente_data = {
        "nombre": "Juan",
        "apellidos": "Pérez",
        "ciudad": "Bogotá",
        "saldo": 500000
    }
    response = client.post("/clientes/", json=cliente_data)
    assert response.status_code == 200
    assert "id" in response.json()
    global CLIENTE_ID
    CLIENTE_ID = response.json()["id"]


def test_crear_producto():
    producto_data = {
        "nombre": "FPV_BTG_PACTUAL_RECAUDADORA",
        "monto_minimo": 75000,
        "categoria": "FPV"
    }
    response = client.post("/productos/", json=producto_data)
    assert response.status_code == 200
    assert "id" in response.json()
    global PRODUCTO_ID
    PRODUCTO_ID = response.json()["id"]


def test_suscripcion_fondo():
    data = {
        "tipo": "apertura",
        "idCliente": CLIENTE_ID,  
        "idProducto": PRODUCTO_ID,  
        "fecha": "2024-10-15T00:00:00Z",
        "monto": 75000
    }
    response = client.post("/transacciones/apertura/", json=data)
    assert response.status_code == 200
    assert "mensaje" in response.json()
    assert response.json()["mensaje"] == f"Suscripción al fondo FPV_BTG_PACTUAL_RECAUDADORA realizada con éxito"


def test_cancelar_suscripcion():
    data = {
        "tipo": "cancelacion",
        "idCliente": CLIENTE_ID, 
        "idProducto": PRODUCTO_ID,  
        "fecha": "2024-10-15T00:00:00Z",
        "monto": 75000
    }
    response = client.post("/transacciones/cancelacion/", json=data)
    assert response.status_code == 200
    assert "mensaje" in response.json()
    assert response.json()["mensaje"] == f"Cancelación del fondo FPV_BTG_PACTUAL_RECAUDADORA realizada con éxito"


def test_ver_historial():
    response = client.get("/transacciones/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  


def test_obtener_clientes():
    response = client.get("/clientes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  


def test_obtener_cliente_por_id():
    response = client.get(f"/clientes/{CLIENTE_ID}")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Juan"


def test_actualizar_saldo_cliente():
    nuevo_saldo = 600000
    response = client.put(f"/clientes/{CLIENTE_ID}", json={"nuevo_saldo": nuevo_saldo})
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Saldo actualizado correctamente"


def test_obtener_productos():
    response = client.get("/productos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  


def test_crear_inscripcion():
    inscripcion_data = {
        "idCliente": CLIENTE_ID,
        "idProducto": PRODUCTO_ID
    }
    response = client.post("/inscripciones/", json=inscripcion_data)
    assert response.status_code == 200
    assert "id" in response.json()
