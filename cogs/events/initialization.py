import os
import discord
import asyncio 

from audioplayer import AudioPlayer
from discord.ext import commands, tasks
from itertools import cycle

from private.config import status
from library.ConsoleSelect import *

from private.config import consoleclr
from private.config import name

from settings.config import General

# INITIALIZATION 

class Initialization(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.status = cycle(status)

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        # CLEAR COMMAND
        clear = lambda: os.system(consoleclr)
        clear()

        # START PROCESS
        print(General.quote())
        AudioPlayer("sounds/setup.wav").play(block=True)
        clear()
        await Console.startProgress(u'\u001b[33;1m Initializing Client  ⚡\u001b[0m')
        set = 0

        # LOOP TO REACH PROCESS
        while (set != 100):
            await asyncio.sleep(0.01)
            await Console.progress(x = set)
            set += 1

        # COMPLETE PROCESS
        await Console.endProgress()
        clear()
        print(f'Loading Complete! Welcome Back, Edelweiss!')
        if (name == 'cleo'): print(u'\u001b[35;1mSeems like you are using the test build of Tachibana (Cleo).\u001b[0m \n')
        elif (name == 'tachibana'): print(u'\u001b[33;1mYou are using the stable version of Tachibana.\u001b[0m \n')
        await asyncio.sleep(0.5)

        # PRINT ESTABLISHMENT
        print(f'[{Time.timeCST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONNECTION ESTABLISHED. ⚡')

    @tasks.loop(seconds = 4)
    async def change_status(self):
        await self.client.change_presence(activity = discord.Game(next(self.status)))

def setup(client):
    client.add_cog(Initialization(client))