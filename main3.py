from discord import app_commands, Intents, Client, Interaction,Game, Embed
from datetime import datetime
from DataBase import *

class Bot(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    
    async def setup_hook(self) -> None:
        return await super().setup_hook()

bot = Bot(intents=Intents.default())

@bot.event
async def on_ready():
    # Send a message to the channel
    channel = bot.get_channel(1006225124376191017)
    date = datetime.now()
    await channel.send("Bot conect at: \n\tData: {} \n\tTime: {}".format(date.date(), date.time().strftime("%H:%M:%S")))

    # Change the status of the bot
    await bot.change_presence(activity=Game(name='çhelp'))

    # Print a message in the terminal
    print("Bot conect at: \n\tData: {} \n\tTime: {} ".format(date.date(), date.time().strftime("%H:%M:%S")))
    

@bot.tree.command()
async def givemebadge(interaction: Interaction):
    await interaction.response.send_message("Listo!, espera 24 horas para reclamar la insignia\nPuedes reclamarla aquí: https://discord.com/developers/active-developer")

@bot.tree.command()
async def hello(interaction: Interaction):
    await interaction.response.send_message("Hello World!")

@bot.tree.command()
async def help(interaction: Interaction):
    """Fuction for send a help message"""
    embed = Embed(title="List of commands", color=0x00ff00)
    embed.add_field(name="Hello", value="Hello World", inline=False)
    embed.add_field(name="BanWord <Word> ", value="Ban a word", inline=False)
    embed.add_field(name="Kick <@User Reason>", value="Kick a user", inline=False)
    embed.add_field(name="Ban <@User Reason>", value="Ban a user", inline=False)
    embed.add_field(name="UnBan <@User>", value="UnBan a user", inline=False)
    await interaction.send(embed=embed)

bot.run(DiscordToken)
