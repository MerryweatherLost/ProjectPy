import os
import discord
import asyncio 

from playsound import playsound

from discord.ext import commands, tasks

from library.ConsoleLib import Time
from library.ConsoleLib import InitProg
from library.ConsoleLib import Roundtrip

from itertools import cycle

from private.config import status
from private.config import consoleclr

from settings.Settings import General

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
        # CLEAR COMMAND
        self.change_status.start()
        clear = lambda: os.system(consoleclr)
        clear()

        # START PROCESS
        print(General.quote())
        playsound('setup.wav')
        clear()
        InitProg.startProgress(u'\u001b[33mInitializing Client\u001b[0m')
        set = 0

        # LOOP TO REACH PROCESS
        while (set != 100):
            await asyncio.sleep(0.01)
            InitProg.progress(x = set)
            set += 1

        # COMPLETE PROCESS
        InitProg.endProgress()
        print(f'Loading Complete! Welcome Back, Edelweiss!\n')
        await asyncio.sleep(0.5)

        # PRINT ESTABLISHMENT
        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONNECTION ESTABLISHED.')
   
    @tasks.loop(seconds = 4)
    async def change_status(self):
        await self.client.change_presence(activity = discord.Game(next(self.status)))


def setup(client):
    client.add_cog(Initialization(client))