import discord

from discord.ext import commands
from library.ConsoleSelect import Time
from library.ConsoleSelect import Roundtrip

class Architect(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help = "The Architects' Ban Hammer.")
    @commands.has_any_role('The Architect')
    async def architectban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.reply(f'Banned {member.mention}!')
        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: ARCHITECT.PY - LOG: ABan was utilized in #{ctx.channel}! [Member: {member}]')

def setup(client):
    client.add_cog(Architect(client))