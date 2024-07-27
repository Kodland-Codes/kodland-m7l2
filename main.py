import discord
from discord.ext import commands
from model import get_class
import requests
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def merhaba(ctx):
    await ctx.send("Merhaba! Ben bir botum!")


@bot.command()
async def check(ctx): #Yapay Zeka Modeli
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(f"./images/{attachment.filename}")
            await ctx.send(get_class(model_path="model1.h5", labels_path="labels1.txt", image_path=f"./images/{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")

@bot.command()
async def sinif_arkadaslarim(ctx): #Yapay Zeka Modeli
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(f"./images/{attachment.filename}")
            await ctx.send(get_class(model_path="model2.h5", labels_path="labels2.txt", image_path=f"./images/{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")


@bot.command()
async def rastgele_film(ctx):
    filmler = ["x", "y", "z"]
    await ctx.send(random.choice(filmler))


@bot.command() #Rastgele resim gonderir
async def rastgele_resim(ctx):
    resimler_listesi = os.listdir('resimler') #['resim1.jpeg', 'resim2.jpeg', 'resim3.jpeg']
    with open(f'resimler/{random.choice(resimler_listesi)}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


@bot.command() #Rastgele resim gonderir
async def rastgele_gif(ctx):
    resimler_listesi = os.listdir('gifler') #['resim1.jpeg', 'resim2.jpeg', 'resim3.jpeg']
    with open(f'gifler/{random.choice(resimler_listesi)}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

bot.run('TOKEN')
