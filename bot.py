```python
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

Charger les variables d'environnement
load_dotenv()

Récupérer le token depuis .env
TOKEN = os.getenv("DISCORD_TOKEN")

Initialisation du bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

Quand le bot est prêt
@bot.event
async def on_ready():
    print(f'Nous avons connecté {bot.user}!')

Commande simple pour dire "Bonjour"
@bot.command()
async def hello(ctx):
    await ctx.send("Salut! Je suis ton bot modérateur!")