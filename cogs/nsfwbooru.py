import discord

from ConsoleLib import Time
from pygelbooru import Gelbooru
from discord.ext import commands

gelbooru = Gelbooru('7a143b6b8021d138af296847f1354d36c893132b805a213b716c32677133b9ad', '847623')

class nsfwBooru(commands.Cog):
    def __init__(self, client):
        self.client = client

# NOT SAFE FOR WORK SECTION
    # ZETTAI RYOUIKI - NSFW
    @commands.command(help = "(NSFW ONLY) Do I even need to explain?", aliases = ['nsfwthighhighs','nsfwthigh-highs','nsfwzr'])
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def nsfwzettairyouiki(self, ctx):
        ROUNDTRIP = round(self.client.latency * 1000)
        NSFWZETTAI = await gelbooru.random_post ( 
            tags = ['1girl','thighhighs','highres'],
            exclude_tags = ['comic']
        )
        embed = discord.Embed (
            title = "Zettai Ryouiki", 
            description = "Here is the image!", 
            color = discord.Color.gold()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = NSFWZETTAI, 
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        embed.set_footer (
            text = f'Project PY: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {ROUNDTRIP}ms.] CONSOLE: BOORU.PY - LOG: Zettai Ryouiki (NSFW) was utilized! \n[Raw Data: {NSFWZETTAI}]')

    
    # UNIFORM - NSFW
    @commands.command(help = "(NSFW ONLY) uniform time.")
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def nsfwuniform(self, ctx):
        ROUNDTRIP = round(self.client.latency * 1000)
        NSFWUNIFORM = await gelbooru.random_post ( 
            tags = ['1girl','uniform','highres'],
            exclude_tags = ['comic']
        )
        embed = discord.Embed (
            title = "Uniform Image", 
            description = "Here is the image!", 
            color = discord.Color.gold()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = NSFWUNIFORM, 
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        embed.set_footer (
            text = f'Project PY: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {ROUNDTRIP}ms.] CONSOLE: BOORU.PY - LOG: Uniform (NSFW) was utilized! \n[Raw Data: {NSFWUNIFORM}]')

    
    # AHEGAO - NSFW
    @commands.command(help = "(NSFW ONLY) facial expressions.")
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def ahegao(self, ctx):
        ROUNDTRIP = round(self.client.latency * 1000)
        AHEGAO = await gelbooru.random_post ( 
            tags = ['ahegao','highres'],
            exclude_tags = ['comic']
        )
        embed = discord.Embed (
            title = "Ahegao Image", 
            description = "Here is the image!", 
            color = discord.Color.gold()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = AHEGAO, 
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        embed.set_footer (
            text = f'Project PY: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {ROUNDTRIP}ms.] CONSOLE: BOORU.PY - LOG: Ahegao (NSFW) was utilized! \n[Raw Data: {AHEGAO}]')


    # GIF - NSFW
    @commands.command(help = "(NSFW ONLY) GIF images.", aliases = ['gifnsfw'])
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def nsfwgif(self, ctx):
        ROUNDTRIP = round(self.client.latency * 1000)
        GIF = await gelbooru.random_post ( 
            tags = ['animated_gif','highres']
        )
        embed = discord.Embed (
            title = "GIF Image", 
            description = "Here is the image!", 
            color = discord.Color.gold()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = GIF, 
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        embed.set_footer (
            text = f'Project PY: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {ROUNDTRIP}ms.] CONSOLE: BOORU.PY - LOG: Gif (NSFW) was utilized! \n[Raw Data: {GIF}]')

    # DOUJIN - NSFW
    @commands.command(help = "(NSFW ONLY) Manga images.", aliases = ['doujinshi','nsfwmanga'])
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def doujin(self, ctx):
        ROUNDTRIP = round(self.client.latency * 1000)
        MANGA = await gelbooru.random_post ( 
            tags = ['comic','highres']
        )
        embed = discord.Embed (
            title = "Doujin Image", 
            description = "Here is the image!", 
            color = discord.Color.gold()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = MANGA, 
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        embed.set_footer (
            text = f'Project PY: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {ROUNDTRIP}ms.] CONSOLE: BOORU.PY - LOG: Doujinshi (NSFW) was utilized! \n[Raw Data: {MANGA}]')

    # CATGIRL - NSFW
    @commands.command(help = "(NSFW ONLY) catgirls.", aliases = ['nsfwcat','catgirlnsfw'])
    @commands.cooldown(rate = 1, per = 1.0)
    @commands.is_nsfw()
    async def nsfwcatgirl(self, ctx):
        ROUNDTRIP = round(self.client.latency * 1000)
        NSFWCATGIRL = await gelbooru.random_post ( 
            tags = ['cat_girl','highres'],
            exclude_tags = ['comic']
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
            url = NSFWCATGIRL, 
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        embed.set_footer (
            text = f'Project PY: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)

        print(f'[{Time.timeFormat()}] [Roundtrip: {ROUNDTRIP}ms.] CONSOLE: BOORU.PY - LOG: Catgirl (NSFW) was utilized! \n[Raw Data: {NSFWCATGIRL}]')

def setup(client):
    client.add_cog(nsfwBooru(client))