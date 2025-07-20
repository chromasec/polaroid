# -*- coding: utf-8 -*-

"""
come with me, Alice, let me show you how deep the rabit-hole goes.
"""

import discord; from discord.ext import commands; import random; from itertools import cycle; from colorama import Fore as C; import os
import asyncio; import httpx; from tasksio import TaskPool; import string; import nest_asyncio; from pystyle import Colorate, Colors, Center
nest_asyncio.apply()

# ascii generator made by kristan p thanks kristan!
def asciigen(length):
    asc = ""
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc

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
polaroid = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), self_bot=1, help_command=None); chroma = polaroid; nazareth = chroma
polaroid2 = httpx.Client(); chroma2 = polaroid2; nazareth2 = chroma2

help1 = f"""
```ansi
[1;37m[ [1;36mPolaroid SB [1;37m| [1;36mCommands [1;37m]
[1;37m{prefix}[1;34mutilityc [number (not required)]
[1;37m{prefix}[1;35mfunc [number (not required)]
[1;37m{prefix}[1;33mraidc [number (not required)]
```"""
help2 = f"""
```ansi
[1;37m[ [1;34mPolaroid SB [1;37m| [1;34mUtility Commands [1;37m]
[1;37m{prefix}[1;34mpurge/clear/clean [number (not required)]
[1;37m{prefix}[1;34mdmscrape/dmsave/ds
[1;37m{prefix}[1;34mmemscrape
[1;37m{prefix}[1;34serverinfo
[1;37m{prefix}[1;34userinfo [mention]
[1;37m{prefix}[1;34avatar [mention]
[1;37m{prefix}[1;34mhypesquad [house]
```"""
help3 = f"""
```ansi
[1;37m[ [1;35mPolaroid SB [1;37m| [1;35mFun Commands [1;37m]
[1;37m{prefix}[1;35mgif [query]
[1;37m{prefix}[1;35mnsfw
[1;37m{prefix}[1;35mcat
[1;37m{prefix}[1;35m8ball [question]
[1;37m{prefix}[1;35mroulette
```"""
help4 = f"""
```ansi
[1;37m[ [1;33mPolaroid SB [1;37m| [1;33mRaid Commands [1;37m]
[1;37m{prefix}[1;33mspam [delay] [number] [message]
[1;37m{prefix}[1;33mgcspam [number] [@target] [name]
[1;37m{prefix}[1;33mlagchat [number]
[1;37m{prefix}[1;33mnuke
[1;37m{prefix}[1;33mdelwh [webhook]
[1;37m{prefix}[1;33mwhspam [webhook] [number] [message]
```"""

@polaroid.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored)
    print(f"                                    (+) Username - {C.LIGHTBLACK_EX}{polaroid.user.name}{C.RESET} [{C.LIGHTBLACK_EX}{polaroid.user.id}{C.RESET}]")
    print(f"                                    {C.LIGHTBLACK_EX}chromasec{C.RESET} or {C.LIGHTBLACK_EX}yugokash{C.RESET} on discord for support")

@polaroid.event
async def on_message(message):
    if message.content.startswith(prefix):
        await message.delete()
        await polaroid.process_commands(message)

@nazareth.command(aliases=["clear", "clean"])
async def purge(ctx, num: int = None):
    await ctx.message.delete()
    if num == None:
        num = None
    async for message in ctx.channel.history(limit=num):
        if message.author == ctx.author:
            try:
                asyncio.create_task(message.delete())
            except:
                await asyncio.sleep(5)

@chroma.command(name="spam") # this is an ugly way to spam, PLEASE HELP NAZ!!!!!!
async def spam(ctx, delay: float, count: int, *, message: str):
    for i in range(count):
        await ctx.send(message)
        await asyncio.sleep(delay)

@chroma.command()
async def stop(ctx):
    await print("shut down has been requested! goodbye world.....") 
    await chroma.close()

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

@chroma.command()
async def ping(ctx):
    msg = await ctx.send("Pinging...")
    latency = round((msg.created_at - ctx.message.created_at).total_seconds() * 1000)
    await msg.edit(content=f"Pong! Latency: `{latency}ms`")


# do note that discord heavily ratelimits gc endpoints! so do stick to 1-10 gcs <3
@nazareth.command()
async def gcspam(ctx, num: int, target: discord.User, *, msg: str):
    penis = {"recipients": [str(nazareth.user.id), str(target.id)]}
    penis2 = {"name": msg}
    for i in range(num):
        async with httpx.AsyncClient() as nazareth3:
            async def gcsex():
                pussy = await nazareth3.post("https://discord.com/api/v9/users/@me/channels", headers=headers, json=penis)
                if pussy.status_code == 200: jizz = pussy.json(); jizz2 = jizz["id"]; await nazareth3.patch(f"https://discord.com/api/v9/channels/{jizz2}", headers=headers, json=penis2)
            await asyncio.gather(*[gcsex() for i in range(num)])

@chroma.command(name="cat")
async def cat(ctx):
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.thecatapi.com/v1/images/search')
        data = response.json()
        funy = data[0]['url']
        await ctx.send(funy)

