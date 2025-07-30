import os
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from discord import User, Member

from dotenv import load_dotenv
from datetime import datetime

import mysql.connector

import sys

# Charge environment variables from .env file
load_dotenv("conf/.env")
TOKEN = os.getenv("DISCORD_TOKEN")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")
JOIN_CHANNEL_ID = os.getenv("JOIN_CHANNEL_ID")
STAFF_CHANNEL_ID = os.getenv("STAFF_CHANNEL_ID")

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

#region Database Init
def close_database():
    """Function to close the database connection."""

    global conn, cursor
    if 'conn' in globals() and 'cursor' in globals():
        print("Closing database connection...")
        cursor.close()
        conn.close()
        print("✅ Database connection closed.")
    else:
        print("❌ No database connection to close.")

try:

    # Open the database file
    with open("DB/init_db.sql", "r") as f:
        sql_script = f.read()

    # Connect to the MySQL database and execute the SQL script
    conn = mysql.connector.connect(
        host="localhost",
        user="botuser",
        password="30Vacascomen.",
        database="discord_bot"
    )

    cursor = conn.cursor()
    for stmt in sql_script.split(";"):
        if stmt.strip():
            cursor.execute(stmt)
    conn.commit()

    print("✅ Base de datos inicializada.")

except Exception as e:
    print(f"❌ Error al inicializar la base de datos: {e}")
    sys.exit(1)


#region: Events and Commands to start and stop the bot

def get_server_data():
    """Function to get the server and user data."""
    global cursor, conn

    for guild in bot.guilds:
            # --- Insertar servidor ---
        insert_server_query = """
            INSERT INTO servers (
                server_id,
                name,
                owner_id,
                created_at,
                description,
                member_count,
                total_roles,
                total_channels,
                afk_timeout,
                afk_channel_id,
                system_channel_id,
                icon_url,
                features
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE name=VALUES(name), member_count=VALUES(member_count)
        """
        cursor.execute(insert_server_query, (
            guild.id,
            guild.name,
            guild.owner_id,
            guild.created_at,
            guild.description,
            guild.member_count,
            len(guild.roles),
            len(guild.channels),
            guild.afk_timeout,
            guild.afk_channel.id if guild.afk_channel else None,
            guild.system_channel.id if guild.system_channel else None,
            str(guild.icon.url) if guild.icon else None,
            ",".join(guild.features)
        ))

        # --- Insertar roles del servidor ---
        insert_role_query = """
            INSERT IGNORE INTO roles (
                role_id,
                server_id,
                name,
                color,
                position,
                mentionable,
                hoist,
                permissions
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        for role in guild.roles:
            if role.name != "@everyone":
                cursor.execute(insert_role_query, (
                    role.id,
                    guild.id,
                    role.name,
                    str(role.color),
                    role.position,
                    role.mentionable,
                    role.hoist,
                    role.permissions.administrator
                ))

        # --- Insertar usuarios y sus roles ---
        insert_user_query = """
            INSERT INTO users (
                user_id,
                server_id,
                username,
                display_name,
                is_bot,
                joined_at,
                status,
                avatar_url,
                boosting_since
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE display_name=VALUES(display_name), status=VALUES(status)
        """

        insert_user_role_query = """
            INSERT IGNORE INTO user_roles (
                user_id,
                role_id
            ) VALUES (%s, %s)
        """

        for member in guild.members:

            #Add the user to the database
            cursor.execute(insert_user_query, (
                member.id,
                guild.id,
                member.name,
                member.display_name,
                member.bot,
                member.joined_at,
                str(member.status),
                str(member.avatar.url) if member.avatar else None,
                member.premium_since
            ))
            #Add the user roles to the database
            for role in member.roles:
                if role.name != "@everyone":
                    cursor.execute(insert_user_role_query, (member.id, role.id ))

        # --- Confirmar cambios ---
        conn.commit()
        print(f"✅ Datos insertados para servidor '{guild.name}' ({guild.id})")

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