#initialization the libraries
from unicodedata import category
import discord 
from discord.ext import commands
from matplotlib.pyplot import title
from pruebas_DataBase import *
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member
import requests
from discord.utils import get
from datetime import datetime


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

@bot.command()
async def suggestion(message):
    """"Fuction to made a suggestion for suggestion"""
    suggestation = message
    
    print("Suggestion:" + suggestion)
    
#Token of the bot
bot.run(DiscordToken)