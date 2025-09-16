from fastapi import FastAPI, HTTPException
from scoring import evaluar_tc_cliente
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/evaluaciones/tarjetas")
def evaluarTarjetacredito(edad: int, ingresos: float):
    if edad < 0 or ingresos < 0:
        raise HTTPException(status_code=400, detail="Datos inválidos")
    
    resultado = evaluar_tc_cliente(edad, ingresos)
    if resultado["califica"]:
        return {
        "status": "APROBADO",
        "mensaje": f"Felicidades, usted accede a {resultado['categoria']}",
        "data": resultado
    }
    else:
        return {
        "status": "RECHAZADO",
        "mensaje": "No cumple con los requisitos para acceder a una tarjeta de crédito",
        "data": resultado
    }