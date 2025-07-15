# -*- coding: utf-8 -*-
import discord; from discord.ext import commands; import random; from itertools import cycle; from colorama import Fore as C; import os
import asyncio; import httpx; from tasksio import TaskPool; import string; import nest_asyncio; from pystyle import Colorate, Colors, Center
nest_asyncio.apply()

ascii = Center.XCenter(r"""              ______                   ______________
_________________  /_____ ________________(_)_____  /
___  __ \  __ \_  /_  __ `/_  ___/  __ \_  /_  __  /
__  /_/ / /_/ /  / / /_/ /_  /   / /_/ /  / / /_/ /
_  .___/\____//_/  \__,_/ /_/    \____//_/  \__,_/
/_/                                                  """); colored = Colorate.Vertical(Colors.white_to_black, ascii)

print(colored)
token = input(Center.XCenter((f"{C.LIGHTBLACK_EX}Insert your token here..{C.RESET} ")))
prefix = ";"

polaroid = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), self_bot=1); chroma = polaroid; nazareth = chroma

@polaroid.event
async def on_message(message):
    if message.content.startswith(prefix):
        await message.delete()

@polaroid.command(name="purge")
async def purge(ctx, amount: int):
    if ctx.author == polaroid.user:
        await ctx.channel.purge(limit=amount)

polaroid.run(token, bot=0)
