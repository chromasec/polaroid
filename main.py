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

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0', 'Content-Type': 'application/json', 'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9', 'Authorization': token, 'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==', 'X-Discord-Locale': 'en-US', 'Origin': 'https://discord.com', 'Connection': 'keep-alive', 'Referer': 'https://discord.com', 'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',}
polaroid = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), self_bot=1); chroma = polaroid; nazareth = chroma
polaroid2 = httpx.Client(); chroma2 = polaroid2; nazareth2 = chroma2

@polaroid.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored)
    print(f"                                                                      (+) Username - {C.LIGHTBLACK_EX}{polaroid.user.name}{C.RESET} [{C.LIGHTBLACK_EX}{polaroid.user.id}{C.RESET}]")
    print(f"                                                                      {C.LIGHTBLACK_EX}chromasec{C.RESET} or {C.LIGHTBLACK_EX}yugokash{C.RESET} on discord for support")

@polaroid.event
async def on_message(message):
    if message.content.startswith(prefix):
        await polaroid.process_commands(message)  # we need ts to keep cmds working apparently so yea
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

# do note that discord heavily ratelimits gc endpoints! so do stick to 1-10 gcs <3
@nazareth.command()
async def gcspam(ctx, num: int, target: discord.User, *, msg: str):
    penis = {"recipients": [str(nazareth.user.id), str(target.id)]}
    penis2 = {"name": msg}
    for i in range(num):
        pussy = nazareth2.post("https://discord.com/api/v9/users/@me/channels", headers=headers, json=penis)
        if pussy.status_code == 200: jizz = pussy.json(); jizz2 = jizz["id"]; nazareth2.patch(f"https://discord.com/api/v9/channels/{jizz2}", headers=headers, json=penis2)

@chroma.command(name="cat")
async def cat(ctx):
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.thecatapi.com/v1/images/search')
        data = response.json()
        funy = data[0]['url']
        await ctx.send(funy)

polaroid.run(token, bot=0)
