import os
import asyncio
from dotenv import load_dotenv
from threading import Thread
from flask import Flask

import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# Crear app Flask para mantener el bot activo
app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    """Endpoint para UptimeRobot"""
    return {"status": "online", "bot": str(bot.user)}, 200

def run_server():
    """Ejecuta el servidor Flask en un thread separado"""
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(
    command_prefix="&",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    await load_cogs()

async def load_cogs():
    """Carga todos los cogs de la carpeta cogs/"""
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Cog cargado: {filename}")
            except Exception as e:
                print(f"Error cargando {filename}: {e}")

# Iniciar servidor Flask en un thread antes de ejecutar el bot
server_thread = Thread(target=run_server, daemon=True)
server_thread.start()
print("Servidor HTTP iniciado en puerto 5000")

bot.run(TOKEN)