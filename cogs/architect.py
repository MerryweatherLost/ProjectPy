import discord
import asyncio
from discord.ext import commands
from datetime import datetime

class Architect(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help = "The Architects' Ban Hammer.")
    @commands.has_any_role('The Architect')
    async def architectban(self, ctx, member : discord.Member, *, reason = None):
            await member.ban(reason = reason)
            await ctx.reply(f'Banned {member.mention}!')
            date_object = datetime.now()
            print(f'[{date_object.strftime("%H:%M:%S - %b %d %Y")}] [ Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE | LOG - ABAN: A user was banned by the Architect! {member}')
        
def setup(client):
    client.add_cog(Architect(client))