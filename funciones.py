

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
    
    UserDataBase.AddWarning(member.display_name)
    
    await ctx.send("The user {} has been warned , Now the user has {} warns".format(member.display_name, UserDataBase.GetWarn(member.display_name)))


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
async def BanWord(ctx,*, message: str):
    """Fuction for add a word to the ban list"""
    BanWords.append(message)
    print(BanWords)
    await ctx.send("The word {} has been added to the ban list".format(message))


@bot.event
async def on_message(message):
    """Fuction for detect some specific words that user write in the channels"""
    print("Mensaje: " + message.content)
    
    #Fuccion for detect if the user write a word that is in the ban list
    words = message.content.split(" ")
    for i in words:
        if i[0] != "ç" or i!="\n":
            Words.addWord(i)
            if i in BanWords:
                if message.author.id != 993090727183667250 :
                    
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} Don't use that word!, Because this word is banned")
                    bot.dispatch('profanity', message, i)
                    print(f"{message.author.mention} Don't use that word!, Because this word is banned")
                    return
    
    await bot.process_commands(message)
