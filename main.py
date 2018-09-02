from discord.ext import commands
import asyncio

token = ""
with open("keys/token", 'r') as keys:
    token = keys.read().split('\n')[0]

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
    user = ctx.message.author.id
    user = "<@" + str(user) + ">"
    await ctx.send('I am alive and I heard you! {}'.format(user))

@bot.command()
async def count(ctx):
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
    ctx.send('Yet to be implemented')
    # TODO use Reddit API to fetch pics of dogs and then display them 

bot.run(token)
