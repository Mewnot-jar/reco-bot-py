# 🤖 RecordBOT - API & Discord Bot (Backend)

![Estado: En Desarrollo](https://img.shields.io/badge/Estado-En%20Desarrollo-orange)

Un sistema híbrido desarrollado en **Python** que combina una API RESTful rápida y un bot de Discord multi-servidor. Diseñado para gestionar y notificar automáticamente sobre tareas, evaluaciones y recordatorios académicos.

## 🚀 Características Principales

* **Arquitectura Híbrida:** Ejecuta simultáneamente un servidor web (FastAPI) y un cliente de Discord (`discord.py`) mediante tareas asíncronas (`asyncio`).
* **Bot Multi-servidor (Cogs):** Estructura modular escalable. Permite a los administradores configurar canales de recepción dinámicamente mediante el comando `!setcanal`.
* **Notificaciones Autónomas:** Un bucle en segundo plano (Task Loop) consulta la base de datos y envía recordatorios automáticos a todos los servidores registrados.
* **Base de Datos NoSQL:** Integración asíncrona con **MongoDB** utilizando el driver `Motor`.

## 🛠️ Tecnologías Utilizadas

* **Python 3.10+**
* **FastAPI:** Para el enrutamiento de la API REST.
* **discord.py:** Framework para la conexión e interacción con la API de Discord.
* **Motor (Motor-Asyncio):** Driver asíncrono para MongoDB.
* **Uvicorn:** Servidor ASGI para producción.

## 📂 Estructura del Proyecto

\`\`\`text
reco-bot-py/
├── api/                # Lógica de la API REST (FastAPI)
│   └── routers/        # Endpoints (ej. /recordatorios)
├── bot/                # Lógica del Bot de Discord
│   ├── client.py       # Inicialización y motor del bot
│   └── cogs/           # Módulos (configuracion.py, notificaciones.py, tareas.py)
├── database/           # Conexión y esquemas de MongoDB
├── main.py             # Archivo raíz (Inicia FastAPI y el Bot)
└── requirements.txt    # Dependencias del proyecto
\`\`\`

## ⚙️ Configuración Local

1. Clona este repositorio.
2. Crea un entorno virtual: `python -m venv venv`
3. Activa el entorno e instala las dependencias: `pip install -r requirements.txt`
4. Crea un archivo `.env` en la raíz con las siguientes variables:
   \`\`\`env
   DISCORD_TOKEN=tu_token_de_discord
   MONGODB_URI=tu_cadena_de_conexion_mongodb
   \`\`\`
5. Ejecuta el servidor: `uvicorn main:app --reload`

## 🌐 Despliegue
Este backend está optimizado para ser desplegado en servicios en la nube como **Render**, utilizando el archivo `main.py` como punto de entrada de Uvicorn.
