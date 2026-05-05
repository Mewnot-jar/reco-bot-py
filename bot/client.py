import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot on")

async def iniciar_bot():
    extensiones = [
        "bot.cogs.tareas",
        "bot.cogs.configuracion",
        "bot.cogs.notificaciones",
    ]
    for ext in extensiones:
        if ext not in bot.extensions:
            await bot.load_extension(ext)
            print(f"Modulo: {ext} cargado.")
    await bot.start(TOKEN)