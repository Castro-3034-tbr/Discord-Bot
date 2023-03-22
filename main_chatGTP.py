#initialization the libraries
from datetime import datetime
from DataBase import *

import discord 
from discord.ext import commands
from matplotlib.pyplot import title
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member
import requests
from discord.utils import get
from pyChatGPT import ChatGPT

#Creamos el chat 
token_session = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..HJ70SFhbuHEo1SMw.ISa8uTK7RDqgo-e9nllVNjhE_KBpcyGgvl_k58W0VCoJ8gCNaYbN6UWLhKdr2I0BkBynm1tg1JhrTxlZ1fDt-tkIbZFlPYZRE1F4MW1goS99s03xwXFaamRmNZG8M8m47yCSkUL78SWAwj5JCF8Ae0p2pzU7afo0-_fFgfRRryvuNwXwe8r9qTYNwiUZYiS8b3fKi3QQavcNyE_I8sNjGxc1eZB8yqAr1xSw754Z1lLzb7ohE6946CzrI7uKZ6l0eZiuKYDauuuMhTuF9dYxtuLf5SFyFPmKKOsT9WScUN_6IhoeHl8xjT7WLdkBFoMGHdkKj-sm_DOU2hC_DGfeoPXbTYsGPIAxZEdtEITO5TVD0oFKOnENFdTm-ffun1w5JKCOzr6dJyaKPxq54rp1ZCnUJoiVEavWAfVSmqJayCXIcXbz4tvZv0lf_IaqLY9LRZYgGiHr6AvH-zHBVpBcxwBN3v8vVSoYfFU9npWmvJTE3qW0O8yXyxrg_kQJkBUemKbzJdPJjzJQArixLDMyOVTYbzkcvWPTeem044g3-o5hTdn_Ly1VEFKvGv-KunaM5KFJV9NB_9YDwmk8iO4sBy2PBamoFSNtqL44gvc8PBO87z2FhyEEUnjiOBjwLq9r5U18WsaoR-ghlpnBjNrudyDGpcLvEHX3KEnSy6eQ5Nqi-uj8l9Vn4l3q2_d4XQs9S3JlZLckG_7yTFlLirVZ1WNiP-PHqISQHq6i5QY1HLAh71LNGlJCEpIkOKnltuv_lJi6vD0zhGNuwkEYPEbwoqNUgsOQd7nS198pKyVtHF_m6O72RvpU-25RzdkzjBGOPKaX5d0PEnxfiaZfm4Px-KTPlYy48NbaAwjHBYL3-5FHhMVJBozl_5LgmcXtqygwnw30GHyIWZklgtp16ypHUu3Y-aRM5IG5UHQDf4SojtBXgvtsaTBdT_LOMDofQmAwPVlliZuoK_HKiTea41sB5l2zZfZFiMi-HtT2kDvtzRaK0nebsp_KOOmzzUaTszmNFFHOyap66p_g7nO7n1vzZPim7UK-ETckSv_HK5usQTfgaZdZBWUOiI0z7vptOv5haW0bgYCa7d7j6sZFFCCiJluQ0aM_HtIJFiA6k8aOpew7_CWzaO5Jk30XAT7YBmxJPAq4_kvaSTgECWB9AxO6zfdKidF9SdCZKPKjQCB4bMjIVNGkWXt3ZJi6KVOuxvShFLAQ6NeoTwlsZesB89k4IEwr_YsTcVXSXJADMoXqk6ZnBQg31Y8UC0iIaox1NXwL4Zlg3aFHhDa1BSDV_jwv02HoumnmwJTlVvdkIZP9cdSkJ-dse3h1QhyQbfVpZZC72ir6RcItqYVP5PjRlvk1S22sQlgsQI9U6N4eKR9dLNIDFOLOJL67CHk3hWygpjjyESUCz_zbulEFY0q45P-4Enver0X8SrCFln3EHb9opVDArx3FY_0Hy1kmkPF_fV8ocX7CmNZN4LbM7QdNbETOsdvtB8f_EvgRDnxTDLrZohPiKAPEz9qHATNKnSB0qx3ZbCgT1ttjXXqIRD3f5-0Fv_7A-lW5ejmUfuvloeWSzLo33nqO3_mO3j5jZYSkjdVVxE8QE93jaNRYpdmJilV9DJBIbQ7e2EckQU27wKbvumk9-nQE24a9lBQCvS4k0KolYqWNodj-ZsSaH4WDZC_5MdLFm0afB2QOSGsH2_qphosFuOrCWjxe7S0_eMG0Xs5XKDzEVePNvNxUTgVFmuYuDuK56ow4am01VX9l-iBO0RvIpuQ1nMlc2NmZdbdcWrZjC7h3X1QrxEpJpIajeP9oys93Xx5i7joglibYIAeBekupDNvpHYOHRIHuxGvfzaJhZ7YWJCbiBO00lYOSqUyNUtvSH79Cp9-k8ThIXXwEixO2Y7KQOB2HPtZx1eHtOUJc7GTAcNVYNniCungkVP73HetqZ_iKgZIF48ggpiiHfsRe3h1EwqxAuOsAltSRUmCoUO4nMC_WkEWgtVcjTSUKkfaohSL8m7lJlVWbZOjBYVSPCoOnVbnHv1LFsWPLedv2nXhQPI61OGjiWxRztVTwBFpUTDJN9uAQWXtWrU30cKJcUHTGmm3xHdAOYC6GJumBHLZC_5HRIg8SdQJ720-NBz-igCUY7RzOtyQqM6hshn2Ap__kcuetu9lTC7SlA6XrviC18hTUYKGp9825ycPzkLhYOUWF8Y9OkgEsgKuE23Om0A7B5f_aNQvNwgkK1o0cmSN7q1H_JlD6kn8NiuSfP7oIyoI8bqdOAISk6Tfv3sYq_3TmW1ka1d8s3No_hIqGR5BFvsuwo7N5h7BaBz0Gz5u6yQ5CkboT5-PYz8cUSnMcJHmEV8k9Ol0NzVsibX6UEIZn1Ps_xKaBwlencmATm92k5wEG-5xc_TRTuJmil68lHaBsDw.QoF1rFLSqRm11v9RXSFDSQ"
api = ChatGPT(token_session)

