```python
import discord
from discord.ext import commands

Token de ton bot (le token est à garder privé !)
TOKEN = 'TON_BOT_TOKEN'
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