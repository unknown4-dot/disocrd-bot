import discord
import random
from discord.ext import commands
import time
import asyncio
from collections import defaultdict

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 

bot = commands.Bot(command_prefix='?', intents=intents)

user_message_history = {}
message_counts = {}
spam_tracker = defaultdict(lambda: defaultdict(int))
spam_messages = defaultdict(lambda: defaultdict(str))
welcome_channels = {} 

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    
    muted_role = discord.utils.get(message.guild.roles, name="Muted")
    if not muted_role:
       
        try:
            muted_role = await message.guild.create_role(name="Muted")
            
            for channel in message.guild.channels:
                await channel.set_permissions(muted_role, send_messages=False, speak=False)
        except discord.Forbidden:
            print("Bot doesn't have permission to create roles")
            return
    
    content = message.content.lower()
    user_id = message.author.id
    channel_id = message.channel.id
    
    
    if spam_messages[channel_id][user_id] == content:
        spam_tracker[channel_id][user_id] += 1
    else:
        spam_tracker[channel_id][user_id] = 1
        spam_messages[channel_id][user_id] = content
    
    
    if spam_tracker[channel_id][user_id] >= 4:
        try:
            await message.author.add_roles(muted_role)
            await message.channel.send(f"{message.author.mention} has been muted for 20 seconds for spamming")
            
            
            await asyncio.sleep(20)
            await message.author.remove_roles(muted_role)
            await message.channel.send(f"{message.author.mention} has been unmuted")
            
            
            spam_tracker[channel_id][user_id] = 0
        except discord.Forbidden:
            await message.channel.send("I don't have permission to mute users!")
    
    
    await bot.process_commands(message)

@bot.event 
async def on_member_join(member):
     if member.guild.id in welcome_channels:
        channel_id = welcome_channels[member.guild.id] 
        channel = bot.get_channel(channel_id)  
        if channel:
            await channel.send(f"{member.mention} | welcome!!")  

@bot.command()
@commands.has_permissions(administrator=True)
async def welcome(ctx):
    try:
        welcome_channels[ctx.guild.id] = ctx.channel.id  
        await ctx.send("the welcome is enabled!!")
    except:
        await ctx.send(f'{ctx.author.mention} | you dont have permission')
    

@bot.command()
async def helpp(ctx):
    embed = discord.Embed(title="commands", color=discord.Color.red())
    
    embed.add_field(name="features", value="?features", inline=False)
    embed.add_field(name="Ban", value="?ban @user", inline=False)
    embed.add_field(name="kick", value="?kick @user", inline=False)
    embed.add_field(name="mute", value="?mute @user", inline=False)
    embed.add_field(name="say", value="?say word", inline=False)
    embed.add_field(name="github", value="?github", inline=False)
    embed.add_field(name="server", value="?server", inline=False)
    embed.add_field(name="answer", value="?answer", inline=False)
    embed.add_field(name="Linux", value="?Linux", inline=False)
    embed.add_field(name="question", value="?question", inline=False)
    embed.add_field(name="welcome", value="?welcome", inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
async def features(ctx):
    embed = discord.Embed(title="Features", color=discord.Color.red())
    embed.add_field(name="Anti-Spam", value="make chats clean and no spam:)", inline=False)
    embed.add_field(name="welcome", value="welcome members:)", inline=False)
    await ctx.send(embed=embed)
    

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
    if ctx.author.top_role.position <= member.top_role.position:
        return await ctx.send(f"{ctx.author.mention} | i cant ban this user the user has higher role")
    
    try:
        await member.ban()
        await ctx.send(f"user has been banned!! | {ctx.author.mention}")
    except:
        await ctx.send("i dont have permission to ban this user | {ctx.author.mention}")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member):
    if ctx.author.top_role.position <= member.top_role.position:
        return await ctx.send(f"{ctx.author.mention} | i cant mute this member the member has higher role")
    
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        await ctx.send("Muted role doesn't exist!")
        return
    
    try:
        await member.add_roles(muted_role)
        await ctx.send(f"the member has been muted!! | {ctx.author.mention}")
    except discord.Forbidden:
        await ctx.send(f"failed to mute :( | {ctx.author.mention}")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    if ctx.author.top_role.position <= member.top_role.position:
        return await ctx.send(f"{ctx.author.mention} | i cant unmute this member the member has higher role")
    
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        await ctx.send("Muted role doesn't exist!")
        return
    
    try:
        await member.remove_roles(muted_role)
        await ctx.send(f"the member has been unmuted!! | {ctx.author.mention}")
    except discord.Forbidden:
        await ctx.send(f"failed to unmute :( | {ctx.author.mention}")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    if ctx.author.top_role.position <= member.top_role.position:
        return await ctx.send(f"{ctx.author.mention} | i cant kick this member the member has higher role")
    
    try:
        await member.kick()
        await ctx.send(f"the member has been kicked!! | {ctx.author.mention}")
    except:
        await ctx.send(f"failed to kick :( | {ctx.author.mention}")

@bot.command()
async def github(ctx):
    await ctx.send(f"my github | https://github.com/unknown4-dot {ctx.author.mention}")

@bot.command()
async def server(ctx):
    await ctx.send(f"here is our server!! | https://discord.gg/JfNrQMEbhH {ctx.author.mention}")

@bot.command()
async def say(ctx, *, message):
    await ctx.send(f"{message} | {ctx.author.mention}")

yo = ["yes", "no"]

@bot.command()
async def answer(ctx):
    pls = random.choice(yo)
    await ctx.send(f"{pls} | {ctx.author.mention}")

@bot.command()
async def Linux(ctx):
    embed = discord.Embed(title="Linux Commands.", color=discord.Color.red())
    embed.add_field(name="touch", value="make files", inline=False)
    embed.add_field(name="mkdir", value="make directory", inline=False)
    embed.add_field(name="rm", value="delete files", inline=False)
    embed.add_field(name="rm -rf", value="force to delete", inline=False)
    embed.add_field(name="rmdir", value="delete directory", inline=False)
    embed.add_field(name="cat", value="show files text", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def question(ctx):
    idkidk = [
        "why do you use github?", "python or javascript?", "is Sudo your favorite bot?",
        "did you join Sudo discord server?", "whats the best android os?", 
        "whats the best linux distro", "whats your favorite gaming console?", 
        "whats your favorite game?", "whats your favorite drink?", "whats your favorite food?",
        "whats your favorite programming language", "why are you a programmer?",
        "android or IOS?"
    ]
    q = random.choice(idkidk)
    await ctx.send(f"{q} | {ctx.author.mention}")


@bot.command()
async def goodBoy(ctx):
         await ctx.send(f"thanks daddy | {ctx.author.mention} ")
         
                         
                                         
@bot.command()
async def ping(ctx):
         embed = discord.Embed(title="Ping", color=discord.Color.red())
         embed.add_field(name="Im Still Online!!", value="Sudo", inline=False)



     
bad_words = ["nigger", "daik 7iz", "daik qa7ba", "daik qahba", "hitler", "jewish", "kys"]                   
         
@bot.event
async def on_message(message):
    
    muted_role = discord.utils.get(message.guild.roles, name="Muted")
    
    if message.author == bot.user:
        return
        
    content = message.content.lower() 
    if any(bad_words in content for bad_words in bad_words):
        await message.author.add_roles(muted_role)
        await message.channel.send(f"{message.author.mention} has been muted!! | reason=bad_words")
        await asyncio.sleep(30)
        await message.author.remove_roles(muted_role)
        await message.channel.send(f"{message.author.mention} | has been unmuted!!")

        await bot.process_commands(message)
        
