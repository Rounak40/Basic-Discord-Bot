

# Import modules

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import requests
import json
import random

#Enter your discord bot token & Prefix here
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
prefix = "!"

#define your client
client = Bot(command_prefix=prefix)

# if you want to remove the deafult HELP command
client.remove_command('help')


#Its a event which will run when the bot is ready/online.
@client.event
async def on_ready():
    print("Logged in as " + client.user.name)
    print("I'm ready")

#Here you can add your cmds


@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")


@client.command(pass_context=True)
async def hello(ctx):
    await client.say(f"Hello {ctx.message.author.mention}")

#play dice
@client.command(pass_context=True)
async def dice(ctx):
    
    #get a random number from ["1","2","3","4","5","6"]
    roll = random.choice(["1","2","3","4","5","6"])
    
    await client.say("**You rolled a: **" + roll)

#Clear messages of any channel
@client.command(pass_context=True)
async def clear(ctx, number : int):
    #check if user has permission to manage channels
    if ctx.message.author.server_permissions.manage_channels:
        try:
            await client.purge_from(ctx.message.channel, limit=number+1)
            await client.say(f"Successfully cleared {str(number)} messages from this channel")
        except:
            # if bot doesn't have permission to delete messages.
            await client.say("I don't have permission to delete messages.") 
    else:
        #user don't have permission to manage channels
        await client.say("You don't have permission to delete messages.")
    
#some calculating commands

@client.command()
async def percent(a: int, b: int):
    divide3 = (a/b)
    ans = divide3*100
    embed = discord.Embed(title="Solved", description=ans, color=0x1500ff)
    await client.say(ans)

@client.command()
async def root(number):
    root_value = int(number)**(1/2.0)
    embed = discord.Embed(title="Solved", description=str(number) + " **root is** " + str(root_value), color=0x1500ff)
    await client.say(embed=embed)

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    embed = discord.Embed(title="Solved", description=str(number) + " **squared is** " + str(squared_value), color=0x1500ff)
    await client.say(embed=embed)


#passing two values in cmd (a: int, b: int)
@client.command()
async def add(a: int, b: int):
    embed = discord.Embed(title="Solved", description=a+b, color=0x1500ff)
    await client.say(embed=embed)

@client.command()
async def multiply(a: int, b: int):
    embed = discord.Embed(title="Solved", description=a*b, color=0x1500ff)
    await client.say(embed=embed)

@client.command()
async def divide(a: int, b: int):
    divide25 = (a/b)
    embed = discord.Embed(title="Solved", description=str(divide25), color=0x1500ff)
    await client.say(embed=embed)

@client.command()
async def subtract(a: int, b: int):
    embed = discord.Embed(title="Solved", description=a-b, color=0x1500ff)
    await client.say(embed=embed)


#api based command
# 1. Requests to url
# 2. Grab data from response
# 3. Send it to the channel
@client.command()
async def bitcoin():
    
    #define url
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    
    #make "GET" requets
    response = requests.get(url)
    
    #grab data from response
    value = response.json()['bpi'] ['USD'] ['rate']

    #send data in channel
    await client.say("Current Bitcoin Price is: $" + value)
    
#example of embed messgaes

#get info of server
@client.command(pass_context=True)
async def serverinfo(ctx):
    
    embed = discord.Embed(name=f"{ctx.message.server.name}'s info".format, color=0x00ff00)
    embed.set_author(name="Server Info")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.set_footer(text="Basic example of embed message!")
    
    await client.say(embed=embed)
    


# get info of any user
@client.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    
    embed = discord.Embed(title=f"{user.name}'s Info",color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined At", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text="Basic example of embed message!")
    
    await client.say(embed=embed)


#get avatar of any user
@client.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    
    embed=discord.Embed(title=f"Avater of {user}", color=0x1500ff)
    embed.set_image(url=user.avatar_url)
    embed.set_footer(text="Basic example of embed message!")
                     
    await client.say(embed=embed)
    
# Run the bot with the token
client.run(TOKEN)
