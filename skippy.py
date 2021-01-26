import discord
from discord.ext import commands
import socket
import time
import datetime


token = 'Nzk4MjI5Nzc5NTAxMTU0Mzc0.X_x_aQ.qM8aLs9_V_pnUYKcWxzC0iIzOOA'
bot = commands.Bot(command_prefix="/")
client = discord.Client()




@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('Этот бот очень удобен для повсидневного использования его создатель использует его почти каждый день')


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ocistka(ctx, amount = None):
    await ctx.channel.purge(limit=int(amount))


@bot.command(pass_context=True)
async def on_message(self, message):
    if message.author == self.user:
        return

    elif message.content == 'Привет':
        await message.channel.send(f' {message.author.mention} hello')

    elif message.content == 'id':
        await message.channel.send(f' {message.author.id} hello')

    elif message.content == 'открой мос ру':
        await message.channel.send('https://www.mos.ru/')

    elif message.content == 'пока':
        await message.channel.send('пока')

    elif message.content == 'спасибо':
        await message.channel.send('спасибо')


    elif message.content == 'спасибо скиппи':
        await message.channel.send('спасибо')

    elif message.content == 'Hello':
        await message.channel.send('Hello, world')


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ip(ctx):
    target = input("Введите названия сайта:")
    await ctx.send(f"IP адрес сайта {target}: {socket.gethostbyname(target)}")#print(f"IP адрес сайта {target}: {socket.gethostbyname(taget)} ")



@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def time(ctx):
    await ctx.send(datetime.datetime.now())




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
async def on_everyban(message):
    if message.content.startswith('!BanEveryone'):
        for member in client.get_all_members():
            if member.bot:
                continue
            await member.ban(reason="*Причина бана*", delete_message_days=7)

@bot.command(pass_context=True)
async def start(ctx):
    await ctx.send("Привет я skippy, вот все комамды этого бота\n"
                   #"1) /ban\n"
                   #"2) /kick\n"
                   #"3) /ocistka\n"
                   "1) /ip\n"
                   "2) /time\n")

bot.run(token)

