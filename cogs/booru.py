import discord

from discord.ext import commands
from pybooru import Danbooru

dancli = Danbooru ('danbooru', username = 'Kettenrad', api_key = 'MHjmmDEju9x9Lc5R8ncuEwE7')

class nsfwBooru(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # ZETTAI RYOUIKI - NSFW
    @commands.command(help = "(NSFW ONLY) Do I even need to explain?", aliases = ['thighhighs','thigh-highs','zr'])
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def zettairyouiki(self, ctx):
        posts = dancli.post_list (
            tags = 'zettai_ryouiki solo', 
            limit = 1, 
            random = True
        )
        for post in posts:
            ZETTAI = (post['file_url'])
            
        embed = discord.Embed (
            title = "Zettai Ryouiki", 
            description = "Here is the image!", 
            color = discord.Color.blue()
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
    
    # UNIFORM - NSFW
    @commands.command(help = "(NSFW ONLY) uniform time.")
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def uniform(self, ctx):
        posts = dancli.post_list (
            tags = 'uniform 1girl', 
            limit = 1, 
            random = True
        )
        for post in posts:
            UNIFORM = (post['file_url'])

        embed = discord.Embed (
            title = "Uniform", 
            description = "Here is the image!", 
            color = discord.Color.dark_green()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = UNIFORM 
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        await ctx.reply(embed = embed)
    
    # AHEGAO - NSFW
    @commands.command(help = "(NSFW ONLY) facial expressions.")
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def ahegao(self, ctx):
        posts = dancli.post_list (
            tags = 'ahegao', 
            limit = 1, 
            random = True
        )
        for post in posts:
            AHEGAO = (post['file_url'])

        embed = discord.Embed (
            title = "Ahegao", 
            description = "Here is the image!", 
            color = discord.Color.greyple()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = AHEGAO
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        await ctx.reply(embed = embed)

    # GIF - NSFW
    @commands.command(help = "(NSFW ONLY) GIF images.", aliases = ['gifnsfw'])
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def gif(self, ctx):
        posts = dancli.post_list (
            tags = 'animated_gif 1girl', 
            limit = 1, 
            random = True
        )
        for post in posts:
            GIF = (post['file_url'])

        embed = discord.Embed (
            title = "GIF Image", 
            description = "Here is the image!", 
            color = discord.Color.greyple()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = GIF
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        await ctx.reply(embed = embed)
    
    # DOUJIN - NSFW
    @commands.command(help = "(NSFW ONLY) Manga images.", aliases = ['doujinshi','nsfwmanga'])
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def doujin(self, ctx):
        posts = dancli.post_list (
            tags = 'comic sex', 
            limit = 1, 
            random = True
        )
        for post in posts:
            MANGA = (post['file_url'])

        embed = discord.Embed (
            title = "Manga Image", 
            description = "Here is the image!", 
            color = discord.Color.greyple()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = MANGA
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        await ctx.reply(embed = embed)
     
    
    # JAHY - QUESTIONABLE
    @commands.command(help = "(NSFW ONLY) Jahy, Jahy, Jahy.")
    @commands.cooldown( rate = 1, per = 1.0 )
    @commands.is_nsfw()
    async def jahy(self, ctx):
        posts = dancli.post_list (
            tags = 'jahy', 
            limit = 1, 
            random = True
        )
        for post in posts:
            JAHY = (post['file_url'])

        embed = discord.Embed (
            title = "Jahy Image", 
            description = "Here is the image!", 
            color = discord.Color.greyple()
            )
        embed.set_author (
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = JAHY
        )
        embed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895122429087739924/booru.png'
        )
        await ctx.reply(embed = embed)

def setup(client):
    client.add_cog(nsfwBooru(client))