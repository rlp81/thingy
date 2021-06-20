import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from random import randint
import json
class Remove_Warn(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    @commands.command(name="Remove_Warn")
    @has_permissions(manage_channels=True)
    async def Remove_Warn(self,context, member: discord.Member= None,number = None):
        if member == None:
            await context.send("You need to mention someone to warn!")
        if not member == None:
            if number == None:
                await context.send("You need to give a warning ID!")
            if not number == None:
                with open('.\\warnings.json', 'r') as f:
                    warns = json.load(f)
                if f"{number}" in warns[str(member.id)]:
                    warns[str(member.id)]['Warnings'] -= 1
                    warns[str(member.id)].pop(f"{int(number)}")
                    with open('.\\warnings.json', 'w') as f:
                        json.dump(warns,f,indent=4)
                    await context.send(f"Successfully removed warning {number} from {member.display_name}.")
                if not f"{number}" in warns[str(member.id)]:
                    await context.send(f"Warning ID {number} does not exist!")


def setup(client):
    client.add_cog(Remove_Warn(client))