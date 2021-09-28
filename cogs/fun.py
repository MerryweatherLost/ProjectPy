import random

from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # POPPY COMMAND
    @commands.command( aliases = ['fascist','nazi'])
    async def hitler(self, ctx):
        responses = ['Last time ive seen a nazi it was Poppy.', 'Poppy was Hitler all Along?', 
        'My Fascist Poppy Can not be this crazy!', 'Poppy Hated People that Dont Belong to His Kind?',
        'Geez, Poppy, Fine Ill take you to See George Wallace for the 50th Time.', 'Poppy is a Dixiecrat']

        await ctx.reply(f'{random.choice(responses)}')
    
    # 

def setup(client):
    client.add_cog(Fun(client))