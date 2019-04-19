import os
import asyncio
import discord
from discord.ext import commands


class massping:


    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases = ["mping"])
    async def massping(self, ctx, message: str, count: int, member: discord.Member=None,):
        author = ctx.message.author
        mloop = 0
        int(count)
        int(mloop)
        while mloop < count:
            await self.bot.say("{} {}".format(message, member.mention))
            int (mloop)
            mloop = mloop + 1
        else:
            await self.bot.say("Completed")
            

def setup(bot):
    bot.add_cog(massping(bot))


