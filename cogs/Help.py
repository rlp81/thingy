import discord
from discord.ext import commands
import os
def send(ctx,msg):
    ctx.send(msg)
class help(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(name="help", aliases=["Help"])
    async def help(self,context, message = None):
        emb= discord.Embed(title="Help command", description="Use -help {command} to get usage.")
        cmds = ""
        if message == None:
            for filename in os.listdir('.\\cogs'):
                if not filename == "template.py":
                    if filename.endswith('.py'):
                        if filename == "Queshelp.py":
                            filename = "Ques.help.py"
                        cmds +=f"{filename[:-3]}\n"
            emb.add_field(name="Commands", value=cmds, inline= False)
            await context.send(embed=emb)
        if not message == None:
            if message == "Ping":
                await context.send("-Ping, shows the bot's latency.")
            if message == "Ques":
                await context.send("-Ques, use -Ques.help for usage.")
            if message == "Kick":
                await context.send(f"-{message} @member <reason>")
            if message == "Ban":
                await context.send(f"-{message} @member <reason>")
            if message == "on_message":
                await context.send("This is an event you can not use it, but you can dm the bot to use an on_message function!")
            if message == "Shutdown":
                await context.send("-Shutdown, Shuts down the bot")
            if message == "Ques.help":
                await context.send("-Ques.help, shows usage for Ques.")
            if message == "List_Warns":
                await context.send("-List_Warns @member, shows warns for a member.")
            if message == "Remove_Warn":
                await context.send("-Remove_Warn @member <ID>, removes warn from a member.")
            if message == "Warn":
                await context.send("-Warn @member, warns a member.")
            if message == "Git_Hub":
                await context.send("Shows Thingy's GitHub repository.")
        

def setup(client):
    client.add_cog(help(client))
