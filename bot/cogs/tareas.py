import discord
from discord.ext import commands
import database.db as database

class Tareas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send(f"Pong! {ctx.author.name.capitalize()} el modulo de tareas funciona correctamente.")

    @commands.command(name="trabajos")
    async def trabajos(self, ctx):
        if database.coleccion_recordatorios is None:
            await ctx.send("No hay conexion con DB.")
            return
        
        cursor = database.coleccion_recordatorios.find({}, {"_id": 0})
        lista_trabajos = await cursor.to_list(length=100)

        if not lista_trabajos:
            await ctx.send("No hay trabajos registrados.")

        embed = discord.Embed(
            title="📚 Trabajos y recordatorios pendientes",
            description="Aqui tienes la lista de tareas: ",
            color=discord.Color.blue()
        )

        for tarea in lista_trabajos:
            titulo_campo = f"📌{tarea['asignatura']} - {tarea['nombre']}"
            detalle_campo = (
                f"**📅 Fecha:** {tarea['fecha']}\n"
                f"**🏷️ Seccion:** {tarea['seccion']}\n"
                f"**📝 Descripcion:** {tarea['descripcion']}"
            )
            embed.add_field(name=titulo_campo, value=detalle_campo, inline=False)
        await ctx.send(embed=embed)
async def setup(bot):
    await bot.add_cog(Tareas(bot))