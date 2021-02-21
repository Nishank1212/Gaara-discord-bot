import discord
from discord.ext import commands

class eightball(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['CLEAR','Clear'])
  @commands.has_permissions(manage_messages=True)
  async def clear(self,ctx, amount : int):
    await ctx.channel.purge(limit= amount+1)


  @commands.command(aliases=['Kick','KICK'])
  @commands.has_permissions(kick_members=True)
  async def kick(self,ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'lol {member.mention} just got kicked')


  @commands.command(aliases=['BAN','Ban'])
  @commands.has_permissions(ban_members=True)
  async def ban(self,ctx,member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'lol {member.mention} just got banned')


  @commands.command(aliases=['UNBAN','Unban'])
  @commands.has_permissions(ban_members=True)
  async def unban(self,ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user

      if(user.name,user.discriminator) == (member_name,member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(user + ' has been unbanned')
        return

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def mute(self,ctx,member:discord.Member):
    muted_role = ctx.guild.get_role(812650737150197770)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + ' Has been muted lol')

def setup(client):
  client.add_cog(eightball(client))    