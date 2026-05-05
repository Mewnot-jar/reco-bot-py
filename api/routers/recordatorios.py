from fastapi import APIRouter
from api.schemas import NuevoRecordatorio
import database.db as database

router = APIRouter()


@router.get("/recordatorios", tags=["Recordatorios"])
async def obtener_recordatorios():
    cursor = database.coleccion_recordatorios.find({}, {"_id":0})
    recordatorios = await cursor.to_list(length=100)
    return recordatorios

@router.post("/recordatorios", tags=["Recordatorios"])
async def crear_recordatorio(recordatorio: NuevoRecordatorio):
    nuevo_dato = recordatorio.model_dump()
    await database.coleccion_recordatorios.insert_one(nuevo_dato)

    if "_id" in nuevo_dato:
        del nuevo_dato["_id"]

    return {"mensaje": "Recordatorio creado correctamente."}
