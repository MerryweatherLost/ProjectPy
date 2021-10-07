
import discord

from discord.ext import commands

# GENERAL COMMANDS

class General(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # PING METHOD
    @commands.command(help = 'Pings the round client latency.', aliases = ['🏓'])
    async def ping(self, ctx):
        embed = discord.Embed (
            title = f'🏓 **Pong!** {round(self.client.latency * 1000)}ms.',
            color = discord.Color.red()
        )
        await ctx.reply(embed = embed)

    # GITHUB
    @commands.command(help = 'Sends the github of the creator.', aliases = ['git'])
    async def github(self, ctx):
        await ctx.reply(f'Here is the GitHub of my creator: https://github.com/MerryweatherLost')

def setup(client):
    client.add_cog(General(client))