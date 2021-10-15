import os
import discord

from discord.ext import commands, tasks

from library.ConsoleLib import Time
from library.ConsoleLib import Roundtrip

from itertools import cycle

from private.config import status
from private.config import consoleclr

# INITIALIZATION 

class Initialization(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.status = cycle(status)

    @commands.Cog.listener()
    # SELF MUST BE THE FIRST ARGUMENT IN THE 
    # FIRST ARGUMENT THAT YOUR FUNCTIONS 
    # IN YOUR CLASS TAKES!
    async def on_ready(self):
        self.change_status.start()
        clear = lambda: os.system(consoleclr)
        clear()
        print(f'[{Time.timeFormat()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONNECTION ESTABLISHED.')
    
    @tasks.loop(seconds = 4)
    async def change_status(self):
        await self.client.change_presence(activity = discord.Game(next(self.status)))


def setup(client):
    client.add_cog(Initialization(client))