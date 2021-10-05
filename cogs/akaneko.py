import discord
import akaneko

from discord.ext import commands
import hmtai

class Akaneko(commands.Cog):
    def __init__(self, client):
        self.client = client

    # WALLPAPER - SFW
    @commands.command(help = "Some safe for work wallpapers.")
    async def wallpaper(self, ctx):
        embed = discord.Embed (
            title = "Wallpaper", 
            description = "Here is the image!", 
            color = discord.Color.blue())
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url)
        embed.set_image (
            url = akaneko.sfw.wallpapers() 
        )
        await ctx.reply(embed=embed)
    
    # MOBILE WALLPAPER - SFW
    @commands.command(help = "Some safe for work mobile walpapers.")
    async def mobilewallpaper(self, ctx):
        embed = discord.Embed (
            title = "Mobile Wallpaper", 
            description = "Here is the image!", 
            color = discord.Color.blue())
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url)
        embed.set_image (
            url = akaneko.sfw.mobileWallpapers()
        )
        await ctx.reply(embed=embed)
        
    # NEKO - SFW
    @commands.command(help = 'Some safe for work neko images.')
    async def akaneko(self, ctx):
        embed = discord.Embed (
            title = "Neko", 
            description = "Here is the image!", 
            color = discord.Color.blue())
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url)
        embed.set_image (
            url = akaneko.sfw.neko(), 
        )
        await ctx.reply(embed=embed)
    
    # FOXGIRL - SFW
    @commands.command(help = 'Some safe for work foxgirl images.')
    async def akafoxgirl(self, ctx):
        embed = discord.Embed (
            title = "Foxgirl", 
            description = "Here is the image!", 
            color = discord.Color.blue())
        embed.set_author ( 
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url)
        embed.set_image (
            url = akaneko.sfw.foxgirl(), 
        )
        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Akaneko(client))