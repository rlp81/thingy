import discord
from discord.ext import commands
import wolframalpha
AI_Client = wolframalpha.Client('E3E6YA-HRHT55JG9J')
AI_Client2 = wolframalpha.Client('E3E6YA-8UHT84A2WA')
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