import discord
from discord.ext import commands
import random
import asyncio

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "test light command")
    async def testlight(self, ctx):
        print(f"rgb placeholder :)")
        await ctx.send(f"Lights would be modified, if this wasn't running on the wrong device.")



def setup(bot):
    bot.add_cog(Fun(bot))