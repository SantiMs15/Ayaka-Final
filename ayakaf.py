import os
import discord
from dotenv import load_dotenv

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}, Lets Translate!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!Hello Ayaka'):
        await message.channel.send("Hi I can translate whatever you want!")

@client.event
async def on_member_join(member):
    await member.create.dm()
    await member.dm_channel.send(f"Bienvenido seas {member}. Este es el servidor de prueba de nuestra bot Ayaka, que esperamos que nos haga pasar la materia :v")

client.run(TOKEN) 
#prueba
