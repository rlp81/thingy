import discord
from discord.ext import commands
import wolframalpha
import json
with open("..\\config.json", "r") as f:
    conf = json.load(f)
ID = conf["Wolframalpha_API_ID"]
AI_Client = wolframalpha.Client(ID)
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
