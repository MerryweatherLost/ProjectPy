import random
import asyncio

from discord.ext import commands
from datetime import datetime

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command( aliases = ['flipcoin', 'coinflip', 'coin', 'headstails'] )
    async def cointoss(self, ctx):
        await ctx.reply("**Flipping Coin...** <a:CoinToss:893194255345012818>")
        await asyncio.sleep(1)
        responses = [ 'Heads.','Tails.' ]
        answer = random.choice(responses)
        await ctx.reply(f'{answer}')
        
    # EIGHT BALL METHOD
    @commands.command( aliases = ['8ball', 'eightball','🎱'] )
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
        print(f'[{date_object.strftime("%H:%M:%S - %b %d %Y")}] [ Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: EIGHTBALL - LOG: 8ball was utilized!\nThe question was: {question}, The answer was: {answer}')

def setup(client):
    client.add_cog(Fun(client))