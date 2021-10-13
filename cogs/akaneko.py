import discord
import akaneko

from library.ConsoleLib import Time
from discord.ext import commands

class Akaneko(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # MOBILE WALLPAPER - SFW
    @commands.command(help = "Some safe for work mobile walpapers.")
    async def mobilewallpaper(self, ctx):
        AKANEKO = akaneko.sfw.mobileWallpapers()
        embed = discord.Embed (
            title = "Mobile Wallpaper", 
            description = "Here is the image!", 
            color = discord.Color.blue())
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url)
        embed.set_image (
            url = AKANEKO
        )
        embed.set_footer (
            text = f'Project PY: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)
        
        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: AKANEKO.PY - LOG: Mobile Wallpaper was utilized! \n[Raw Data: {AKANEKO}]')
        
    # NEKO - SFW
    @commands.command(help = 'Some safe for work neko images.')
    async def akaneko(self, ctx):
        AKANEKO = akaneko.sfw.neko()
        embed = discord.Embed (
            title = "Neko", 
            description = "Here is the image!", 
            color = discord.Color.blue())
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url)
        embed.set_image (
            url = AKANEKO
        )
        embed.set_footer (
            text = f'Project PY: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)
    
        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: AKANEKO.PY - LOG: Neko was utilized! \n[Raw Data: {AKANEKO}]')
    
    # FOXGIRL - SFW
    @commands.command(help = 'Some safe for work foxgirl images.')
    async def akafoxgirl(self, ctx):
        AKANEKO = akaneko.sfw.foxgirl()
        embed = discord.Embed (
            title = "Foxgirl", 
            description = "Here is the image!", 
            color = discord.Color.blue())
        embed.set_author ( 
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url)
        embed.set_image (
            url = AKANEKO
        )
        embed.set_footer (
            text = f'Project PY: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: AKANEKO.PY - LOG: Foxgirl was utilized! \n[Raw Data: {AKANEKO}]')

def setup(client):
    client.add_cog(Akaneko(client))