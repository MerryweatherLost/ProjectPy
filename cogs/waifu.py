import discord
from discord.ext.commands.core import is_nsfw
import hmtai

from waifu import WaifuAioClient
from discord.ext import commands

from ConsoleLib import Time

class Waifu(commands.Cog):
    def __init__(self, client):
        self.client = client

    ## WAIFU GENERATOR

    # GENERAL
    @commands.command( help = 'General Waifu image.', aliases = ['waifugen','wgen'] )
    async def waifu(self, ctx):
        async with WaifuAioClient() as client:
            WAIFU: str = await client.sfw(category='waifu')
            embed = discord.Embed (
                title = "Waifu Image", 
                description = "Here is the image!", 
                color = discord.Color.dark_teal())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = WAIFU, 
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
            )
            await ctx.reply(embed = embed)
    
            print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: WAIFU.PY - LOG: Waifu was utilized! \n[Raw Data: {WAIFU}]')

    
    # NSFW
    @commands.command( help = 'General Waifu image.', aliases = ['waifunsfw'] )
    @commands.is_nsfw()
    async def nsfwwaifu(self, ctx):
        async with WaifuAioClient() as client:
            NSFW_WAIFU: str = await client.nsfw(category='waifu')
            embed = discord.Embed (
                title = "Waifu Image", 
                description = "Here is the image!", 
                color = discord.Color.dark_teal())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = NSFW_WAIFU, 
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
            )
            await ctx.reply(embed = embed)

            print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: WAIFU.PY - LOG: Waifu (NSFW) was utilized! \n[Raw Data: {NSFW_WAIFU}]')


    # NEKO
    @commands.command(help = 'Neko Waifu image.', aliases = ['nekomimi'])
    async def neko(self, ctx):
        async with WaifuAioClient() as client:
            NEKO: str = await client.sfw(category='neko')
            embed = discord.Embed (
                title = "Neko Image", 
                description = "Here is the image!", 
                color = discord.Color.dark_teal())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = NEKO, 
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
            )
            await ctx.reply(embed = embed)

            print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: WAIFU.PY - LOG: Nekomimi was utilized! \n[Raw Data: {NEKO}]')

    # NEKO - NSFW
    @commands.command(help = 'Neko Waifu image.', aliases = ['nsfwneko', 'nekomiminsfw'])
    @commands.is_nsfw()
    async def nekonsfw(self, ctx):
        async with WaifuAioClient() as client:
            NSFW_NEKO: str = await client.nsfw(category = 'neko')
            embed = discord.Embed (
                title = "Neko Image", 
                description = "Here is the image!", 
                color = discord.Color.dark_teal())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url
            )
            embed.set_image (
                url = NSFW_NEKO, 
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
            )
            await ctx.reply(embed = embed)

            print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: WAIFU.PY - LOG: Nekomimi (NSFW) was utilized! \n[Raw Data: {NSFW_NEKO}]')
    
    # HAPPY
    @commands.command(help = 'Happy image of a waifu.')
    async def happy(self, ctx):
        async with WaifuAioClient() as client:
            sfw_happy: str = await client.sfw(category = 'happy')
            embed = discord.Embed (
                title = "Happy Image", 
                description = "Here is the image!", 
                color = discord.Color.dark_teal())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = sfw_happy, 
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
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
                color = discord.Color.dark_teal())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = sfw_smile, 
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
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
                color = discord.Color.dark_teal())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = sfw_smug, 
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
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
                color = discord.Color.dark_teal())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = sfw_dance, 
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
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
                color = discord.Color.dark_teal())
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = sfw_cry, 
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
            )
            await ctx.reply(embed=embed)

    # HIGHFIVE
    @commands.command(help = 'Give a high five to someone. EX: :highfive @member.', aliases = ['hifive','high-five','hf'] )
    async def highfive(self, ctx, member : discord.Member):
        async with WaifuAioClient() as client:
            HIGHFIVE: str = await client.sfw(category = 'highfive')
            MENTION = member.mention
            DISPLAY = member.display_name
            AUTHOR = ctx.author.display_name
            
            embed = discord.Embed (
                title = 'Highfive',
                description = f'Heya {MENTION}, here is a high five!',
                color = discord.Color.red()
            )
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url
            )
            embed.set_image (
                url = HIGHFIVE
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
            )

            await ctx.reply(embed = embed)   

            print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE: WAIFU.PY - LOG: Highfive was utilized! \n[Author: {AUTHOR}] [Mentioned: {DISPLAY}] [Raw Data: {HIGHFIVE}]')

    # KILL
    @commands.command(help = 'Kill a member in chat. EX: :kill @member.', aliases = ['murder', 'slaughter'] )
    async def kill(self, ctx, member : discord.Member):
        async with WaifuAioClient() as client:
            KILL: str = await client.sfw(category = 'kill')
            MENTION = member.mention
            DISPLAY = member.display_name
            AUTHOR = ctx.author.display_name
            ROUNDTRIP = round(self.client.latency * 1000)
            
            embed = discord.Embed (
                title = 'Kill',
                description = f'{MENTION} was killed by {AUTHOR}!',
                color = discord.Color.red()
            )
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url
            )
            embed.set_image (
                url = KILL
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
            )

            await ctx.reply(embed = embed)   

            print(f'[{Time.timeFormat()}] [Roundtrip: {ROUNDTRIP}ms.] CONSOLE: WAIFU.PY - LOG: Kill was utilized! \n[Author: {AUTHOR}] [Mentioned: {DISPLAY}] [Raw Data: {KILL}]')
    
    # HUG
    @commands.command(help = 'Hug a member in chat. EX: :hug @member.',)
    async def hug(self, ctx, member : discord.Member):
        async with WaifuAioClient() as client:
            HUG: str = await client.sfw(category = 'hug')
            MENTION = member.mention
            DISPLAY = member.display_name
            AUTHOR = ctx.author.display_name
            ROUNDTRIP = round(self.client.latency * 1000)

            embed = discord.Embed (
                title = 'Hug',
                description = f'{MENTION} was hugged by {AUTHOR}!',
                color = discord.Colour.red()
            )
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url
            )
            embed.set_image (
                url = HUG
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
            )

            await ctx.reply(embed = embed)   

            print(f'[{Time.timeFormat()}] [Roundtrip: {ROUNDTRIP}ms.] CONSOLE: WAIFU.PY - LOG: Hug was utilized! \n[Author: {AUTHOR}] [Mentioned: {DISPLAY}] [Raw Data: {HUG}]')

    
    # WAVE
    @commands.command(help = 'Wave at a member in chat. EX: :wave @member.')
    async def wave(self, ctx, member : discord.Member ):
        async with WaifuAioClient() as client:
            WAVE: str = await client.sfw(category = 'wave')
            MENTION = member.mention
            DISPLAY = member.display_name
            AUTHOR = ctx.author.display_name
            ROUNDTRIP = round(self.client.latency * 1000)

            embed = discord.Embed (
                title = 'Wave',
                description = f'{AUTHOR} just waived at {MENTION}!',
                color = discord.Colour.red()
            )
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url
            )
            embed.set_image (
                url = WAVE
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
            )

            await ctx.reply(embed = embed)   

            print(f'[{Time.timeFormat()}] [Roundtrip: {ROUNDTRIP}ms.] CONSOLE: WAIFU.PY - LOG: Wave was utilized! \n[Author: {AUTHOR}] [Mentioned: {DISPLAY}] [Raw Data: {WAVE}]')
    
    # BONK
    @commands.command(help = 'Bonk a member in chat. EX: :bonk @member.')
    async def bonk(self, ctx, member : discord.Member ):
        async with WaifuAioClient() as client:
            BONK: str = await client.sfw(category = 'bonk')
            MENTION = member.mention
            DISPLAY = member.display_name
            AUTHOR = ctx.author.display_name
            ROUNDTRIP = round(self.client.latency * 1000)

            embed = discord.Embed (
                title = 'Bonk',
                description = f'{MENTION} just got bonked by {AUTHOR}!',
                color = discord.Colour.red()
            )
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url
            )
            embed.set_image (
                url = BONK
            )
            embed.set_footer (
                text = f'Project PY: {Time.timeFormatUniversial()}'
            )

            await ctx.reply(embed = embed)   
            
            print(f'[{Time.timeFormat()}] [Roundtrip: {ROUNDTRIP}ms.] CONSOLE: WAIFU.PY - LOG: Bonk was utilized! \n[Author: {AUTHOR}] [Mentioned: {DISPLAY}] [Raw Data: {BONK}]')
        
    # DEPRESSION
    @commands.command(help = 'Simulate crippiling depression.')
    async def depression(self, ctx):
        embed=discord.Embed(
            title = "Depression Image", 
            description = "Here is the image!", 
            color = discord.Color.dark_teal())
        embed.set_author(
            name = ctx.author.display_name, 
            icon_url = ctx.author.avatar_url)
        embed.set_image(
            url = hmtai.useHM("2_9","depression"), 
        )
        embed.set_footer (
            text = f'Project PY: {Time.timeFormatUniversial()}'
        )
        await ctx.reply(embed = embed)


def setup(client):
    client.add_cog(Waifu(client))