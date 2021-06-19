import discord
import os
from discord.ext import commands

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
    print(f"{client.user} is ready.")
    channel = client.get_channel(852602739090784330)
    for filename in os.listdir('./cogs'):
        if not filename == "template.py":
            if filename.endswith('.py'):
                try:
                    client.load_extension(f'cogs.{filename[:-3]}')
                    print(f'cogs.{filename[:-3]} loaded successfully')
                    botinfo.startmes += f"cogs.{filename[:-3]} loaded successfully \n"
                except:
                    print(f'cogs.{filename[:-3]} failed to load.')
                    botinfo.startmes += f"cogs.{filename[:-3]} failed to load \n"
    await channel.send(botinfo.startmes)

client.run("ODM3OTEzNDEzMTQwNzQyMTQ0.YIzdrQ.vHXjlRsoCwR60cV-X8tD9saa5Ns")