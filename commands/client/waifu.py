import discord

from waifu import WaifuAioClient
from discord.ext import commands

from library.ConsoleSelect import Time
from library.ConsoleSelect import Roundtrip

from private.config import signature

class Waifu(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    # WAIFU GROUP
    @commands.group (
        help = 'Waifu group that contains all single waifu commands. If called without context, then returns general waifu.',
        pass_context = True
    )
    async def waifu(self, ctx):
        if ctx.invoked_subcommand is None:
            async with WaifuAioClient() as client:
                WAIFU: str = await client.sfw(category='waifu')
                embed = discord.Embed (
                    title = "Waifu Image", 
                    description = "Here is the image!", 
                    color = signature
                )
                embed.set_author (
                    name = ctx.author.display_name, 
                    icon_url = ctx.author.avatar_url
                )
                embed.set_image (
                    url = WAIFU, 
                )
                embed.set_footer (
                    text = f'{self.client.user.name}'
                )
                message = ctx.message
                embed.timestamp = message.created_at
                await ctx.reply(embed = embed)
        
                print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Waifu was utilized in #{ctx.channel}! \n[Raw Data: {WAIFU}]')

    # NSFW
    @waifu.command( help = 'General Waifu image.', aliases = ['waifunsfw'] )
    @commands.is_nsfw()
    async def nsfw(self, ctx):
        async with WaifuAioClient() as client:
            NSFW_WAIFU: str = await client.nsfw(category='waifu')
            embed = discord.Embed (
                title = "Waifu Image", 
                description = "Here is the image!", 
                color = signature
            )
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url)
            embed.set_image (
                url = NSFW_WAIFU, 
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Waifu (NSFW) was utilized in #{ctx.channel}! \n[Raw Data: {NSFW_WAIFU}]')

    # NEKO
    @waifu.command(help = 'Neko Waifu image.', aliases = ['nekomimi'])
    async def neko(self, ctx):
        async with WaifuAioClient() as client:
            NEKO: str = await client.sfw(category='neko')
            AUTHOR_NAME = ctx.author.display_name
            AUTHOR_IMAGE = ctx.author.avatar_url

            embed = discord.Embed (
                title = "Neko Image", 
                description = "Here is the image!", 
                color = signature
            )
            embed.set_author (
                name = AUTHOR_NAME, 
                icon_url = AUTHOR_IMAGE
            )
            embed.set_image (
                url = NEKO, 
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Nekomimi was utilized in #{ctx.channel}! \n[Raw Data: {NEKO}]')

    # NEKO - NSFW
    @waifu.command(help = 'Neko Waifu image.', aliases = ['nsfwneko', 'nekomiminsfw'])
    @commands.is_nsfw()
    async def nekonsfw(self, ctx):
        async with WaifuAioClient() as client:
            NSFW_NEKO: str = await client.nsfw(category = 'neko')
            AUTHOR_NAME = ctx.author.display_name
            AUTHOR_IMAGE = ctx.author.avatar_url

            embed = discord.Embed (
                title = "Neko Image", 
                description = "Here is the image!", 
                color = signature
            )
            embed.set_author (
                name =  AUTHOR_NAME,
                icon_url = AUTHOR_IMAGE
            )
            embed.set_image (
                url = NSFW_NEKO, 
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Nekomimi (NSFW) was utilized in #{ctx.channel}! \n[Raw Data: {NSFW_NEKO}]')
    
    # HAPPY
    @waifu.command(help = 'Happy image of a waifu.')
    async def happy(self, ctx):
        async with WaifuAioClient() as client:
            HAPPY: str = await client.sfw(category = 'happy')
            AUTHOR_NAME = ctx.author.display_name
            AUTHOR_IMAGE = ctx.author.avatar_url

            embed = discord.Embed (
                title = "Happy Image", 
                description = "Here is the image!", 
                color = signature
            )
            embed.set_author (
                name =  AUTHOR_NAME,
                icon_url = AUTHOR_IMAGE
            )
            embed.set_image (
                url = HAPPY, 
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)
        
            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Happy was utilized in #{ctx.channel}! \n[Raw Data: {HAPPY}]')
    
    # SMILE
    @waifu.command(help = 'Smiling image of a waifu.', aliases = ['🙂'])
    async def smile(self, ctx):
        async with WaifuAioClient() as client:
            SMILE: str = await client.sfw(category = 'smile')
            AUTHOR_NAME = ctx.author.display_name
            AUTHOR_IMAGE = ctx.author.avatar_url

            embed = discord.Embed (
                title = "Smile Image", 
                description = "Here is the image!", 
                color = signature
            )
            embed.set_author (
                name =  AUTHOR_NAME,
                icon_url = AUTHOR_IMAGE
            )
            embed.set_image (
                url = SMILE, 
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Smile was utilized in #{ctx.channel}! \n[Raw Data: {SMILE}]')

    # SMUG
    @waifu.command(help = 'Smug image of a waifu. - My personal favorite.')
    async def smug(self, ctx):
        async with WaifuAioClient() as client:
            SMUG: str = await client.sfw(category = 'smug')
            AUTHOR_NAME = ctx.author.display_name
            AUTHOR_IMAGE = ctx.author.avatar_url

            embed = discord.Embed (
                title = "Smug Image", 
                description = "Here is the image!", 
                color = signature
            )
            embed.set_author (
                name = AUTHOR_NAME,
                icon_url = AUTHOR_IMAGE
            )
            embed.set_image (
                url = SMUG, 
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Smug was utilized in #{ctx.channel}! \n[Raw Data: {SMUG}]')

    # DANCE
    @waifu.command(help = 'Dance image of a waifu.')
    async def dance(self, ctx):
        async with WaifuAioClient() as client:
            DANCE: str = await client.sfw(category = 'smile')
            AUTHOR_NAME = ctx.author.display_name
            AUTHOR_IMAGE = ctx.author.avatar_url

            embed = discord.Embed (
                title = "Dancing Image", 
                description = "Here is the image!", 
                color = signature
            )
            embed.set_author (
                name = AUTHOR_NAME,
                icon_url = AUTHOR_IMAGE
            )
            embed.set_image (
                url = DANCE, 
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Dance was utilized in #{ctx.channel}! \n[Raw Data: {DANCE}]')

    # CRY
    @waifu.command(help = 'Crying image of a waifu.')
    async def cry(self, ctx):
        async with WaifuAioClient() as client:
            CRY: str = await client.sfw(category = 'cry')
            AUTHOR_NAME = ctx.author.display_name
            AUTHOR_IMAGE = ctx.author.avatar_url

            embed = discord.Embed (
                title = "Crying Image", 
                description = "Here is the image!", 
                color = signature
            )
            embed.set_author (
                name = AUTHOR_NAME, 
                icon_url = AUTHOR_IMAGE
            )
            embed.set_image (
                url = CRY, 
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Cry was utilized in #{ctx.channel}! \n[Raw Data: {CRY}]')

    # MODULAR COMMAND LIST - ACCEPTS MEMBER

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
                color = ctx.author.color
            )
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url
            )
            embed.set_image (
                url = HIGHFIVE
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)   

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Highfive was utilized in #{ctx.channel}! \n[Author: {AUTHOR}] [Mentioned: {DISPLAY}] [Raw Data: {HIGHFIVE}]')

    # KILL
    @commands.command(help = 'Kill a member in chat. EX: :kill @member.', aliases = ['murder', 'slaughter'] )
    async def kill(self, ctx, member : discord.Member):
        async with WaifuAioClient() as client:
            KILL: str = await client.sfw(category = 'kill')
            MENTION = member.mention
            DISPLAY = member.display_name
            AUTHOR = ctx.author.display_name
            
            embed = discord.Embed (
                title = 'Kill',
                description = f'{MENTION} was killed by {AUTHOR}!',
                color = ctx.author.color
            )
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url
            )
            embed.set_image (
                url = KILL
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)   

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Kill was utilized in #{ctx.channel}! \n[Author: {AUTHOR}] [Mentioned: {DISPLAY}] [Raw Data: {KILL}]')
    
    # HUG
    @commands.command(help = 'Hug a member in chat. EX: :hug @member.',)
    async def hug(self, ctx, member : discord.Member):
        async with WaifuAioClient() as client:
            HUG: str = await client.sfw(category = 'hug')
            MENTION = member.mention
            DISPLAY = member.display_name
            AUTHOR = ctx.author.display_name

            embed = discord.Embed (
                title = 'Hug',
                description = f'{MENTION} was hugged by {AUTHOR}!',
                color = ctx.author.color
            )
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url
            )
            embed.set_image (
                url = HUG
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)   

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Hug was utilized in #{ctx.channel}! \n[Author: {AUTHOR}] [Mentioned: {DISPLAY}] [Raw Data: {HUG}]')

    
    # WAVE
    @commands.command(help = 'Wave at a member in chat. EX: :wave @member.')
    async def wave(self, ctx, member : discord.Member ):
        async with WaifuAioClient() as client:
            WAVE: str = await client.sfw(category = 'wave')
            MENTION = member.mention
            DISPLAY = member.display_name
            AUTHOR = ctx.author.display_name

            embed = discord.Embed (
                title = 'Wave',
                description = f'{AUTHOR} just waved at {MENTION}!',
                color = ctx.author.color
            )
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url
            )
            embed.set_image (
                url = WAVE
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)   

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Wave was utilized in #{ctx.channel}! \n[Author: {AUTHOR}] [Mentioned: {DISPLAY}] [Raw Data: {WAVE}]')
    
    # BONK
    @commands.command(help = 'Bonk a member in chat. EX: :bonk @member.')
    async def bonk(self, ctx, member : discord.Member ):
        async with WaifuAioClient() as client:
            BONK: str = await client.sfw(category = 'bonk')
            MENTION = member.mention
            DISPLAY = member.display_name
            AUTHOR = ctx.author.display_name

            embed = discord.Embed (
                title = 'Bonk',
                description = f'{MENTION} just got bonked by {AUTHOR}!',
                color = ctx.author.color
            )
            embed.set_author (
                name = ctx.author.display_name, 
                icon_url = ctx.author.avatar_url
            )
            embed.set_image (
                url = BONK
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)   

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Bonk was utilized in #{ctx.channel}! \n[Author: {AUTHOR}] [Mentioned: {DISPLAY}] [Raw Data: {BONK}]')

    # SLAP
    @commands.command(help = 'Slap a member. No questions asked.')
    async def slap(self, ctx, member: discord.Member):
        async with WaifuAioClient() as client:
            SLAP: str = await client.sfw(category = 'slap')
            MENTION = member.mention
            DISPLAY = member.display_name
            AUTHOR = ctx.author.display_name

            embed = discord.Embed (
                title = 'Slap',
                description = f'{AUTHOR} has just slapped {MENTION} right across the face!',
                color = ctx.author.color
            )            
            embed.set_author (
                name = ctx.author.display_name,
                icon_url = ctx.author.avatar_url
            )
            embed.set_image (
                url = SLAP
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)   

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Slap was utilized in #{ctx.channel}! \n[Author: {AUTHOR}] [Mentioned: {DISPLAY}] [Raw Data: {SLAP}]')
    
    # WINK
    @commands.command(help = 'Slap a member. No questions asked.')
    async def wink(self, ctx, member: discord.Member):
        async with WaifuAioClient() as client:
            WINK: str = await client.sfw(category = 'wink')
            MENTION = member.mention
            DISPLAY = member.display_name
            AUTHOR = ctx.author.display_name

            embed = discord.Embed (
                title = 'Wink',
                description = f'{AUTHOR} just winked right at {MENTION}!',
                color = ctx.author.color
            )            
            embed.set_author (
                name = ctx.author.display_name,
                icon_url = ctx.author.avatar_url
            )
            embed.set_image (
                url = WINK
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.reply(embed = embed)   

            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: WAIFU.PY - LOG: Wink was utilized in #{ctx.channel}! \n[Author: {AUTHOR}] [Mentioned: {DISPLAY}] [Raw Data: {WINK}]')

def setup(client):
    client.add_cog(Waifu(client))