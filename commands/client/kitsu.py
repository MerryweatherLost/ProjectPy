import discord
from discord.ext import commands

from library.ConsoleSelect import *
from library.RatingSelect import Rating

from discord.ext import commands
from private.config import signature

import kitsu

import asyncio

class Kitsu(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.kit = kitsu.Client()
    
    @commands.group(help = 'Kitsu library for certain lookup.')
    async def kitsu(self, ctx):
        if ctx.invoked_subcommand is None:  
            embed = discord.Embed (description = 'That is not a visible subcommand.', color = signature)
            await ctx.reply(embed = embed)
                        
    @kitsu.command(help = 'Lookup anime from the database.')
    async def anime(self, ctx, *, anime: str):
        kya = await self.kit.search_anime(str(anime), limit = 1)
        message: discord.Message = await ctx.reply('The anime was found! <a:checkmark:903852585360949289> give me a moment... <a:burenyeo:909530018806390784>')
        await asyncio.sleep(1)
        
        if kya.nsfw == True: unsafe = 'Yes'
        elif kya.nsfw == False: unsafe = 'No'
        else: unsafe = 'Unsure'
        
        synopsis = (kya.synopsis[:1021] + '...') if len(kya.synopsis) > 1021 else kya.synopsis
        
        if len(kya.abbreviated_titles) == 0: titles = "No other titles were found."
        else: titles = ', '.join(kya.abbreviated_titles)

        em = discord.Embed (
            title = f"{kya.title('en_jp')}",
            color = Color.white
        )
        if kya.canonical_title != kya.title: 
            em.add_field (name = f"Canonical Title", value = f"*{kya.canonical_title}*")

        em.add_field     (name = "Abbreviated Titles", value = f"{titles}" + "\u200b", inline = False) 
        em.add_field     (name = "Synopsis", value = f"{synopsis}", inline = False)
        
        em.add_field     (name = "Entry Created", value = f"{kya.created_at.date()}")
        em.add_field     (name = "Start Date", value = f"{kya.start_date.date()}")
        em.add_field     (name = "End Date", value = f"{kya.end_date.date()}");
        
        em.add_field     (name = "Episode Count", value = f"{kya.episode_count}")
        em.add_field     (name = "Episode Length", value = f"{kya.episode_length} min.")
        em.add_field     (name = "Average Rating", value = f"{kya.average_rating}% {Rating.similarEmoji(kya.average_rating)}")
        
        em.add_field     (name = "NSFW Themes? (Not Accurate)", value = f"{unsafe}")
        em.add_field     (name = "Age Rating", value = f"{kya.age_rating_guide}")
        em.add_field     (name = "Popularity Ranking", value = f"{kya.popularity_rank}")
        em.add_field     (name = "Rating Ranking", value = f"{kya.rating_rank}")
        
        em.add_field     (name = "Show Type", value = f"{kya.show_type.upper()}")
        em.add_field     (name = "Status", value = f"{kya.status}")
        
        em.set_thumbnail (url = kya.poster_image('original'))
        em.set_image     (url = kya.cover_image('original'))
        
        em.set_footer    (text = f"Anime ID: {kya.id} • Updated At: {kya.updated_at.date()}")
        em.timestamp = ctx.message.created_at
        
        await message.delete()
        await ctx.reply(embed = em)
    
    # @kitsu.command(help = 'Looks for trending anime.')
    # async def trending(self, ctx):
    #     kya = await self.kit.trending_anime()
    #     em = discord.Embed (description = kya)
    #     await ctx.reply(embed = em)
        
def setup(client):
    client.add_cog(Kitsu(client))