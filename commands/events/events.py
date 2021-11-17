import discord
import asyncio
from audioplayer import AudioPlayer
from discord.ext import commands, tasks

from PIL import Image, ImageFont, ImageDraw
from discord.ext.commands.errors import CommandInvokeError

from library.ConsoleSelect import *

# CLASS FOR ALL GENERAL EVENTS
class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

# ALL GENERAL EVENT ERRORS
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        message: discord.Message = await ctx.reply('Hold on! An error has occured within the bot! Awaiting reason... <a:loading:893139868157354034>')
        if isinstance(error, commands.MissingRequiredArgument):
            msg = 'Please pass in the required arguments.'
            embed = discord.Embed (description = msg)
            embed.set_footer (text = f'{self.client.user.name}')
            embed.timestamp = message.created_at

        if isinstance(error, commands.MissingPermissions):
            msg = 'You are missing permissions for this command.'
            embed = discord.Embed (description = msg)
            embed.set_footer (text = f'{self.client.user.name}')
            embed.timestamp = message.created_at

        if isinstance(error, commands.UserNotFound):
            msg = 'Unfortunately, I can not find this member, try again and check the user.'
            embed = discord.Embed (description = msg)
            embed.set_footer (text = f'{self.client.user.name}')
            embed.timestamp = message.created_at

        if isinstance(error, commands.TooManyArguments):
            msg = 'Too many arguments within this response, check the required amount.'
            embed = discord.Embed (description = msg)
            embed.set_footer (text = f'{self.client.user.name}')
            embed.timestamp = message.created_at

        if isinstance(error, commands.CommandNotFound):
            msg = 'Whoops, looks like I can not find that command! Try inputting it correctly, or check t!help or ask **Edelweiss#1337** for assistance!'
            embed = discord.Embed (description = msg)
            embed.set_footer (text = f'{self.client.user.name}')
            embed.timestamp = message.created_at

        if isinstance(error, commands.CommandOnCooldown):
            msg = 'This command is on a cooldown! Wait a moment...'
            embed = discord.Embed (description = msg)
            embed.set_footer (text = f'{self.client.user.name}')
            embed.timestamp = message.created_at

        if isinstance(error, commands.NSFWChannelRequired):
            msg = 'Seems like this command needs a NSFW channel.'  
            embed = discord.Embed (description = msg)
            embed.set_footer (text = f'{self.client.user.name}')
            embed.timestamp = message.created_at

        if isinstance(error, CommandInvokeError):
            msg = f'I can not pick up this error from my handler! Notify **Edelweiss#1337!**\nError Specified: {error}'
            embed = discord.Embed (description = msg)
            embed.set_footer (text = f'{self.client.user.name}')
            embed.timestamp = message.created_at

            await Console.error(Time.CST(), Roundtrip.rt(self), "Command Invoke Error ⊖ Required Attention ⊖", f"\n{error}")

        await asyncio.sleep(1)
        await message.delete()
        await ctx.reply(embed = embed)
        AudioPlayer("sounds/error.wav").play(block=True)

# ALL GENERAL EVENTS
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await Console.event(Time.timeCST(), Roundtrip.rt(self), f"Member {member} has joined the server.")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        await Console.event(Time.timeCST(), Roundtrip.rt(self), f"Member {member} has left the server.")

def setup(client):
    client.add_cog(Events(client))