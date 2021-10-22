import random
import asyncio
import discord

from discord.ext import commands

from library.ConsoleSelect import Time
from library.ConsoleSelect import Essentials
from library.ConsoleSelect import Roundtrip
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

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: COINTOSS - LOG: cointoss was utilized in #{ctx.channel}! [ Coin: {answer} ]')
   
    # PYTHON METHOD
    @commands.command( help = "The language it was programmed in.", aliases = ['py'] )
    async def python(self, ctx):
        embed = discord.Embed (
            title = 'Python Website',
            description = 'Python is the language I was programmed in.',
            url = 'https://www.python.org/',
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
        AUTHOR_NAME = ctx.author.display_name
        AUTHOR_IMAGE = ctx.author.avatar_url

        message: discord.Message = await ctx.reply('8ball is thinking... <a:loading:893139868157354034>')    

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
            name = AUTHOR_NAME,
            icon_url = AUTHOR_IMAGE
        )
        embed.set_footer (
            text = f'Tachibana: {Time.dateTimeUTC()}'
        )
        await asyncio.sleep(1)   

        await message.delete()
        await ctx.reply(embed = embed)
        
        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: EIGHTBALL - LOG: 8ball was utilized in #{ctx.channel}! [ Question: {str.upper(question)} ] [ Answer: {answer} ]')
    
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
        if (member == None):
            PROFILE = ctx.author.display_name
            IMAGE = ctx.author.avatar_url
            COLOR = ctx.author.color
        else:
            PROFILE = member.display_name
            IMAGE = member.avatar_url
            COLOR = member.color

        embed = discord.Embed (
            title = f"{PROFILE}'s Profile Image",
            color = COLOR
        )
        embed.set_author (
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
        )
        embed.set_image (
            url = IMAGE
        )
        await ctx.reply(embed = embed)
    
    # STATE METHOD
    @commands.command(help = 'Returns state flags. (information coming soon...)')
    async def state(self, ctx, *, name):
        embed = discord.Embed()
        embed.set_image(url = USA.states(str.lower(name)))

        await ctx.reply(embed = embed)
        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: STATE - LOG: State was utilized in #{ctx.channel}! [State Flag: {str.title(name)}]')

    # TERRITORY METHOD
    @commands.command(help = 'Returns territory flags. (information coming soon...)')
    async def territory(self, ctx, *, name):
        embed = discord.Embed()
        embed.set_image(url = USA.territories(str.lower(name)))
        
        await ctx.reply(embed = embed)
        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: TERRITORY - LOG: Territory was utilized in #{ctx.channel}! [Territory Flag: {str.title(name)}]')

    # GENSHIN IMPACT METHOD
    @commands.command(help = 'Returns genshin impact images.')
    async def genshin(self, ctx, *, name):
        embed = discord.Embed()
        embed.set_image(url = Genshin.characters(str.lower(name)))

        await ctx.reply(embed = embed)
        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: GENSHIN - LOG: Genshin was utilized in #{ctx.channel}! [Genshin Impact Character: {str.title(name)}]')
     

    # .
    @commands.command(name = '.', help = '.')
    async def dot(self, ctx):
        await ctx.reply('.')  

def setup(client):
    client.add_cog(Fun(client))