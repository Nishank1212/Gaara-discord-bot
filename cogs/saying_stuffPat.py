import discord
from discord.ext import commands
import requests

class Say(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['PAT','Pat'])
  async def pat(self,ctx):
  
    url = "https://some-random-api.ml/animu/pat"

    response = requests.request("GET", url).json()
    final_pat = url=response['link']

    embed=discord.Embed(title='Pat',colour=discord.Colour.blue())
    embed.set_image(url= final_pat)
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=embed)

  @commands.command(aliases=['Say','SAY'])
  async def say(self,ctx,*,lines):
    embed = discord.Embed(title='Saying Your Words...',description=lines,colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Say(client))