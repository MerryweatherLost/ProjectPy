import discord
import asyncio

from library.ConsoleLib import Time
from library.ConsoleLib import Color
from library.ConsoleLib import DurationConverter
from library.ConsoleLib import Roundtrip

from settings.Settings import Admin
from discord.ext import commands

class Administration(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # ADMINISTRATION #

    # CLEAR METHOD
    @commands.command(help = "Clears an amount of messages.")
    @commands.has_permissions(manage_messages = True)
    @commands.cooldown(rate = 1, per = 5)
    async def clear(self, ctx, amount = 5):
        if (amount >= Admin.clearlimit):
            embed = discord.Embed (
                description = f'Woah! too many requests! Try something less than {Admin.clearlimit}.',
                color = Color.tachi
            )
            embed.set_footer (
                text = f'Tachibana: {Time.timeFormatUniversial()}'
            )            
            message: discord.Message = await ctx.reply(embed = embed)
            await asyncio.sleep(3)
            await message.delete()
            print(f'[{Time.timeFormat()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE | LOG - CLEAR: Channel #{ctx.channel} was unsuccessfully cleared! Larger amount than expected! [Amount: {amount}] [Limit: {Admin.clearlimit}]')
        else:
            await ctx.channel.purge(limit = amount)
            print(f'[{Time.timeFormat()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE | LOG - CLEAR: Channel #{ctx.channel} was cleared {amount} times using this command!')
    
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Please specify an amount of messages to delete.')

    # KICK METHOD
    @commands.command(help = "Kicks a person from the server.")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        if (member == ctx.author):
            await ctx.reply('You can not kick yourself!')
        else:
            await member.kick(reason = reason)
            await ctx.reply(f'Kicked **{member}!**')
            print(f'[{Time.timeFormat()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE | LOG - KICK: A user was kicked in #{ctx.channel}! [{member}]')
        
    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("You don't have the required permissions to do that!")

    # BAN METHOD
    @commands.command(help = "Bans a person from the server.")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : commands.MemberConverter, *, reason = None):
        if (member == ctx.author):
            await ctx.reply('You can not ban yourself!')
        else:    
            await ctx.guild.ban(member, reason = reason)
            await ctx.reply(f'Banned **{member}!**')
            print(f'[{Time.timeFormat()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE | LOG - BAN: A user was banned in #{ctx.channel}! [{member}]')
    
    # TEMP BAN METHOD
    @commands.command(help = "Temporarily bans a person from the server. - (UNSTABLE)")
    @commands.has_permissions(ban_members = True)
    async def tempban(self, ctx, member: commands.MemberConverter, duration: DurationConverter):
        if (member == ctx.author):
            await ctx.reply('You can not tempban yourself dummy!')
        else:
            multiplier = {'s': 1, 'm': 60}
            amount, unit = duration

            await ctx.guild.ban(member)
            await ctx.reply(f'**{member}!** has been banned for **{amount}{unit}.**')
            await asyncio.sleep(amount * multiplier[unit])
            await ctx.guild.unban(member)
            print(f'[{Time.timeFormat()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE | LOG - TEMPBAN: A user was temporarily banned in #{ctx.channel}! [{member}]')

    # UNBAN METHOD
    @commands.command(help = "Unbans a person from the server.")
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        if (member == ctx.author):
            await ctx.reply('You can not unban yourself dummy!')
        else:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.reply(f'Unbanned **{user.mention}!**')
                    
                    print(f'[{Time.timeFormat()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE | LOG - UNBAN: A user was unbanned in #{ctx.channel}! [{member}]')
                    return  

def setup(client):
    client.add_cog(Administration(client))