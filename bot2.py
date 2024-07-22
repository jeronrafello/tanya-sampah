import discord
from discord.ext import commands
from kodland_utils import *
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def flip(ctx):
    await ctx.send("flip_coin")

@bot.command()
async def meme(ctx):
    selected = random.choice(os.listdir('images'))
    with open(f'images/{selected}','rb') as f:
        pictures = discord.File(f)
    await ctx.send(file=pictures)

# Daftar sampah

organik = ['kotoran', 'makanan basi','rambut']
kertas  = ['kardus', 'koran', 'cup plastik']
plastik = ['kantong plastik', 'botol kemasan','']
logam   = ['kawat', 'besi berkarat','kaleng']

@bot.command()
async def tanya_sampah(ctx):
    await ctx.send('apa sampah yang ingin diperiksa ?')
    message = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    message = str(message.content)

if  message.lower()  in organik:
    await ctx.send(' itu sampah organik ')
    await ctx.send(' daur ulang ')
elif message.lower() in plastik:     
    await ctx.send(' buat sesuatu unik ')
    await ctx.send('bisa buat kotak pencil nih')
elif message.lower() in kertas:
    await ctx.send(' dibuat pupuk ')
    await ctx.send(' bisa buat kertas pesawat ')
elif message.lower() in logam:  
    await ctx.send(' berkilau ')
    await ctx.send(' menempel dengan magnet ')
else : 
    await ctx.send(' itu bukan sampah !')
