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
      embed=discord.Embed(title='Error',description='Cannot warn Someone higher than you!',colour=discord.Colour.blue())
      await ctx.send(embed=embed)

    elif member.id == ctx.author.id:
      embed=discord.Embed(title='Error',description='Cannot warn yourself',colour=discord.Colour.blue())
      await ctx.send(embed=embed)

    elif ctx.guild.me.top_role < member.top_role:
      embed=discord.Embed(title='Error',description='Cannot warn! Member has higher role than me',colour=discord.Colour.blue())
      await ctx.send(embed=embed)

    elif member.bot:
      embed=discord.Embed(title='Error',description='Cannot warn Bot! No use!',colour=discord.Colour.blue())
      await ctx.send(embed=embed)

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
          await message.edit(content=f'Warned {member.mention}, now has {bankinfo["warns"]} warn')



          collection.replace_one({"guild":bankinfo['guild'],"member":bankinfo['member']},{"guild":bankinfo['guild'],"member":bankinfo['member'],"warns":bankinfo['warns']})

  @commands.command()
  async def case(self,ctx,member:discord.Member=None):
    

    if member == None:
      member = ctx.author

    bankinfo = collection.find_one({"guild":ctx.guild.id,"member": member.id})

    if not bankinfo:
        await ctx.send('No Data Found')

    else:
     
        embed=discord.Embed(title='Warns',description=f'{member.mention} has {bankinfo["warns"]} warns',colour=discord.Colour.blue())
        await ctx.send(embed=embed)

  @commands.command(aliases=['CW','Cw'])
  @commands.has_permissions(ban_members=True)
  async def cw(self,ctx,member:discord.Member):
    bankinfo = collection.find_one({"guild":ctx.guild.id,"member": member.id})
    if not bankinfo:
      
        embed=discord.Embed(title='Error',description='Nothing To clear',colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    else:
      #bankinfo['warns'] = 0
      collection.remove({"guild":bankinfo['guild'],"member":bankinfo['member']})


      embed=discord.Embed(title='Cleared!',description=f'Data Cleared for {member.mention}',colour=discord.Colour.blue())
      await ctx.send(embed=embed)

    #collection.replace_one({"guild":bankinfo['guild'],"member":bankinfo['member']},{"guild":bankinfo['guild'],"member":bankinfo['member'],"warns":bankinfo['warns']})



def setup(client):
  client.add_cog(Warn(client))	