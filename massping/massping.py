import os
import asyncio
import discord
from discord.ext import commands


class massping:
"""Lose yourself some friends"""

    def __init__(self,bot):
        self.bot = bot
    
    
    #commands.command(pass_context=True)
    #checks.admin_or_permissions(manage_roles=True)
    #sync def 
    
    
    
    @commands.command(pass_context=True, aliases = ["welovegeneral", "generaleoleyop", "generaleoleyluv", "mightygeneral"])
    @commands.cooldown(rate=1, per=172800, type=commands.BucketType.user)
    async def hailgeneraleoley(self, ctx):
        """Just do it!"""
        author = ctx.message.author
        await self.bot.say("As a reward for showing your respect towards the great mighty generaleoley, you have been awarded 100000 credits!")
        reward = int(100000)
        bank = self.bot.get_cog("Economy").bank
        bank.deposit_credits(author, reward)
    
    
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


