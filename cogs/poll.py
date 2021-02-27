import discord
from discord.ext import commands

class Poll(commands.Cog):
  def __init__(self,client):
    self.client=client

  # @commands.command(aliases=['POLL','Poll'])
  # async def poll(self,ctx):
  #   await ctx.send('What is The qestion you want?(note:there will be only 4 options)')

  #   def check()

    # msg1 = await ctx.wait_for('message',check=check)

def setup(client):
  client.add_cog(Poll(client))