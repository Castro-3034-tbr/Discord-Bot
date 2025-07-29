import os
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from discord import User, Member

from dotenv import load_dotenv
from datetime import datetime

# Charge environment variables from .env file
load_dotenv("conf/.env")
TOKEN = os.getenv("DISCORD_TOKEN")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")

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

    # Change the status of the bot
    await bot.change_presence(activity=discord.Game(name='çhelp'))

    # Print a message in the terminal
    print(ready_message)

    #Obtain server data
    get_server_data()


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

    #Send a message to the terminal
    print(stop_message)

    exit(0)

#region: Events 


#region: Commands



bot.run(TOKEN)