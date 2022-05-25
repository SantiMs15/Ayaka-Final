import os
import discord
from dotenv import load_dotenv

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!translate'):
        await message.channel.send("I can translate whatever you want!")

@client.event
async def on_connect():
    print("Lets Translate!")


client.run(TOKEN) 
