import discord
from discord.ext import commands

class Dm(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['DM','Dm'])
  async def dm(self,ctx,member:discord.Member=None,*, message = None):
    if member == None:
      await ctx.send('Pls Menton Who Should i DM')

    elif message == None:
      await ctx.send('What Should I Say???')

    else:
      await member.send(message)
      await ctx.channel.purge(limit= 1)
      await ctx.send('Message Sent Succesfully')



def setup(client):
  client.add_cog(Dm(client))    