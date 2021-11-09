import discord
import hmtai

from discord.ext import commands
from private.config import signature

from library.ConsoleSelect import Time
from library.ConsoleSelect import Roundtrip

class Hmtai(commands.Cog):
    def __init__(self, client):
        self.client = client

    # HMTAI GROUP
    @commands.group(help = 'HMtai library which contains subcommands of hmtai.')
    async def hmtai(self, ctx):
        if ctx.invoked_subcommand is None:
            em = discord.Embed (description = 'Unable to find that subcommand! Please use `help htmai` to view them!')
            await ctx.reply(embed = em)
    
    # DLC - VEIN05'S LIBRARY
    @hmtai.command(help = 'DLC imagery from the port.')
    @commands.is_nsfw()
    async def dlc(self, ctx):
        em = discord.Embed (title = "HMTAI - DLC")
        em.set_author (name = ctx.author.display_name, icon_url = ctx.author.avatar_url)
        em.set_image  (url = hmtai.useHM("dlc", "vein05"))
        em.set_footer (text = f'{self.client.user.name}')

        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        
    # DEPRESSION
    @hmtai.command(help = 'Simulate crippiling depression.')
    async def depression(self, ctx):
        em = discord.Embed (title = "HMTAI - Depression", color = signature)
        em.set_author (name = ctx.author.display_name, icon_url = ctx.author.avatar_url)
        em.set_image  (url = hmtai.useHM("2_9","depression"),)
        em.set_footer (text = f'{self.client.user.name}')

        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)

    # NEKO
    @hmtai.command(help = 'Neko images from the hmtai library.')
    async def neko(self, ctx):
        em = discord.Embed (title = "HMTAI - Neko", color = signature)
        em.set_author (name = ctx.author.display_name, icon_url = ctx.author.avatar_url)
        em.set_image  (url = hmtai.useHM("2_6","sfwNeko"),)
        em.set_footer (text = f'{self.client.user.name}')

        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)    

    # NSFW COMMANDS
    # ZETTAI RYOUIKI - NSFW
    @hmtai.command(help = 'Absolute Territory.', aliases = ['zettairyouiki','zr','thigh-highs','th','thighhighs'])
    @commands.is_nsfw()
    async def zettai(self, ctx):
        em = discord.Embed (title = "HMTAI - Zettai Ryouiki (NSFW)", color = signature)
        em.set_author (name = ctx.author.display_name, icon_url = ctx.author.avatar_url)
        em.set_image  (url = hmtai.useHM("2_9","zetRyo"),)
        em.set_footer (text = f'{self.client.user.name}')

        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)        

    # NEKO - NSFW
    @hmtai.command(help = 'Neko (nsfw) images from the hmtai library.')
    async def nsfwneko(self, ctx):
        em = discord.Embed (title = "HMTAI - Neko (NSFW)", color = signature)
        em.set_author (name = ctx.author.display_name, icon_url = ctx.author.avatar_url)
        em.set_image  (url = hmtai.useHM("2_9","nsfwNeko"),)
        em.set_footer (text = f'{self.client.user.name}')

        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)                

    # MOBILE WALLPAPER
    @hmtai.command(help = 'Returns nsfw mobile wallpapers.', aliases = ['mwallpaper','mwp','mobile'])
    async def mobilewallpaper(self, ctx):
        em = discord.Embed (title = "HMTAI - Name", color = signature)
        em.set_author (name = ctx.author.display_name, icon_url = ctx.author.avatar_url)
        em.set_image  (url = hmtai.useHM("2_9","nsfwMW"),)
        em.set_footer (text = f'{self.client.user.name}')

        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)    

    # # TEMPLATE
    # @hmtai.command(help = '')
    # async def name(self, ctx):
    #     em = discord.Embed (title = "HMTAI - Name", color = signature)
    #     em.set_author (name = ctx.author.display_name, icon_url = ctx.author.avatar_url)
    #     em.set_image  (url = hmtai.useHM("2_9","name"),)
    #     em.set_footer (text = f'{self.client.user.name}')

    #     em.timestamp = ctx.message.created_at
    #     await ctx.reply(embed = em)    

def setup(client):
    client.add_cog(Hmtai(client))