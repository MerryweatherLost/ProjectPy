import asyncio
from asyncio.tasks import sleep
import discord

from library.ConsoleSelect import *

from discord.ext import commands
from private.config import signature

from anekos import NekosLifeClient, SFWImageTags, NSFWImageTags

class Neko(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.nya = NekosLifeClient()
        
    # ------------------   
    # Neko Group - Text and Images
    # ------------------             
    
    @commands.group(help = 'Lets you do some text oriented things, and if there is no invoked subcommand, neko images will be placed.', aliases = ['nekomimi'])
    async def neko(self, ctx):
        if ctx.invoked_subcommand is None:  
            res = await self.nya.image(SFWImageTags.NEKO)
            em = discord.Embed (
                title = "Nekomimi",
                description = "If you were trying to access other commands, do so by `prefix` neko `subcommand`!",
                color = discord.Color.dark_grey()
            )
            em.set_image  (url = res.url)
            em.set_footer (text = f'{self.client.user.name}')
            em.timestamp = ctx.message.created_at
            await ctx.reply(embed = em)
            await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Neko", ctx.channel, f"[Raw Data: {res.url}]")
    
    # -- Neko Text -- #          
    
    # Neko Owoify
    @neko.command(help = 'Owoify a message.')
    async def owoify(self, ctx, *, text: str):
        if len(text) < 1 or len(text) > 200:
            message: discord.Message = await ctx.reply("**Your text must be between 1 or 200 characters!**")
            await asyncio.sleep(3); await message.delete(); return
        else: result = await self.nya.owoify(text)
        await ctx.reply(result.text)
    
    # Neko Cat Text   
    @neko.command(help = 'Sends catlike text.')
    async def cattext(self, ctx):
        result = await self.nya.random_cat_text()
        await ctx.reply(result.text)

    # Neko Fact
    @neko.command(help = 'Neko facts.')
    async def fact(self, ctx):
        result = await self.nya.random_fact_text()
        await ctx.reply(result.text)
    
    # -- Neko Images - SFW Branch -- #    
    
    # Neko Random
    @neko.command(help = 'Returns a random image.')
    async def random(self, ctx):
        result = await self.nya.random_image(sfw = True, nsfw = False)
        em = discord.Embed (
            title = "Random",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = result.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        
    # Neko Meow
    @neko.command(help = 'Images of actual cats.')
    async def meow(self, ctx):
        res = await self.nya.image(SFWImageTags.MEOW)
        em = discord.Embed (
            title = "Meow",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Meow", ctx.channel, f"[Raw Data: {res.url}]")

    # Neko GIF
    @neko.command(help = 'Images of nekos doing cute stuff. (Animated)')
    async def gif(self, ctx):
        res = await self.nya.image(SFWImageTags.NEKOGIF)
        em = discord.Embed (
            title = "Gif",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "GIF", ctx.channel, f"[Raw Data: {res.url}]")

    # Neko Avatar
    @neko.command(help = 'Fetches a neko avatar.', aliases = ['av'])
    async def avatar(self, ctx):
        res = await self.nya.image(SFWImageTags.AVATAR)
        em = discord.Embed (
            title = "Neko Avatar",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Avatar", ctx.channel, f"[Raw Data: {res.url}]")
 
    # Smug
    @neko.command(help = 'Fetches smug nekos doing smug things.')
    async def smug(self, ctx):
        res = await self.nya.image(SFWImageTags.SMUG)
        em = discord.Embed (
            title = "Smug",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Smug", ctx.channel, f"[Raw Data: {res.url}]")
    
    # Baka
    @neko.command(help = 'Baka...')
    async def baka(self, ctx):
        res = await self.nya.image(SFWImageTags.BAKA)
        em = discord.Embed (
            title = "Baka",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Baka", ctx.channel, f"[Raw Data: {res.url}]")

    # Neko Cuddle
    @neko.command(help = 'Cuddling images.')
    async def cuddle(self, ctx):
        res = await self.nya.image(SFWImageTags.CUDDLE)
        em = discord.Embed (
            title = "Cuddle",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Cuddle", ctx.channel, f"[Raw Data: {res.url}]")

    # Neko Feed
    @neko.command(help = 'Feeding images.')
    async def feed(self, ctx):
        res = await self.nya.image(SFWImageTags.FEED)  
        em = discord.Embed (
            title = "Feed",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Feed", ctx.channel, f"[Raw Data: {res.url}]")

    # Neko Waifu
    @neko.command(help = 'Waifu images.')
    async def waifu(self, ctx):
        res = await self.nya.image(SFWImageTags.WAIFU)
        em = discord.Embed (
            title = "Waifu",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Waifu", ctx.channel, f"[Raw Data: {res.url}]")
        
    # Neko Slap
    @neko.command(help = 'Slapping images.')
    async def slap(self, ctx):
        res = await self.nya.image(SFWImageTags.SLAP)
        em = discord.Embed (
            title = "Slap",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Slap", ctx.channel, f"[Raw Data: {res.url}]")     
           
    # Neko Pat
    @neko.command(help = 'Patting images.')
    async def pat(self, ctx):
        res = await self.nya.image(SFWImageTags.PAT)    
        em = discord.Embed (
            title = "Pat",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Pat", ctx.channel, f"[Raw Data: {res.url}]")
        
    @neko.command(help = 'Poking images.')
    async def poke(self, ctx):
        res = await self.nya.image(SFWImageTags.POKE)
        em = discord.Embed (
            title = "Poke",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Poke", ctx.channel, f"[Raw Data: {res.url}]")
    
    @neko.command(help = 'Kissing images.')
    async def kiss(self, ctx):
        res = await self.nya.image(SFWImageTags.KISS)  
        em = discord.Embed (
            title = "Kiss",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Cuddle", ctx.channel, f"[Raw Data: {res.url}]")
        
    # Neko Wallpaper
    @neko.command(help = 'Cuddling images.')
    async def wallpaper(self, ctx):
        res = await self.nya.image(SFWImageTags.WALLPAPER)
        em = discord.Embed (
            title = "Wallpaper",
            color = discord.Color.dark_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Wallpaper", ctx.channel, f"[Raw Data: {res.url}]")
                      
    # ------------------               
    # NSFW Image Library
    # ------------------      
    
    @commands.group(help = 'NSFW category of neko imagery and miscellaneous items.')
    @commands.is_nsfw()
    async def nekonsfw(self, ctx):
        if ctx.invoked_subcommand is None:
            res = await self.nya.image(NSFWImageTags.ERONEKO)
            em = discord.Embed (
                title = "Neko (NSFW)",
                description = "If you were trying to access other commands, do so by `prefix` nekonsfw `subcommand`!",
                color = discord.Color.darker_grey()
            )
            em.set_image  (url = res.url)
            em.set_footer (text = f'{self.client.user.name}')
            em.timestamp = ctx.message.created_at
            await ctx.reply(embed = em)
            await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Neko (NSFW)", ctx.channel, f"[Raw Data: {res.url}]")      
  
    # Neko Gif (NSFW)
    @nekonsfw.command(help = 'Not safe for work nekos. (NSFW) (Animated)')
    async def gif(self, ctx):
        res = await self.nya.image(NSFWImageTags.NSFW_NEKO_GIF)
        em = discord.Embed (
            title = "Neko Gif (NSFW)",
            color = discord.Color.darker_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Gif (NSFW)", ctx.channel, f"[Raw Data: {res.url}]")
 
    # Neko Avatar (NSFW)
    @nekonsfw.command(help = 'Images of neko avatars. (NSFW)')
    async def avatar(self, ctx):
        res = await self.nya.image(NSFWImageTags.AVATAR)
        em = discord.Embed (
            title = "Avatar (NSFW)",
            color = discord.Color.darker_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Avatar (NSFW)", ctx.channel, f"[Raw Data: {res.url}]")
     
    # Neko Boobs (NSFW)
    @nekonsfw.command(help = 'Images of neko avatars. (NSFW)')
    async def boobs(self, ctx, size = None):
        if size != None: str.lower(size)
        if (size == 'small'): res = await self.nya.image(NSFWImageTags.SMALLBOOBS); si = 'Small'
        else: res = await self.nya.image(NSFWImageTags.BOOBS); si = 'Normal'
        
        em = discord.Embed (
            title = f"Boobs (NSFW) - {si}",
            color = discord.Color.darker_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Boobs (NSFW)", ctx.channel, f"[Raw Data: {res.url}] [Size: {si}]")
                   
    # Neko Spank (NSFW)
    @nekonsfw.command(help = 'Spanking image. (NSFW)')
    async def spank(self, ctx):
        res = await self.nya.image(NSFWImageTags.SPANK)
        em = discord.Embed (
            title = "Spank (NSFW)",
            color = discord.Color.darker_grey()
        )
        em.set_image  (url = res.url)
        em.set_footer (text = f'{self.client.user.name}')
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "NEKO.PY", "Spank (NSFW)", ctx.channel, f"[Raw Data: {res.url}]")
                                
def setup(client):
    client.add_cog(Neko(client))