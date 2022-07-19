#Library initialization 
from cmath import e
from http import server
import discord
from discord.ext import commands
from matplotlib.style import use
from class_user import *

#Do a bot login
bot = commands.Bot(command_prefix='ç', description='Bot de prueba', help_command=None)

#Make a event to listen the messages 
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

#Make a event when the bot is ready
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='çhelp'))
    print('Bot conectado')

#Make a event to return info of the server
@bot.command()
async def info(ctx):
    
    embed = discord.Embed(title= 'Info of server', description=' Informacion:', color=0x00ff00)
    embed.add_field(name='Name of server', value=ctx.guild.name )
    embed.add_field(name='ID of servidor', value=ctx.guild.id)
    embed.add_field(name="Users quantity", value=f'{ctx.guild.member_count}')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    
    await ctx.send(embed=embed)

#Make a event to return info of the user
@bot.command()
async def userinfo(ctx, *, user: discord.User ):
    #Info of the discord user
    embed = discord.Embed(title= 'Info of user', description='Info:', color=0x00ff00)
    embed.add_field(name='Name of the user', value=user.name )
    embed.add_field(name='ID:', value=user.id)
    embed.set_thumbnail(url=user.avatar_url)
    
    #Info of the user in the list
    for user_i in user_list:
        if user_i.get_name() == user.name:
            embed.add_field(name='Warnings:', value=user_i.get_warnings())
            break
    await ctx.send(embed=embed)

#Fuction to return the info of the server
@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(title = f"{ctx.name} Info", description = "Information of this Server", color = discord.Colour.blue())
    embed.add_field(name = '🆔Server ID', value = f"{ctx.id}", inline = True)
    embed.add_field(name = '📆Created On', value = ctx.created_at.strftime("%b %d %Y"), inline = True)
    embed.add_field(name = '👑Owner', value = f"{ctx.owner}", inline = True)
    embed.add_field(name = '👥Members', value = f'{ctx.member_count} Members', inline = True)
    embed.add_field(name = '💬Channels', value = f'{ctx.text_channel_count} Text | {ctx.voice_channel_count} Voice', inline = True)
    embed.add_field(name = '🌎Region', value = f'{ctx.region}', inline = True)
    embed.set_thumbnail(url = ctx.icon_url)
    embed.set_footer(text = "⭐ • Duo")    
    embed.set_author(name = f'{ctx.name}', url = embed.Empty, icon_url = {ctx.icon_url})
    await ctx.send(embed=embed)

#Fuction to add a warning to the user
@bot.command()
async def addwarning(ctx, *, user: discord.User ):
    for user_i in user_list:
        if user_i.name == user.name:
            user_i.addwarning()
            await ctx.send(f"The user {user.name} has been warn")


#Fuction to add a user to the list of users
@bot.command()
async def adduser(ctx, *, user: discord.User ):
    user = User(user.name, user.id, user.avatar_url)
    user_list.append(user)
    await ctx.send(f'{user.name} was added to the list')


#Fuction to set a role for the user
@bot.command()
async def setRole(ctx, *, user: discord.User,role:discord.Role ):
    print(user.name)
    if role in user.roles:
        print(role.name)
        #await ctx.send(f'{user} already has the role {role}')
    else :
        await user.add_roles(role)
        #await ctx.send (f'{user.name} has been added to the role {role.name}')

#F


#List to save the users
user_list = []

bot.run('OTkzMDkwNzI3MTgzNjY3MjUw.GGpX7c.w2lT-w4fRuH266hq02IxoWAJSG1H3Zwpp63ai0')
