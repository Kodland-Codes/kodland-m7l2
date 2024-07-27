import discord
from discord.ext import commands
from model import get_class
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
    
@bot.command()
async def merhaba(ctx):
    await ctx.send("Selam!")
    

@bot.command('dansbozkurttürkiye')
async def dansbozkurtturkiye(ctx):
    await ctx.send("https://www.youtube.com/shorts/qftQ6tcCrPM!")

@bot.command()
async def bye(ctx):
    await ctx.send(":saluting_face:")
    
@bot.command()
async def naber(ctx):
    await ctx.send("İyiyim,senden naber")


bot.run('TOKEN')