#Create the bot 
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='ç', description='Bot de prueba',  intents=intents)
bot.remove_command('help')

#Commands
@bot.event
async def on_ready():
    """Fuction for the bot is ready"""
    #Send a message to the channel
    channel = bot.get_channel(1006225124376191017)
    date = datetime.now()
    await channel.send("Bot conect at: \n\tData: {} \n\tTime: {}".format(date.date(),date.time().strftime("%H:%M:%S")) )
    
    #Change the status of the bot
    await bot.change_presence(activity=discord.Game(name='çhelp'))
    
    #Print a message in the terminal
    print("Bot conect at: \n\tData: {} \n\tTime: {} ".format(date.date(), date.time().strftime("%H:%M:%S")))

@bot.command()
async def help(ctx):
    """Fuction for send a help message"""
    embed = discord.Embed(title="List of commands", color=0x00ff00)
    embed.add_field(name="Hello", value="Hello World", inline=False)
    embed.add_field(name="BanWord <Word> ", value="Ban a word", inline=False)
    embed.add_field(name="Kick <@User Reason>", value="Kick a user", inline=False)
    embed.add_field(name="Ban <@User Reason>", value="Ban a user", inline=False)
    embed.add_field(name="UnBan <@User>", value="UnBan a user", inline=False)
    await ctx.send(embed=embed)


#Events for a user join and leave the server 

@bot.event
async def on_member_join(member):
    """Fuction for a user join in the server"""
    
    #Add the user to the database
    roles = [role for role in member.roles]
    name = member.display_name
    id = str(member.id)
    created_at = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
    joined_at = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
    top_role = str(member.top_role)
    UserDataBase.AddUser(User(name, id, roles ,created_at, joined_at, top_role))
    
    #Send a message to the channel
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
    #Remove the user from the database
    UserDataBase.RemoveUser(member.name)
    #Send a message to the channel
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

@bot.command()
async def Stop(ctx):
    """Fuction for stop the bot but The admins can use this command"""
    if ctx.author.id == 327803995244593153 or ctx.author.id == 718854635674402816:
        await ctx.send("I am stopping")
        await bot.logout()
    else:
        await ctx.send("You must't use this command to stop the bot")

@bot.command()
async def AddUser(ctx, *, member: discord.Member):
    """Function to add a user to the database"""
    
    #Information of the user
    roles = [role for role in member.roles]
    name = member.display_name
    id = str(member.id)
    created_at = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
    joined_at = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
    top_role = str(member.top_role)
    
    #Add the user to the database
    UserDataBase.AddUser(User(name, id, roles ,created_at, joined_at, top_role))
    
    
    await ctx.send("The user {} has been added to the database" .format(member.name))

