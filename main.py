import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.routers import recordatorios
from bot.client import iniciar_bot
from database.db import conectar_db, cerrar_db
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    await conectar_db()
    tarea_bot = asyncio.create_task(iniciar_bot())
    yield
    await cerrar_db()
app = FastAPI(title="API recordatorios", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["https://reco-bot-py.onrender.com"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(recordatorios.router)

@app.get("/", tags=["Estado"])
def estado_servidor():
    return {"mensaje": "El servidor y la estructura modular estan funcionando."}

