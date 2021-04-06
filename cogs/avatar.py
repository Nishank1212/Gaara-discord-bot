import discord
from discord.ext import commands

class Avatar(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def avatar(self,ctx,member:discord.Member=None ):
    if member is None:
      member=ctx.author
      embed=discord.Embed(title='Avatar',colour=discord.Colour.blue())
      embed.set_image(url = member.avatar_url)
      await ctx.send(embed=embed)
    else:
      embed=discord.Embed(title='Avatar',colour=discord.Colour.blue())
      embed.set_image(url = member.avatar_url)
      await ctx.send(embed=embed)

  @commands.command()
  async def wasted(self,ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
        a = member.avatar_url
    else:
        a = member.avatar_url
    thisurl = ('https://some-random-api.ml/canvas/wasted?avatar=' + "{}".format(a))
    final_url = thisurl.replace("webp", "png")
    embed = discord.Embed(title='Wasted Image', colour=discord.Colour.blue())
    embed.set_image(url = final_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def invert(self,ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
        a = member.avatar_url
    else:
        a = member.avatar_url
    thisurl = ('https://some-random-api.ml/canvas/invert?avatar=' + "{}".format(a))
    final_url = thisurl.replace("webp", "png")
    embed = discord.Embed(title='Inverted Image', colour=discord.Colour.blue())
    embed.set_image(url = final_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def invertgrey(self,ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
        a = member.avatar_url
    else:
        a = member.avatar_url
    thisurl = ('https://some-random-api.ml/canvas/invertgreyscale?avatar=' + "{}".format(a))
    final_url = thisurl.replace("webp", "png")
    embed = discord.Embed(title='Inverted Greyscale Image', colour=discord.Colour.blue())
    embed.set_image(url = final_url)
    await ctx.send(embed=embed)
  
  @commands.command()
  async def bright(self,ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
        a = member.avatar_url
    else:
        a = member.avatar_url
    thisurl = ('https://some-random-api.ml/canvas/brightness?avatar=' + "{}".format(a))
    final_url = thisurl.replace("webp", "png")
    embed = discord.Embed(title='Brightened Image', colour=discord.Colour.blue())
    embed.set_image(url = final_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def blue(self,ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
        a = member.avatar_url
    else:
        a = member.avatar_url
    thisurl = ('https://some-random-api.ml/canvas/blue?avatar=' + "{}".format(a))
    final_url = thisurl.replace("webp", "png")
    embed = discord.Embed(title='Bluened Image', colour=discord.Colour.blue())
    embed.set_image(url = final_url)
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Avatar(client))