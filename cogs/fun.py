import random
import asyncio

from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command( aliases = ['flipcoin', 'coinflip', 'coin', 'headstails'] )
    async def cointoss(self, ctx):
        await ctx.reply("**Flipping Coin...** <a:CoinToss:893194255345012818>")
        await asyncio.sleep(1)
        responses = [
            'Heads.','Tails.'
        ]
        await ctx.reply(f'{random.choice(responses)}')
    

def setup(client):
    client.add_cog(Fun(client))