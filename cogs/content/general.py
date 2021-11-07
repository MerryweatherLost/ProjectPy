import discord
import python_weather

from discord.ext import commands
from discord.ext.commands.core import is_owner

from library.ConsoleSelect import Time
from library.ConsoleSelect import Color
from library.ConsoleSelect import Roundtrip

from library.ConsoleSelect import *
from library.WeatherSelect import Weather

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
            text = f"{self.client.user.name}: {Time.timeUTC()}"
        )
        await ctx.reply(embed = embed)

    # GITHUB
    @commands.command(help = 'Sends the github of the creator.', aliases = ['git'])
    async def github(self, ctx):
        await ctx.reply(f'Here is the GitHub of my creator: https://github.com/MerryweatherLost')

    # WEATHER
    @commands.command(help = 'Sends weather information of a city. (Quotes needed in the city parameter.)')
    async def weather(self, ctx, city, standard = None):
        client = python_weather.Client(format = Weather.standard(standard))
        STN = Weather.standard(standard)

        weather = await client.find(city)

        wembed = discord.Embed (
            title = (f'{str(weather.current.observation_point)}'),
            description = (f'**Temperature for Today:** {weather.current.temperature}{STN}'),
            color = Color.weather
        )
        wembed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/899394919012118548/wther.png'
        )
        # TOP FIELD
        wembed.add_field (name = 'Skies ⛅', value = weather.current.sky_text)
        wembed.add_field (name = 'Precipitation 🌦️', value = f'{weather.current.humidity}{"%"}')
        wembed.add_field (name = 'Wind Display 🚩', value = weather.current.wind_display)
        
        # BOTTOM FIELD
        wembed.add_field (name = 'Source', value = weather.provider)
        wembed.add_field (name = 'Feels Like', value = f'{weather.current.feels_like}{STN}')
        wembed.add_field (name = 'Observation Point', value = weather.current.observation_point)

        wembed.set_footer (text = f'Date 🗓️: {weather.current.date} - Alerts ⚠️: {weather.alert_message}')

        await ctx.reply(embed = wembed)
        await Console.log(Time.timeCST(), Roundtrip.rt(self), "GENERAL.PY", "Weather", ctx.channel, f'[Location[↗]: {weather.current.observation_point}] [Temperature: {weather.current.temperature}°{STN}] [Windspeed: {weather.current.wind_display}]')
        await client.close()

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
        embed.set_footer(text = f'Timestamp: {Time.timeUTC()}')
        await ctx.reply(embed = embed)
    
    # WHOIS
    @commands.command(help = 'Gets information about a person.')
    async def whois(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        rolelist = [list.mention for list in member.roles if list != ctx.guild.default_role]
        roles = " ".join(rolelist)
        if member.display_name == '{self.client.user.name}': desc = "*Why are you looking me up...?*" 
        else: desc = ""
        em = discord.Embed (
            title = f"{member.display_name}'s Information",
            color = member.color,
            description = desc
        )
        em.set_thumbnail (
            url = member.avatar_url
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
            text = f'ID: {member.id} - Timestamp: {Time.timeUTC()}',
        )
        await ctx.reply(embed = em)


def setup(client):
    client.add_cog(General(client))