import os
import asyncio
import discord
from discord.ext import commands

loop = True

class massping:


    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def massping(self, ctx, count: int, member: discord.Member=None,):
        "Pings a user the "Count" amount of times.
        author = ctx.message.author

        while loop == True:
            await self.bot.say("GET REKT {}".format(member.mention))
        else:
            print ("exit")

def setup(bot):
    bot.add_cog(massping(bot))


