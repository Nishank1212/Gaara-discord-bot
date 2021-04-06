import discord
from discord.ext import commands
import json

class Join(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['swm'])
  @commands.has_permissions(manage_messages=True)
  async def set_welcome_message(self,ctx,*,message):
    with open("welcome.json",'r') as f:
      welcome = json.load(f)

    try:
       a = welcome[str(ctx.guild.id)]
       del a

    except:
      pass

    welcome[str(ctx.guild.id)] = message


    
    with open('welcome.json','w') as f:
      json.dump(welcome,f)
    
    await ctx.send(f'Welcome message set to `{message}`')
    await ctx.send('Make sure to use the swc command to set the welcome channel and provide a channel id there')


  @commands.command(aliases=['swc'])
  @commands.has_permissions(manage_messages=True)
  async def set_welcome_channel(self,ctx,id:int):
    ids = []
    for i in ctx.guild.channels:
      ids.append(i.id)

    if id in ids:
      await ctx.send(f'Welcome Channel Set to <#{id}>!')
      await ctx.send('Make sure to use the swm command to set the welcome message like ~~swm <message>')


      with open("channel.json",'r') as f:
        channel = json.load(f)

      channel[str(ctx.guild.id)] = id

      with open("channel.json",'w') as f:
        json.dump(channel,f)

    else:
      await ctx.send('invalid id provided')

  @commands.command(aliases=['DW','diablewelcome'])
  async def welcomedisable(self,ctx):
    with open('welcome.json','r') as f:

      mod = json.load(f)

    with open('channel.json','r') as y:

      mod2 = json.load(y)

    try:
      del mod[str(ctx.guild.id)]
      del mod2[str(ctx.guild.id)]
      await ctx.send('Welcoming Disabled sucesfully...')

    except:
      await ctx.send('Welcoming was never on')



def setup(client):
  client.add_cog(Join(client))