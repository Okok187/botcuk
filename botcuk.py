import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
scores={"1302200946075369472":0}
lis={"1":"IŞIKLARI KAPA","2":"MUSLUĞU KAPA"}
description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description, intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
@bot.event
async def on_guild_join(self, guild):
    scores[guild] = 0


@bot.command()
async def puanım(ctx):
    await ctx.send(scores[str(ctx.guild.id)])
@bot.command()
async def ekle(ctx):
    scores[str(ctx.guild.id)]+=10
@bot.command()
async def liste(ctx):
    await ctx.send("yaptığınız şeyin üstten sırasını giriniz bu metin buna dahil değildir ve bunu !yaptığım ve numarası olarak yazınız")
    await ctx.send(lis["1"])
    await ctx.send(lis["2"])
@bot.command()
async def yaptığım(ctx,c:str):
    await ctx.send(lis[c])
    await ctx.send("bunu yaptınız için size 10 puan eklenmiştir")
    scores[str(ctx.guild.id)]+=10

bot.run('token here')
