import discord

from ConsoleLib import Time
from pygelbooru import Gelbooru
from discord.ext import commands


gelbooru = Gelbooru('7a143b6b8021d138af296847f1354d36c893132b805a213b716c32677133b9ad', '847623')

class Booru(commands.Cog):
    def __init__(self, client):
        self.client = client

# SAFE FOR WORK SECTION
    # WALLPAPER - SFW
    @commands.command(help = "Some safe for work wallpapers.")
    @commands.cooldown(rate = 1, per = 1.0)
    async def wallpaper(self, ctx):
        WALLPAPER = await gelbooru.random_post ( 
            tags = ['wallpaper'], 
            exclude_tags = ['nude','sex','nipples','panties','anus','vaginal','cleavage'] 
        )
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
        await ctx.reply(embed = embed)
        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: BOORU.PY - LOG: Wallpaper was utilized! \n[Raw Data: {WALLPAPER}]')

    # ZETTAI RYOUIKI - SFW  
    @commands.command(help = 'I do not need to explain.', aliases = ['thighhighs','thigh-highs','zr'])
    @commands.cooldown( rate = 1, per = 1.0 )
    async def zettairyouiki(self, ctx):
        ZETTAI = await gelbooru.random_post ( 
            tags = ['1girl','thighhighs','highres'], 
            exclude_tags = ['nude','sex','nipples','panties','anus','vaginal','comic'] 
        )
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
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: BOORU.PY - LOG: Zettai Ryouiki was utilized! \n[Raw Data: {ZETTAI}]')


    # UNIFORM - SFW
    @commands.command(help = "Uniform time.")
    @commands.cooldown( rate = 1, per = 1.0 )
    async def uniform(self, ctx):
        UNIFORM = await gelbooru.random_post ( 
            tags = ['1girl','uniform','highres'], 
            exclude_tags = ['nude','sex','nipples','panties','anus','vaginal','comic'] 
        )
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
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: BOORU.PY - LOG: Uniform was utilized! \n[Raw Data: {UNIFORM}]')


    # CAR - SFW
    @commands.command(help = 'Car images. 🚗', aliases = ['vroom'])
    @commands.cooldown(rate = 1, per = 1.0)
    async def car(self, ctx):
        CAR = await gelbooru.random_post ( 
            tags = ['car'], 
            exclude_tags = ['nude','sex','nipples','panties','anus','vaginal','comic'] 
        )
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
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: BOORU.PY - LOG: Car was utilized! \n[Raw Data: {CAR}]')

    # GUN - SFW
    @commands.command(help = 'Gun images.', aliases = ['pew'])
    @commands.cooldown(rate = 1, per = 1.0)
    async def gun(self, ctx):
        GUN = await gelbooru.random_post ( 
            tags = ['gun'], 
            exclude_tags = ['nude','sex','nipples','panties','anus','vaginal','comic'] 
        )
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
        await ctx.reply(embed = embed)
        
        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: BOORU.PY - LOG: Gun was utilized! \n[Raw Data: {GUN}]')

    # CATGIRL - NSFW
    @commands.command(help = "Catgirls.", aliases = ['cat'])
    @commands.cooldown(rate = 1, per = 1.0)
    async def catgirl(self, ctx):
        CATGIRL = await gelbooru.random_post ( 
            tags = ['cat_girl','highres'],
            exclude_tags = ['nude','sex','nipples','panties','anus','vaginal','comic','penis'] 
        )
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
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: BOORU.PY - LOG: Gatgirl (NSFW) was utilized! \n[Raw Data: {CATGIRL}]')

def setup(client):
    client.add_cog(Booru(client))