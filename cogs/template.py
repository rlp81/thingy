import discord
from discord.ext import commands

class template(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    

def setup(client):
    client.add_cog(template(client))