@nazareth.command()
async def lagchat(ctx, num: int):
    penis = {"content": asciigen(1000)}
    async def chatlag():
        async with httpx.AsyncClient() as nazareth3:
            await nazareth3.post(f"https://discord.com/api/v9/channels/{ctx.channel.id}/messages", headers=headers, json=penis)
    await asyncio.gather(*[chatlag() for i in range(num)])

@nazareth.command()
async def gif(ctx, query: str):
    key = "ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34" # dont remove
    vagina = nazareth2.get(f"https://api.giphy.com/v1/gifs/search?api_key={key}&q={query}&limit=25&offset=0&rating=X&lang=en")
    penis = vagina.json(); sperm = random.choice(penis["data"])["images"]["original"]["url"]; await ctx.send(sperm)

@nazareth.command()
async def nsfw(ctx):
    categories = ["waifu", "neko", "trap", "blowjob"]
    vagina = nazareth2.get(f"https://api.waifu.pics/nsfw/{random.choice(categories)}")
    penis = vagina.json(); sperm = penis["url"]; await ctx.send(sperm)

@nazareth.command(name="8ball")
async def _8ball(ctx, question: str):
    responses = [
    "Yes, definitely.","Without a doubt.", "Absolutely.",
    "Signs point to yes.", "Most likely.", "Ask again later.",
    "Cannot predict now.", "Better not tell you now.", "Don't count on it.",
    "My sources say no.", "Very doubtful.", "Absolutely not."]; await ctx.reply(random.choice(responses))

@nazareth.command()
async def roulette(ctx, chamber: int):
    bullet = random.randint(1, 6)
    if chamber == bullet: await ctx.reply("*You pull the trigger, everything goes black. You died.*")
    else: await ctx.reply("*You pull the trigger, nothing happens. You survived.*")

@nazareth.command()
async def help(ctx, time: int = None):
    if time: await ctx.send(help1, delete_after=time)
    else: await ctx.send(help1)

@nazareth.command()
async def utilityc(ctx, time: int = None):
    if time: await ctx.send(help2, delete_after=time)
    else: await ctx.send(help2)

@nazareth.command()
async def func(ctx, time: int = None):
    if time: await ctx.send(help3, delete_after=time)
    else: await ctx.send(help3)

@nazareth.command()
async def raidc(ctx, time: int = None):
    if time: await ctx.send(help4, delete_after=time)
    else: await ctx.send(help4)

@chroma.command()
async def serverinfo(ctx):
    guild = ctx.guild
    text_channels = len(guild.text_channels)
    voice_channels = len(guild.voice_channels)
    members = guild.member_count
    owner = guild.owner
    created = guild.created_at.strftime("%Y-%m-%d %H:%M:%S")

    info = (
        f"**Server Name:** {guild.name}\n"
        f"**Server ID:** {guild.id}\n"
        f"**Owner:** {owner}\n"
        f"**Members:** {members}\n"
        f"**Text Channels:** {text_channels}\n"
        f"**Voice Channels:** {voice_channels}\n"
        f"**Created On:** {created}"
    )
    await ctx.send(info)

@chroma.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    joined = member.joined_at.strftime("%Y-%m-%d %H:%M:%S") if member.joined_at else "Unknown"
    created = member.created_at.strftime("%Y-%m-%d %H:%M:%S")

    info = (
        f"**User:** {member} (ID: {member.id})\n"
        f"**Display Name:** {member.display_name}\n"
        f"**Account Created:** {created}\n"
        f"**Joined Server:** {joined}\n"
        f"**Top Role:** {member.top_role}\n"
        f"**Bot:** {member.bot}"
    )
    await ctx.send(info)

@chroma.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(f"{member}'s avatar URL:\n{member.avatar.url}")

@nazareth.command()
async def hypesquad(ctx, house: str):
    houses = {'bravery':1,'brilliance':2,'balance':3}
    if house in houses: 
        async with httpx.AsyncClient() as nazareth3: await nazareth3.post('https://discord.com/api/v9/hypesquad/online', headers=headers, json={'house_id': houses[house]}); await ctx.send(f"`#Polaroid : Hypesquad house changed to {house}.`")

@nazareth.command()
async def delwh(ctx, whurl: str):
    await ctx.message.delete()
    async with httpx.AsyncClient() as nazareth3:
        await nazareth3.delete(whurl); await ctx.send("`#Polaroid : Webhook deleted.`")

@nazareth.command()
async def whspam(ctx, whurl: str, num: int, *, message):
    await ctx.message.delete()
    async with httpx.AsyncClient() as nazareth3:
        await ctx.send("`#Polaroid : Spamming webhook.`")
        for i in range(num): await nazareth3.post(whurl, json={"content": message})

@nazareth.command()
async def spam2(ctx, num: int, message: str):
    penis = {"content": message}
    async with httpx.AsyncClient() as nazareth3:
        async def msgsex():
            await nazareth3.post(f"https://discord.com/api/v9/channels/{ctx.channel.id}/messages", headers=headers, json=penis)
        await asyncio.gather(*[msgsex() for _i in range(num)])

## NUKE SOON ##

polaroid.run(token, bot=0)
