import hmtai

from discord.ext import commands

class Akansfw(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # ZETTAI RYOUIKI - NSFW
    @commands.command(help = "(NSFW ONLY) Do I even need to explain?", aliases = ['thighhighs','thigh-highs','zr'])
    @commands.is_nsfw()
    async def zettairyouiki(self, ctx):
        await ctx.reply(hmtai.useHM("2_9","zetRyo"))
    
    # UNIFORM - NSFW
    @commands.command(help = "(NSFW ONLY) uniform time.")
    @commands.is_nsfw()
    async def nsfwuniform(self, ctx):
        await ctx.reply(hmtai.useHM("2_9","uniform"))
    
    # AHEGAO - NSFW
    @commands.command(help = "(NSFW ONLY)")
    @commands.is_nsfw()
    async def ahegao(self, ctx):
        await ctx.reply(hmtai.useHM("2_9","ahegao"))

    # GIF - NSFW
    @commands.command(help = "(NSFW ONLY) GIF images.", aliases = [''])
    @commands.is_nsfw()
    async def nsfwgif(self, ctx):
        await ctx.reply(hmtai.useHM("2_9","gif"))
    
    # DOUJIN - NSFW
    @commands.command(help = "(NSFW ONLY) Manga images.", aliases = ['doujinshi','nsfwmanga'])
    @commands.is_nsfw()
    async def doujin(self, ctx):
        await ctx.reply(hmtai.useHM("2_9","manga"))
    
    
    # JAHY - QUESTIONABLE
    @commands.command(help = "(NSFW ONLY) Jahy, Jahy, Jahy.")
    @commands.is_nsfw()
    async def jahy(self, ctx):
        await ctx.reply(hmtai.useHM("2_9","jahy"))

def setup(client):
    client.add_cog(Akansfw(client))