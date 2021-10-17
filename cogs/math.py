import discord
from discord.ext import commands

class Math(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # MATH COMMAND
    @commands.command(help = 'Does a scheme of math.')
    async def math(self, ctx, num1: float,  op, num2: float):
        # Arithmetic Operators
        dropon = True
        if (op == '+' or op == 'plus'):
            result = num1 + num2
        elif (op == '-' or op == 'minus'):
            result = num1 - num2
        elif (op == '*' or op == 'x'):
            result = num1 * num2
        elif (op == '/' or op == 'divide'):
            result = num1 / num2
        elif (op == '%' or op == 'remainder'):
            result = num1 % num2
        elif (op == '**' or op == 'exponent'):
            result = num1 ** num2
        elif (op == '//' or op == 'floor'):
            result = num1 // num2
        else: dropon = False
        
        if (dropon == False):
            embed = discord.Embed (description = '**Invalid Operator!**')
        elif (dropon == True): 
            embed = discord.Embed (description = f'**The result is:** {result}')

        await ctx.reply(embed = embed)

    @commands.command(aliases = ['mathr'], help = 'Rounds the math before calculating.')
    async def mathround(self, ctx, num1: int,  op, num2: int):
        # Arithmetic Operators
        dropon = True
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
        else: dropon = False
        
        if (dropon == False):
            embed = discord.Embed (description = '**Invalid Operator!**')
        elif (dropon == True): 
            embed = discord.Embed (description = f'**The result is:** {result}')

        await ctx.reply(embed = embed)

def setup(client):
    client.add_cog(Math(client))
