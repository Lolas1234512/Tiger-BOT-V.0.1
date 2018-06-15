import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

TOKEN = 'NDU2Nzk1ODQ5NTYxOTk3MzEy.DgP3fw.mzsod-ZFy61p3zX2QudQyTRTJ7Y'

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='.help | Developing/Testing'))
    print ("IM NOT READY")
    print ("OK IM READY " + bot.user.name)
    print ("IM RUNNING ON: " + bot.user.id)

@bot.command(pass_context=True)
async def test(ctx):
    await bot.say(":robot: Beep Boop! TigerBOT Works! :robot:")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The users joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Ima kick, {}. You bad Tiger!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.say(":punch: Ima ban, {}. You really bad Tiger".format(user.name))
    await bot.ban(user)

@bot.command(pass_context=True)
async def howloser(ctx):

 possible_responses = ["You're total Loser!", "You're 70% Loser", "You're 50% Loser", "You are not an Loser!"]

 current_response = random.choice(possible_responses)

 await bot.say(current_response)

@bot.command(pass_context=True)
async def clear(ctx, number):
    mgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit = 1000000):
        mgs.append(x)
    await bot.delete_messages(mgs)
    await Client.delete_message(x)

@bot.command(pass_context=True)
async def developer(ctx):
    await bot.say (":robot: Beep Boop Developer is <MadTigerZ> Beep Boop :robot:")

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(
        colour = discord.Colour.blue()

    )

    embed.set_author(name='Commands of TigerBOT')
    embed.add_field(name='test', value='Returns message if BOT working well', inline=False)
    embed.add_field(name='info', value='Gives you information', inline=False)
    embed.add_field(name='kick', value='Kicks the user', inline=False)
    embed.add_field(name='ban', value='Bans the user', inline=False)
    embed.add_field(name='clear', value='Clears the chat', inline=False)
    embed.add_field(name='howloser', value='Command, that tells how much loser you are!', inline=False)
    embed.add_field(name='developer', value='This Command tells you, who is the developer of this bot!', inline=False)
    embed.add_field(name='help', value='Shows this message', inline=False)
    embed.add_field(name='whatislove', value='Shows what is love!', inline=False)
    embed.add_field(name='group', value='Shows you ROBLOX group (You need to join!)', inline=False)
    embed.add_field(name='partners', value='Shows you Discord server partners', inline=False)
    embed.add_field(name='cat', value='[Gives you cat photo] STILL WORKING ON IT', inline=False)
    embed.add_field(name='dog', value='[Gives you dog photo] STILL WORKING ON IT', inline=False)

    await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
async def whatislove(ctx):
   await bot.say(":heart: Baby don't hurt me, please don't hurt me! :heart:")

@bot.command(pass_context=True)
async def partners(ctx):
    await bot.say(":robot: Beep Boop Partners is <xRedPearl,KawaiiiiKitten> Beep Boop :robot:")

@bot.command(pass_context=True)
async def funny(ctx):
    await bot.say("You're not funny :smile:")    

@bot.command(pass_context=True)
async def kill(ctx, user: discord.Member):
    await bot.say("{} Has been killed you bad boy!".format(user.name))
    await bot.kill(user)

@bot.command(pass_context=True)
async def group(ctx):
    await bot.say("Join this ROBLOX group and buy T-SHIRTS! https://web.roblox.com/My/Groups.aspx?gid=3087592 P.S I will do giveaways from Robux!")

@bot.command(pass_context=True)
async def cat(ctx):
    await bot.say("Coming soon!")

@bot.command(pass_context=True)
async def dog(ctx):
    await bot.say("Coming soon!")            
            
bot.run(TOKEN)