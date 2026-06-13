import discord
from discord.ext import commands


class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        """Conecta el bot al canal de voz donde estés"""
        if not ctx.author.voice:
            await ctx.send("❌ Debes estar en un canal de voz!")
            return

        channel = ctx.author.voice.channel
        try:
            await channel.connect()
            await ctx.send(f"✅ Conectado a {channel.name}")
        except Exception as e:
            await ctx.send(f"❌ Error: {e}")

    @commands.command()
    async def leave(self, ctx):
        """Desconecta el bot del canal de voz"""
        if not ctx.voice_client:
            await ctx.send("❌ No estoy en un canal de voz!")
            return

        await ctx.voice_client.disconnect()
        await ctx.send("✅ Desconectado")


async def setup(bot):
    await bot.add_cog(Voice(bot))
