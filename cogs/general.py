import random
import asyncio
import discord

from discord import message
from datetime import datetime
from discord.ext import commands

# GENERAL COMMANDS

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
        question_var = await ctx.reply("**Awaiting Response from** 🎱 <a:loading:893139868157354034> ...")
        await asyncio.sleep(1)
        responses = [
            # POSITIVES
            'It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes.',
            'Outlook good.', 'Signs point to yes.', 'That is correct.',
            'That is incorrect.','Indeed.', 'Affirmative.',
            # NEUTRALS
            'Reply hazy, try again.',
            'Ask again later.','Can not predict now.', 
            'I can not find a result for that, try again.','Try again.',
            # NEGATIVES
            "Don't count on it.", 'My reply is no.', 'My sources say no.', 
            'Obviously not.', 'Negative.'
        ]
           
        await ctx.reply(f'Question: **{question}**\nAnswer: {random.choice(responses)}')
    
        date_object = datetime.now()
        print(f'{date_object} | CONSOLE | EIGHTBALL - LOG: EightBall was utilized!\nThe question was: {question}')
        
def setup(client):
    client.add_cog(General(client))