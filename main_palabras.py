#initialization the libraries
from multiprocessing import AuthenticationError
from pyexpat.errors import messages
import discord 
from discord.ext import commands
from matplotlib.pyplot import title
from DataBase import *

from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member
import requests
from discord.utils import get



#Create the bot 
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='ç', description='Bot de prueba',  intents=intents)
bot.remove_command('help')


#Commands

@bot.event
async def on_ready():
    """Fuction for the bot is ready"""
    await bot.change_presence(activity=discord.Game(name='çhelp'))
    print("Bot conect\n--------------------------------")

@bot.command()
async def help(ctx):
    """Fuction for send a help message"""
    embed = discord.Embed(title="List of commands", color=0x00ff00)
    embed.add_field(name="Hello", value="Hello World", inline=False)
    embed.add_field(name="BanWord <Word> ", value="Ban a word", inline=False)
    embed.add_field(name="Kick <@User Reason>", value="Kick a user", inline=False)
    embed.add_field(name="Ban <@User Reason>", value="Ban a user", inline=False)
    await ctx.send(embed=embed)



@bot.event
async def on_member_join(member):
    """Fuction for a user join in the server"""
    channel = bot.get_channel(997088393483780176)
    embed = discord.Embed(title= 'The server have new user')
    embed.add_field(name='Name', value=member.name)
    embed.add_field(name='ID', value=member.id)
    embed.set_thumbnail(url=member.avatar_url)
    await member.add_role(997153212819832972)
    await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    """Fuction for a user remove from the server"""
    channel = bot.get_channel(997088393483780176)
    embed = discord.Embed(title= 'The server lost a user ')
    embed.add_field(name='Name', value=member.name)
    embed.add_field(name='ID', value=member.id)
    embed.set_thumbnail(url=member.avatar_url)
    
    await channel.send(embed=embed)



@bot.command()
async def Hello(ctx):
    """Fucntion to send Hello World"""
    await ctx.send("Hello World")


@bot.command(pass_context=True)
async def join(ctx):
    """Fucntion for join a voice channel"""
    if ( ctx.author.voice ):
        channel= ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel, You need to be in a voice channel to use this command")

@bot.command(pass_context=True)
async def leave(ctx):
    """Fucntion for join a leave a voice channel"""
    if ( ctx.voice_client ):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I leave your voice channel")
    else:
        await ctx.send("I am not a voice channel, I need to be in a voice channel to use this command")


@bot.command()
async def BanWord(ctx,*, message: str):
    """Fuction for add a word to the ban list"""
    BanWords.append(message)
    print(BanWords)
    await ctx.send("The word {} has been added to the ban list".format(message))

@bot.command()
async def Stop(ctx):
    """Fuction for stop the bot but The admins can use this command"""
    if ctx.author.id == 327803995244593153:
        await ctx.send("I am stopping")
        await bot.logout()
    else:
        await ctx.send("You must't use this command to stop the bot")

@bot.event
async def on_message(message):
    """Fuction for detect some specific words that user write in the channels"""
    print("Mensaje: " + message.content)
    
    #Fuccion for detect if the user write a word that is in the ban list
    words = message.content.split(" ")
    for i in words:
        if i[0] != "ç":
            Words.addWord(i)
            if i in BanWords:
                if message.author.id != 993090727183667250 :
                    
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} Don't use that word!, Because this word is banned")
                    bot.dispatch('profanity', message, i)
                    print(f"{message.author.mention} Don't use that word!, Because this word is banned")
                    return
    
    await bot.process_commands(message)


#Token of the bot
bot.run(DiscordToken)