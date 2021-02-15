import discord
from discord.ext import commands
import requests

class Animals(commands.Cog):
  def __init__(self,client):
    self.client = client
  
  @commands.command(aliases=['Cat','CAT'])
  async def cat(self,ctx):

    url = "https://aws.random.cat/meow"

    response = requests.request("GET", url).json()

    final_cat =  response['file']
    embed=discord.Embed(title='Cat',description='AWWWWWW',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_cat)
    await ctx.send(embed=embed)

  @commands.command(aliases=['DOG','Dog'])
  async def dog(self,ctx):

    url = "https://some-random-api.ml/img/dog"

    response = requests.request("GET", url).json()

    final_dog =  response['link']
    embed=discord.Embed(title='Dog',description='AWWWWWW',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_dog)
    await ctx.send(embed=embed)

  @commands.command(aliases=['PANDA','Panda'])
  async def panda(self,ctx):

    url = "https://some-random-api.ml/img/panda"

    response = requests.request("GET", url).json()

    final_panda =  response['link']
    embed=discord.Embed(title='Panda',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_panda)
    await ctx.send(embed=embed)

  @commands.command(aliases=['REDPANDA','RedPanda','Redpanda'])
  async def redpanda(self,ctx):

    url = "https://some-random-api.ml/img/red_panda"

    response = requests.request("GET", url).json()

    final_red_panda =  response['link']
    embed=discord.Embed(title='Red Panda',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_red_panda)
    await ctx.send(embed=embed)
  
  @commands.command(aliases=['KOALA','Koala'])
  async def koala(self,ctx):

    url = "https://some-random-api.ml/img/koala"

    response = requests.request("GET", url).json()

    final_koala =  response['link']
    embed=discord.Embed(title='Koala',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_koala)
    await ctx.send(embed=embed)

  @commands.command(aliases=['BIRD','Bird'])
  async def bird(self,ctx):

    url = "https://some-random-api.ml/img/birb"

    response = requests.request("GET", url).json()

    final_bird =  response['link']
    embed=discord.Embed(title='Bird',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_bird)
    await ctx.send(embed=embed)

  @commands.command(aliases=['FOX','Fox'])
  async def fox(self,ctx):

    url = "https://some-random-api.ml/img/fox"

    response = requests.request("GET", url).json()

    final_fox =  response['link']
    embed=discord.Embed(title='Fox',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_fox)
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Animals(client))