#initialization the libraries
import discord 
from discord.ext import commands
from matplotlib.pyplot import title
from pruebas_DataBase import *
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member
import requests
from discord.utils import get
from datetime import datetime

import googletrans


#Create the bot 
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='ç', description='Bot de prueba',  intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    """Fuction for the bot is ready"""

    
    #Print a message in the terminal
    print("Bot conect")

translator = googletrans.Translator()

@bot.command()
async def Translate(ctx, *, text):
    """Function to translate a word"""
    #Get the text to translate
    text = text.split(",")
    textIn = text[0]
    lenguage1 = text[1]
    lenguage2 = text[2]

    translated = translator.translate(textIn, src="es" ,dest="en" ) 
    
    await ctx.send(translated)

#Token of the bot
bot.run(DiscordToken)