import os
import discord
import requests
import textwrap
import dateutil.parser
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw


class Spotify(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help = 'Sends spotify track from person.')
    async def spotify(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        spotify_result = next((activity for activity in member.activities if isinstance(activity, discord.Spotify)), None)
        if spotify_result is None:
            await ctx.send(f'{member.name} is not listening to Spotify.')
            return

        # Images
        track_background_image = Image.open('assets/spotify_template_rend.png')
        album_image = Image.open(requests.get(spotify_result.album_cover_url, stream=True).raw).convert('RGBA')

        # Fonts
        title_font = ImageFont.truetype('fonts/JetBrainsMono-Bold.ttf', 24)
        artist_font = ImageFont.truetype('fonts/JetBrainsMono-Bold.ttf', 18)
        album_font = ImageFont.truetype('fonts/JetBrainsMono-Bold.ttf', 14)
        start_duration_font = ImageFont.truetype('fonts/JetBrainsMono-Bold.ttf', 12)
        end_duration_font = ImageFont.truetype('fonts/JetBrainsMono-Bold.ttf', 12)

        # Positions
        title_text_position = 195, 35
        artist_text_position = 195, 75
        album_text_position = 195, 100
        start_duration_text_position = 190, 163
        end_duration_text_position = 554, 163

        # CONDITION TO FIX LENGTH
        if (len(spotify_result.artist) > 35):
            spotiartist = textwrap.fill(spotify_result.artist, 35) 
            album_text_position = 195, 125
        else:
            spotiartist = spotify_result.artist

        if (len(spotify_result.title) > 18):
            spotititle = textwrap.fill(spotify_result.title, 18) 
            title_text_position = 195, 25
            artist_text_position = 195, 85
            album_text_position = 195, 130
        else:
            spotititle = spotify_result.title

        # Draws
        draw_on_image = ImageDraw.Draw(track_background_image)
        draw_on_image.text(title_text_position, spotititle, (60,180,60), font=title_font)
        draw_on_image.text(artist_text_position, f'by {spotiartist}', (60,180,60), font=artist_font)
        draw_on_image.text(album_text_position, spotify_result.album, (60,180,60), font=album_font)
        draw_on_image.text(start_duration_text_position, '0:00', (60,180,60), font=start_duration_font)
        draw_on_image.text(end_duration_text_position,
                           f"{dateutil.parser.parse(str(spotify_result.duration)).strftime('%M:%S')}",
                           (60,180,60), font=end_duration_font)

        # Background Color
        album_color = album_image.getpixel((600, 200))
        background_image_color = Image.new('RGBA', track_background_image.size, album_color)
        background_image_color.paste(track_background_image, (0, 0), track_background_image)

        # Resize
        album_image_resize = album_image.resize((175, 175))
        background_image_color.paste(album_image_resize, (0, 20), album_image_resize)

        # Save Image
        background_image_color.convert('RGB').save('spotify_render.png', 'PNG')

        await ctx.reply(file = discord.File('spotify_render.png'))
        await ctx.send(f"https://open.spotify.com/track/{spotify_result.track_id}")

def setup(client):
    client.add_cog(Spotify(client))