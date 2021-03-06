import os
import sys
import time
import discord

import itertools
import threading
from discord.ext import commands

from private.config import *
from library.ConsoleSelect import *

from pretty_help import PrettyHelp

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rFinding Command: ' + c)
        sys.stdout.flush()
        time.sleep(0.2)
    
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

@client.command(help = 'Loads package.')
@commands.is_owner()
# LOAD_EXTENSION: Loading the 'cog' folder
async def load(extension):
    client.load_extension(f'commands.{extension}')

@client.command(help = 'Unloads package.')
@commands.is_owner()
# EXTENSION: Unloading the 'cog' folder
async def unload(extension):
    client.unload_extension(f'commands.{extension}')

@client.command(help = 'Reloads package.')
@commands.is_owner()
# EXTENSIONS: Reloading the 'cog' folder
async def reload(extension):
    client.reload_extension(f'commands.{extension}')

# GENERAL LOAD HANDLER
print(f'< Loading all files within the Commands Folder >')
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')
        t = threading.Thread(target = animate)
        done = False
        t.start()
        time.sleep(0.1)
        done = True
        print(f' » Loaded {filename}!')

# EVENT LOAD
print(f'\n< Loading all files within the Events Folder >')
for filename in os.listdir('./commands/events'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.events.{filename[:-3]}')
        t = threading.Thread(target = animate)
        done = False
        t.start()
        time.sleep(0.1)
        done = True
        print(f' » Loaded {filename}!')

# ADMINISTRATION LOAD
print(f'\n< Loading all files within the Administration Folder >')
for filename in os.listdir('./commands/admin'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.admin.{filename[:-3]}')
        t = threading.Thread(target = animate)
        done = False
        t.start()
        time.sleep(0.1)
        done = True
        print(f' » Loaded {filename}!')

# CLIENT LOAD
print(f'\n< Loading all files within the Client Folder >')
for filename in os.listdir('./commands/client'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.client.{filename[:-3]}')
        t = threading.Thread(target = animate)
        done = False
        t.start()
        time.sleep(0.1)
        done = True
        print(f' » Loaded {filename}!')

# CONTENT LOAD
print(f'\n< Loading all files within the Content Folder >')
for filename in os.listdir('./commands/content'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.content.{filename[:-3]}')
        t = threading.Thread(target = animate)
        done = False
        t.start()
        time.sleep(0.1)
        done = True
        print(f' » Loaded {filename}!')

print('\nCompleted all loading tasks!')

client.run(config)