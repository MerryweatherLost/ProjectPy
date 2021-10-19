import discord
from discord.ext import commands

from library.ConsoleLib import Time
from library.ConsoleLib import Essentials

class Math(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # MATH COMMAND
    @commands.command(help = 'Does a scheme of math.')
    async def math(self, ctx, num1: float, op, num2: float):
        # Arithmetic Operators - Float
        mathembed = discord.Embed (
            title = 'math.py - Normal Version',
            description = f'{Essentials.Math(num1, op, num2)}'
        )
        mathembed.set_footer (
            text = f'Tachibana: {Time.timeUTC()}'
        )
        await ctx.reply(embed = mathembed)

    @commands.command(aliases = ['mathr'], help = 'Rounds the math before calculating.')
    async def mathround(self, ctx, num1: int,  op, num2: int):
        # Arithmetic Operators - Integer
        mathembed = discord.Embed (
            title = 'math.py - Round Version',
            description = f'{Essentials.Math(num1, op, num2)}'
        )
        mathembed.set_footer (
            text = f'Tachibana: {Time.timeUTC()}'
        )
        await ctx.reply(embed = mathembed)

def setup(client):
    client.add_cog(Math(client))
