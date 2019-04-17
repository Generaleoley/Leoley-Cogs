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
        await self.bot.say("GET REKT {}".format(user))


def setup(bot):
    bot.add.cog(massping(bot))
