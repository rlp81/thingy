import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
class ban(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(name="Ban")
    @has_permissions(ban_members=True)
    async def ban(self,context,member: discord.Member = None,*, message = None):
        if member == None:
            await context.send("You need to mention someone to ban!")
        if not member == None:
            if message == None:
                await context.send(f"You need a reason to ban {member}!")
            if not message == None:
                await member.ban(reason=message)
                try:
                    embed = discord.Embed(title="Ban Notice", description=f"You have been banned for {message}")
                    await member.send(embed=embed)
                except:
                    await context.send("User has their dms closed.")
                await context.send(f"{member} kicked successfully!")

def setup(client):
    client.add_cog(ban(client))