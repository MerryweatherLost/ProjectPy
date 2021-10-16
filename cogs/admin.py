import asyncio

import discord
from discord.ext import commands

from library.ConsoleLib import Time
from library.ConsoleLib import Color
from library.ConsoleLib import DurationConverter
from library.ConsoleLib import Roundtrip

from settings.Settings import Admin


class Administration(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # ADMINISTRATION #

    # CLEAR METHOD
    @commands.command(help = "Clears an amount of messages.")
    @commands.has_permissions(manage_messages = True)
    @commands.cooldown(rate = 1, per = 5)
    async def clear(self, ctx, amount = 5):
        if (amount > Admin.clearlimit):
            embed = discord.Embed (
                description = f'Woah! too many requests! Try something less than or equal to {Admin.clearlimit}.',
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
    async def kick(self, ctx, member : commands.MemberConverter, *, reason = None):
        if (member == ctx.author):
            await ctx.reply('You can not kick yourself!')
        else:
            await member.kick(reason = reason)
            await ctx.reply(f'Kicked **{member}!**')
            print(f'[{Time.timeFormat()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE | LOG - KICK: A user was kicked in #{ctx.channel}! [Member: {member}] [Reason: {reason}]')
        
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
            embed = discord.Embed (
                description = f'Banned **{member}**, the reason was: **{reason}**',
                color = Color.tachi
            )
            embed.set_footer (
                text = f'Tachibana Administration Protocol: {Time.timeFormatUniversial()}'
            )    
            await ctx.guild.ban(member, reason = reason)
            await ctx.reply(f'Banned **{member}!**')
            print(f'[{Time.timeFormat()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE | LOG - BAN: A user was banned in #{ctx.channel}! [Member: {member}] [Reason: {reason}]')
    
    # TEMP BAN METHOD
    @commands.command(help = "Temporarily bans a person from the server. - (UNSTABLE)")
    @commands.has_permissions(ban_members = True)
    async def tempban(self, ctx, member: commands.MemberConverter, duration: DurationConverter, *, reason = None):
        if (member == ctx.author):
            await ctx.reply('You can not tempban yourself dummy!')
        else:
            multiplier = {'s': 1, 'm': 60}
            amount, unit = duration

            embed = discord.Embed (
                description = f'**{member}!** has been banned for **{amount}{unit}.**',
                color = Color.tachi
            )
            embed.set_footer (
                text = f'Tachibana Administration Protocol: {Time.timeFormatUniversial()}'
            )

            await ctx.guild.ban(member, reason = reason)
            await ctx.reply(embed = embed)

            await asyncio.sleep(amount * multiplier[unit])

            await ctx.guild.unban(member)
            print(f'[{Time.timeFormat()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE | LOG - TEMPBAN: A user was temporarily banned in #{ctx.channel}! [Member: {member}] [Reason: {reason}]')

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
                    embed = discord.Embed (
                        description = f'Unbanned **{user.mention}!**',
                        color = Color.tachi
                    )
                    embed.set_footer (
                        text = f'Tachibana Administration Protocol: {Time.timeFormatUniversial()}'
                    )
                    await ctx.guild.unban(user)
                    await ctx.reply(embed = embed)
                    
                    print(f'[{Time.timeFormat()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE | LOG - UNBAN: A user was unbanned in #{ctx.channel}! [{member}]')
                    return  

def setup(client):
    client.add_cog(Administration(client))