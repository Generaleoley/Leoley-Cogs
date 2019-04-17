import os
import asyncio
import discord
from discord.ext import commands

class massping:

    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def massping(self, ctx, count: int, member: discord.Member=None,):
        author = ctx.message.author
        await self.bot.say("GET REKT {}".format(mention.member))

def setup(bot):
    bot.add_cog(massping(bot))

