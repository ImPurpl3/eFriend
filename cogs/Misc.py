import discord
import random

from discord.ext import commands
from discord.ext.commands import Bot

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Misc(bot))