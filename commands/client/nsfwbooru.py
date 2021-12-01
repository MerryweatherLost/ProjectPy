import discord
from discord.ext import commands

from library.ConsoleSelect import Time
from library.ConsoleSelect import Roundtrip

from library.AnimeSelect import AnimeNSFWGel

class nsfwBooru(commands.Cog):
    def __init__(self, client):
        self.client = client

# NOT SAFE FOR WORK SECTION
    # ZETTAI RYOUIKI - NSFW
    @commands.command(help = "(NSFW ONLY) Do I even need to explain?", aliases = ['nsfwthighhighs','nsfwthigh-highs','nsfwzr'])
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def nsfwzettairyouiki(self, ctx):
        NSFWZETTAI = await AnimeNSFWGel.nsfwzettai()
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
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: BOORU.PY - LOG: Zettai Ryouiki (NSFW) was utilized in #{ctx.channel}! \n[Raw Data: {NSFWZETTAI}]')

    
    # UNIFORM - NSFW
    @commands.command(help = "(NSFW ONLY) uniform time.")
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def nsfwuniform(self, ctx):
        NSFWUNIFORM = AnimeNSFWGel.nsfwuniform()
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
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: BOORU.PY - LOG: Uniform (NSFW) was utilized in #{ctx.channel}! \n[Raw Data: {NSFWUNIFORM}]')

    
    # AHEGAO - NSFW
    @commands.command(help = "(NSFW ONLY) facial expressions.")
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def ahegao(self, ctx):
        AHEGAO = AnimeNSFWGel.ahegao()
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
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: BOORU.PY - LOG: Ahegao (NSFW) was utilized in #{ctx.channel}! \n[Raw Data: {AHEGAO}]')


    # GIF - NSFW
    @commands.command(help = "(NSFW ONLY) GIF images.", aliases = ['gifnsfw'])
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def nsfwgif(self, ctx):
        GIF = AnimeNSFWGel.nsfwgif()
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
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: BOORU.PY - LOG: Gif (NSFW) was utilized in #{ctx.channel}! \n[Raw Data: {GIF}]')

    # DOUJIN - NSFW
    @commands.command(help = "(NSFW ONLY) Manga images.", aliases = ['doujinshi','nsfwmanga'])
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def doujin(self, ctx):
        MANGA = AnimeNSFWGel.doujinshi()
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
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: BOORU.PY - LOG: Doujinshi (NSFW) was utilized in #{ctx.channel}! \n[Raw Data: {MANGA}]')

    # CATGIRL - NSFW
    @commands.command(help = "(NSFW ONLY) catgirls.", aliases = ['nsfwcat','catgirlnsfw'])
    @commands.cooldown(rate = 1, per = 1.0)
    @commands.is_nsfw()
    async def nsfwcatgirl(self, ctx):
        NSFWCATGIRL = AnimeNSFWGel.nsfwcatgirl()
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
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: BOORU.PY - LOG: Catgirl (NSFW) was utilized in #{ctx.channel}! \n[Raw Data: {NSFWCATGIRL}]')

def setup(client):
    client.add_cog(nsfwBooru(client))