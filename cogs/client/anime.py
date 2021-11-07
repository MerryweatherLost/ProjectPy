import asyncio
import discord

from library.ConsoleSelect import Time
from library.ConsoleSelect import Essentials
from library.ConsoleSelect import Roundtrip

from library.AnimeSelect import DharMann
from library.AnimeSelect import AnimeList

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
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: ANIME.PY - LOG: Coffee was utilized in #{ctx.channel}! \n[Raw Data: {COFFEE}]')

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
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: ANIME.PY - LOG: Apple Juice was utilized in #{ctx.channel}! \n[Raw Data: {APPL}]')

    # DHARMANN - SFW
    @commands.command(help = 'Emotional Relief.')
    async def dhar(self, ctx):
        DHAR = DharMann.DharQuote()   
        DHARIMG = DharMann.DharImage()    
        embed = discord.Embed (
            title = 'Dhar Mann',
            description = f'**Hey Dhar Mann fam!** \n**Quote:** {DHAR}',
            color = discord.Color.default()
        )
        embed.set_author (
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
        )
        embed.set_image (
            url = DHARIMG
        )
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: ANIME.PY - LOG: Dhar was utilized in #{ctx.channel}! \n[Raw Data: {DHAR}]')

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
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: ANIME.PY - LOG: DDLC was utilized in #{ctx.channel}! \n[Raw Data: {DDLC}]')
    
    # POSITIVITY - SFW
    @commands.command(help = 'Sends positive message.')
    async def positivity(self, ctx):     
        POSIMG = AnimeList.PositivityImage()
        POSINFO = AnimeList.PositivityInfo()
        POSMSG = AnimeList.Positivity()
        embed = discord.Embed (
            title = 'Positive Message',
            description = f'**{POSINFO}** \n{POSMSG}',
            color = discord.Color.green()
        )
        embed.set_image (
            url = POSIMG
        )
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: ANIME.PY - LOG: POSITIVITY was utilized in #{ctx.channel}! \n[Raw Data: {POSIMG}] \n[Quote: {POSMSG}]')
    
    # SPECIALWAIFU - SFW
    @commands.command(help = 'List of handpicked, pristine waifus.', aliases = ['waifuspec','specwaifu','wspec'])
    async def specialwaifu(self, ctx):   
        WAIFUSPECIAL = AnimeList.SpecialWaifu()
        embed = discord.Embed (
            title = 'Special Waifu Image',
            description = 'Here is the image!',
            color = discord.Color.gold()
        )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
        )
        embed.set_image (
            url = WAIFUSPECIAL
        )
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: ANIME.PY - LOG: SPECIALWAIFU was utilized in #{ctx.channel}! \n[Raw Data: {WAIFUSPECIAL}]')

def setup(client):
    client.add_cog(Anime(client))