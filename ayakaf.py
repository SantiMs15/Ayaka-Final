from gettext import translation
import discord
import googletrans
from discord.ext import commands
from googletrans import Translator
import os
from dotenv import load_dotenv
client=discord.Client()
load_dotenv()
TOKEN=os.getenv('TOKEN')
@client.event
async def on_ready():
    print("Tamo activos")
@client.event
async def on_reaction_add(reaction, user):
    channel=reaction.message.channel
    if reaction.emoji=='us':
        translation = translate_text('en', reaction.message.content)
client.run(TOKEN)
