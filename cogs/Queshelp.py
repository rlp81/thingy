import discord
from discord.ext import commands

class Queshelp(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="Ques.help")
    async def Queshelp(self, context):
        embed = discord.Embed(title="Question command help")
        embed.description = "I am powered by Wolframalpha!\nGo [here](https://www.wolframalpha.com) for a list of what I can do!"
        await context.send(embed=embed)

def setup(client):
    client.add_cog(Queshelp(client))