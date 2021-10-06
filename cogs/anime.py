import discord
import random

from discord.ext import commands
    
class Anime(commands.Cog):
    def __init__(self, client):
        self.client = client

    # COFFEE - SFW
    @commands.command(help = 'Emotional Relief.')
    async def coffee(self, ctx):
        embed = discord.Embed (
            title = 'Coffee',
            description = 'Have some coffee! ☕',
            color = discord.Color.green()
            )
        embed.set_author (
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
            )
        embed.set_image (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/895067885549019157/6dubb6nhxjr71_waifu2x_2x_png.png'
            )
        await ctx.reply(embed = embed)

    # DDLC - SFW
    @commands.command(help = 'Images of the Doki Doki Literature Club characters.')
    async def ddlc(self, ctx):
        dokidoki = [
            'https://media.discordapp.net/attachments/335232645044633601/895051979225702440/sample_a95c5fe38157038a7a94dbb119c6bc6bbcf23d68.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895053705907408907/b6820ae5fd84f484491e7308ccf4b400.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895053860463317033/doki_doki_literature_club___festival_time___gift__by_katzianxero_dbxqttd-fullview.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895053926850760764/R.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895053980273631262/doki_doki_literature_club__light_ver___by_apricot_crown-dbyfydi.png'
            'https://cdn.discordapp.com/attachments/862584354211364894/895054111383359519/R.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895054158640599060/R.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895054243956940830/R.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895054625579859978/monika_natsuki_sayori_and_yuri_doki_doki_literature_club_drawn_by_hushabye__8b0a188cd0ee2fa8938b926f.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895054962642526279/ddlc1_by_yorieofthecastle-dbulcc1.png']
        DDLC = random.choice(dokidoki)
        embed = discord.Embed (
            title = 'DDLC',
            description = 'Here is the image!',
            color = discord.Color.red()
            )
        embed.set_author (
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
        )
        embed.set_image (
            url = DDLC
        )
        await ctx.reply(embed = embed)

def setup(client):
    client.add_cog(Anime(client))