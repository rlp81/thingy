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
    
def setup(client):
    client.add_cog(on_message(client))