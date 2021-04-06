import discord
from discord.ext import commands
import json
import requests

class Inspire(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def inspire(self,ctx):
    def get_quote():
      response = requests.get("https://zenquotes.io/api/random")
      json_data = json.loads(response.text)
      quote = json_data[0]['q'] + " -" + json_data[0]['a']
      return(quote)
    quote = get_quote()
    embed=discord.Embed(title='Inspirational Quote',colour=discord.Colour.blue())
    embed.add_field(name='Here is the quote...', value=quote,inline=False)
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Inspire(client))