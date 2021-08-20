import discord
import asyncio
import os
import time
import re
import json

from datetime import datetime
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Member, Role

token_file = open('token.json')
token_data = json.load(token_file)

bot = commands.Bot(command_prefix = 'e!', case_insensitive=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="my python scripts - [e!]"))
    print('eFriend is Online!')
    time.sleep(1)
    botChannel = bot.get_channel(877846874453839882)
    botLog = bot.get_channel(878382115325116486)
    await botChannel.send('eFriend is Online!')
    embed = discord.Embed(
            title="eFriend Status",
            color=0x1c98c9,
            description="eFriend Is Online!",
            timestamp=datetime.utcnow())
    embed.set_thumbnail(url = 'https://share-cdn.picrew.me/shareImg/org/202108/947708_ZTToBXtF.png')
    embed.set_author(name = 'eFriend Log', icon_url = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/microsoft/74/robot-face_1f916.png')
    await botLog.send(embed = embed)

@bot.listen('on_message')
async def reloadreact(message):
    if message.content == 'eFriend is Online!': 
        await message.add_reaction('✅')
        await bot.process_commands(message)

with open('banned_terms.txt') as file:
    term_list = '|'.join(s for l in file for s in l.split(', '))
    term_checker = re.compile(term_list).search

@bot.listen('on_message')
async def on_message(message):
    if term_checker(message.content):
        termB = message.content
        await message.delete()
        print(f'term banned - from message: {termB}')

for filename in os.listdir('./cogs'):
    if filename.endswith('py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token_data["TOKEN"])