import discord
from discord.ext import commands
from os import getenv
import requests




class Joke(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['JOKE','Joke'])
  async def joke(self,ctx):

    return

    url = "https://official-joke-api.appspot.com/random_joke"

   

    response = requests.request("GET", url).json()
    embed = discord.Embed(title='Joke :rofl:',description=f"{response['setup']}\n{response['punchline']}",colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=embed)

  @commands.command(aliases=['MEME','Meme'])
  async def meme(self,ctx):

    url = "https://meme-api.herokuapp.com/gimme"

    response = requests.request("GET", url).json()

    final_meme =  response['url']
    embed=discord.Embed(title='Meme',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=final_meme)
    await ctx.send(embed=embed)

  @commands.command(aliases=['GOODJOKE','GoodJoke','goodjoke','Goodjoke','GOOD','Good'])
  async def good(self,ctx,choice=None):
    if choice == None:
      await ctx.send('I may be too good but I cant do that hermano')
    elif choice.lower() == 'joke':
      embed=discord.Embed(title='Good Joke',description='Am I a joke to you')
      embed.set_image(url="https://i.kym-cdn.com/entries/icons/original/000/027/424/joke.jpg")
      embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
      await ctx.send(embed=embed)


def setup(client):
  client.add_cog(Joke(client))
