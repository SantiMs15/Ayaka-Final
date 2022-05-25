from http import client
import os
import discord
from dotenv import load_dotenv

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_connect():
    print("Lets Translate!")


client.run(TOKEN) 