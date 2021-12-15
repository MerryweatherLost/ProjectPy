import os

import discord
from discord.ext import commands

from private.config import *
from library.ConsoleSelect import *

from time import sleep

from pretty_help import PrettyHelp
    
intents = discord.Intents().all() 
intents.members = True 

client = commands.Bot (
    command_prefix = prefix, 
    help_command = PrettyHelp (color = Color.tachi), 
    case_insensitive = True,
    strip_after_prefix = True,
    intents = intents
)

clear = lambda: os.system(consoleclr)
clear()

@client.command(hidden = True, help = 'Loads package.')
@commands.is_owner()
# LOAD_EXTENSION: Loading the 'cog' folder
async def load(extension):
    client.load_extension(f'commands.{extension}')

@client.command(hidden = True, help = 'Unloads package.')
@commands.is_owner()
# EXTENSION: Unloading the 'cog' folder
async def unload(extension):
    client.unload_extension(f'commands.{extension}')

@client.command(hidden = True, help = 'Reloads package.')
@commands.is_owner()
# EXTENSIONS: Reloading the 'cog' folder
async def reload(extension):
    client.reload_extension(f'commands.{extension}')

# GENERAL LOAD HANDLER
print(f'Indexing the Commands Folder for Commands...')
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')
        sleep(0.1)
        print(f' » Loaded {filename}!')

# EVENT LOAD
print(f'\nLoading all files within the Events Folder...')
for filename in os.listdir('./commands/events'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.events.{filename[:-3]}')
        sleep(0.1)
        print(f' » Loaded {filename}!')

# ADMINISTRATION LOAD
print(f'\nLoading all files within the Administration Folder...')
for filename in os.listdir('./commands/admin'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.admin.{filename[:-3]}')
        sleep(0.1)
        print(f' » Loaded {filename}!')

# CLIENT LOAD
print(f'\nLoading all files within the Client Folder...')
for filename in os.listdir('./commands/client'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.client.{filename[:-3]}')
        sleep(0.1)
        print(f' » Loaded {filename}!')

# CONTENT LOAD
print(f'\nLoading all files within the Content Folder...')
for filename in os.listdir('./commands/content'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.content.{filename[:-3]}')
        sleep(0.1)
        print(f' » Loaded {filename}!')

print('\nAll files successfully loaded, starting client...')

client.run(config)