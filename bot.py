#example 2
#import discord
#from discord.ext import commands

#client = discord.Client()
#Bot = commands.Bot(command_prefix="/")

#@client.event
#async def on_ready():
 #   print('We have logged in as {0.user}'.format(client))





#@client.event
#async def clear(ctx, amount=30):
  #  await ctx.channel.purge(limit=amount)
 #   await ctx.channel.send("сообщение удалено")


#@client.event
#async def kik(ctx, member:discord.Member,*,reason=None):
  #  await member.kick(reason=reason)
 #   await ctx.channel.send("На одного долбаеба в чате стало меньше")
    #await message.channel.send(f' Иди нахуй {message.author.mention} ')

#@client.event
#async def ban(ctx, member:discord.Member,*,reason=None):
 #   await member.ban(reason=reason)



#@client.event
#async def on_message(message):

#     return#!on_start
  #  if message.content.startswith('$hello'):
 #       await message.channel.send('Hello!')

#client.run('NzgzMzI4ODI1ODE1NzI4MTcw.X8ZJ0Q._ZmSDDkuRzwP4mk_J7B4LcmjNBI')



import discord
from discord.ext import commands
import requests
#import webbrowser


token = 'NzgzMzI4ODI1ODE1NzI4MTcw.X8ZJ0Q._ZmSDDkuRzwP4mk_J7B4LcmjNBI'
bot = commands.Bot(command_prefix="/")
client = discord.Client()


@bot.event
async def on_start(message):
    print("Здарова бро")


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ocistka(ctx, amount = None):
    await ctx.channel.purge(limit=int(amount))



@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kik(ctx, member:discord.Member,*,reason=None):
    await member.kick(reason=reason)
    await ctx.channel.send("На одного долбаеба в чате стало меньше")


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member,*,reason=None):
    await member.ban(reason=reason)


@bot.command(pass_context=True)
async def on_message(message):
    if message.content.startswith('!BanEveryone'):
        for member in client.get_all_members():
            if member.bot:
                continue
            await member.ban(reason="*Причина бана*", delete_message_days=7)

@bot.command(pass_context=True)
async def start(ctx):
    await ctx.send("здарова бро, иди нахуй вот все комамды этого бота\n"
                   "1) /ban\n"
                   "2) /kick\n"
                   "3) /ocistka\n")

bot.run(token)












