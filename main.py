#initialization the libraries
from logging import error
from re import A
import discord 
from discord.ext import commands
from DataBase import *
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member
import requests



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
    channel = bot.get_channel(997088393483780176)
    embed = discord.Embed(title= 'The server have new user')
    embed.add_field(name='Name', value=member.name)
    embed.add_field(name='ID', value=member.id)
    embed.set_thumbnail(url=member.avatar_url)
    
    await channel.send(embed=embed)

#Fuction for a user remove from the server
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(997088393483780176)
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
    for i in BanWords: # Go through the list of bad words;
        if message.content in BanWords:
            await message.delete()
            await message.channel.send(f"{message.author.mention} Don't use that word!, Because this word is banned")
            bot.dispatch('profanity', message, i)
            return # So that it doesn't try to delete the message again, which will cause an error.
    await bot.process_commands(message)


#Fuction for  Kick a user
@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, * , reason=None):
    print("Kick a user")
    print("Reason",reason)
    await member.kick(reason=reason)
    
    embed = discord.Embed(title= 'A admin has kicked a user')
    embed.add_field(name='Name', value=member.name)
    embed.add_field(name='ID', value=member.id)
    embed.add_field(name='Reason', value=reason)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have the permission to use this command")


#Fuction for Ban a user
@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, * , reason= None):
    await member.ban(reason=reason)
    embed = discord.Embed(title= 'A admin has banned a user')
    embed.add_field(name='Name', value=member.name)
    embed.add_field(name='ID', value=member.id)
    embed.add_field(name='Reason', value=reason)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have the permission to use this command")


#Token of the bot
bot.run(DiscordToken)