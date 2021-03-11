import discord
from discord.ext import commands


class Roles(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  @commands.has_permissions(kick_members = True)
  async def addrole(self,ctx,member:discord.Member,role:discord.Role,*, reason=None):
    # if role in ctx.guild.roles():
    await member.add_roles(role, reason=reason)
    embed=discord.Embed(title='Added Role',description=f'{role} role was added to {member.mention} by {ctx.author.mention} for {reason}',colour=discord.Colour.blue())
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def unrole(self,ctx,member:discord.Member,role:discord.Role,*, reason=None):
    await member.remove_roles(role,reason=reason) 
    embed=discord.Embed(title='Removed Role',description=f'{role} role was removed from {member.mention} by {ctx.author.mention} for {reason}',colour=discord.Colour.blue())
    await ctx.send(embed=embed)


# # #  wait i already did it it is working also check discord

  
def setup(client):
  client.add_cog(Roles(client))