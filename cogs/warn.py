from os import getenv
import discord
from discord.ext import commands
from pymongo import MongoClient
import asyncio
cluster = MongoClient(getenv("WARN_PASS")) # Don't include "<" and ">" fill in those with your credentials
collection = cluster.warning.warning

class Warn(commands.Cog):
  def __init__(self,client):
    self.client = client


  @commands.command(aliases=['WARN','Warn'])
  @commands.has_permissions(ban_members=True)
  async def warn(self,ctx,member:discord.Member=None):
    

    if member == None:
      await ctx.send('Who should I warn?')
      return

    bankinfo = collection.find_one({"guild":ctx.guild.id,"member": member.id})

    if member.top_role > ctx.author.top_role:
      await ctx.send('You cant warn someone higher than you')

    elif member.id == ctx.author.id:
      await ctx.send('You cannot warn yourself')

    elif member.bot:
      await ctx.send('No use warning bot man!')

    elif not bankinfo:
      collection.insert_one({"guild":ctx.guild.id,"member":member.id,"warns":1})
      message = await ctx.send(f'Warning {member.mention}...')
      await asyncio.sleep(2)
      await message.edit(content=f'Warned {member.mention}, now has 1 warn')

    else:
      if bankinfo['warns'] >= 4:
        await member.ban(reason='Warn limit exceeded')
        await ctx.send(f'{member.mention} got banned for exceeding warn limits lol')
        collection.remove({"guild":bankinfo['guild'],"member":bankinfo['member']})

      else:
        bankinfo['warns'] += 1

        message = await ctx.send(f'Warning {member.mention}...')
        await asyncio.sleep(2)
        await message.edit(content=f'Warned {member.mention} ,now has {bankinfo["warns"]} warns')


        collection.replace_one({"guild":bankinfo['guild'],"member":bankinfo['member']},{"guild":bankinfo['guild'],"member":bankinfo['member'],"warns":bankinfo['warns']})

  @commands.command()
  async def case(self,ctx,member:discord.Member=None):
    

    if member == None:
      member = ctx.author

    bankinfo = collection.find_one({"guild":ctx.guild.id,"member": member.id})

    if not bankinfo:
      await ctx.send('No Data Found')

    else:
      await ctx.send(f'user has {bankinfo["warns"]} warns')

  @commands.command(aliases=['CW','Cw'])
  @commands.has_permissions(ban_members=True)
  async def cw(self,ctx,member:discord.Member):
    bankinfo = collection.find_one({"guild":ctx.guild.id,"member": member.id})
    if not bankinfo:
      await ctx.send('Nothing to clear')

    else:
      #bankinfo['warns'] = 0
      collection.remove({"guild":bankinfo['guild'],"member":bankinfo['member']})
      await ctx.send('data cleared')

    #collection.replace_one({"guild":bankinfo['guild'],"member":bankinfo['member']},{"guild":bankinfo['guild'],"member":bankinfo['member'],"warns":bankinfo['warns']})



def setup(client):
  client.add_cog(Warn(client))