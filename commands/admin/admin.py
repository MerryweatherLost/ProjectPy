import asyncio

import discord
from discord.ext import commands
from discord.utils import get

from library.ConsoleSelect import Time
from library.ConsoleSelect import Color
from library.ConsoleSelect import DurationConverter
from library.ConsoleSelect import Roundtrip
from library.ConsoleSelect import Console

from settings.config import Admin


class Administration(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # ADMINISTRATION #

    # CLEAR METHOD
    @commands.command(help = "Clears an amount of messages.")
    @commands.has_permissions(manage_messages = True)
    @commands.cooldown(rate = 1, per = 5)
    async def clear(self, ctx, amount: int):
        if (amount > Admin.clearlimit):
            embed = discord.Embed (
                description = f'Woah! too many requests! Try something less than or equal to {Admin.clearlimit}.',
                color = Color.tachi
            )
            embed.set_footer (
                text = f'{self.client.user.name}'
            )            
            embed.timestamp = ctx.message.created_at
            message: discord.Message = await ctx.reply(embed = embed)
            await asyncio.sleep(3)
            await message.delete()
            await Console.log(Time.CST(), Roundtrip.rt(self), "ADMIN.PY", "Clear", ctx.channel, 
            extra = f'#{ctx.channel} was unsuccessfully cleared! Larger amount than expected! [Amount: {amount}] [Limit: {Admin.clearlimit}]')
        else:
            await ctx.channel.purge(limit = amount)
            await Console.log(Time.CST(), Roundtrip.rt(self), "ADMIN.PY", "Clear", ctx.channel, 
            extra = f"#{ctx.channel} was cleared {amount} times using this command!")

    # KICK METHOD
    @commands.command(help = "Kicks a person from the server.")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : commands.MemberConverter, *, reason = None):
        if (member == ctx.author):
            embed = discord.Embed(description = 'You can not kick yourself!')
            await ctx.reply(embed = embed)
        else:
            await member.kick(reason = reason)
            await ctx.reply(f'Kicked **{member}!**')
            Console.log(Time.CST, Roundtrip.rt(self), "ADMIN.PY", "Clear", ctx.channel, 
            extra = f'A user by the name of {member.mention} was kicked! - Reason: {reason}')

    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("You don't have the required permissions to do that!")

    # BAN METHOD
    @commands.command(help = "Bans a person from the server.")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : commands.MemberConverter, *, reason = None):
        if (member == ctx.author):
            embed = discord.Embed(description = 'You can not ban yourself!')
            await ctx.reply(embed = embed)
        else:
            if (reason): rb = f', with the reason being **{reason}.**'
            else: rb = '.'
            embed = discord.Embed (
                description = f'Banned **{member}**{rb}',
                color = Color.tachi
            )
            embed.set_footer (
                text = f'{self.client.user.name} Administration Protocol'
            )    
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.guild.ban(member, reason = reason)
            await ctx.reply(f'Banned **{member}!**')
            Console.log(Time.CST(), Roundtrip.rt(self), "ADMIN.PY", ctx.channel,
            extra = f'A user by the name of {member.mention} was banned! - Reason: {reason}')
    
    # TEMP BAN METHOD
    @commands.command(help = "Temporarily bans a person from the server. - (UNSTABLE)")
    @commands.has_permissions(ban_members = True)
    async def tempban(self, ctx, member: commands.MemberConverter, duration: DurationConverter, *, reason = None):
        if (member == ctx.author):
            embed = discord.Embed(description = 'You can not tempban yourself dummy!')
            await ctx.reply(embed = embed)
        else:
            multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
            amount, unit = duration

            if (reason): rb = f', with the reason being **{reason}.**'
            else: rb = '.'
            embed = discord.Embed (
                description = f'**{member}** has been banned for **{amount}{unit}**{rb}',
                color = Color.tachi
            )
            embed.set_footer (
                text = f'{self.client.user.name} Administration Protocol'
            )
            message = ctx.message
            embed.timestamp = message.created_at
            await ctx.guild.ban(member, reason = reason)
            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE | LOG - TEMPBAN: A user was temporarily banned in #{ctx.channel}! [Member: {member}] [Reason: {reason}]')
            await ctx.reply(embed = embed)

            await asyncio.sleep(amount * multiplier[unit])

            await ctx.guild.unban(member)
            print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE | LOG - TEMPBAN: A user was unbanned due to the amount being reached. [Member: {member}] [Afformentioned Reason: {reason}]')

    # UNBAN METHOD
    @commands.command(help = "Unbans a person from the server.")
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        if (member == ctx.author):
            embed = discord.Embed(description = 'You can not unban yourself dummy!')
            await ctx.reply(embed = embed)
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
                    embed.timestamp = ctx.message.created_at
                    await ctx.guild.unban(user)
                    await ctx.reply(embed = embed)
                    
                    print(f'[{Time.CST()}] [Roundtrip: {Roundtrip.rt(self)}ms.] CONSOLE | LOG - UNBAN: A user was unbanned in #{ctx.channel}! [{member}]')
                    return  

    # MUTE METHOD
    @commands.command(help = "Adds a mute role to a person for a specified duration or none.")
    @commands.has_any_role('Admin','House of Lords')
    async def mute(self, ctx, member: discord.Member, duration: DurationConverter, *, reason = None):
        mute = 843662762600431637
        if (member == ctx.author):
            await ctx.reply("Listen, can you not mute yourself...?")
        else:
            multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
            amount, unit = duration

            if (reason): rb = f', with the reason being {str.capitalize(reason)}'
            else: rb = '.'

            em = discord.Embed (
                description = f'**{member}** has been muted for {amount}{unit}{rb}'
            )
            em.set_footer (
                text = f'{self.client.user.name} Administration Protocol'
            )
            em.timestamp = ctx.message.created_at
            await member.add_roles(roles = mute, reason = reason)
            await asyncio.sleep(amount * multiplier[unit])
            await member.remove_roles(roles = mute, reason = 'The specified time is over.')
            
    # @commands.command(help = 'Adds roles to users.')
    # async def addrole(self, ctx, member: discord.Member, role):
    #     role = get(member.guild.roles, name=f"{role}")
    #     await member.add_roles(*role, reason = None)
    #     await ctx.reply(f'Added roles to {member.mention}!')

def setup(client):
    client.add_cog(Administration(client))