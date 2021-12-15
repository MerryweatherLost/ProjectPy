import discord
from discord.ext import commands

from library.ConsoleSelect import Time
from library.ConsoleSelect import Essentials

from private.config import signature

class Math(commands.Cog, description = 'Math, feared by many, mastered by none.'):
    def __init__(self, client):
        self.client = client
    
    # MATH GROUP
    @commands.group(help = 'Provides two versions of math schemes.')
    async def math(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed (description = 'That is not a visible subcommand.', color = signature)
            await ctx.reply(embed = embed)

    # INTEGER MATH COMMAND
    @math.command(aliases = ['mathr', 'mathrnd'], help = 'Rounds the math before calculating.')
    async def standard(self, ctx, num1: int,  op, num2: int):
        # Arithmetic Operators - Integer
        mathembed = discord.Embed (
            title = 'math.py - Standard Version',
            description = f'{Essentials.Math(num1, op, num2)}'
        )
        mathembed.set_footer (
            text = f'{self.client.user.name}'
        )
        mathembed.timestamp = ctx.message.created_at
        await ctx.reply(embed = mathembed)

    # FLOAT MATH COMMAND
    @math.command(help = 'Does a scheme of math.')
    async def round(self, ctx, num1: float, op, num2: float):
        # Arithmetic Operators - Float
        mathembed = discord.Embed (
            title = 'math.py - Round Version',
            description = f'{Essentials.Math(num1, op, num2)}'
        )
        mathembed.set_footer (
            text = f'{self.client.user.name}'
        )
        mathembed.timestamp = ctx.message.created_at
        await ctx.reply(embed = mathembed)

def setup(client):
    client.add_cog(Math(client))
