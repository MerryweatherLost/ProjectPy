import discord
import random
from discord.ext import commands

class Anime(commands.cog):
    def __init__(self, client):
        self.client = client

    # DDLC - SFW
    @commands.command(help = 'Images of the Doki Doki Literature Club characters.')
    async def ddlc(self, ctx):
        dokidoki = [
            'https://cdn.discordapp.com/attachments/576096750331494420/895016615651979264/image5.jpg',
            
        ]
        DDLC = random.choice(dokidoki)
        embed = discord.Embed (
            title = 'DDLC',
            description = 'Here is the image!',
            color = discord.Color.gold()
            )
        embed.set_author (
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
        )
        embed.set_image (
            url = DDLC
        )
        
def setup(client):
    client.add_cog(Anime(client))