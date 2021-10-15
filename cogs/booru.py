import discord
from discord.ext import commands

from library.ConsoleLib import Time
from library.AnimeSelect import AnimeGelbooru

class Booru(commands.Cog):
    def __init__(self, client):
        self.client = client

# SAFE FOR WORK SECTION
    # WALLPAPER - SFW
    @commands.command(help = "Some safe for work wallpapers.")
    @commands.cooldown(rate = 1, per = 1.0)
    async def wallpaper(self, ctx):
        WALLPAPER = await AnimeGelbooru.WALLPAPER()
        embed = discord.Embed (
            title = "Wallpaper Image", 
            description = "Here is the image!", 
            color = discord.Color.light_grey()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = WALLPAPER, 
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        embed.set_footer (
            text = f'Tachibana: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)
        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: BOORU.PY - LOG: Wallpaper was utilized! \n[Raw Data: {WALLPAPER}]')

    # ZETTAI RYOUIKI - SFW  
    @commands.command(help = 'I do not need to explain.', aliases = ['thighhighs','thigh-highs','zr'])
    @commands.cooldown( rate = 1, per = 1.0 )
    async def zettairyouiki(self, ctx):
        ZETTAI = await AnimeGelbooru.ZETTAI()
        embed = discord.Embed (
            title = "Zettai Ryouiki", 
            description = "Here is the image!", 
            color = discord.Color.light_grey()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = ZETTAI, 
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        embed.set_footer (
            text = f'Tachibana: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: BOORU.PY - LOG: Zettai Ryouiki was utilized! \n[Raw Data: {ZETTAI}]')


    # UNIFORM - SFW
    @commands.command(help = "Uniform time.")
    @commands.cooldown( rate = 1, per = 1.0 )
    async def uniform(self, ctx):
        UNIFORM = await AnimeGelbooru.UNIFORM()
        embed = discord.Embed (
            title = "Uniform", 
            description = "Here is the image!", 
            color = discord.Color.light_grey()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = UNIFORM, 
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        embed.set_footer (
            text = f'Tachibana: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: BOORU.PY - LOG: Uniform was utilized! \n[Raw Data: {UNIFORM}]')


    # CAR - SFW
    @commands.command(help = 'Car images. 🚗', aliases = ['vroom'])
    @commands.cooldown(rate = 1, per = 1.0)
    async def car(self, ctx):
        CAR = await AnimeGelbooru.CAR()
        embed = discord.Embed (
            title = "Car Image", 
            description = "Here is the image!", 
            color = discord.Color.light_grey()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = CAR, 
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        embed.set_footer (
            text = f'Tachibana: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: BOORU.PY - LOG: Car was utilized! \n[Raw Data: {CAR}]')

    # GUN - SFW
    @commands.command(help = 'Gun images.', aliases = ['pew'])
    @commands.cooldown(rate = 1, per = 1.0)
    async def gun(self, ctx):
        GUN = await AnimeGelbooru.GUN()
        embed = discord.Embed (
            title = "Gun Image", 
            description = "Here is the image!", 
            color = discord.Color.light_grey()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = GUN, 
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        embed.set_footer (
            text = f'Tachibana: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)
        
        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: BOORU.PY - LOG: Gun was utilized! \n[Raw Data: {GUN}]')

    # CATGIRL - SFW
    @commands.command(help = "Catgirls.", aliases = ['cat'])
    @commands.cooldown(rate = 1, per = 1.0)
    async def catgirl(self, ctx):
        CATGIRL = await AnimeGelbooru.CATGIRL()
        embed = discord.Embed (
            title = "Catgirl Image", 
            description = "Here is the image!", 
            color = discord.Color.gold()
        )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
        )
        embed.set_image (
            url = CATGIRL, 
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        embed.set_footer (
            text = f'Tachibana: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: BOORU.PY - LOG: Catgirl was utilized! \n[Raw Data: {CATGIRL}]')

def setup(client):
    client.add_cog(Booru(client))