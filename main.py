#initialization the libraries
import discord 
from discord.ext import commands
from DataBase import *


#Create the bot 
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='ç', description='Bot de prueba',  intents=intents)



"""Commands"""

#Fuction for the bot is ready
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='çhelp'))
    print("Bot conect\n--------------------------------")

#Fuction for a user join in the server
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(966262686314823680)
    embed = discord.Embed(title= 'The server have new user')
    embed.add_field(name='Name', value=member.name)
    embed.add_field(name='ID', value=member.id)
    embed.set_thumbnail(url=member.avatar_url)
    
    await channel.send(embed=embed)

#Fuction for a user remove from the server
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(966262686314823680)
    embed = discord.Embed(title= 'The server lost a user ')
    embed.add_field(name='Name', value=member.name)
    embed.add_field(name='ID', value=member.id)
    embed.set_thumbnail(url=member.avatar_url)
    
    await channel.send(embed=embed)


#Fucntion to send Hello World
@bot.command()
async def Hello(ctx):
    await ctx.send("Hello World")

#Fucntion for join a leave a voice channel
@bot.command(pass_context=True)
async def join(ctx):
    if ( ctx.author.voice ):
        channel= ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel, You need to be in a voice channel to use this command")

@bot.command(pass_context=True)
async def leave(ctx):
    if ( ctx.voice_client ):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I leave your voice channel")
    else:
        await ctx.send("I am not a voice channel, I need to be in a voice channel to use this command")


#Fuction for add a word to the ban list
@bot.command()
async def BanWord(ctx,*, message: str):
    BanWords.append(message)
    print(BanWords)
    await ctx.send("The word {} has been added to the ban list".format(message))

#Fuction for detect some specific words that user write in the channels 
@bot.event
async def on_message(message):
    print(message.content)
    if message.content in BanWords:
        await message.delete()
        await message.channel.send("The word {} is ban in this server.".format(message.content))
    return 


#Token of the bot
bot.run(DiscordToken)