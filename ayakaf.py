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
async def on_reaction_add(reaction, user):
    print("emoji-id")
    print(reaction.emoji.id)
    if reaction.count==1:
        if reaction.emoji.id==979203901544890438:
            tradu= Translator ()
            trans_en= tradu.translate(reaction.message.content, src='es' , dest='en')
            await reaction.message.channel.send(trans_en.text)
client.run(TOKEN)




