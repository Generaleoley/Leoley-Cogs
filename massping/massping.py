import os
import asyncio
import discord
from discord.ext import commands

class massping:

    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def massping(self, ctx, member: discord.Member=None,):
        author = ctx.message.author
        await self.bot.say("Get Rekt {}".format(author))
        print ("1 complete")
        await self.bot.say("GET REKT {}".format(member))

def setup(bot):
    bot.add.cog(massping(bot))

