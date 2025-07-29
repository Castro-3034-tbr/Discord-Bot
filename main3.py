from discord import app_commands, Intents, Client, Interaction
import discord
from datetime import datetime
from DataBase import *

class Bot(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)


bot = Bot(intents=Intents.default())


@bot.event
async def on_ready():
    """Fuction for the bot is ready"""
    # Send a message to the channel
    channel = bot.get_channel(1006225124376191017)
    date = datetime.now()
    await channel.send("Bot conect at: \n\tData: {} \n\tTime: {}".format(date.date(), date.time().strftime("%H:%M:%S")))

    # Change the status of the bot
    await bot.change_presence(activity=discord.Game(name='çhelp'))

    # Print a message in the terminal
    print("Bot conect at: \n\tData: {} \n\tTime: {} ".format(
        date.date(), date.time().strftime("%H:%M:%S")))


@bot.event
async def on_member_join(member):
    """Fuction for a user join in the server"""

    # Add the user to the database
    roles = [role for role in member.roles]
    name = member.display_name
    id = str(member.id)
    created_at = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
    joined_at = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
    top_role = str(member.top_role)
    UserDataBase.AddUser(
        User(name, id, roles, created_at, joined_at, top_role))

    # Send a message to the channel
    channel = bot.get_channel(997088393483780176)
    embed = discord.Embed(title='The server have new user')
    embed.add_field(name='Name', value=member.name)
    embed.add_field(name='ID', value=member.id)
    embed.set_thumbnail(url=member.avatar_url)
    await member.add_role(997153212819832972)
    await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    """Fuction for a user remove from the server"""
    # Remove the user from the database
    UserDataBase.RemoveUser(member.name)
    # Send a message to the channel
    channel = bot.get_channel(997088393483780176)
    embed = discord.Embed(title='The server lost a user ')
    embed.add_field(name='Name', value=member.name)
    embed.add_field(name='ID', value=member.id)
    embed.set_thumbnail(url=member.avatar_url)

    await channel.send(embed=embed)



@bot.tree.command()
async def givemebadge(interaction: Interaction):
    await interaction.response.send_message("Listo!, espera 24 horas para reclamar la insignia\nPuedes reclamarla aquí: https://discord.com/developers/active-developer")

@bot.tree.command()
async def help(interaction: Interaction):
    embed = discord.Embed(title="List of commands", color=0x00ff00)
    embed.add_field(name="Hello", value="Hello World", inline=False)
    embed.add_field(name="BanWord <Word> ", value="Ban a word", inline=False)
    embed.add_field(name="Kick <@User Reason>",value="Kick a user", inline=False)
    embed.add_field(name="Ban <@User Reason>",value="Ban a user", inline=False)
    embed.add_field(name="UnBan <@User>", value="UnBan a user", inline=False)
    await interaction.response.send_message(embed=embed)

@bot.tree.command()
async def hello(interaction: Interaction):
    await interaction.response.send_message("Hello World")

@bot.tree.command()
async def stop(interaction: Interaction):
    if interaction.member.id == 327803995244593153 or interaction.author.id == 718854635674402816:
        await interaction.response.send_message("Bot is stoping")
        await bot.logout()
    else:
        await interaction.response.send_message("You don't have permission to use this command")

@bot.tree.command()
async def adduser(interaction: Interaction):
    """Fuction to add a user to the database"""
    roles = [role for role in interaction.member.roles]
    name = interaction.member.display_name
    id = str(interaction.member.id)
    crated_at = interaction.member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
    joined_at = interaction.member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
    top_role = str(interaction.member.top_role)
    
    #Add the user to the database
    UserDataBase.AddUser(User(name, id, roles, crated_at, joined_at, top_role))
    
    await interaction.response.send_message("The user {} was added to the database".format(name))

bot.run(DiscordToken)
