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
        await ctx.reply(hmtai.listHM("2_6","wallpaper"))
    
    # MOBILE WALLPAPER - SFW
    @commands.command(help = "Some safe for work mobile walpapers.")
    async def mobilewallpaper(self, ctx):
        await ctx.reply(hmtai.listHM("2_6","mobileWallpaper"))
        
    # NEKO - SFW
    @commands.command(help = "Some safe for work neko images. - Request from Ho Chi Minh")
    async def akaneko(self, ctx):
        await ctx.reply(akaneko.sfw.neko())
    
    # FOXGIRL - SFW
    @commands.command(help = "Some safe for work foxgirl images. - Request from Ho Chi Minh")
    async def akafoxgirl(self, ctx):
        await ctx.reply(akaneko.sfw.foxgirl())
        
def setup(client):
    client.add_cog(Akaneko(client))