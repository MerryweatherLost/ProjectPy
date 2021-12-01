import discord
import python_weather

from discord.ext import commands
from discord.ext.commands.core import is_owner

from library.ConsoleSelect import Time
from library.ConsoleSelect import Color
from library.ConsoleSelect import Roundtrip

from library.ConsoleSelect import *

from library.PillowSelect import Avatar

from PIL import Image
import requests

from settings.config import version

# GENERAL COMMANDS

class General(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # PING METHOD
    @commands.command(help = 'Pings the round client latency.', aliases = ['🏓'])
    async def ping(self, ctx):
        embed = discord.Embed (
            description = f'**Pong! {Roundtrip.rt(self)}ms.**', 
            color = Color.tachi
        )
        embed.set_footer (
            text = f'{self.client.user.name}'
        )
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)

    # GITHUB
    @commands.command(help = 'Sends the github of the creator.', aliases = ['git'])
    async def github(self, ctx):
        await ctx.reply(f'Here is the GitHub of my creator: https://github.com/MerryweatherLost')

    # TOP DOG METHOD
    @commands.command(help = 'Returns highest role.', aliases = ['tr'])
    async def toprole(self, ctx, member: commands.MemberConverter = None):
        if (member == None):
            await ctx.reply(f'**Highest Role:** {ctx.author.top_role}')
        else:
            await ctx.reply(f'**Highest Role:** {member.top_role}')

    # VERSION
    @commands.command(help = 'Shows the current version of the bot.')
    async def version(self, ctx):
        embed = discord.Embed(description = f'The current version is: **{version}**', color = Color.tachi)
        await ctx.reply(embed = embed)

    # VOICE STATUS
    @commands.command(help = 'Checks for voice status.')
    @is_owner()
    async def voicestatus(self, ctx, member: commands.MemberConverter = None):
        if (member == None):
            VOICE = ctx.author.voice
            ADDRESS = 'Your'
        else:
            VOICE = member.voice
            ADDRESS = 'Their'

        embed = discord.Embed (description = f'**{ADDRESS} status in voice is:** {VOICE}')
        await ctx.reply(embed = embed)

    # ROLE COUNT
    @commands.command(help = 'Returns a number roles of a user or if not implimented, yours.')
    async def rolecount(self, ctx, member: commands.MemberConverter = None):
        member = member or ctx.author
        await ctx.reply(f'**Number of Roles:** {len(member.roles)} roles detected for the user.')

    # ROLES
    @commands.command(help = 'Returns a number roles of a user or if not implimented, yours.')
    async def roles(self, ctx, member: commands.MemberConverter = None):
        member = member or ctx.author
        rolelist = [r.mention for r in member.roles if r != ctx.guild.default_role]
        roles = " ".join(rolelist)
        embed = discord.Embed (
            title = f'Roles for {member.display_name}', 
            description = f'{roles}', color = member.color
        )
        embed.add_field(name = 'Role Count', value = f'{len(member.roles)} roles present for the user.', inline = True)
        embed.timestamp = ctx.message.created_at
        await ctx.reply(embed = embed)
    
    # WHOIS
    @commands.command(help = 'Gets information about a person.')
    async def whois(self, ctx, member: discord.Member = None):
        # DEFINE MEMBER OR CONTEXT.AUTHOR AS MEMBER
        member = member or ctx.author
        # SET ROLE LIST AS LIST.MENTION @Rolenamehere FOR LIST :IN: MEMBER.ROLES :IF: LIST != @EVERYONE
        rolelist = [list.mention for list in member.roles if list != ctx.guild.default_role]
        # SPACE OUT, JOIN ROLELIST
        roles = " ".join(rolelist)

        if member.display_name == '{self.client.user.name}': desc = "*Why are you looking me up...?*" 
        else: desc = ""
        
        image = Image.open(requests.get(member.avatar_url, stream = True).raw).convert('RGBA')
        Avatar.crop_to_circle(image)

        imageresize = image.resize((250, 250))
        
        imageresize.save('cache/whois.png', 'PNG')
        file = discord.File("cache/whois.png", filename="whois.png")

        em = discord.Embed (
            title = f"{member.display_name}'s Information",
            color = member.color,
            description = desc
        )
        em.set_thumbnail (
            url = ('attachment://whois.png')
        )
        em.add_field (
            name = "Guild Join Date",
            value = f'{member.joined_at.strftime("%H:%M UTC - %b %d, %Y")}',
        )
        em.add_field (
            name = "Creation Date",
            value = f'{member.created_at.strftime("%H:%M UTC - %b %d, %Y")}',
        )
        em.add_field (
            name = f"Roles List [{len(member.roles[1:])}]",
            value = f"{roles}",
            inline = False
        )
        em.set_footer (
            text = f'ID: {member.id}'
        )
        em.timestamp = ctx.message.created_at
        await ctx.reply(file = file, embed = em)

    # AVATAR GROUP
    @commands.group(help = 'Avatar group that holds different ways of displaying avatars.')
    async def avatar(self, ctx):
        if ctx.invoked_subcommand is None:
            em = discord.Embed (description = 'Unable to find that subcommand! Please use `help avatar` to view them!')
            await ctx.reply(embed = em)
            
    @avatar.command(help = 'square', aliases = ['sq'])
    async def square(self, ctx, member: discord.Member = None):        
        member = member or ctx.author
        embed = discord.Embed (
            title = f"{member.display_name}'s Profile Image",
            color = member.color
        )
        embed.set_author (
            name = member.display_name,
            icon_url = member.avatar_url
        )
        embed.set_image (
            url = member.avatar_url
        )
        await ctx.reply(embed = embed)   
         
    # CIRCLE AVATAR
    @avatar.command(help = 'Returns your avatar image in a circle.', aliases = ['avcircle','avc'])
    async def circle(self, ctx, member : discord.Member = None):
        member = member or ctx.author
        im = Image.open(requests.get(member.avatar_url, stream = True).raw).convert('RGBA')
        Avatar.crop_to_circle(im)
        imageresize = im.resize((250, 250))
        imageresize.save('cache/cropped.png')

        await ctx.reply(file = discord.File('cache/cropped.png'))

def setup(client):
    client.add_cog(General(client))