import os
import asyncio
import discord
from discord.ext import commands
from __main__ import send_cmd_help

loop = True


class massping:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def massping(self, ctx, user: str, count: int):
        server = ctx.message.server
        host = ctx.message.author
    while loop == True:
      await.bot.say("GET REKT {}".format(user))
       ''' if loop > 200:
            await self.bot.say ("Stupid kid... trying to mass ping someone over 200 times... well if you think you are SOOOOO clever... you're wrong...")

        if user == host:
            await self.bot.say("You're stupid, don't mass ping yourself")


        if user == self.bot.user.id:
            await self.bot.say ("WTF {}!!! DON'T MASS PING ME.".format(host))


        while loop < count:
            await self.bot.say("HAPPY APRIL FOOLS! {} ".format(user))
            loop = loop + 1
        else:
            await self.bot.say ("{} Did you enjoy pinging {}, {} times?".format(host.mention, user, count)'''

def setup(bot):
    bot.add.cog(massping(bot))
