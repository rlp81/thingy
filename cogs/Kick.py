import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
class kick(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    @commands.command(name="Kick")
    @has_permissions(kick_members=True)
    async def kick(self,context,*,member: discord.Member = None, reason = None):
        if member == None:
            await context.send("You need to mention someone to kick!")
        if not member == None:
            if reason == None:
                await context.send(f"You need a reason to kick {member}!")
            if not reason == None:
                client = self.client
                await member.kick(reason=reason)
                try:
                    embed = discord.Embed(title="Kick Notice", description=f"You have been kicked for {reason}, Rejoin the [server](https://discord.gg/jmD7bYzadB) if you wish.")
                    await member.send(embed=embed)
                except:
                    await context.send("User has their dms closed.")
                await context.send(f"{member} kicked successfully!")
        

def setup(client):
    client.add_cog(kick(client))