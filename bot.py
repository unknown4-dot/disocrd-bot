import discord
import random
from discord.ext import commands
import time


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)


@bot.command()
async def helpp(ctx):
    embed = discord.Embed(title="commands",
    color=discord.Color.blue())
    
    embed.add_field(
    name="Ban",
    value="?ban @user",
    inline=False)
    
    embed.add_field(
    name="kick",
    value="?kick @user",
    inline=False)
    
    embed.add_field(
    name="mute",
    value="?mute @user",
    inline=False)
    
    embed.add_field(
    name="say",
    value="?say word",
    inline=False)
    
    embed.add_field(
    name="github",
    value="?github",
    inline=False)
    
    embed.add_field(
    name="server",
    value="?server",
    inline=False)
    
    embed.add_field(
    name="answer",
    value="?answer",
    inline=False)
    
    embed.add_field(
    name="Linux",
    value="?Linux",
    inline=False)
    
    embed.add_field(
    name="question",
    value="?question",
    inline=False)
    
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
    try:
        await member.mute()
        await ctx.send(f"the member has been muted!! | {ctx.author.mention}")
    except:
        await ctx.send(f"failed to mute :( | {ctx.author.mention}")
        
        
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
    await ctx.send(f"my github | {ctx.author.mention}")
    
    
    
@bot.command()
async def server(ctx):
    await ctx.send(f"here is our server!! | {ctx.author.mention}")
    
       
@bot.command()
async def say(ctx, *, message):
    await ctx.send(f"{message} | {ctx.author.mention}")
    

yo = ["yes", "no"]
 
pls = random.choice(yo)
   
@bot.command()
async def answer(ctx):
   await ctx.send(f"{pls} | {ctx.author.mention}")
   
   
@bot.command()
async def Linux(ctx):
   embed = discord.Embed(
   title="Linux Commands.",
   color=discord.Color.red())
   
   embed.add_field(
   name="touch",
   value="make files",
   inline=False)
   
   embed.add_field(
   name="mkdir",
   value="make directory",
   inline=False)
   
   embed.add_field(
   name="rm",
   value="delete files",
   inline=False)
   
   embed.add_field(
   name="rm -rf",
   value="force to delete",
   inline=False)
   
   embed.add_field(
   name="rmdir",
   value="delete directory",
   inline=False)
   
   embed.add_field(
   name="cat",
   value="show files text",
   inline=False)
   
   await ctx.send(embed=embed)

question = ["why do you use github?", "python or javascript?", "is Sudo your favorite bot?",
 "did you join Sudo discord server?", "whats the best android os?", 
 "whats the best linux distro", "whats your favorite gaming console?", 
 "whats your favorite game?", "whats your favorite drink?", "whats your favorite food?",
 "whats your favorite programming language", "why are you a programmer?",
 "android or IOS?"]




@bot.command()
async def question(ctx):
      idkidk = ["why do you use github?", "python or javascript?", "is Sudo your favorite bot?",
 "did you join Sudo discord server?", "whats the best android os?", 
 "whats the best linux distro", "whats your favorite gaming console?", 
 "whats your favorite game?", "whats your favorite drink?", "whats your favorite food?",
 "whats your favorite programming language", "why are you a programmer?",
 "android or IOS?"]
 
      q = random.choice(idkidk)
      await ctx.send(f"{q} | {ctx.author.mention}")
      
   
