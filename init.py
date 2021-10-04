import os
import datetime
import discord

from discord.ext import commands

client = commands.Bot(command_prefix = ':')

@client.command()
@commands.is_owner()
# LOAD_EXTENSION: Loading the 'cog' folder
async def load(extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
# EXTENSION: Unloading the 'cog' folder
async def unload(extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
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
    print(f'[{date_object.strftime("%H:%M:%S - %b %d %Y")}] CONSOLE: JOIN | LOG: Member {member} has joined the server!')

@client.event
async def on_member_remove(member):
    date_object = datetime.now()
    print(f'[{date_object.strftime("%H:%M:%S - %b %d %Y")}] CONSOLE: LEAVE | LOG: Member {member} has left the server!')

client.run('ODkxNzAzMTE2MTAwMTU3NDkx.YVCNPQ.3AJF5N4SE6imB_jxvBuMk-ddNCg')
