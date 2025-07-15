# -*- coding: utf-8 -*-

"""
come with me alice, let me show you how deep the rabbit hole goes.
"""

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
async def on_ready():
    print(colored)
    print(f"(+) Username - {C.LIGHTBLACK_EX}{polaroid.user.name}{C.RESET} [{C.LIGHTBLACK_EX}{polaroid.user.id}{C.RESET}]")
    print(f"{C.LIGHTBLACK_EX}chromasec{C.RESET} or {C.LIGHTBLACK_EX}yugokash{C.RESET} on discord for support")

@polaroid.event
async def on_message(message):
    if message.content.startswith(prefix):
        await polaroid.process_commands(message)  # we need ts to keep cmds working apparently so yea
        await asyncio.sleep(3) 
        await message.delete()



@chroma.command(name="quickpurge")
async def quickpurge(ctx, amount: int, delay: float):
    if ctx.author == polaroid.user:
        await ctx.channel.purge(limit=amount, check=lambda m: m.author == polaroid.user, bulk=True, delay=delay)

@chroma.command(name="advancedpurge")
async def advancedpurge(ctx, amount: int, delay: float):
    if ctx.author == polaroid.user:
        messages = await ctx.channel.history(limit=amount).flatten()
        user_messages = [m for m in messages if m.author == polaroid.user]
        for message in user_messages:
            await message.delete()
            await asyncio.sleep(delay)

@chroma.command(name="spam")
async def spam(ctx, message: str, count: int, delay: float): # ugly way to spam, but will do the job...
    for _ in range(count):
        await ctx.send(message)
        await asyncio.sleep(delay)

@nazareth.command(aliases=["dmsave", "ds"])
async def dmscrape(ctx):
    async for message in ctx.channel.history(limit=None, oldest_first=True): 
        print(f"[{C.LIGHTBLACK_EX}{message.author.name}{C.RESET}] {C.LIGHTBLACK_EX}{message.content}{C.RESET}"); 
        if message.attachments:
            print(Center.XCenter(f"[{C.LIGHTBLACK_EX}{message.author.name}{C.RESET}] {C.LIGHTBLACK_EX}{message.attachments[0].url}{C.RESET}"))

@nazareth.command(aliases=["mscrape", "ms"])
async def memscrape(ctx):
    users = set()
    async for message in ctx.channel.history(limit=1000):
        users.add(message.author.id)
    users = list(users)
    for user in users:
        print(Center.XCenter(user))

@chroma.command(name="cat")
async def cat(ctx):
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.thecatapi.com/v1/images/search')
        data = await response.json()
        funy = data[0]['url']
        await ctx.send(funy)

polaroid.run(token, bot=0)
