import discord
from discord.ext import commands
import asyncio

class eightball(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['CLEAR','Clear'])
  @commands.has_permissions(manage_messages=True)
  async def clear(self,ctx, amount : int):
    await ctx.channel.purge(limit= amount+1)
    message = await ctx.send(f'{amount} messages deleted by Me on Command of {ctx.author.mention}')
    await asyncio.sleep(3)
    await message.delete()


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

  @commands.command(description="Mutes the specified user.")
  @commands.has_permissions(manage_messages=True)
  async def mute(self,ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.blue())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)

  @commands.command(description="Unmutes a specified user.")
  @commands.has_permissions(manage_messages=True)
  async def unmute(self,ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.blue())
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(eightball(client))    