import discord
from discord.ext import commands

class Ping(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['PING','Ping'])
  async def ping(self,ctx):
    embed=discord.Embed(title='Pong!',colour=discord.Colour.blue())
    embed.add_field(name='\u200b',value=f':smile: Bot Latency - {round(self.client.latency * 1000)}ms',inline=True)
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    embed.set_author(name='Latency',icon_url='https://store-images.s-microsoft.com/image/apps.24298.14073362953807348.18acabda-19d7-4bf5-8056-352b7495ecef.fc31be50-f27e-4c81-9b14-18c06c40e837?mode=scale&q=90&h=270&w=270&background=%23FFFFFF')
    await ctx.send(embed=embed)


  @commands.command(hidden=True,aliases=['TOTALCMDS','TotalCommands','Totalcommands','totacommands','TOTALCOMMANDS','Totalcmds'])
  async def totalcmds(self,ctx):
    await ctx.send(f'There are {len(self.client.commands)} commands')

  @commands.command(aliases=['INTRODUCTION','Introduction','intro','INTRO','Intro'])
  async def introduction(self,ctx):
    embed=discord.Embed(title='A little bit about me...',description='Hi I am Grogu, I am made by Nishank I am a multipurpose bot,looking forward for working with you my friend....', colour=discord.Colour.blue())
    embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQu2-YpR5b5CGTfsCA1JvbD122qPOg0z5206g&usqp=CAU")
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=embed)

  @commands.command(aliases=['memcount','MEM','Mem','MemCount','MEMCOUNT','Memcount'])
  async def mem(self,ctx):
    embed=discord.Embed(title=ctx.guild.name,description=f'There are {ctx.guild.member_count} members in the server',colour=discord.Colour.blue())
    embed.set_footer(text=f'FBI agent:{ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


def setup(client):
  client.add_cog(Ping(client))
  