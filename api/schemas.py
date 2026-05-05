from pydantic import BaseModel

class NuevoRecordatorio(BaseModel):
    nombre: str
    asignatura: str
    fecha: str
    descripcion: str
    seccion: str