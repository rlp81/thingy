import discord
from discord.ext import commands

class ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="Ping")
    async def ping(self, context):
        pong = self.client.latency
        pong = int(pong*1000)
        await context.send(f"My ping is {round(pong)}ms")
    
def setup(client):
    client.add_cog(ping(client))