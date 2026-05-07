import discord
from discord.ext import commands
import database.db as database

class Configuracion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="setcanal")
    @commands.has_permissions(administrator=True)
    async def set_canal_recordatorios(self, ctx, canal: discord.TextChannel):
        try:
            col_config = database.coleccion_configuraciones

            await col_config.update_one(
                {"guild_id": ctx.guild.id},
                {
                    "$set": {
                        "guild_name": ctx.guild.name,
                        "channel_id": canal.id,
                        "channel_name": canal.name,
                    }
                },
                upsert=True
            )
            await ctx.send(f"Configuracion exitosa - Canal seleccionado: {canal.mention}")
        except Exception as e:
            print(e)
            await ctx.send(e)
    @set_canal_recordatorios.error
    async def set_canal_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes permisos, bobo.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Falta mencionar el canal.")
        elif isinstance(error, commands.ChannelNotFound):
            await ctx.send("No se encontro el canal.")

    @commands.command(name="link")
    async def obtener_link(self, ctx):
        await ctx.send(f"Entra a https://front-reco-bot-react.vercel.app/ para configurar los recordatorios.")

async def setup(bot):
    await bot.add_cog(Configuracion(bot))