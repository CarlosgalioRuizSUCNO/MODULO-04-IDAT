from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_endpoitn_rechazo():
    response = client.get("/evaluaciones/tarjetas?edad=17&ingresos=2000")
    assert response.status_code == 200
    assert response.json()["status"] == "RECHAZADO"

def test_endpoint_regular():
    response = client.get("/evaluaciones/tarjetas?edad=24&ingresos=3500")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "APROBADO"
    assert body["data"]["categoria"] == "Tarjeta OH"

def test_endpoint_premium():
    response = client.get("/evaluaciones/tarjetas?edad=30&ingresos=7500")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "APROBADO"
    assert body["data"]["categoria"] == "Tarjeta OH Premium"

def test_endpoint_datos_invalido():
    response = client.get("/evaluaciones/tarjetas?edad=-5&ingresos=30")
    assert response.status_code == 400
    assert response.json()["detail"] == "Datos inválidos"