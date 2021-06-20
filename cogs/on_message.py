import json
import discord
from discord.ext import commands
class on_message(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_message(self, message):
        if str(message.channel.type) == 'private':
            if not message.author == self.client.user:
                channel = self.client.get_channel(852602739090784330)
                await channel.send(f"**New ModMail!**\n{message.author}:{message.content}")
        with open('warnings.json', 'r') as f:
            warns = json.load(f)
        if not str(message.author.id) in warns:
            warns[message.author.id] = {}
            warns[message.author.id]['Warnings'] = 0
            with open('warnings.json', 'w') as f:
                json.dump(warns,f,indent=4)
def setup(client):
    client.add_cog(on_message(client))