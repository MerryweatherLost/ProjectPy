
import discord

from discord.ext import commands
from library.ConsoleLib import Time
from library.ConsoleLib import Color
from library.ConsoleLib import Roundtrip

# GENERAL COMMANDS

class General(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # PING METHOD
    @commands.command(help = 'Pings the round client latency.', aliases = ['🏓'])
    async def ping(self, ctx):
        embed = discord.Embed (
            description = f'⚪ **Pong! {Roundtrip.rt(self)}ms.**',
            color = Color.white
        )
        embed.set_footer (
            text = f"Tachibana: {Time.pureTimeUniversial()}"
        )
        await ctx.reply(embed = embed)

    # GITHUB
    @commands.command(help = 'Sends the github of the creator.', aliases = ['git'])
    async def github(self, ctx):
        await ctx.reply(f'Here is the GitHub of my creator: https://github.com/MerryweatherLost')
        
    # TOP DOG METHOD
    @commands.command(help = 'Returns highest role.', aliases = ['tr'])
    async def toprole(self, ctx, member: commands.MemberConverter = None):
        if (member == None):
            await ctx.reply(f'**Highest Role:** {ctx.author.top_role}')
        else:
            await ctx.reply(f'**Highest Role:** {member.top_role}')

    # ROLES
    @commands.command(help = 'Returns a number roles of a user or if not implimented, yours.')
    async def roles(self, ctx, member: commands.MemberConverter = None):
        if (member == None):
            await ctx.reply(f'**Number of Roles:** {len(ctx.author.roles)} roles detected for the user.')
        else:
            await ctx.reply(f'**Number of Roles:** {len(member.roles)} roles detected for the user.')

def setup(client):
    client.add_cog(General(client))