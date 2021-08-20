import discord
import os
import sys
import importlib
import time

from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get

def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)

class Maintenance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True, hidden = True)
    @commands.has_role('Bot Owner') 
    async def addrole(self, ctx):
        member = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name='mod')
        await member.add_roles(role)
        await ctx.send('Role Added!')
    
    @commands.command(pass_context = True, hidden = True, aliases = ['reload','reloadall','restartall'])
    @commands.has_role('Bot Owner')
    async def restart(self, ctx):
        await ctx.send("Restarting... Allow up to 5 seconds")
        restart_program()

def setup(bot):
    bot.add_cog(Maintenance(bot))