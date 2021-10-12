import discord

from ConsoleLib import Time
from ConsoleLib import Essentials

from AnimeSelect import AnimeList
from discord.ext import commands
    
class Anime(commands.Cog):
    def __init__(self, client):
        self.client = client

    # COFFEE - SFW
    @commands.command(help = 'Emotional Relief.')
    async def coffee(self, ctx):
        COFFEE = AnimeList.Coffee()
        embed = discord.Embed (
            title = 'Coffee',
            description = 'Have some coffee! ☕',
            color = discord.Color.green()
            )
        embed.set_author (
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = COFFEE
            )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: ANIME.PY - LOG: Coffee was utilized! \n[Raw Data: {COFFEE}]')

    # APPLEJUICE - SFW
    @commands.command(help = 'Emotional Relief.')
    async def applejuice(self, ctx):
        APPL = AnimeList.AppleJuice()
        embed = discord.Embed (
            title = 'Apple Juice',
            description = 'Have some apple juice! 🍎',
            color = discord.Color.red()
            )
        embed.set_author (
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = APPL
            )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: ANIME.PY - LOG: Apple Juice was utilized! \n[Raw Data: {APPL}]')

    # DHARMANN - SFW
    @commands.command(help = 'Emotional Relief.')
    async def dhar(self, ctx):
        DHAR = AnimeList.Dhar()
        embed = discord.Embed (
            title = 'Dhar Mann',
            description = f'Hey Dhar Mann fam!: {DHAR}',
            color = discord.Color.default()
        )
        embed.set_author (
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
        )
        embed.set_image (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/896981047848353812/unknown.png'
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: ANIME.PY - LOG: Dhar was utilized! \n[Raw Data: {DHAR}]')

    # DDLC - SFW
    @commands.command(help = 'Images of the Doki Doki Literature Club characters.')
    async def ddlc(self, ctx):
        DDLC = AnimeList.DokiDoki()
        embed = discord.Embed (
            title = 'DDLC',
            description = 'Here is the image!',
            color = discord.Color.red()
            )
        embed.set_author (
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
        )
        embed.set_image (
            url = DDLC
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: ANIME.PY - LOG: DDLC was utilized! \n[Raw Data: {DDLC}]')
    
    # RENAULT - SFW
    @commands.command(help = 'Renault. Renault.')
    async def renault(self, ctx):
        await ctx.reply(AnimeList.Renault())

def setup(client):
    client.add_cog(Anime(client))