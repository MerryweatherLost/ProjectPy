import os
import discord
import asyncio

from discord.ext import commands

from private.config import config
from private.config import prefix
from private.config import consoleclr

from library.ConsoleLib import Time
from library.ConsoleLib import Color

from pretty_help import PrettyHelp

client = commands.Bot (
    command_prefix = prefix, 
    help_command = PrettyHelp (color = Color.tachi), 
    case_insensitive = True,
    strip_after_prefix = True
)

clear = lambda: os.system(consoleclr)
clear()

@client.command(help = 'Loads package.')
@commands.is_owner()
# LOAD_EXTENSION: Loading the 'cog' folder
async def load(extension):
    client.load_extension(f'cogs.{extension}')

@client.command(help = 'Unloads package.')
@commands.is_owner()
# EXTENSION: Unloading the 'cog' folder
async def unload(extension):
    client.unload_extension(f'cogs.{extension}')

@client.command(help = 'Reloads package.')
@commands.is_owner()
# EXTENSIONS: Reloading the 'cog' folder
async def reload(extension):
    client.reload_extension(f'cogs.{extension}')

# COMMAND HANDLER
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_member_join(member: discord.Member):
    print(f'[{Time.timeCST()}] [Roundtrip: {round(client.latency * 1000)}ms.] CONSOLE: JOIN | LOG: Member {member} has joined the server!')

@client.event
async def on_member_remove(member: discord.Member):
    print(f'[{Time.timeCST()}] [Roundtrip: {round(client.latency * 1000)}ms.] CONSOLE: LEAVE | LOG: Member {member} has left the server!')
        
@client.event
async def on_command_error(ctx, error):
    message: discord.Message = await ctx.reply('Hold on! An error has occured within the bot! Awaiting reason... <a:loading:893139868157354034>')
    if isinstance(error, commands.MissingRequiredArgument):
        msg = 'Please pass in the required arguments.'
        embed = discord.Embed (
            description = msg
        )
        embed.set_footer (
            text = f'Tachibana Error Reporting: {Time.timeUTC()}'
        )

    elif isinstance(error, commands.MissingPermissions):
        msg = 'You are missing permissions for this command.'
        embed = discord.Embed (
            description = msg
        )
        embed.set_footer (
            text = f'Tachibana Error Reporting: {Time.timeUTC()}'
        )

    elif isinstance(error, commands.UserNotFound):
        msg = 'Unfortunately, I can not find this member, try again and check the user.'
        embed = discord.Embed (
            description = msg
        )
        embed.set_footer (
            text = f'Tachibana Error Reporting: {Time.timeUTC()}'
        )

    elif isinstance(error, commands.TooManyArguments):
        msg = 'Too many arguments within this response, check the required amount.'
        embed = discord.Embed (
            description = msg
        )
        embed.set_footer (
            text = f'Tachibana Error Reporting: {Time.timeUTC()}'
        )

    elif isinstance(error, commands.CommandNotFound):
        msg = 'Whoops, looks like I can not find that command! Try inputting it correctly, or check t!help or ask **Edelweiss#1337** for assistance!'
        embed = discord.Embed (
            description = msg
        )
        embed.set_footer (
            text = f'Tachibana Error Reporting: {Time.timeUTC()}'
        )

    elif isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is on a cooldown! Wait a moment...'
        embed = discord.Embed (
            description = msg
        )
        embed.set_footer (
            text = f'Tachibana Error Reporting: {Time.timeUTC()}'
        )

    elif isinstance(error, commands.NSFWChannelRequired):
        msg = 'Seems like this command needs a NSFW channel.'  
        embed = discord.Embed (
            description = msg
        )
        embed.set_footer (
            text = f'Tachibana Error Reporting: {Time.timeUTC()}'
        )

    else:
        msg = "I can not pick up this error from my handler! Notify **Edelweiss#1337!**"
        embed = discord.Embed (
            description = msg
        )
        embed.set_footer (
            text = f'Tachibana Error Reporting: {Time.timeUTC()}'
        )
        print(f'[{Time.timeCST()}] [Roundtrip: {round(client.latency * 1000)}ms.] CONSOLE: ERROR: ATTENTION! | LOG: Required Attention to Unknown Error!')   
        print(error)

    await asyncio.sleep(1)
    await message.delete()
    await ctx.reply(embed = embed)

client.run(config)