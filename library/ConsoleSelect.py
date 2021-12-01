import sys
import discord
from datetime import datetime
from discord.ext import commands

from private.config import signature

def __init__(self, client):
    self.client = client
    
class Time:
    def CST():
        """Sets the datetime to `CST` (Central Standard Time)."""
        date_object = datetime.now()
        formTime = date_object.strftime("%H:%M:%S - %b %d %Y")
        return formTime

class Essentials():
    def Math(num1: float, op, num2: float):
        """Math Calculations to process for math.py."""
        valid = True
        if (op == '+' or op == 'plus'):
            result = num1 + num2
        elif (op == '-' or op == 'minus'):
            result = num1 - num2
        elif (op == '*' or op == 'x' or op == 'times'):
            result = num1 * num2
        elif (op == '/' or op == 'divide'):
            result = num1 / num2
        elif (op == '%' or op == 'remainder'):
            result = num1 % num2
        elif (op == '**' or op == 'exponent'):
            result = num1 ** num2
        elif (op == '//' or op == 'floor'):
            result = num1 // num2
        elif (op == 'ceil'):
            result = -(num1 // -num2)
        else: valid = False

        if (valid == False):
            embed = '**Invalid Operator!**'
            return embed
        elif (valid == True): 
            embed = f'**The result is:** {format(result, ".2f")}'
            return embed

class Color:
    """`class` meant to handle requests for colors."""
    white = discord.Color.from_rgb(230,230,230)
    """Returns a factory setting of a white color for RGB. `tuple`"""
    tachi = signature
    """Returns a factory setting of a signature Tachibana color for RGB. `tuple`"""
    weather = discord.Color.from_rgb(113, 175, 222)
    """Returns a factory setting of a signature Weather color for RGB. `tuple`"""

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

        if amount.isdigit() and unit in ['s','m','h','d']:
            return (int(amount), unit)
        
        raise commands.BadArgument(message = 'Not a valid duration.')

class Roundtrip: 
    def rt(self):
        roundtrip = round(self.client.latency * 1000)
        return roundtrip
        
class Console:
    async def log(timestamp, roundtrip, filename, cmd, channel, extra: None) -> str:
        """
        ### Meant to be a global log for printing statements. ###
        `timestamp:` Returns the time from the parameter argument.
        `roundtrip:` Returns the miliseconds of latency.
        `filename:` Filename of the library of commands.
        `cmd:` Name of the command.
        `channel:` Channel of the belonging `ctx.channel`.
        `extra: -> None or str. Normally fstring is used to display other information.`
        """
        print(f"[{timestamp}] [Roundtrip: {roundtrip}ms.] CONSOLE: {filename} - LOG: {cmd} was utilized in #{channel}! {extra}")
        
    async def event(timestamp, roundtrip, context: None) -> str:
        """
        ### Meant to be a global log for printing statements. (Event Variant) ###
        `timestamp:` Returns the time from the parameter argument.
        `roundtrip:` Returns the miliseconds of latency.
        `context: -> None or str. Normally fstring is used to display other information.`
        """        
        print(f"[{timestamp}] [Roundtrip: {roundtrip}ms.] CONSOLE - EVENT: {context}")

    async def error(timestamp, roundtrip, type, context: None) -> str:
        """
        ### Meant to be a global log for printing statements. (Error Variant) ###
        `timestamp:` Returns the time from the parameter argument.
        `roundtrip:` Returns the miliseconds of latency.
        `type:` Returns the type of error.
        `context: -> None or str. Normally fstring is used to display other information.`
        """        
        print(f"[{timestamp}] [Roundtrip: {roundtrip}ms.] CONSOLE - ERROR: {type} - LOG: {context}")
            
    async def startProgress(title):
        global progress_x
        sys.stdout.write(title + ": |" + " "*44 + "|" + chr(8)*45)
        sys.stdout.flush()
        progress_x = 0

    async def progress(x):
        global progress_x
        x = int(x * 44 // 100)
        sys.stdout.write("█" * (x - progress_x))
        sys.stdout.flush()
        progress_x = x

    async def endProgress():
        sys.stdout.write("█" * (44 - progress_x) + "|\n")
        sys.stdout.flush()    