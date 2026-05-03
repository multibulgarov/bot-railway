import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"БОТ ЗАПУЩЕН: {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Привет 👋 я работаю!")

bot.run(TOKEN)
