import asyncio
import discord

from library.console import Time
from library.console import Essentials
from library.console import Roundtrip

from library.anime import AnimeList
from library.anime import Positivity

from discord.ext import commands
    
class Anime(commands.Cog, description = 'General anime nuisances.'):
    def __init__(self, client):
        self.client = client

    # COFFEE - SFW
    @commands.command(help = 'Emotional Relief.')
    async def coffee(self, ctx):  
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
            url = AnimeList.Coffee()    
        )
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)

    # APPLEJUICE - SFW
    @commands.command(help = 'Emotional Relief.')
    async def applejuice(self, ctx):   
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
            url = AnimeList.AppleJuice()     
        )
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)

    # DHARMANN - SFW
    @commands.command(help = 'Emotional Relief.')
    async def dhar(self, ctx):
        embed = discord.Embed (
            title = 'Dhar Mann',
            description = f'**Hey Dhar Mann fam!** \n**Quote:** {AnimeList.dharMann("txt")}',
            color = discord.Color.default()
        )
        embed.set_author (
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
        )
        embed.set_image (
            url = AnimeList.dharMann("img")
        )
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)

    # DDLC - SFW
    @commands.command(help = 'Images of the Doki Doki Literature Club characters.')
    async def ddlc(self, ctx):    
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
            url = AnimeList.DokiDoki()   
        )
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)

    # POSITIVITY - SFW
    @commands.command(help = 'Sends positive message.')
    async def positivity(self, ctx):     
        embed = discord.Embed (
            title = 'Positive Message',
            description = f'**{Positivity.random_desc()}** \n{Positivity.random_quote()}',
            color = discord.Color.green()
        )
        embed.set_image (
            url = Positivity.image()
        )
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)
    
    # SPECIALWAIFU - SFW
    @commands.command(help = 'List of handpicked, pristine waifus.', aliases = ['waifuspec','specwaifu','wspec'])
    async def specialwaifu(self, ctx):   
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
            url = AnimeList.SpecialWaifu()
        )
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)

def setup(client):
    client.add_cog(Anime(client))