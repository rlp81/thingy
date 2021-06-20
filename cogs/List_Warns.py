import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from random import randint
import json
class List_Warns(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    @commands.command(name="List_Warns")
    @has_permissions(manage_channels=True)
    async def List_Warns(self,context, member: discord.Member= None):
        if member == None:
            await context.send("You need to mention someone to warn!")
        if not member == None:
            embed = discord.Embed(title=f"{member.display_name}'s warnings")
            with open(".\\warnings.json", "r") as f:
                warns = json.load(f)
            list = warns[str(member.id)]
            for key, value in list.items():
                if key == "Warnings":
                    embed.add_field(name=key, value=value, inline=False)
                if not key == "Warnings":
                    embed.add_field(name=key, value=f"ID: {key}, Reason: {warns[str(member.id)][str(key)]}", inline=False)
            await context.send(embed=embed)


def setup(client):
    client.add_cog(List_Warns(client))