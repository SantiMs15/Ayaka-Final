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

client.run(TOKEN) 
