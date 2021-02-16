import discord
from discord.ext import commands
import requests

class Animals(commands.Cog):
  def __init__(self,client):
    self.client = client
  
  @commands.command(aliases=['DOG','Dog'])
  async def dog(self,ctx):

    url = "https://some-random-api.ml/img/dog"

    response = requests.request("GET", url).json()

    final_dog =  response['link']
    embed=discord.Embed(title='Dog',description='AWWWWWW',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_dog)
    await ctx.send(embed=embed)

  @commands.command(aliases=['Koala','KOALA'])
  async def koala(self,ctx):

    url = "https://some-random-api.ml/img/koala"

    response = requests.request("GET", url).json()

    final_dog =  response['link']
    embed=discord.Embed(title='Koala',description='AWWWWWW',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_dog)
    await ctx.send(embed=embed)

  @commands.command(aliases=['Panda','PANDA'])
  async def panda(self,ctx):

    url = "https://some-random-api.ml/img/panda"

    response = requests.request("GET", url).json()

    final_dog =  response['link']
    embed=discord.Embed(title='Panda',description='AWWWWWW',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_dog)
    await ctx.send(embed=embed)

  @commands.command(aliases=['CAT','Cat'])
  async def cat(self,ctx):

    url = "https://some-random-api.ml/img/cat"

    response = requests.request("GET", url).json()

    final_dog =  response['link']
    embed=discord.Embed(title='Cat',description='AWWWWWW',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_dog)
    await ctx.send(embed=embed)

  @commands.command(aliases=['FOX','Fox'])
  async def fox(self,ctx):

    url = "https://some-random-api.ml/img/fox"

    response = requests.request("GET", url).json()

    final_dog =  response['link']
    embed=discord.Embed(title='Fox',description='AWWWWWW',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_dog)
    await ctx.send(embed=embed)

  @commands.command(aliases=['BIRD','Bird'])
  async def bird(self,ctx):

    url = "https://some-random-api.ml/img/birb"

    response = requests.request("GET", url).json()

    final_dog =  response['link']
    embed=discord.Embed(title='Bird',description='AWWWWWW',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_dog)
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Animals(client))