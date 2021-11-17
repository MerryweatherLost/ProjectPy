import discord
import akaneko

from library.ConsoleSelect import *
from discord.ext import commands
from private.config import signature

class Akaneko(commands.Cog):
    def __init__(self, client):
        self.client = client
        # AKANEKO = akaneko.nsfw.ass()
        # AKANEKO = akaneko.nsfw.bdsm()
        # AKANEKO = akaneko.nsfw.blowjob()
        # AKANEKO = akaneko.nsfw.bondage()
        # AKANEKO = akaneko.nsfw.netorare()
        # AKANEKO = akaneko.nsfw.doujin()
        # AKANEKO = akaneko.nsfw.yuri()
        # AKANEKO = akaneko.nsfw.thighs()
        # AKANEKO = akaneko.nsfw.succubus()
        # AKANEKO = akaneko.nsfw.gangbang()
        # AKANEKO = akaneko.nsfw.tentacles()
        # AKANEKO = akaneko.nsfw.foxgirl()
        
    # Akaneko Group - SFW / Nekomimi if invoked without subcommand.
    @commands.group(help = 'Group that contains all the safe for work commands in this library. Otherwise, it returns a nekomimi if no subcommand is invoked.')
    async def akaneko(self, ctx):
        if ctx.invoked_subcommand is None:
            img = akaneko.sfw.neko()
            em = discord.Embed (
                title = "Nekomimi",
                description = "If you were trying to access other commands, do so by `prefix` akaneko `subcommand`!",
                color = Color.white
            )
            em.set_image  (url = img)
            em.set_footer (text = f'{self.client.user.name}')
            em.timestamp = ctx.message.created_at
            await ctx.reply(embed = em)
            await Console.log(Time.CST(), Roundtrip.rt(self), "AKANEKO.PY", "Foxgirl", ctx.channel, f"[Raw Data: {img}]")
    
    # Foxgirl
    @akaneko.command(help = 'Images of a foxgirl.')
    async def foxgirl(self, ctx):
        img = akaneko.sfw.foxgirl()
        em = discord.Embed (
            title = "Foxgirl",
            color = Color.white
        )
        em.set_image  (url = img)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "AKANEKO.PY", "Foxgirl", ctx.channel, f"[Raw Data: {img}]")
    
    # Wallpaper / Desktop
    @akaneko.command(help = 'Desktop oriented wallpapers.')
    async def wallpaper(self, ctx):
        img = akaneko.sfw.wallpapers()
        em = discord.Embed (
            title = "Wallpaper",
            color = Color.white
        )
        em.set_image  (url = img)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "AKANEKO.PY", "Wallpaper - Desktop", ctx.channel, f"[Raw Data: {img}]")
        
    # Wallpaper - Mobile
    @akaneko.command(help = 'Mobile oriented wallpapers.')
    async def mobilewallpaper(self, ctx):
        img = akaneko.sfw.mobileWallpapers()
        em = discord.Embed (
            title = "Mobile Wallpaper",
            color = Color.white
        )
        em.set_image  (url = img)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "AKANEKO.PY", "Wallpaper - Mobile", ctx.channel, f"[Raw Data: {img}]")
    
    # Akaneko - NSFW Commands
    @commands.group(help = 'Group that contains all the not safe for work commands in this library.')
    @commands.is_nsfw()
    async def akansfw(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed (description = 'That is not a visible subcommand.', color = signature)
            await ctx.reply(embed = embed)
        
    @akansfw.command(help = 'Desktop oriented wallpapers. (NSFW)')
    async def nsfwwallpaper(self, ctx):
        img = akaneko.nsfw.wallpapers()
        em = discord.Embed (
            title = "Wallpaper (NSFW)",
            color = Color.white
        )
        em.set_image  (url = img)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "AKANEKO.PY", "Wallpaper - Desktop (NSFW)", ctx.channel, f"[Raw Data: {img}]")
        
    @akansfw.command(help = 'Mobile oriented wallpapers. (NSFW)')
    async def nsfwmobilewallpaper(self, ctx):
        img = akaneko.nsfw.mobileWallpapers()
        em = discord.Embed (
            title = "Mobile Wallpaper (NSFW)",
            color = Color.white
        )
        em.set_image  (url = img)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "AKANEKO.PY", "Wallpaper - Mobile (NSFW)", ctx.channel, f"[Raw Data: {img}]")
        
    @akansfw.command(help = 'Returns uniform images. (NSFW)')
    async def uniform(self, ctx):
        img = akaneko.nsfw.uniform()
        em = discord.Embed (
            title = "Uniform (NSFW)",
            color = Color.white
        )
        em.set_image  (url = img)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "AKANEKO.PY", "Uniform (NSFW)", ctx.channel, f"[Raw Data: {img}]")
        
    @akansfw.command(help = 'Returns maid images. (NSFW)')
    async def maid(self, ctx):
        img = akaneko.nsfw.maid()
        em = discord.Embed (
            title = "Maid (NSFW)",
            color = Color.white
        )
        em.set_image  (url = img)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "AKANEKO.PY", "Maid (NSFW)", ctx.channel, f"[Raw Data: {img}]")
    
    @akansfw.command(help = 'Returns school oriented settings or imagery. (NSFW)')
    async def school(self, ctx):
        img = akaneko.nsfw.school()
        em = discord.Embed (
            title = "School (NSFW)",
            color = Color.white
        )
        em.set_image  (url = img)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "AKANEKO.PY", "School (NSFW)", ctx.channel, f"[Raw Data: {img}]")

    @akansfw.command(help = 'Returns images with glasses involved. (NSFW)')
    async def glasses(self, ctx):
        img = akaneko.nsfw.glasses()
        em = discord.Embed (
            title = "Glasses (NSFW)",
            color = Color.white
        )
        em.set_image  (url = img)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "AKANEKO.PY", "Glasses (NSFW)", ctx.channel, f"[Raw Data: {img}]")
 
    @akansfw.command(help = 'Returns hentai imagery. (NSFW)')
    async def hentai(self, ctx):
        img = akaneko.nsfw.hentai()
        em = discord.Embed (
            title = "Hentai (NSFW)",
            color = Color.white
        )
        em.set_image  (url = img)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "AKANEKO.PY", "Hentai (NSFW)", ctx.channel, f"[Raw Data: {img}]")       

    @akansfw.command(help = 'Returns gif images. (NSFW)')
    async def gif(self, ctx):
        img = akaneko.nsfw.gif()
        em = discord.Embed (
            title = "Gif (NSFW)",
            color = Color.white
        )
        em.set_image  (url = img)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "AKANEKO.PY", "Gif (NSFW)", ctx.channel, f"[Raw Data: {img}]")
        
    # @akansfw.command()
    # async def name(self, ctx):
    #     img = EDIT
    #     em = discord.Embed (
    #         title = "EDIT (NSFW)",
    #         color = Color.white
    #     )
    #     em.set_image  (url = img)
    #     em.set_footer (text = f'{self.client.user.name}')
    #     em.timestamp = ctx.message.created_at
    #     await ctx.reply(embed = em)
    #     Console.log(Time.CST(), Roundtrip.rt(self), "AKANEKO.PY", "EDIT", ctx.channel, f"[Raw Data: {img}]")
                
        
    
def setup(client):
    client.add_cog(Akaneko(client))