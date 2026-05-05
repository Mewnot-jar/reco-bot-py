from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API recordatorios")

class NuevoRecordatorio(BaseModel):
    nombre: str
    asignatura: str
    fecha: str
    descripcion: str
    seccion: str

test_db = []

@app.get("/")
def estado_servidor():
    return {"mensaje": "Servidor On"}

@app.get("/recordatorios")
def obtener_recordatorios():
    return test_db

@app.post("/recordatorio")
def crear_recordatorio(recordatorio: NuevoRecordatorio):
    nuevo_dato = recordatorio.model_dump()
    test_db.append(nuevo_dato)
    return {"mensaje": "Nuevo recordatorio agregado con exito."}

