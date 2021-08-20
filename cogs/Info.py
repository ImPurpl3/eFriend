import discord
import random

from discord.ext import commands
from discord.ext.commands import Bot

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['bot','binfo'], name = 'botinfo', help = '- Bot Info')
    async def botinfo(self, ctx):
        cogping = format(round(self.bot.latency * 1000))
        embed = discord.Embed(
            title="eFriend Info",
            color=0x7a81fa,
            description=f"Bot Made By: ImPurpl3\nMade with: discord.py\nVer: 1.0\nBot Server Location: US-EAST\nHosted By: Atlantic.net\nPing: {cogping}ms\nLines of Code: 114"
            )
        embed.set_thumbnail(url = 'https://share-cdn.picrew.me/shareImg/org/202108/947708_ZTToBXtF.png')
        embed.set_author(name = 'Bot Info', icon_url = 'https://emoji.gg/assets/emoji/3224_info.png')
        embed.set_footer(text="eFriend says hi!")
        await ctx.send(embed = embed)

    @commands.command(help = '- Pings the Discord servers and replys with a delay in ms.')
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command(aliases = ['serverinfo'], name = 'info', help = '- Basic Server Info')
    async def info(self, ctx):
        boostCount = ctx.guild.premium_subscription_count
        embed = discord.Embed(
            title="Our Server Info",
            color=0x7a81fa,
            description=f"Members: {ctx.guild.member_count}\nBots: 5\nMembers (Excluding Bots): {ctx.guild.member_count - 5}\nNumber of Boosts: {boostCount}\nBoosts Needed for Level 2: {15 - boostCount}\nBoosts Needed for Level 3: {30 - boostCount}"
            )
        embed.set_author(name = 'Server Info', icon_url = 'https://emoji.gg/assets/emoji/3224_info.png')
        embed.set_footer(text="Server Was Created On August 19, 2021")
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Info(bot))