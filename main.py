import os
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from discord import User, Member

from dotenv import load_dotenv
from datetime import datetime

import sys

# Charge environment variables from .env file
load_dotenv("conf/.env")
TOKEN = os.getenv("DISCORD_TOKEN")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")
JOIN_CHANNEL_ID = os.getenv("JOIN_CHANNEL_ID")

# Set up intents and create bot instance
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Required to access member data
intents.guilds = True  # Required to access guild data
intents.presences = True  # Required to access presence data
intents.messages = True  # Required to access message data
intents.emojis = True  # Required to access custom emojis
intents.reactions = True  # Required to access reactions
intents.voice_states = True  # Required to access voice state data
intents.bans = True  # Required to access ban data
bot = commands.Bot(command_prefix="ç", intents=intents)


#region: Events and Commands to start and stop the bot

def get_server_data():
    """Function to get the server and user data."""

    # Server data
    for guild in bot.guilds:
        print(f"\nServer: {guild.name}")
        print(f"ID: {guild.id}")
        print(f"Owner: {guild.owner}")
        print(f"Total members: {guild.member_count}")
        print(f"Total channels: {len(guild.channels)}, list: {[channel.name for channel in guild.channels]}")
        print(f"Total roles: {len(guild.roles)}, list: {[role.name for role in guild.roles if role.name != '@everyone']}")
        print(f"Custom emojis: {len(guild.emojis)}, list: {[emoji.name for emoji in guild.emojis]}")
        print(f"Creation date: {guild.created_at.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Server description: {guild.description if guild.description else 'No description available'}")
        print(f"Verification level: {guild.verification_level}")
        print(f"AFK voice channel: {guild.afk_channel.name if guild.afk_channel else 'No AFK voice channel'}")
        print(f"Welcome channel: {guild.system_channel.name if guild.system_channel else 'No welcome channel'}")
        print("---" * 40)

        # Iterate over all members (requires intents.members = True)
        for member in guild.members:
            print(f"User: {member.name}")
            print(f"ID: {member.id}")
            print(f"Display name: {member.display_name}")
            print(f"Bot: {member.bot}")
            print(f"Status: {member.status}")
            print(f"Roles: {[role.name for role in member.roles if role.name != '@everyone']}")
            print("-" * 20)
        print("/////" * 40)


@bot.event
async def on_ready():
    """Message when the bot is ready."""
    print(f"Bot is ready as {bot.user.name} (ID: {bot.user.id})")
    
    #Set the message
    ready_message = (
        f"The bot was started on date and time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    )
    
    #Send a initial message to a bot log channel
    log_channel = bot.get_channel(int(LOG_CHANNEL_ID))
    if log_channel:
        await log_channel.send(ready_message)
    else:
        print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")

    # Change the status of the bot
    await bot.change_presence(activity=discord.Game(name='çhelp'))

    # Print a message in the terminal
    print(ready_message)

    # #Obtain server data
    # get_server_data()


@bot.command()
async def Stop(ctx):
    """Fuction for stop the bot but The admins can use this command"""

    #Set the mensage
    stop_message = (
        f"The bot was stopped on date and time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n for {ctx.author.name}"
    )

    #Send the message to the log channel
    log_channel = bot.get_channel(int(LOG_CHANNEL_ID))
    if log_channel:
        await log_channel.send(stop_message)
    else:
        print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")

    #Send a message to the terminal
    print(stop_message)

    sys.exit(0)

#region: Events 

@bot.event
async def on_member_join(member):
    """Event for when a user joins the server."""
    print("A user has joined *************************************")

    #Obtain user and server information
    UserName = member.name
    UserID = member.id
    UserAvatar = member.avatar.url if member.avatar else member.default_avatar.url

    ServerName = member.guild.name
    ServerID = member.guild.id

    DateJoined = member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC") if member.joined_at else "Unknown"

    # Create the embed
    embed = discord.Embed(
        title='New User Joined',
        description=f'{member.name} has joined the server!',
        color=discord.Color.green()
    )
    embed.add_field(name='User ID', value=UserID)
    embed.add_field(name='Date Joined', value=DateJoined)
    embed.set_thumbnail(url=UserAvatar)

    # Send to log channel
    channel = bot.get_channel(int(JOIN_CHANNEL_ID))
    if channel:
        await channel.send(embed=embed)
    else:
        print(f"Channel with ID {JOIN_CHANNEL_ID} not found.")

    print(f"User {UserName} (ID: {UserID}) joined server {ServerName} (ID: {ServerID}) on {DateJoined}")

    # Set a default role for the user
    role_name = "User"
    role = discord.utils.get(member.guild.roles, name=role_name)

    if role:
        try:
            await member.add_roles(role)
            print(f"Assigned role '{role.name}' to {member.name}")
        except discord.Forbidden:
            print(f"No permission to assign role '{role.name}' to {member.name}")
        except Exception as e:
            print(f"Error assigning role: {e}")
    else:
        print(f"Role '{role_name}' not found in the server.")


@bot.event
async def on_member_remove(member):
    """Event for when a user leaves the server."""
    print("A user has left *************************************")

    #Obtain user and server information
    UserName = member.name
    UserID = member.id
    UserAvatar = member.avatar.url if member.avatar else member.default_avatar.url

    ServerName = member.guild.name
    ServerID = member.guild.id

    embed = discord.Embed(
        title='User Left',
        description=f'{member.name} has left the server.',
        color=discord.Color.red()
    )
    embed.add_field(name='User ID', value=UserID)
    embed.add_field(name='Date Left', value=datetime.now().strftime("%a, %d %B %Y, %I:%M %p UTC"))
    embed.set_thumbnail(url=UserAvatar)

    channel = bot.get_channel(int(JOIN_CHANNEL_ID))
    if channel:
        await channel.send(embed=embed)
    else:
        print(f"Channel with ID {JOIN_CHANNEL_ID} not found.")

    print(f"User {UserName} (ID: {UserID}) left server {ServerName} (ID: {ServerID})")

#region: Commands

@bot.command()
async def Hello(ctx):
    """Function to say hello (Test command)"""
    await ctx.send("Hello, I am a bot created by @castro_3034_tbr")

bot.run(TOKEN)