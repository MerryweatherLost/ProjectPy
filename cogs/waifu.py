import discord
import hmtai

from waifu import WaifuAioClient
from discord.ext import commands

class Waifu(commands.Cog):
    def __init__(self, client):
        self.client = client

    ## WAIFU GENERATOR

    # GENERAL
    @commands.command( help = 'General Waifu image.', aliases = ['waifugen','wgen'] )
    async def waifu(self, ctx):
        async with WaifuAioClient() as client:
            sfw_waifu: str = await client.sfw(category='waifu')
            embed = discord.Embed (
                title = "Waifu Image", 
                description = "Here is the image!", 
                color = discord.Color.blue())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = sfw_waifu, 
            )
            await ctx.reply(embed = embed)

    # NEKO
    @commands.command(help = 'Neko Waifu image.')
    async def neko(self, ctx):
        async with WaifuAioClient() as client:
            sfw_neko: str = await client.sfw(category='neko')
            embed = discord.Embed (
                title = "Neko Image", 
                description = "Here is the image!", 
                color = discord.Color.blue())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = sfw_neko, 
            )
            await ctx.reply(embed = embed)

    
    # HIGHFIVE
    @commands.command(help = 'Give a high five to someone. EX: :highfive @member.', aliases = ['hifive','high-five','hf'] )
    async def highfive(self, ctx, member : discord.Member):
        async with WaifuAioClient() as client:
            sfw_highfive: str = await client.sfw(category = 'highfive')
            await ctx.reply(f'Heya {member.mention}, here is a high five!\n{sfw_highfive}')            
    
    # HAPPY
    @commands.command(help = 'Happy image of a waifu.')
    async def happy(self, ctx):
        async with WaifuAioClient() as client:
            sfw_happy: str = await client.sfw(category = 'happy')
            embed = discord.Embed (
                title = "Happy Image", 
                description = "Here is the image!", 
                color = discord.Color.blue())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = sfw_happy, 
            )
            await ctx.reply(embed = embed)
    
    # SMILE
    @commands.command(help = 'Smiling image of a waifu.', aliases = ['🙂'])
    async def smile(self, ctx):
        async with WaifuAioClient() as client:
            sfw_smile: str = await client.sfw(category = 'smile')
            embed = discord.Embed (
                title = "Smile Image", 
                description = "Here is the image!", 
                color = discord.Color.blue())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = sfw_smile, 
            )
            await ctx.reply(embed=embed)

    # SMUG
    @commands.command(help = 'Smug image of a waifu. - My personal favorite.')
    async def smug(self, ctx):
        async with WaifuAioClient() as client:
            sfw_smug: str = await client.sfw(category = 'smug')
            embed = discord.Embed (
                title = "Smug Image", 
                description = "Here is the image!", 
                color = discord.Color.blue())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = sfw_smug, 
            )
            await ctx.reply(embed=embed)

    # DANCE
    @commands.command(help = 'Dance image of a waifu.')
    async def dance(self, ctx):
        async with WaifuAioClient() as client:
            sfw_dance: str = await client.sfw(category = 'smile')
            embed = discord.Embed (
                title = "Dancing Image", 
                description = "Here is the image!", 
                color = discord.Color.blue())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = sfw_dance, 
            )
            await ctx.reply(embed=embed)

    # CRY
    @commands.command(help = 'Crying image of a waifu.')
    async def cry(self, ctx):
        async with WaifuAioClient() as client:
            sfw_cry: str = await client.sfw(category = 'cry')
            embed = discord.Embed (
                title = "Crying Image", 
                description = "Here is the image!", 
                color = discord.Color.blue())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = sfw_cry, 
            )
            await ctx.reply(embed=embed)

    # KILL
    @commands.command(help = 'Kill a member in chat. EX: :kill @member.', aliases = ['murder', 'slaughter'] )
    async def kill(self, ctx, member : discord.Member):
        async with WaifuAioClient() as client:
            sfw_kill: str = await client.sfw(category = 'kill')
            await ctx.reply(f'**You just killed** {member.mention}!\n{sfw_kill}')
    
    # HUG
    @commands.command(help = 'Hug a member in chat. EX: :hug @member.',)
    async def hug(self, ctx, member : discord.Member):
        async with WaifuAioClient() as client:
            sfw_hug: str = await client.sfw(category = 'hug')
            await ctx.reply(f'**You just hugged** {member.mention}!\n{sfw_hug}')
    
    # WAVE
    @commands.command(help = 'Wave at a member in chat. EX: :wave @member.')
    async def wave(self, ctx, member : discord.Member ):
        async with WaifuAioClient() as client:
            sfw_wave: str = await client.sfw(category = 'wave')
            await ctx.reply(f'**You just waved at** {member.mention}!\n{sfw_wave}')
    
    # BONK
    @commands.command(help = 'Bonk a member in chat. EX: :bonk @member.')
    async def bonk(self, ctx, member : discord.Member ):
        async with WaifuAioClient() as client:
            sfw_bonk: str = await client.sfw(category = 'bonk')
            await ctx.reply(f'**You just bonked** {member.mention}!')
            embed = discord.Embed ( 
                title = 'Bonk Image',
                color = discord.Color.blue())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = sfw_bonk, 
            )
            await ctx.reply(embed = embed)
        
    # DEPRESSION
    @commands.command(help = 'Simulate crippiling depression.')
    async def depression(self, ctx):
        embed=discord.Embed(
            title = "Depression Image", 
            description = "Here is the image!", 
            color = discord.Color.blue())
        embed.set_author(
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url)
        embed.set_image(
            url = hmtai.useHM("2_9","depression"), 
        )
        await ctx.reply(embed=embed)


def setup(client):
    client.add_cog(Waifu(client))