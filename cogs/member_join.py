import discord
from discord.ext import commands
import json

class Join(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['swm','SWM','Swm'])
  @commands.has_permissions(administrator=True)
  async def set_welcome_message(self,ctx,*,message):
    with open("welcome.json",'r') as f:
      welcome = json.load(f)

    welcome[str(ctx.guild.id)] = message

    with open('welcome.json','w') as f:
      json.dump(welcome,f)
    
    await ctx.send(f'Welcome message set to `{message}`')


  @commands.command(aliases=['swc','SWC','Swc'])
  @commands.has_permissions(administrator=True)
  async def set_welcome_channel(self,ctx,id:int):
    ids = []
    for i in ctx.guild.channels:
      ids.append(i.id)

    if id in ids:
      await ctx.send(f'Welcome Channel Set to <#{id}>!')

      with open("channel.json",'r') as f:
        channel = json.load(f)

      channel[str(ctx.guild.id)] = id

      with open("channel.json",'w') as f:
        json.dump(channel,f)

    else:
      await ctx.send('invalid id provided')


def setup(client):
  client.add_cog(Join(client))