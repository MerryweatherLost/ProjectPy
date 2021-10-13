import os
import discord

from discord.ext import commands, tasks
from library.ConsoleLib import Time
from itertools import cycle

# INITIALIZATION 

class Initialization(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.status = cycle(['with Scripts', 'with Discord.py'])

    @commands.Cog.listener()
    # SELF MUST BE THE FIRST ARGUMENT IN THE 
    # FIRST ARGUMENT THAT YOUR FUNCTIONS 
    # IN YOUR CLASS TAKES!
    async def on_ready(self):
        self.change_status.start()
        clear = lambda: os.system('clear')
        clear()
        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONNECTION ESTABLISHED.')
    
    @tasks.loop(seconds = 4)
    async def change_status(self):
        await self.client.change_presence(activity = discord.Game(next(self.status)))


def setup(client):
    client.add_cog(Initialization(client))