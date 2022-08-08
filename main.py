#initialization the libraries
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
@has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, * , reason=None):
    """Fuction for  Kick a user"""
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

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, * , reason= None):
    """#Fuction for Ban a user"""
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


@bot.command(pass_context=True)
@has_permissions(manage_messages=True)
async def setRole(ctx, user: discord.Member,* , role: discord.Role):
    """Fuction to set a role to a user"""
    print(role)
    if role is user.roles:
        await ctx.send(f"{user.username} has this role")
    else:
        print("hola")
        await user.add_roles(role)
        await ctx.send(f"The role {role.username} has been added to the user {user.username}")

@setRole.error
async def role_error(ctx, error):
    if inistance (error,commands.MissingPermissions):
        await ctx.send("You dont have the permission to use this command")



#Token of the bot
bot.run(DiscordToken)