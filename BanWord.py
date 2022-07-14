import discord 
from discord.ext import commands
from DataBase import *

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='ç', description='Bot de prueba',  intents=intents)

@bot.event
async def on_message(message):
    print(message.content)
    if message.content in BanWords:
        await message.delete()
        await message.channel.send("The word {} is ban in this server.".format(message.content))
    return 

#Token of the bot
bot.run(DiscordToken)