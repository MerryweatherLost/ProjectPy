import discord
import akaneko

from library.ConsoleSelect import Time
from library.ConsoleSelect import Color
from library.ConsoleSelect import Roundtrip

from library.AnimeSelect import AkaNSFW

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
            text = f'Tachibana: {Time.dateTimeUTC()}'
        )
        await ctx.reply(embed = embed)
        
        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: AKANEKO.PY - LOG: Mobile Wallpaper was utilized in #{ctx.channel}! \n[Raw Data: {AKANEKO}]')
        
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
            text = f'Tachibana: {Time.dateTimeUTC()}'
        )
        await ctx.reply(embed = embed)
    
        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: AKANEKO.PY - LOG: Neko was utilized in #{ctx.channel}! \n[Raw Data: {AKANEKO}]')
    
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
            text = f'Tachibana: {Time.dateTimeUTC()}'
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: AKANEKO.PY - LOG: Foxgirl was utilized in #{ctx.channel}! \n[Raw Data: {AKANEKO}]')

    # SCHOOL - NSFW
    @commands.command(help = 'Not safe for work school images.')
    async def akaschool(self, ctx):
        AKASCHOOL = AkaNSFW.school()
        school = discord.Embed (
            title = "School Image",
            description = "Here is the image!",
            color = Color.tachi
        )
        school.set_author ( 
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
        )
        school.set_image (
            url = AKASCHOOL
        )
        school.set_footer (
            text = f'Tachibana: {Time.dateTimeUTC()}'
        )
        await ctx.reply(embed = school)        

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: AKANEKO.PY - LOG: School was utilized in #{ctx.channel}! \n[Raw Data: {AKASCHOOL}]')

    # MAID - NSFW
    @commands.command(help = 'Not safe for work school images.')
    async def akamaid(self, ctx):
        AKAMAID = AkaNSFW.maid()
        school = discord.Embed (
            title = "Maid Image",
            description = "Here is the image!",
            color = Color.tachi
        )
        school.set_author ( 
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
        )
        school.set_image (
            url = AKAMAID
        )
        school.set_footer (
            text = f'Tachibana: {Time.dateTimeUTC()}'
        )
        await ctx.reply(embed = school)        

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: AKANEKO.PY - LOG: akamaid was utilized in #{ctx.channel}! \n[Raw Data: {AKAMAID}]')
        
    # GIF - NSFW
    @commands.command(help = 'Not safe for work school images.')
    async def akagif(self, ctx):
        AKAGIF = AkaNSFW.gif()
        school = discord.Embed (
            title = "GIF Image",
            description = "Here is the image!",
            color = Color.tachi
        )
        school.set_author ( 
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
        )
        school.set_image (
            url = AKAGIF
        )
        school.set_footer (
            text = f'Tachibana: {Time.dateTimeUTC()}'
        )
        await ctx.reply(embed = school)        

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: AKANEKO.PY - LOG: akagif was utilized in #{ctx.channel}! \n[Raw Data: {AKAGIF}]')

def setup(client):
    client.add_cog(Akaneko(client))