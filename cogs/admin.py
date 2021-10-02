import discord

from datetime import datetime
from discord.ext import commands

class Administration(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # ADMINISTRATION #

    # CLEAR METHOD
    @commands.command()
    @commands.has_any_role('admin')
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount)
        date_object = datetime.now()
        print(f'{date_object.strftime("%H:%M:%S %b %d %Y")}: CONSOLE | LOG - CLEAR: A channel was cleared using this command!')

    # KICK METHOD
    @commands.command()
    @commands.has_any_role('admin')
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        if not member:
            await ctx.reply('Invalid Member.')
        else:   
            await member.kick(reason = reason)
            await ctx.reply(f'Kicked {member.mention}!')
            date_object = datetime.now()
            print(f'{date_object.strftime("%H:%M:%S %b %d %Y")}: CONSOLE | LOG - KICK: A user was kicked! {member}')
        
    # BAN METHOD
    @commands.command()
    @commands.has_any_role('admin')
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        if not member:
            await ctx.reply('Invalid Member.')
        else:   
            await member.ban(reason = reason)
            await ctx.reply(f'Banned {member.mention}!')
            date_object = datetime.now()
            print(f'{date_object.strftime("%H:%M:%S %b %d %Y")}: CONSOLE | LOG - BAN: A user was banned! {member}')

    # UNBAN METHOD
    @commands.command()
    @commands.has_any_role('The Architect')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.reply(f'Unbanned {user.mention}!')
                date_object = datetime.now()
                print(f'{date_object.strftime("%H:%M:%S %b %d %Y")}: CONSOLE | LOG - UNBAN: A user was unbanned! {member}')
                return  

def setup(client):
    client.add_cog(Administration(client))