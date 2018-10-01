import discord
from discord.ext import commands
import asyncio
import os

token = os.environ.get("DISCORDDOGBOT")
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    print(message.content)
    await bot.process_commands(message)

@bot.command()
async def test(ctx):
    """
    This command is used to check if the bot is functioning properly
    """
    user = ctx.message.author.id
    user = "<@" + str(user) + ">"
    await ctx.send('I am alive and I heard you! {}'.format(user))

@bot.command()
async def count(ctx):
    """
    Returns the number of messages by the user from the last 100 messages in channel
    """
    user = ctx.message.author.id
    user = "<@" + str(user) + ">"
    counter = 0
    tmp = await ctx.send('Calculating messages...')
    async for log in ctx.message.channel.history():
        if log.author == ctx.message.author:
            counter += 1
    await tmp.edit(content='You have {} messages in the <#{}> channel'.format(counter, ctx.message.channel.id))

@bot.command()
async def doggo(ctx):
    """
    Returns an image of a dog
    """
    embed = discord.Embed(description="Hello There", color=0x00ff00, type="rich")
    image = discord.File("images/image001.jpg", filename="Dog.jpg")
    await ctx.send(embed=embed, file=image)

## TODO: Fetch top photos from the Reddit API

bot.run(token)
