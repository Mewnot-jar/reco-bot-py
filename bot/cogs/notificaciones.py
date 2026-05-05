import discord
from discord.ext import commands, tasks
import database.db as database

class Notificaciones(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.enviar_lista_auto.start()
    def cog_unload(self):
        self.enviar_lista_auto.cancel()

    @tasks.loop(minutes=1)
    async def enviar_lista_auto(self):
        await self.bot.wait_until_ready()

        try:
            col_config = database.coleccion_configuraciones
            col_tareas = database.coleccion_recordatorios

            cursor_tareas = col_tareas.find()
            lista_trabajos = await cursor_tareas.to_list(length=100)

            if not lista_trabajos:
                return
            
            embed =  discord.Embed(
                title="📢 Evaluaciones Pendientes",
                description="Aqui tienes la lista actualizada de las tareas pendientes.",
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

            cursor_config = col_config.find()
            lista_configuraciones = await cursor_config.to_list(length=500)

            for configuracion in lista_configuraciones:
                canal = self.bot.get_channel(configuracion["channel_id"])
                if canal:
                    await canal.send(embed=embed)
        except Exception as e:
            print(e)
async def setup(bot):
    await bot.add_cog(Notificaciones(bot))