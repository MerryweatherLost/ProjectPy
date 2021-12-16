import discord
from owoify.owoify import owoify

from library.console import *
from discord.ext import commands

from owoify import owoify

class Owoify(commands.Cog, description = 'owo.'):
    def __init__(self, client):
        self.client = client
        self.owo = owoify
        
    @commands.group(help = 'Holds all owoify subcommands.')
    async def owoify(self, ctx):
        if ctx.invoked_subcommand is None:
            em = discord.Embed (description = 'That is not a visible subcommand.', color = signature)
            await ctx.reply(embed = em)

    @owoify.command(help = 'Lower Level.')
    async def low(self, ctx, *, msg:str):
        await ctx.reply(self.owo(msg, 'owo'))
            
    @owoify.command(help = 'Medium Level.')
    async def med(self, ctx, *, msg:str):
        await ctx.reply(self.owo(msg, 'uwu'))
        
    @owoify.command(help = 'Maximum Level.')
    async def max(self, ctx, *, msg:str):
        await ctx.reply(self.owo(msg, 'uvu'))   
            
def setup(client):
    client.add_cog(Owoify(client))