import hmtai
import discord

from discord.ext import commands

class Akansfw(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # ZETTAI RYOUIKI - NSFW
    @commands.command(help = "(NSFW ONLY) Do I even need to explain?", aliases = ['thighhighs','thigh-highs','zr'])
    @commands.is_nsfw()
    async def zettairyouiki(self, ctx):
        embed=discord.Embed(
            title="Zettau Ryouiki", 
            description="Here is the image!", 
            color=discord.Color.blue())
        embed.set_author(
            name=ctx.author.display_name, 
            icon_url=ctx.author.avatar_url)
        embed.set_image(
            url=hmtai.useHM("2_9","zetRyo"), 
        )
        await ctx.reply(embed=embed)
    
    # UNIFORM - NSFW
    @commands.command(help = "(NSFW ONLY) uniform time.")
    @commands.is_nsfw()
    async def nsfwuniform(self, ctx):
        embed=discord.Embed(
            title="Uniform", 
            description="Here is the image!", 
            color=discord.Color.blue())
        embed.set_author(
            name=ctx.author.display_name, 
            icon_url=ctx.author.avatar_url)
        embed.set_image(
            url=hmtai.useHM("2_9","uniform"), 
        )
        await ctx.reply(embed=embed)
    
    # AHEGAO - NSFW
    @commands.command(help = "(NSFW ONLY)")
    @commands.is_nsfw()
    async def ahegao(self, ctx):
        embed=discord.Embed(
            title="Ahegao", 
            description="Here is the image!", 
            color=discord.Color.blue())
        embed.set_author(
            name=ctx.author.display_name, 
            icon_url=ctx.author.avatar_url)
        embed.set_image(
            url=hmtai.useHM("2_9","ahegao"), 
        )
        await ctx.reply(embed=embed)
        

    # GIF - NSFW
    @commands.command(help = "(NSFW ONLY) GIF images.", aliases = ['gifnsfw'])
    @commands.is_nsfw()
    async def nsfwgif(self, ctx):
        embed=discord.Embed(
            title="GIF Image", 
            description="Here is the image!", 
            color=discord.Color.blue())
        embed.set_author(
            name=ctx.author.display_name, 
            icon_url=ctx.author.avatar_url)
        embed.set_image(
            url=hmtai.useHM("2_9","gif"), 
        )
        await ctx.reply(embed=embed)
    
    # DOUJIN - NSFW
    @commands.command(help = "(NSFW ONLY) Manga images.", aliases = ['doujinshi','nsfwmanga'])
    @commands.is_nsfw()
    async def doujin(self, ctx):
        embed=discord.Embed(
            title="Doujin", 
            description="Here is the image!", 
            color=discord.Color.blue())
        embed.set_author(
            name=ctx.author.display_name, 
            icon_url=ctx.author.avatar_url)
        embed.set_image(
            url=hmtai.useHM("2_9","manga"), 
        )
        await ctx.reply(embed=embed)
    
    
    # JAHY - QUESTIONABLE
    @commands.command(help = "(NSFW ONLY) Jahy, Jahy, Jahy.")
    @commands.is_nsfw()
    async def jahy(self, ctx):
        embed=discord.Embed(
            title="Jahy", 
            description="Here is the image!", 
            color=discord.Color.blue())
        embed.set_author(
            name=ctx.author.display_name, 
            icon_url=ctx.author.avatar_url)
        embed.set_image(
            url=hmtai.useHM("2_9","jahy"), 
        )
        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Akansfw(client))