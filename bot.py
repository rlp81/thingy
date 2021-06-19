import discord
import os
from discord.ext import commands
import json
import time
curr_time = time.localtime()
curr_clock = time.strftime("%H:%M:%S", curr_time)
conf = ""
try:
    with open("config.json", "r") as f:
        conf = json.load(f)
except:
    print("ERROR: can not access config.json")
Token = conf[str("Token")]
Startup_Channel_ID = conf[str("Startup_channel_ID")]

client = commands.Bot(command_prefix="-", help_command=None)

@client.command()
async def load(context, extintion):
    try:
        client.load_extension(f'cogs.{extintion}')
        await context.send(f"cogs.{extintion} loaded sucessfully!")
    except:
        await context.send(f"cogs.{extintion} failed to load!")
class botinfo:
    startmes = ""
    def listcom(clist):
        for filename in os.listdir('./cogs'):
            if not filename == "template.py":
                if filename.endswith('.py'):
                    clist = clist +filename[:-3]
        return clist
@client.command()
async def unload(context, extintion):
    try:
        client.unload_extension(f'cogs.{extintion}')
        await context.send(f"cogs.{extintion} unloaded sucessfully!")
    except:
        await context.send(f"cogs.{extintion} failed to unload!")

@client.command()
async def reload(context, extintion):
    try:
        client.unload_extension(f'cogs.{extintion}')
        client.load_extension(f'cogs.{extintion}')
        await context.send(f"cogs.{extintion} reloaded sucessfully!")
    except:
        await context.send(f"cogs.{extintion} failed to reload!")


@client.event
async def on_ready():
    print("Start up initiated")
    time.sleep(2)
    print("Loading cogs..")
    time.sleep(4)
    channel = client.get_channel(int(Startup_Channel_ID))
    for filename in os.listdir('./cogs'):
        if not filename == "template.py":
            if filename.endswith('.py'):
                try:
                    client.load_extension(f'cogs.{filename[:-3]}')
                    print(f'cogs.{filename[:-3]} loaded successfully')
                    botinfo.startmes += f"cogs.{filename[:-3]} loaded successfully \n"
                    time.sleep(1)
                except:
                    print(f'cogs.{filename[:-3]} failed to load.')
                    botinfo.startmes += f"cogs.{filename[:-3]} failed to load \n"
                    time.sleep(1)
    await channel.send(botinfo.startmes)
    time.sleep(3)
    print(f"Started Up Finished\n---------------------------\n{curr_clock} | {client.user} is ready.\n---------------------------\n Token used: {Token}")

client.run(Token)
