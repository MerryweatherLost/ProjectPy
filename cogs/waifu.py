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
            await ctx.reply(sfw_waifu)

    # NEKO
    @commands.command(help = 'Neko Waifu image.')
    async def waifuneko(self, ctx):
        async with WaifuAioClient() as client:
            sfw_neko: str = await client.sfw(category='neko')
            await ctx.reply(sfw_neko)
    
    # HIGHFIVE
    @commands.command(help = 'Give a high five to someone. EX: :highfive @member.', aliases = ['hifive','high-five','hf'] )
    async def highfive(self, ctx, member : discord.Member):
        async with WaifuAioClient() as client:
            sfw_highfive: str = await client.sfw(category = 'highfive')
            await ctx.reply(f'Heya {member.mention}, here is a high five!\n{sfw_highfive}')
    
    # HAPPY
    @commands.command(help = 'Happy image of a waifu.')
    async def waifuhappy(self, ctx):
        async with WaifuAioClient() as client:
            sfw_happy: str = await client.sfw(category = 'happy')
            await ctx.reply(sfw_happy)
    
    # SMILE
    @commands.command(help = 'Smiling image of a waifu.', aliases = ['waifu🙂'])
    async def waifusmile(self, ctx):
        async with WaifuAioClient() as client:
            sfw_smile: str = await client.sfw(category = 'smile')
            await ctx.reply(sfw_smile)

    # SMUG
    @commands.command(help = 'Smug image of a waifu. - My personal favorite.')
    async def waifusmug(self, ctx):
        async with WaifuAioClient() as client:
            sfw_smug: str = await client.sfw(category = 'smug')
            await ctx.reply(sfw_smug)

    # DANCE
    @commands.command(help = 'Dance image of a waifu.')
    async def waifudance(self, ctx):
        async with WaifuAioClient() as client:
            sfw_dance: str = await client.sfw(category = 'smile')
            await ctx.reply(sfw_dance)

    # CRY
    @commands.command(help = 'Crying image of a waifu.')
    async def waifucry(self, ctx):
        async with WaifuAioClient() as client:
            sfw_cry: str = await client.sfw(category = 'cry')
            await ctx.reply(sfw_cry)

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
            await ctx.reply(f'**You just bonked** {member.mention}!\n{sfw_bonk}')
        
    # DEPRESSION
    @commands.command(help = 'Simulate crippiling depression.')
    async def depression(self, ctx):
        await ctx.reply(hmtai.useHM("2_9","depression"))


def setup(client):
    client.add_cog(Waifu(client))