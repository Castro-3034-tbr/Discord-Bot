import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from datetime import datetime

# Charge environment variables from .env file
load_dotenv("conf/.env")
TOKEN = os.getenv("DISCORD_TOKEN")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")

# Set up intents and create bot instance
intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix="ç", intents=intents)


@bot.event
async def on_ready():
    """Message when the bot is ready."""
    print(f"Bot activo como: {bot.user}")
    
    #Configure the ready message
    ready_message = (
        f"The bot was started on date and time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    )
        
    
    #Send a initial message to a bot log channel
    log_channel = bot.get_channel(int(LOG_CHANNEL_ID))
    if log_channel:
        await log_channel.send(ready_message)


bot.run(TOKEN)