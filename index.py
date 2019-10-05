import discord
from discord.ext import commands
import datetime
import os
import json
import asyncio
from itertools import cycle

#client config

status = ["Prefix = '>>'", 'ArdanKR_#3402', '>>도움말', "접두사 = '>>'", 'ArdanKR_#3402', 'WolHaBOT']

client = commands.Bot(command_prefix = '>>')
client.remove_command('help')

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status, type=3))
        await asyncio.sleep(5)

#commands

@client.event
async def on_message(message):

    if message.content.startswith('>>리스트'):
        list = []
        for server in client.servers:
            list.append(server.name)
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name="__**봇이 접속해있는 서버 목록**__")
        embed.add_field(name='``서버 목록``', value="\n".join(list))
        

        await client.send_message(message.channel, embed=embed)

    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
