import discord
import requests
import dateutil.parser
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw


class Spotify(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def track(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        spotify_result = next((activity for activity in member.activities if isinstance(activity, discord.Spotify)), None)
        if spotify_result is None:
            await ctx.send(f'{member.name} is not listening to Spotify.')
            return

        # Images
        track_background_image = Image.open('assets/spotify_template.png')
        album_image = Image.open(requests.get(spotify_result.album_cover_url, stream=True).raw).convert('RGBA')

        # Fonts
        title_font = ImageFont.truetype('arial.ttf', 18)
        artist_font = ImageFont.truetype('arial.ttf', 14)
        album_font = ImageFont.truetype('arial.ttf', 14)
        start_duration_font = ImageFont.truetype('arial.ttf', 12)
        end_duration_font = ImageFont.truetype('arial.ttf', 12)

        # Positions
        title_text_position = 150, 20
        artist_text_position = 150, 60
        album_text_position = 150, 80
        start_duration_text_position = 161, 121
        end_duration_text_position = 515, 121

        # Draws
        draw_on_image = ImageDraw.Draw(track_background_image)
        draw_on_image.text(title_text_position, spotify_result.title, 'black', font=title_font)
        draw_on_image.text(artist_text_position, f'by {spotify_result.artist}', 'black', font=artist_font)
        draw_on_image.text(album_text_position, spotify_result.album, 'black', font=album_font)
        draw_on_image.text(start_duration_text_position, '0:00', 'black', font=start_duration_font)
        draw_on_image.text(end_duration_text_position,
                           f"{dateutil.parser.parse(str(spotify_result.duration)).strftime('%M:%S')}",
                           'black', font=end_duration_font)

        # Background colour
        album_color = album_image.getpixel((250, 100))
        background_image_color = Image.new('RGBA', track_background_image.size, album_color)
        background_image_color.paste(track_background_image, (0, 0), track_background_image)

        # Resize
        album_image_resize = album_image.resize((140, 156))
        background_image_color.paste(album_image_resize, (0, 0), album_image_resize)

        # Save image
        background_image_color.convert('RGB').save('spotify.png', 'PNG')

        await ctx.send(file=discord.File('spotify.png'))


def setup(client):
    client.add_cog(Spotify(client))