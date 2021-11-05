import random
import asyncio
import discord

from discord.ext import commands

from library.ConsoleSelect import *
from library.GenshinSelect import Genshin
from library.PoliticalSelect import USA

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command( help = "Coin Tosser.", aliases = ['flipcoin', 'coinflip', 'coin', 'headstails','<a:CoinToss:893194255345012818>'] )
    async def cointoss(self, ctx,):
        message: discord.Message = await ctx.reply("**Flipping Coin...** <a:CoinToss:893194255345012818>")
        await asyncio.sleep(1)
        answer = Essentials.CoinToss()
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
            text = f'Tachibana: {Time.dateTimeUTC()}'
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

        answer = Essentials.eightball()
        embed = discord.Embed (
            title = "8-Ball", 
            description = f'Question: **{question}**\nAnswer: **{answer}**',
            color = discord.Color.default()
        )
        embed.set_thumbnail (
            url = Essentials.ballImage(),            
        )
        embed.set_author (
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
        )
        embed.set_footer (
            text = f'Tachibana: {Time.dateTimeUTC()}'
        )
        await asyncio.sleep(1)   

        await message.delete()
        await ctx.reply(embed = embed)
        
        await Console.log(Time.timeCST(), Roundtrip.rt(self), "FUN.PY", "8Ball", ctx.channel, f"[Question: {str.capitalize(question)}] [Answer: {answer}]")
    
    # POPPY METHOD
    @commands.command( help = 'You know what I am talking about.', aliases = ['hitler','fascist'] )
    @commands.has_any_role('The Architect')
    async def poppy(self, ctx):
        responses = [
            'Literally Poppy.','Last time I heard of Poppy was when he was meeting David Duke.',
            'Poppy is a true Neo-Confederate.','Poppy? Why he is the biggest nationalist you have ever seen.',
            'How come Poppy is a Neanderthal?'
        ]
        answer = random.choice(responses)   
        await ctx.reply(answer)

    # AVATAR METHOD
    @commands.command(help = 'Pulls the avatar of yourself.', aliases = ['av'])
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed (
            title = f"{member.display_name}'s Profile Image",
            color = member.color
        )
        embed.set_author (
            name = member.display_name,
            icon_url = member.avatar_url
        )
        embed.set_image (
            url = member.avatar_url
        )
        await ctx.reply(embed = embed)
    
    # STATE METHOD
    @commands.command(help = 'Returns state flags. (information coming soon...)')
    async def state(self, ctx, *, name):
        embed = discord.Embed()
        embed.set_image(url = USA.states(str.lower(name)))

        await ctx.reply(embed = embed)
        await Console.log(Time.timeCST(), Roundtrip.rt(self), "FUN.PY", "State", ctx.channel, f"[State Flag: {str.title(name)}]")

    # TERRITORY METHOD
    @commands.command(help = 'Returns territory flags. (information coming soon...)')
    async def territory(self, ctx, *, name):
        embed = discord.Embed(color = Color.tachi)
        embed.set_image(url = USA.territories(str.lower(name)))
        
        await ctx.reply(embed = embed)
        await Console.log(Time.timeCST(), Roundtrip.rt(self), "FUN.PY", "Territory", ctx.channel, f"[Territory Flag: {str.title(name)}]")

    # GENSHIN IMPACT METHOD
    @commands.command(help = 'Returns genshin impact images.')
    async def genshin(self, ctx, *, name):
        embed = discord.Embed(color = Color.tachi)
        embed.set_image(url = Genshin.characters(str.lower(name)))

        await ctx.reply(embed = embed)
        await Console.log(Time.timeCST(), Roundtrip.rt(self), "FUN.PY", "Territory", ctx.channel, f"[Territory Flag: {str.title(name)}]")
     
    # .
    @commands.command(name = '.', help = '.')
    async def dot(self, ctx):
        message: discord.Message = await ctx.reply('.')  
        await asyncio.sleep(1); message.delete()

def setup(client):
    client.add_cog(Fun(client))