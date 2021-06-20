import discord
from discord.ext import commands

class Git_Hub(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    @commands.command(name="Git_Hub")
    async def Git_Hub(self, context):
        await context.send("Check out my Git Hub repository [here](https://github.com/rlp81/thingy)!")

def setup(client):
    client.add_cog(Git_Hub(client))