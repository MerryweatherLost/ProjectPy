import os
import datetime
import discord 

from discord.ext import commands
from pretty_help import PrettyHelp
    
client = commands.Bot(command_prefix = ':', help_command = PrettyHelp(), case_insensitive = True)

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
async def on_member_join(member):
    date_object = datetime.now()
    print(f'[{date_object.strftime("%H:%M:%S - %b %d %Y")}] [ Roundtrip: {round(client.latency * 1000)}ms.] CONSOLE: JOIN | LOG: Member {member} has joined the server!')

@client.event
async def on_member_remove(member):
    date_object = datetime.now()
    print(f'[{date_object.strftime("%H:%M:%S - %b %d %Y")}] [ Roundtrip: {round(client.latency * 1000)}ms.] CONSOLE: LEAVE | LOG: Member {member} has left the server!')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('Please pass in the required arguments.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply('Whoops, looks like I can not find that command! Try inputting it correctly, and remember, it can be case sensitive!')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.reply('This command is on a cooldown! Wait a moment...')
        
client.run('ODkxNzAzMTE2MTAwMTU3NDkx.YVCNPQ.3AJF5N4SE6imB_jxvBuMk-ddNCg')