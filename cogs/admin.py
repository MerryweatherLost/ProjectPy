import discord
import asyncio

from ConsoleLib import Time
from discord.ext import commands

class DurationConverter(commands.Converter):
    """
    Duration Converter
    ------------------
    A Duration Converter meant to count the number of amounts and units from an argument.

        Variables
        ---------
            amount: `float`,

            The number passed in first to delegate how much.

            unit: `str`,
            
            The unit after the amount in seconds or minutes `s, m`.

        Raises
        ------
            BadArgument:

                The error comes from a invalid duration set, such as a value that does not equate to a `float`.
    """

    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]

        if amount.isdigit() and unit in ['s','m']:
            return (int(amount), unit)
        
        raise commands.BadArgument(message = 'Not a valid duration.')

class Administration(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # ADMINISTRATION #

    # CLEAR METHOD
    @commands.command(help = "Clears an amount of messages.")
    @commands.has_any_role('Admin')
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount)
        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE | LOG - CLEAR: A channel was cleared using this command!')
    
    @clear.error
    async def clear_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Please specify an amount of messages to delete.')

    # KICK METHOD
    @commands.command(help = "Kicks a person from the server.")
    @commands.has_any_role('Admin')
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason = reason)
        await ctx.reply(f'Kicked **{member}!**')

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE | LOG - KICK: A user was kicked! {member}')
        
    # BAN METHOD
    @commands.command(help = "Bans a person from the server.")
    @commands.has_any_role('Admin')
    async def ban(self, ctx, member : commands.MemberConverter, *, reason = None):
        await ctx.guild.ban(member, reason = reason)
        await ctx.reply(f'Banned **{member}!**')
        
        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE | LOG - BAN: A user was banned! {member}')
    
    # TEMP BAN METHOD
    @commands.command(help = "Temporarily bans a person from the server. - (UNSTABLE)")
    @commands.has_any_role('Admin')
    async def tempban(self, ctx, member: commands.MemberConverter, duration: DurationConverter):
        multiplier = {'s': 1, 'm': 60}
        amount, unit = duration

        await ctx.guild.ban(member)
        await ctx.reply(f'**{member}!** has been banned for **{amount}{unit}.**')
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)

        print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE | LOG - TEMPBAN: A user was temporarily banned! {member}')

    # UNBAN METHOD
    @commands.command(help = "Unbans a person from the server.")
    @commands.has_any_role('Admin')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.reply(f'Unbanned **{user.mention}!**')
                
                print(f'[{Time.timeFormat()}] [Roundtrip: {round(self.client.latency * 1000)}ms.] CONSOLE | LOG - UNBAN: A user was unbanned! {member}')
                return  

def setup(client):
    client.add_cog(Administration(client))