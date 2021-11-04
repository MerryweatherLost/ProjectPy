import discord

from discord.ext import commands
from library.ConsoleSelect import Time
from library.ConsoleSelect import Roundtrip

from PIL import Image, ImageChops, ImageDraw
import requests

class Architect(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help = "The Architects' Ban Hammer.")
    @commands.has_any_role('The Architect')
    async def architectban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.reply(f'Banned {member.mention}!')
        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE: ARCHITECT.PY - LOG: ABan was utilized in #{ctx.channel}! [Member: {member}]')
    
    @commands.command()
    @commands.has_any_role('The Architect')
    async def avarch(self, ctx, member : discord.Member = None):
        member = member or ctx.author

        def crop_to_circle(im):
            bigsize = (im.size[0] * 3, im.size[1] * 3)
            mask = Image.new('L', bigsize, 0)
            ImageDraw.Draw(mask).ellipse((0, 0) + bigsize, fill=255)
            mask = mask.resize(im.size, Image.ANTIALIAS)
            mask = ImageChops.darker(mask, im.split()[-1])
            im.putalpha(mask)

        im = Image.open(requests.get(member.avatar_url, stream = True).raw).convert('RGBA')
        crop_to_circle(im)
        im.save('cache/cropped.png')
        
        await ctx.reply(file = discord.File('cache/cropped.png'))

def setup(client):
    client.add_cog(Architect(client))