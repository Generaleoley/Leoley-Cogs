import discord
import os
from .utils.dataIO import fileIO
from discord.ext import commands
import random
import asyncio
import clashroyale
import io

footinfo = "Bot by Generaleoley | eSports"

class royalerumble:
    """Bot for Royale Rumble Tournament"""

    def __init__(self, bot):
        self.bot = bot
        self.auth = self.bot.get_cog('crtools').auth
        self.clans = self.bot.get_cog('crtools').clans
        self.clash = clashroyale.OfficialAPI(self.auth.getOfficialToken(), is_async=True)

    @commands.command(pass_context=True, no_pm=True, aliases=["reg"])
    def register(self, ctx, series: int):
        """Registers the user for Royale Rumble, for the series number please contact a staff member."""
        if series != None:
            if series != 2:
                await self.bot.say("User registered")
            else:
                await self.bot.say("Invalid Series Number, please contact a staff member")
        else:
            await self.bot.say("Please enter a seires number, if in doubt, please contact a staff member")


def setup(bot):
    bot.add_cog(royalerumble(bot))
