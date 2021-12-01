import discord
from discord.ext import commands

from library.ConsoleSelect import *

from datetime import date
from datetime import timedelta

from library.RatingSelect import Rating 

import python_weather
from python_weather import Client

from library.WeatherSelect import Weather

class WeatherStats(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.pyweather = Client

    @commands.group(help = 'Sends weather information of a city. (Quotes needed in the city parameter.)')
    async def weather(self, ctx):
        if ctx.invoked_subcommand is None:
            em = discord.Embed (description = 'That is not a visible subcommand.', color = signature)
            await ctx.reply(embed = em)    
        
    @weather.command(help = 'Sends the weather in imperial formatting.')
    async def imperial(self, ctx, *, city):
        client = self.pyweather(format = 'F')
        weather = await client.find(city)
        stn = python_weather.IMPERIAL
                
        em = discord.Embed (
            title = (f'{str(weather.current.observation_point)}'),
            color = Color.weather
        )
        # INFORMATION
        em.add_field (name = 'Temperature for Today', value = f'{weather.current.temperature}° {Weather.scale_name(stn)}', inline = False)
        em.add_field (name = 'Link to Weather Statistics', value = f'[Click Here]({weather.url})', inline = False)
        
        # TOP FIELD
        em.add_field (name = 'Skies ⛅', value = weather.current.sky_text)
        em.add_field (name = 'Precipitation 🌦️', value = f'{weather.current.humidity}{"%"}')
        em.add_field (name = 'Wind Display 🚩', value = weather.current.wind_display)
        
        # BOTTOM FIELD
        em.add_field (name = 'Source', value = weather.provider)
        em.add_field (name = 'Feels Like', value = f'{weather.current.feels_like}{stn}')
        em.add_field (name = 'Observation Point', value = weather.current.observation_point)

        em.set_footer (text = f'Date 🗓️: {weather.current.date} • UTC: {weather.timezone_offset} • Alerts ⚠️: {weather.alert_message}')

        em.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/899394919012118548/wther.png'
        )
        
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "GENERAL.PY", "Weather", ctx.channel, f'[Location[↗]: {weather.current.observation_point}] [Temperature: {weather.current.temperature}°{stn}] [Windspeed: {weather.current.wind_display}]')
        await client.close()
        
    @weather.command(help = 'Sends the weather in metric formatting.')
    async def metric(self, ctx, *, city):
        client = self.pyweather(format = 'C')
        weather = await client.find(city)
        stn = python_weather.METRIC
                
        em = discord.Embed (
            title = (f'{str(weather.current.observation_point)}'),
            color = Color.weather
        )
        # INFORMATION
        em.add_field (name = 'Temperature for Today', value = f'{weather.current.temperature}° {Weather.scale_name(stn)}', inline = False)
        em.add_field (name = 'Link to Weather Statistics', value = f'[Click Here]({weather.url})', inline = False)
        
        # TOP FIELD
        em.add_field (name = 'Skies ⛅', value = weather.current.sky_text)
        em.add_field (name = 'Precipitation 🌦️', value = f'{weather.current.humidity}{"%"}')
        em.add_field (name = 'Wind Display 🚩', value = weather.current.wind_display)
        
        # BOTTOM FIELD
        em.add_field (name = 'Source', value = weather.provider)
        em.add_field (name = 'Feels Like', value = f'{weather.current.feels_like}{stn}')
        em.add_field (name = 'Observation Point', value = weather.current.observation_point)

        em.set_footer (text = f'Date 🗓️: {weather.current.date} • UTC: {weather.timezone_offset} • Alerts ⚠️: {weather.alert_message}')

        em.set_thumbnail (
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/899394919012118548/wther.png'
        )
        
        await ctx.reply(embed = em)
        await Console.log(Time.CST(), Roundtrip.rt(self), "GENERAL.PY", "Weather", ctx.channel, f'[Location[↗]: {weather.current.observation_point}] [Temperature: {weather.current.temperature}°{stn}] [Windspeed: {weather.current.wind_display}]')
        await client.close()
    
    @commands.command(help = 'Checks the temperature in the area.', aliases = ['temp'])
    async def temperature(self, ctx, stn, *, city:str):
        st = Weather.standard(stn)  
        client = self.pyweather(format = st)
        weather = await client.find(city)
        
        em = discord.Embed (color = discord.Color.red())
        em.add_field  (name = "Temperature", value = f"The temperature for **{weather.current.observation_point}** is: **{weather.current.temperature}° {Weather.scale_name(st)}**", inline = False)
        em.set_footer (text = f"Date Recorded: {weather.current.day} • Source: {weather.provider}")
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await client.close()
        
    @commands.command(help = 'Forecast Testing.')
    async def forecast(self, ctx, stn, *, city:str):
        today = date.today().strftime('%A')
        yeast = date.today() - timedelta(days = 1)
        yesterday = yeast.strftime('%A')
        
        st = Weather.standard(stn)
        client = self.pyweather(format = st)       
        weather = await client.find(city) 
        
        em = discord.Embed (
            title = f"{weather.location_name}",
            color = Color.weather
        )
        
        for forecast in weather.forecasts:
            if today == forecast.day:
                em.add_field (name = "Summary for Today", value = f"Today for {weather.location_name}, we will have {str.lower(forecast.sky_text)} {Rating.skiesEmoji(forecast.sky_text)} skies, with the average temperature of {forecast.temperature}°{st}, high {forecast.high}°{st}, low {forecast.low}°{st}, with precipitation of {Rating.checkNum(forecast.precip)}%. {Rating.precipEmoji(Rating.checkNum(forecast.precip))} Winds at {weather.current.wind_display}.", inline = False)
                em.add_field (name = 'Current Weather Statistics', value = f'[Click Here]({weather.url})', inline = False)
                     
            if today != forecast.day and yesterday != forecast.day:
                em.add_field ( 
                name = forecast.day, 
                value = f"""
                    **Skies:** {forecast.sky_text} {Rating.skiesEmoji(forecast.sky_text)}
                    **Average Temperature:** {forecast.temperature}° {Weather.scale_name(st)}
                    **High:** {forecast.high}°{st}, **Low:** {forecast.low}°{st}
                    **Precipitation:** {Rating.checkNum(forecast.precip)}% {Rating.precipEmoji(Rating.checkNum(forecast.precip))}
                """, inline = False
            )
        
        em.set_footer (text = f"Source: {weather.provider}")
        em.timestamp = ctx.message.created_at
        await ctx.reply(embed = em)
        await client.close()
            
            
            
def setup(client):
    client.add_cog(WeatherStats(client))
    
    # em.add_field (name = 'High / Low', value = f'High: {weather.high} • Low: {weather.current.low}', inline = False)
        