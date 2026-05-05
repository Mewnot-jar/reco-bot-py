from fastapi import APIRouter
from api.schemas import NuevoRecordatorio
import database.db as database
from bson import ObjectId
router = APIRouter()


@router.get("/recordatorios", tags=["Recordatorios"])
async def obtener_recordatorios():
    cursor = database.coleccion_recordatorios.find({})
    recordatorios = await cursor.to_list(length=100)
    for tarea in recordatorios:
        tarea["id"] = str(tarea["_id"])
        del tarea["_id"]
    return recordatorios

@router.post("/recordatorios", tags=["Recordatorios"])
async def crear_recordatorio(recordatorio: NuevoRecordatorio):
    nuevo_dato = recordatorio.model_dump()
    await database.coleccion_recordatorios.insert_one(nuevo_dato)

    if "_id" in nuevo_dato:
        del nuevo_dato["_id"]

    return {"mensaje": "Recordatorio creado correctamente."}

@router.delete("/recordatorios{id}", tags=["Recordatorios"])
async def borrar_recordatorio(id: str):
    filtro = {"_id": ObjectId(id)}
    resultado = await database.coleccion_recordatorios.delete_one(filtro)
    if resultado.deleted_count > 0:
        return {"mensaje": "Tarea eliminada."}
    else:
        return {"mensaje": "Error 404"}
    
