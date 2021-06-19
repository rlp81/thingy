import discord
from discord.ext import commands
import wolframalpha
AI_Client = wolframalpha.Client('apiid')
class Ques(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    @commands.command(name="Ques")
    async def Ques(self, context, message):
        res = AI_Client.query(message)
        answer = next(res.results).text
        await context.send(answer)
def setup(client):
    client.add_cog(Ques(client))
