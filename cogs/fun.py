import random
import asyncio
import discord

from discord.ext import commands
from datetime import datetime

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command( help = "Coin Tosser.", aliases = ['flipcoin', 'coinflip', 'coin', 'headstails'] )
    async def cointoss(self, ctx):
        await ctx.reply("**Flipping Coin...** <a:CoinToss:893194255345012818>")
        await asyncio.sleep(1)
        responses = [ 'Heads.','Tails.' ]
        answer = random.choice(responses)
        await ctx.reply(f'{answer}')
    
    # PYTHON METHOD
    @commands.command( help = "The language it was programmed in.", aliases = ['py'] )
    async def python(self, ctx):
        await ctx.reply('Python is the language I was programmed in.') 

    # EIGHT BALL METHOD
    @commands.command( help = "8ball, takes in one argument, the question. EX: 8ball will I gain fortune?", name = "8ball", aliases = ['eightball','🎱'] )
    async def _8ball(self, ctx, *, question):
        await ctx.reply("**Awaiting Response from** 🎱 <a:loading:893139868157354034> ...")
        await asyncio.sleep(1)
        responses = [
            # POSITIVES
            'It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes.',
            'Outlook good.', 'Signs point to yes.', 'That is correct.',
            'Indeed.', 'Affirmative.',
            # NEUTRALS
            'Reply hazy, try again.',
            'Ask again later.','Can not predict now.', 
            'I can not find a result for that, try again.','Try again.',
            # NEGATIVES
            "Don't count on it.", 'My reply is no.', 'My sources say no.', 
            'Obviously not.', 'Negative.','Absolutely false.','Decidedly not.',
            'No', 'That is incorrect.'
        ]
        answer = random.choice(responses)   
        await ctx.reply(f'Question: **{question}**\nAnswer: {answer}')
    
        date_object = datetime.now()
        print(f'[{date_object.strftime("%H:%M:%S - %b %d %Y")}] [ Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: EIGHTBALL - LOG: 8ball was utilized! [ Question: {question} ] [ Answer: {answer} ]')
    
    # POPPY METHOD
    @commands.command( help = 'You know what I am talking about.', aliases = ['hitler','fascist'] )
    async def poppy(self, ctx):
        responses = [
            'Literally Poppy.','Last time I heard of Poppy was when he was meeting David Duke.',
            'Poppy is a true Neo-Confederate.','Poppy? Why he is the biggest nationalist you have ever seen.',
            'How come Poppy is a Neanderthal?'
        ]
        answer = random.choice(responses)   
        await ctx.reply(answer)

def setup(client):
    client.add_cog(Fun(client))