import discord
import os
from .utils.dataIO import fileIO, dataIO
from discord.ext import commands
import random
import asyncio
import clashroyale
import io
import json
from cogs.utils import checks

footinfo = "Bot by Generaleoley | eSports"

tags_path = "data/crtools/tags.json"
clans_path = "data/crtools/clans.json"

tags_bs_path = "data/crtools/tags_bs.json"
clubs_path = "data/crtools/clubs.json"

auth_path = "data/crtools/auth.json"
constants_path = "data/crtools/constants.json"

class tags:
    """Tags Management, borrowed from GR8"""

    def __init__(self):
        self.tags = dataIO.load_json(tags_path)

    async def verifyTag(self, tag):
        """Check if a player/can tag is valid"""
        check = ['P', 'Y', 'L', 'Q', 'G', 'R', 'J', 'C', 'U', 'V', '0', '2', '8', '9']

        if any(i not in check for i in tag):
            return False
        else:
            return True

    async def formatTag(self, tag):
        """Sanitize and format CR Tag"""
        return tag.strip('#').upper().replace('O', '0')
        return True

    async def formatName(self, name):
        """Sanitize player Name"""
        p = re.sub(r'<c\d>(.*)<\/c>', r'\1', name)
        return p or name

    async def linkTagCR(self, tag, userID):
        """Link a CR player tag to a discord User"""
        tag = await self.formatTag(tag)

        self.tags.update({userID: {'tag': tag}})
        dataIO.save_json(tags_path, self.tags)

    async def unlinkTagCR(self, userID):
        """Unlink a CR player tag to a discord User"""
        if self.tags.pop(str(userID), None):
            dataIO.save_json(tags_path, self.tags)
            return True
        return False

    async def getTagCR(self, userID):
        """Get a user's CR Tag"""
        return self.tags[userID]['tag']

    async def getUserCR(self, serverUsers, tag):
        """Get User from CR Tag"""
        for user in serverUsers:
            if user.id in self.tags:
                player_tag = self.tags[user.id]['tag']
                if player_tag == await self.formatTag(tag):
                    return user
        return None

class auth:
    """RoyaleAPI key management"""

    def __init__(self):
        self.auth = dataIO.load_json(auth_path)

    async def addToken(self, key):
        """Add a RoyaleAPI Token"""
        self.auth['RoyaleAPI'] = key
        dataIO.save_json(auth_path, self.auth)

    async def addTokenOfficial(self, key):
        """Add a api.clashroyal.com Token"""
        self.auth['OfficialAPI'] = key
        dataIO.save_json(auth_path, self.auth)

    def getToken(self):
        """Get RoyaleAPI Token"""
        return self.auth['RoyaleAPI']

    def getOfficialToken(self):
        """Get OfficialAPI Token"""
        return self.auth['OfficialAPI']
 

class royalerumble:
    """Bot for Royale Rumble Tournament"""

    def __init__(self, bot):
        self.bot = bot
        self.auth = self.bot.get_cog('crtools').auth
        self.clans = self.bot.get_cog('crtools').clans
        self.clash = clashroyale.OfficialAPI(self.auth.getOfficialToken(), is_async=True)

    #async def addMember ()    
        
    @commands.command(pass_context=True, no_pm=True, aliases=["reg"])
    async def register(self, ctx, series: int):
        """Registers the user for Royale Rumble, for the series number please contact a staff member."""
        if series != None:
            if series == 2:
                try:
                    author = ctx.message.author
                    profiletag = await self.tags.getTagCR(author.id)
                    profiledata = await self.clash.get_player(profiletag)
                    trophies = profiledata.trophies
                    cards = profiledata.cards
                    maxtrophies = profiledata.best_trophies
                    maxwins = profiledata.challenge_max_wins

                    if profiledata.clan is None:
                        await self.bot.say("You must be in a legend clan to register")
                    else:
                        clanname = profiledata.clan.name
                    
                    playerinfo = {
                                'Name' : author,
                                'Tag' : profiletag,
                                'Trophies' : trophies,
                                'Personal Best' : maxtrophies,
                                'Max Wins' : maxwins}
                    try:
                        infodict = json.dumps(playerinfo)
                        playersfile = open("dict.json","w")
                        playersfile.write(infodict)
                        playersfile.close()
                    except:
                        await self.bot.say("Error Saving Information, please report the bug in #report-bug")
                    
                    await self.bot.say("User registered")
                except clashroyale.RequestError:
                    return await self.bot.say("Error: cannot reach Clash Royale Servers. Please try again later.")
                except KeyError:
                    return await self.bot.say("You must associate a tag with this member first using ``{}save #tag @member``".format(ctx.prefix))
            else:
                await self.bot.say("Invalid Series Number, please contact a staff member")
        else:
            await self.bot.say("Please enter a seires number, if in doubt, please contact a staff member")

    def createuser(user):
        
            
def setup(bot):
    bot.add_cog(royalerumble(bot))