@bot.command()
async def RemoveUser(ctx,*, user: discord.User):
    """Function to remove a user from the database"""
    
    #Information of the user
    name = user.name
    
    #Remove the user from the database
    UserDataBase.RemoveUser(name)
    
    await ctx.send("The user {} has been removed from the database" .format(name))

@bot.command()
async def AddWarning(ctx, *, member : discord.Member):
    """Function to add a warning to a user"""
    channel = 1058468583837007971
    if ctx.author.id == 718854635674402816:
        UserDataBase.AddWarning(member.display_name)
        embed = discord.Embed(title='Warning added to the user')
        embed.add_field(name='Name', value=member.display_name)
        embed.add_field(name='ID', value=member.id)
        embed.add_field(name='Warnings', value=UserDataBase.GetWarn(member.display_name))
        embed.add_field(name='Admin', value=ctx.author.name)
        
        embed.set_thumbnail(url=member.avatar_url)
        
    if UserDataBase.GetWarn(member.display_name) == 1:
        embed.add_field(title= "Aclaration", value= "The user have 1 warning")

    if UserDataBase.GetWarn(member.display_name) == 2:
        #Send a message to the channel
        embed.add_field(title= "Aclaration", value= "The user have 2 warnings, the next warning will be a ban")
    elif UserDataBase.GetWarn(member.display_name) == 3:
        #Ban de user
        await ctx.guild.ban(member)
        embed.add_field(title= "Aclaration", value= "The user have 3 warnings, the user has been banned")
        UserDataBase.RemoveUser(member.display_name)
    
    await ctx.send(embed=embed)
    

@bot.command()
async def RemoveWarning(ctx, *, member : discord.Member):
    """Function to remove a warning to a user"""
    UserDataBase.RemoveWarning(member.display_name)

@bot.command()
async def UserInfo(ctx, member: discord.Member = None):
    """Function to get the information of a user""" 
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at, title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)
    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    embed.add_field(name="Warning:", value=UserDataBase.GetWarn(member.display_name))

    await ctx.send(embed=embed)

@bot.command()
async def ServerInfo(ctx):
    """Fuction to send the server info"""
    
    #Get the server info
    bot = 0 
    
    for i in ctx.guild.members:
        if i.bot == True:
            bot +=1
    users = ctx.guild.member_count - bot
    
    text = 0
    voice = 0
    category = 0
    for i in ctx.guild.channels:
        print (i.type)
        if i.type == discord.ChannelType.text:
            text += 1
        elif i.type == discord.ChannelType.voice:
            voice += 1
        elif i.type == discord.ChannelType.category:
            category += 1
    
    general = text + voice + category
    
    #Send the server info
    embed = discord.Embed(title="Server Info", color=0x00ff00)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
    embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
    embed.add_field(name="Server Owner", value=ctx.guild.owner.mention, inline=True)
    embed.add_field(name="Server Created at", value=ctx.guild.created_at.strftime("%d/%m/%Y"), inline=True)
    embed.add_field(name="Number of Roles ", value=len(ctx.guild.roles), inline=True)
    embed.add_field(name="Number of Members", value="{} members\n {} Bots , {} Humans ".format(ctx.guild.member_count, bot , users), inline=True)
    embed.add_field(name="Number of Channels", value= "{} channels\n {} Categories \n {} Text {} Voice ".format(general,  category , text , voice), inline=True)
    await ctx.send(embed=embed)

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


@bot.command(pass_context=True)
async def SetRole(ctx,member: discord.Member,* , role: discord.Role):
    """Fuction for set a role to a user"""
    id = ctx.message.author.id
    print(id)
    if id == 327803995244593153:
        if role in member.roles:
            await ctx.send("{} has this role" .format(member.mentioned))
        else:
            await member.add_roles(role)
            await ctx.send(f"The role {role} has been added to the user {member}")
    else:
        await ctx.send("You don't have the permission to use this command")

@bot.command()
async def GenerateText(ctx,*, message):
    """"""Fuction for generate a text whit the model""""""
    #Read a message
    print("Mensaje: " + message)
    #Send a message
    resp = api.send_message(message)
    respuesta = resp["message"]
    print("Respuesta: ", respuesta)
    
    #Modificacion de su ultimo mesaje para que ponga el texto generado
    await ctx.send(respuesta)


@bot.command()
async def BanWord(ctx,*, message: str):
    """Fuction for add a word to the ban list"""
    BanWords.append(message)
    print(BanWords)
    await ctx.send("The word {} has been added to the ban list".format(message))



#Token of the bot
bot.run(DiscordToken)