import random
from datetime import datetime

from discord.ext import commands

class General(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # PING METHOD
    @commands.command(aliases = ['🏓'])
    async def ping(self, ctx):
        await ctx.reply(f'🏓 **Reported Latency:** {round(self.client.latency * 1000)}ms.')

    # GITHUB
    @commands.command(aliases = ['git'])
    async def github(self, ctx):
        await ctx.reply(f'Here is the GitHub of my creator: https://github.com/MerryweatherLost')

    # EIGHT BALL METHOD
    @commands.command( aliases = ['8ball', 'eightball','🎱'] )
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes.',
                    'Outlook good.', 'Signs point to yes.', 'Reply hazy, try again.',
                    'Ask again later.','Can not predict now.', "Don't count on it.",
                    'My reply is no.', 'My sources say no.', 'Obviously not.',]
                    
        await ctx.reply(f'Question: **{question}**\nAnswer: {random.choice(responses)}')
        date_object = datetime.now()
        print(f'{date_object} | CONSOLE | EIGHTBALL | LOG: EightBall was utilized!\nThe question was: {question}')

    @commands.command( aliases = ['fascist','nazi'])
    async def hitler(self, ctx):
        responses = ['Last time ive seen a nazi it was Poppy.', 'Poppy was Hitler all Along?', 
        'My Fascist Poppy Can not be this crazy!', 'Poppy Hated People that Dont Belong to His Kind?',
        'Geez, Poppy, Fine Ill take you to See George Wallace for the 50th Time.', 'Poppy is a Dixiecrat']

        await ctx.reply(f'{random.choice(responses)}')
        
def setup(client):
    client.add_cog(General(client))