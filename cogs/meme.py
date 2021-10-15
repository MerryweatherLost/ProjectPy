import asyncio
import discord

from discord.ext import commands

from library.ConsoleLib import Time
from library.ConsoleLib import Essentials

from library.MemeSelect import MemeList

class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    # RENAULT - SFW
    @commands.command(help = 'Renault. Renault.')
    async def renault(self, ctx):
        await ctx.reply(MemeList.Renault())

    # BIDEN - SFW
    @commands.command(help = 'Sends biden image.')
    async def biden(self, ctx):
        biden = discord.Embed (
            color = discord.Color.blue()
        )
        biden.set_image (
            url = MemeList.Biden()
        )
        await ctx.reply(embed = biden)
    
    # TRUMP - SFW
    @commands.command(help = 'Sends trump image.')
    async def trump(self, ctx):
        trump = discord.Embed (
            color = discord.Color.red()
        )
        trump.set_image (
            url = MemeList.Trump()
        )
        await ctx.reply(embed = trump)

    # BRI'ISH? - SFW
    @commands.command(name = "bri'ish", help = "bri'ish?")
    async def briish(self, ctx):
        embed = discord.Embed (
            description = 'Piss off mate!',
            color = discord.Color.greyple()
        )
        embed.set_image (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/898197974855868456/images.png'
        )
        message: discord.Message = await ctx.reply("bri'ish?")
        await asyncio.sleep(1)
        await message.edit(content = None, embed = embed)

def setup(client):
    client.add_cog(Meme(client))