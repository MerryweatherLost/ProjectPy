import asyncio
import discord
from discord.ext import commands

from library.ConsoleSelect import *
from library.SauceSelect import *

from pysaucenao import *

class SauceNow(commands.Cog):
    def __init__(self, client):
        self.client = client

    # PIXNAO - METHOD
    @commands.command(help = 'Delivers the sauce by image. [Pixiv]')
    async def pixnao(self, ctx, image: str):
        # INITIAL API INITALIZATION
        sauce = SauceNao(api_key = 'ad5dd123e3b1b2ccdd38575f2736287b0aea1e26')
        results = await sauce.from_url(url = image)
        # INSTANCE CHECK
        if isinstance(results[0], PixivSource):
            message: discord.Message = await ctx.reply('I found a match... <a:checkmark:903852585360949289> gimmie me a second... <a:cleo:902025889179631637>')
            await asyncio.sleep(1)
            embed = discord.Embed (
                title = f'{results[0].title}',
                url = f'{results[0].url}'
            )
            embed.set_thumbnail (
                url = f'{results[0].thumbnail}'
            )
            embed.add_field (name = 'Type', value = f'{results[0].type.capitalize()}')
            embed.add_field (name = 'Similarity', value = f'{results[0].similarity}% {SauceSelect.similarEmoji(sim = results[0].similarity)}')
            embed.add_field (name = 'Author Name', value = f'{results[0].author_name}')
            embed.add_field (name = 'Author Link', value = f'[Link]({results[0].author_url})')
            embed.add_field (name = 'Result Count', value = f'{len(results)}')
            embed.add_field (name = 'Index ID', value = f'{results[0].index_id}')
            embed.timestamp = message.created_at
            await message.delete()
            await ctx.reply(embed = embed)
            print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: SAUCENAO.PY - LOG: SauceNao [Pixiv] was utilized in #{ctx.channel}! \n[Raw Data: {results[0].url}]')
            print(f'[Short Remainder: {results.short_remaining}] [Long Remainder: {results.long_remaining}]')
        else:
            embed = discord.Embed(description = 'I can not find this within the Pixiv Category, try another one or get a clearer image.')
            await ctx.reply(embed = embed)
    
    # BOORUNAO - METHOD
    @commands.command(help = 'Delivers the sauce by image. [Gelbooru/Danbooru]')
    async def boorunao(self, ctx, image: str):
        # INITIAL API INITALIZATION
        sauce = SauceNao(api_key = 'ad5dd123e3b1b2ccdd38575f2736287b0aea1e26')
        results = await sauce.from_url(url = image); len(results)
        # INSTANCE CHECK
        if isinstance(results[0], BooruSource):
            message: discord.Message = await ctx.reply('I found a match... <a:checkmark:903852585360949289> gimmie me a second... <a:cleo:902025889179631637>')
            await asyncio.sleep(1)
            embed = discord.Embed (
                title = f'{results[0].title}',
                url = f'{results[0].url}'
            )
            embed.set_thumbnail (
                url = f'{results[0].thumbnail}'
            )
            embed.add_field (name = 'Type', value = f'{results[0].type.capitalize()}')
            embed.add_field (name = 'Similarity', value = f'{results[0].similarity}% {SauceSelect.similarEmoji(sim = results[0].similarity)}')
            embed.add_field (name = 'Author Name', value = f'{results[0].author_name}')
            embed.add_field (name = 'Author Link', value = f'[Link]({results[0].author_url})')
            embed.add_field (name = 'Index ID', value = f'{results[0].index_id}')
            embed.timestamp = message.created_at
            embed.set_footer (
                text = f'Source URL: {results[0].source_url} Index: {results[0].index}'
            )
            await message.delete()
            await ctx.reply(embed = embed)
            print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: SAUCENAO.PY - LOG: SauceNao [Gelbooru/Danbooru] was utilized in #{ctx.channel}!')
            print(f'[Raw Data: {results[0].url}] [Short Remainder: {results.short_remaining}] [Long Remainder: {results.long_remaining}]')
        else:
            embed = discord.Embed(description = 'I can not find this within the Booru Category, try another one or get a clearer image.')
            await ctx.reply(embed = embed)

    # # ANIMENAO - METHOD
    # @commands.command(help = 'Delivers the sauce by image. [Anime, Eroge, Etc...]')
    # async def animenao(self, ctx, image: str):
    #     # INITIAL API INITALIZATION
    #     sauce = SauceNao(api_key = 'ad5dd123e3b1b2ccdd38575f2736287b0aea1e26')
    #     results = await sauce.from_url(url = image); len(results)
    #     # INSTANCE CHECK
    #     if isinstance(results[4], AnimeSource):
    #         message: discord.Message = await ctx.reply('I found a match... <a:checkmark:903852585360949289> gimmie me a second... <a:cleo:902025889179631637>')
    #         await asyncio.sleep(1)
    #         embed = discord.Embed (
    #             title = f'{results[4].title}',
    #             url = f'{results[4].url}'
    #         )
    #         embed.set_thumbnail (
    #             url = f'{results[4].thumbnail}'
    #         )
    #         embed.add_field (name = 'Type', value = f'{results[4].type.capitalize()}')
    #         embed.add_field (name = 'Similarity', value = f'{results[4].similarity}% {SauceSelect.similarEmoji(sim = results[4].similarity)}')
    #         embed.add_field (name = 'Author Name', value = f'{results[4].author_name}')
    #         embed.add_field (name = 'Author Link', value = f'[Link]({results[4].author_url})')
    #         embed.add_field (name = 'Index ID', value = f'{results[4].index_id}')
    #         embed.timestamp = message.created_at
    #         embed.set_footer (
    #             text = f'Source URL: {results[4].source_url} Index: {results[4].index}'
    #         )
    #         await message.delete()
    #         await ctx.reply(embed = embed)
    #         print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: SAUCENAO.PY - LOG: SauceNao [Anime] was utilized in #{ctx.channel}! \n[Raw Data: {results[4].url}]')
    #         print(f'[Short Remainder: {results.short_remaining}] [Long Remainder: {results.long_remaining}]')
    #     else:
    #         embed = discord.Embed(description = 'I can not find this within the Anime Category, try another one or get a clearer image.')
    #         await ctx.reply(embed = embed)
    

def setup(client):
    client.add_cog(SauceNow(client))
