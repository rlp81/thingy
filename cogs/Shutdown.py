import discord
from discord.ext import commands
import json
with open('.\\config.json', 'r') as f:
    own = json.load(f)
ownerid =own["owner_ID"]
class shutdown(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="Shutdown")
    async def shutdown(self, context):
        if context.author.id == int(ownerid):
            client = self.client
            await context.send("Shutting down..")
            await client.change_presence(status=discord.Status.offline)
            await client.close()
        if not context.author.id == int(ownerid):
            await context.send("You must be Coal to run this command.")
    
def setup(client):
    client.add_cog(shutdown(client))