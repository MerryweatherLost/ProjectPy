import discord

from waifu import WaifuAioClient

from discord.ext import commands

class Waifu(commands.Cog):
    def __init__(self, client):
        self.client = client

    ## WAIFU GENERATOR

    # GENERAL
    @commands.command( aliases = ['waifugen','wgen'] )
    async def waifu(self, ctx):
        async with WaifuAioClient() as client:
            sfw_waifu: str = await client.sfw(category='waifu')
            await ctx.reply(sfw_waifu)

    # NEKO
    @commands.command()
    async def neko(self, ctx):
        async with WaifuAioClient() as client:
            sfw_neko: str = await client.sfw(category='neko')
            await ctx.reply(sfw_neko)
    
    # HIGHFIVE
    @commands.command(aliases = ['hifive','high-five','hf'] )
    async def highfive(self, ctx):
        async with WaifuAioClient() as client:
            sfw_highfive: str = await client.sfw(category = 'highfive')
            await ctx.reply(sfw_highfive)
    
    # HAPPY
    @commands.command()
    async def happy(self, ctx):
        async with WaifuAioClient() as client:
            sfw_happy: str = await client.sfw(category = 'happy')
            await ctx.reply(sfw_happy)
    
    # SMILE
    @commands.command(aliases = ['🙂'])
    async def happy(self, ctx):
        async with WaifuAioClient() as client:
            sfw_smile: str = await client.sfw(category = 'smile')
            await ctx.reply(sfw_smile)

    # DANCE
    @commands.command()
    async def dance(self, ctx):
        async with WaifuAioClient() as client:
            sfw_dance: str = await client.sfw(category = 'smile')
            await ctx.reply(sfw_dance)

    # CRY
    @commands.command()
    async def cry(self, ctx):
        async with WaifuAioClient() as client:
            sfw_cry: str = await client.sfw(category = 'cry')
            await ctx.reply(sfw_cry)

    # KILL
    @commands.command(aliases = ['murder', 'slaughter'] )
    async def kill(self, ctx, member : discord.Member):
        await ctx.reply(f'**You just killed** {member.mention}!')

        async with WaifuAioClient() as client:
            sfw_kill: str = await client.sfw(category = 'kill')
            await ctx.reply(sfw_kill)
    
    # HUG
    @commands.command()
    async def hug(self, ctx, member : discord.Member):
        await ctx.reply(f'**You just hugged** {member.mention}!')

        async with WaifuAioClient() as client:
            sfw_hug: str = await client.sfw(category = 'hug')
            await ctx.send(sfw_hug)
    
    # WAVE
    @commands.command()
    async def wave(self, ctx, member : discord.Member ):
        await ctx.reply(f'**You just waved at** {member.mention}!')

        async with WaifuAioClient() as client:
            sfw_wave: str = await client.sfw(category = 'wave')
            await ctx.send(sfw_wave)


def setup(client):
    client.add_cog(Waifu(client))