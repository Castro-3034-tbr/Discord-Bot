#initialization the libraries
import discord 
from discord.ext import commands
from apykey import *


#Create the bot 
bot = commands.Bot(command_prefix='ç', description='Bot de prueba')


"""Commands"""

#Fuction for the bot is ready
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='çhelp'))
    print("Bot conect\n --------------------------------")

#Fuction for a user join in the server

intents = discord.Intents.default()
intents.members = True

@bot.event
async def on_menber_join(member):
    chanel = bot.get_channel("966262686314823680")
    await chanel.send(f"{member.mention} has joined the server")

#Token of the bot
bot.run(keys.get_discord_key())