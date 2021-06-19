import discord
from discord.ext import commands

class shutdown(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="Shutdown")
    async def shutdown(self, context):
        client = self.client
        await context.send("Shutting down..")
        await client.change_presence(status=discord.Status.offline)
        await client.close()
    
def setup(client):
    client.add_cog(shutdown(client))