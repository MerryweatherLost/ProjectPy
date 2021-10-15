import discord
import random

from datetime import datetime
from discord.ext import commands


def __init__(self, client):
    self.client = client

class Time:
    """
    ConsoleLib.Time
    ~~~~~~~~~~~~~~~~~~~~~
    Time class for the Console Library.

    Created by: Raymond Allison
    """
    
    def timeFormat():
        """
        Sets the time format and returns a String version for the console.

        Variables
        -----------
        formTime:
            variable from `date_object.strftime()` to cut down drastically on size. 
            It will be used in console logging. 
        """
        date_object = datetime.now()
        formTime = date_object.strftime("%H:%M:%S - %b %d %Y")
        return formTime
    def timeFormatUniversial():
        """
        Sets the time format, UTC.

        Variables
        -----------
        formTime:
            variable from date_object.strftime("%H:%M:%S - %b %d %Y") to cut down drastically on size. 
            It will be used in console logging. 
        """
        date_object = datetime.utcnow()
        formTime = date_object.strftime("%H:%M UTC - %b %d, %Y")
        return formTime
    def pureTimeUniversial():
        """
        Sets the time format, UTC.

        Variables
        -----------
        formTime:
            variable from date_object.strftime("%H:%M:%S) in UTC to cut down on size.
        """
        date_object = datetime.utcnow()
        formTime = date_object.strftime("%H:%M UTC")
        return formTime

class Essentials:
    def response8ball():
        """
        Responses handler for a randomized 8ball.

        Variables
        ---------
        responses: `str`, `list`,

        List of literal strings to pull from later on.

        response8ball: `var`,

        Picks one literal string from a `random.choice` function.
        """
        responses = [
            # POSITIVES
            'It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes.',
            'Outlook good.', 'Signs point to yes.', 'That is correct.',
            'Indeed.', 'Affirmative.',
            # NEUTRALS
            'Reply hazy, try again.',
            'Ask again later.','Can not predict now.', 
            'I can not find a result for that, try again.','Try again.',
            # NEGATIVES
            "Don't count on it.", 'My reply is no.', 'My sources say no.', 
            'Obviously not.', 'Negative.','Absolutely false.','Decidedly not.',
            'No.', 'That is incorrect.'
        ]
        response8ball = random.choice(responses)
        return response8ball
    def ballImage():
        """Just returns an 8ball image."""
        ballImage = 'https://cdn.discordapp.com/attachments/576096750331494420/896414018133196800/8b.png'
        return ballImage
    def CoinToss():
        """
        Responses handler for a randomized coinflip.

        Variables
        ---------
        responses: `str`, `list`,

        List of literal strings to pull from later on.

        coinflip: `var`,

        Picks one literal string from a `random.choice` function.
        """
        responses = [ 'Heads.','Tails.' ]
        coinflip = random.choice(responses)
        return coinflip

class Color:
    """`class` meant to handle requests for colors."""
    white = discord.Color.from_rgb(230,230,230)
    """Returns a factory setting of a white color for RGB. `tuple`"""
    tachi = discord.Color.from_rgb(235, 179, 82)
    """Returns a factory setting of a signature Tachibana color for RGB. `tuple`"""

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

class Roundtrip: 
    def rt(self):
        roundtrip = round(self.client.latency * 1000)
        return roundtrip
    