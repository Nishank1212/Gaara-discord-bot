import discord
from discord.ext import commands
import requests

class Animals(commands.Cog):
  def __init__(self,client):
    self.client = client
  
  @commands.command(aliases=['DOG','Dog'])
  async def animal(self,ctx,choice):

    url = f"https://some-random-api.ml/img/{choice.lower()}"

    response = requests.request("GET", url).json()

    final_dog =  response['link']
    embed=discord.Embed(title=f'{choice}',description='AWWWWWW',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_dog)
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Animals(client))