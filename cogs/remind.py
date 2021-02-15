import discord
from discord.ext import commands
from asyncio import sleep as s 

class Remind(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['REMIND','Remind'])
  async def remind(self,ctx,time: int,hsr=None,*,msg):
    if hsr == None:
      await ctx.send('along with the reminder in the end even type s for seconds r m for minutes or h for hours')

    if hsr.lower() == 'h' or hsr.lower() == 'hour' or hsr.lower() == 'hours' or hsr.lower() == 'hrs' or hsr.lower() == 'hr':
      await ctx.send(f'Reminder set for {msg}')
      await s(3600*time)
      await ctx.author.send(f'{msg},{ctx.author.mention}')
      await ctx.send(f'{msg},{ctx.author.mention}')
    if hsr.lower() == 'm' or hsr.lower() == 'minutes' or hsr.lower() == 'minute' or hsr.lower() == 'mins' or hsr.lower() == 'min':
      await ctx.send(f'Reminder set for {msg}')
      await s(60*time)
      await ctx.author.send(f'{msg},{ctx.author.mention}')
      await ctx.send(f'{msg},{ctx.author.mention}')
    if hsr.lower() == 's' or hsr.lower() == 'second' or hsr.lower() == 'seconds' or hsr.lower() == 'sec' or hsr.lower() == 'secs':
      await ctx.send(f'Reminder set for {msg}')
      await s(time)
      await ctx.author.send(f'{msg},{ctx.author.mention}')
      await ctx.send(f'{msg},{ctx.author.mention}')

def setup(client):
  client.add_cog(Remind(client))