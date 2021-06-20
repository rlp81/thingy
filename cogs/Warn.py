import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from random import randint
import json
class Warn(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    @commands.command(name="Warn")
    @has_permissions(manage_channels=True)
    async def warn(self,context, member: discord.Member= None):
        if member == None:
            await context.send("You need to mention someone to warn!")
        if not member == None:
            def check(m):
                return m.author.id == context.author.id
            await context.send(f"What's the reason of warning, {member}?")
            msg = await self.client.wait_for('message', check=check)
            ID =randint(100,999)
            with open('.\\warnings.json', 'r') as f:
                warns = json.load(f)
            warns[str(member.id)]['Warnings'] += 1
            warns[str(member.id)][f'{ID}'] = msg.content
            with open('.\\warnings.json', 'w') as f:
                json.dump(warns,f,indent=4)
            with open('.\\warnings.json', 'r') as f:
                ifwarn = json.load(f)
            await context.send(f"Warned {member} with warning ID {ID} for {msg.content}")
            if ifwarn[str(member.id)][str('Warnings')] == 2:
                guild = context.guild
                mutedrole = discord.utils.get(guild.roles, name="Muted")
                if not mutedrole:
                    mutedrole = await guild.create_role(name="Muted")

                    for channel in guild.channels:
                        await channel.set_permissions(mutedrole, speak = False, send_messages = False)

                await member.add_roles(mutedrole)
                await context.send(f"I muted {member.mention} for 2 hours because they achieved 2 warnings.")
                await member.send(f"You were muted in {guild.name} because you achieved 2 warnings.")
                await asyncio.sleep(7200)
                await member.remove_roles(mutedrole)
            if ifwarn[str(member.id)][str('Warnings')] == 6:
                reason = f"{member} achieved 6 Warnings"
                await context.send(f"{member} was banned because they had 6 warns.")
                embed = discord.Embed(title="Ban Notice", description=f"You have been banned because you achieved 6 warnings.")
                await member.send(embed=embed)
                await member.ban(reason=reason)
            if ifwarn[str(member.id)][str('Warnings')] == 3:
                reason = f"{member} achieved 3 Warnings"
                await context.send(f"{member} was kicked because they had 3 warns.")
                embed = discord.Embed(title="Kick Notice", description=f"You have been kicked because you achieved 3 warnings. Rejoin the [server](https://discord.gg/jmD7bYzadB) if you wish.")
                await member.send(embed=embed)
                await member.kick(reason=reason)


def setup(client):
    client.add_cog(Warn(client))