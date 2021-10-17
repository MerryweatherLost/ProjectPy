import discord

import python_weather

from discord.ext import commands
from library.ConsoleLib import Time
from library.ConsoleLib import Color
from library.ConsoleLib import Roundtrip

# GENERAL COMMANDS

class General(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # PING METHOD
    @commands.command(help = 'Pings the round client latency.', aliases = ['🏓'])
    async def ping(self, ctx):
        embed = discord.Embed (
            description = f'⚪ **Pong! {Roundtrip.rt(self)}ms.**',
            color = Color.white
        )
        embed.set_footer (
            text = f"Tachibana: {Time.timeUTC()}"
        )
        await ctx.reply(embed = embed)

    # GITHUB
    @commands.command(help = 'Sends the github of the creator.', aliases = ['git'])
    async def github(self, ctx):
        await ctx.reply(f'Here is the GitHub of my creator: https://github.com/MerryweatherLost')

    # WEATHER
    @commands.command(help = 'Sends weather information of a city. (Quotes needed in the city parameter.)')
    async def weather(self, ctx, city, standard = None):
        if (standard != None):
            str.lower(standard)
        else:
            standard = 'imperial'
            
        if (standard == 'metric'): STANDARD = python_weather.METRIC
        elif (standard == 'imperial'): STANDARD = python_weather.IMPERIAL
        elif (standard == None): STANDARD = python_weather.IMPERIAL
        else: STANDARD = python_weather.IMPERIAL

        client = python_weather.Client(format = STANDARD)
        weather = await client.find(city)

        wembed = discord.Embed (
            title = (f'{str(weather.location_name)}'),
            description = (f'**Temperature for Today:** {weather.current.temperature}{STANDARD}'),
            color = Color.weather
        )
        wembed.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/899394919012118548/wther.png'
        )
        # TOP FIELD
        wembed.add_field (name = 'Skies ☁️', value = weather.current.sky_text)
        wembed.add_field (name = 'Precipitation 🌧️', value = f'{weather.current.humidity}{"%"}')
        wembed.add_field (name = 'Wind Display 🚩', value = weather.current.wind_display)
        # BOTTOM FIELD
        wembed.add_field (name = 'Source', value = weather.provider)
        wembed.add_field (name = 'Feels Like', value = f'{weather.current.feels_like}{STANDARD}')
        wembed.add_field (name = 'Observation Point', value = weather.current.observation_point)

        wembed.set_footer (text = f'Date: {weather.current.date} Alerts: {weather.alert_message}')

        await ctx.reply(embed = wembed)
        await client.close()

    # TOP DOG METHOD
    @commands.command(help = 'Returns highest role.', aliases = ['tr'])
    async def toprole(self, ctx, member: commands.MemberConverter = None):
        if (member == None):
            await ctx.reply(f'**Highest Role:** {ctx.author.top_role}')
        else:
            await ctx.reply(f'**Highest Role:** {member.top_role}')

    # ROLES
    @commands.command(help = 'Returns a number roles of a user or if not implimented, yours.')
    async def roles(self, ctx, member: commands.MemberConverter = None):
        if (member == None):
            await ctx.reply(f'**Number of Roles:** {len(ctx.author.roles)} roles detected for the user.')
        else:
            await ctx.reply(f'**Number of Roles:** {len(member.roles)} roles detected for the user.')

def setup(client):
    client.add_cog(General(client))