import discord
from discord.ext import commands

class Spoon(commands.Cog):
  def __init__(self,client):
    self.client = client
  
  @commands.command(aliases=['SPOONFEEDING','Spoonfeeding'])
  async def spoonfeeding(self,ctx):
    embed=discord.Embed(title='Spoonfeeding',colour=discord.Colour.blue())
    embed.set_image(url="https://i.imgur.com/RUdPyQP.jpg")
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=embed)


  @commands.command(aliases=['HEHE','Hehe'])
  async def hehe(self,ctx,boi=None):
    if boi == None:
      pass
    if boi.lower() == 'boi':
      embed=discord.Embed(title='HEHE BOI',colour=discord.Colour.blue())
      embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4RDXTOYRPJi4WPaZbJlvivcrk3nowtkkeHA&usqp=CAU')
      embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
      await ctx.send(embed=embed)

    else:
      pass

  @commands.command(aliases=['KHOPDI','Khopdi'])
  async def khopdi(self,ctx,tod=None):
    if tod == None:
      pass
    if tod.lower() == 'tod':
      embed=discord.Embed(title='KHOPDI TOD',colour=discord.Colour.blue())
      embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbZO1mUMszhrPewrOsm-Igxj4jYnYT5f6Zcw&usqp=CAU')
      embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
      await ctx.send(embed=embed)

    else:
      pass



def setup(client):
  client.add_cog(Spoon(client))