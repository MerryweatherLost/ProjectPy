import asyncio
import discord

from discord.ext import commands

from library.ConsoleSelect import *
from library.FunSelect import _Fun

from library.GenshinSelect import Genshin
from library.PoliticalSelect import USA

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command( help = "Coin Tosser.", aliases = ['flipcoin', 'coinflip', 'coin', 'headstails','<a:CoinToss:893194255345012818>'] )
    async def cointoss(self, ctx,):
        message: discord.Message = await ctx.reply("**Flipping Coin...** <a:CoinToss:893194255345012818>")
        await asyncio.sleep(1)
        answer = _Fun.coin_toss()
        await message.edit(content = f'{answer}')
   
    # PYTHON METHOD
    @commands.command( help = "The language it was programmed in.", aliases = ['py'] )
    async def python(self, ctx):
        embed = discord.Embed (
            title = 'Python Website',
            description = 'Python is the language I was programmed in.',
            url = 'https://www.python.org/', 
            color = Color.tachi
        )
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        await ctx.reply(embed = embed) 

    # EIGHT BALL METHOD
    @commands.command ( 
        help = "8ball, takes in one argument, the question. EX: 8ball will I gain fortune?", 
        name = "8ball", 
        aliases = ['eightball','🎱'] 
    )
    async def _8ball(self, ctx, *, question):
        message: discord.Message = await ctx.reply('8ball is thinking... <a:checkmark:903852585360949289>')    
        answer = _Fun.eight_ball('txt')
        embed = discord.Embed (
            title = "8-Ball", 
            description = f'Question: **{question}**\nAnswer: **{answer}**',
            color = discord.Color.default()
        )
        embed.set_thumbnail (
            url = _Fun.eight_ball('url')           
        )
        embed.set_author (
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
        )
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        embed.timestamp = message.created_at
        await asyncio.sleep(1)   

        await message.delete()
        await ctx.reply(embed = embed)
        
        await Console.log(Time.CST(), Roundtrip.rt(self), "FUN.PY", "8Ball", ctx.channel, f"[Question: {str.capitalize(question)}] [Answer: {answer}]")
    
    # STATE METHOD
    @commands.command(help = 'Returns state flags. (information coming soon...)')
    async def state(self, ctx, *, name):
        embed = discord.Embed()
        embed.set_image(url = await USA.states(str.lower(name)))
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)
        await Console.log(Time.CST(), Roundtrip.rt(self), "FUN.PY", "State", ctx.channel, f"[State Flag: {str.title(name)}]")

    # TERRITORY METHOD
    @commands.command(help = 'Returns territory flags. (information coming soon...)')
    async def territory(self, ctx, *, name):
        embed = discord.Embed(color = Color.tachi)
        embed.set_image(url = await USA.territories(str.lower(name)))
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at        
        await ctx.reply(embed = embed)
        await Console.log(Time.CST(), Roundtrip.rt(self), "FUN.PY", "Territory", ctx.channel, f"[Territory Flag: {str.title(name)}]")

    # GENSHIN IMPACT METHOD
    @commands.command(help = 'Returns genshin impact images.')
    async def genshin(self, ctx, *, name):
        embed = discord.Embed(color = Color.tachi)
        embed.set_image(url = await Genshin.characters(str.lower(name)))
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)
        await Console.log(Time.CST(), Roundtrip.rt(self), "FUN.PY", "Territory", ctx.channel, f"[Territory Flag: {str.title(name)}]")
     
    # .
    @commands.command(name = '.', help = '.')
    async def dot(self, ctx):
        message: discord.Message = await ctx.reply('.')  
        await asyncio.sleep(1); message.delete()

def setup(client):
    client.add_cog(Fun(client))