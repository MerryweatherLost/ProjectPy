import discord
from discord.ext import commands

from library.ConsoleSelect import Time
from library.AnimeSelect import AnimeGel
from library.ConsoleSelect import Roundtrip

class Booru(commands.Cog):
    def __init__(self, client):
        self.client = client

# SAFE FOR WORK SECTION
    # WALLPAPER - SFW
    @commands.command(help = "Some safe for work wallpapers.")
    @commands.cooldown(rate = 1, per = 1.0)
    async def wallpaper(self, ctx):
        WALLPAPER = await AnimeGel.WALLPAPER()
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
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)
        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: BOORU.PY - LOG: Wallpaper was utilized in #{ctx.channel}! \n[Raw Data: {WALLPAPER}]')

    # ZETTAI RYOUIKI - SFW  
    @commands.command(help = 'I do not need to explain.', aliases = ['thighhighs','thigh-highs','zr'])
    @commands.cooldown( rate = 1, per = 1.0 )
    async def zettairyouiki(self, ctx):
        ZETTAI = await AnimeGel.ZETTAI()
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
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: BOORU.PY - LOG: Zettai Ryouiki was utilized in #{ctx.channel}! \n[Raw Data: {ZETTAI}]')


    # UNIFORM - SFW
    @commands.command(help = "Uniform time.")
    @commands.cooldown( rate = 1, per = 1.0 )
    async def uniform(self, ctx):
        UNIFORM = await AnimeGel.UNIFORM()
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
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: BOORU.PY - LOG: Uniform was utilized in #{ctx.channel}! \n[Raw Data: {UNIFORM}]')


    # CAR - SFW
    @commands.command(help = 'Car images. ????', aliases = ['vroom'])
    @commands.cooldown(rate = 1, per = 1.0)
    async def car(self, ctx):
        CAR = await AnimeGel.CAR()
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
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: BOORU.PY - LOG: Car was utilized in #{ctx.channel}! \n[Raw Data: {CAR}]')

    # GUN - SFW
    @commands.command(help = 'Gun images.', aliases = ['pew'])
    @commands.cooldown(rate = 1, per = 1.0)
    async def gun(self, ctx):
        GUN = await AnimeGel.GUN()
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
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)
        
        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: BOORU.PY - LOG: Gun was utilized in #{ctx.channel}! \n[Raw Data: {GUN}]')

    # CATGIRL - SFW
    @commands.command(help = "Catgirls.", aliases = ['cat'])
    @commands.cooldown(rate = 1, per = 1.0)
    async def catgirl(self, ctx):
        CATGIRL = await AnimeGel.CATGIRL()
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
            text = f'{self.client.user.name}'
        )
        message = ctx.message
        embed.timestamp = message.created_at
        await ctx.reply(embed = embed)

        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: BOORU.PY - LOG: Catgirl was utilized in #{ctx.channel}! \n[Raw Data: {CATGIRL}]')

def setup(client):
    client.add_cog(Booru(client))