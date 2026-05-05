import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

client = None
db = None
coleccion_recordatorios = None
coleccion_configuraciones = None

async def conectar_db():
    global cliente, db, coleccion_recordatorios, coleccion_configuraciones
    try:
        client = AsyncIOMotorClient(MONGODB_URI)
        db = client.reco
        coleccion_recordatorios = db.recordatorios
        coleccion_configuraciones = db.configuraciones

        await client.admin.command('ping')
        print("MongoDB Atlas ON")
    except Exception as e:
        print(e)
async def cerrar_db():
    global client
    if client:
        client.close()
        print("MongoDB Atlas OFF")