import discord
from discord.ext import commands

class Hiwelcome(commands.Cog):
  def __init__(self,client):
    self.client = client

  
  @commands.command(aliases=['WELCOME','Welcome'])
  async def welcome(self,ctx,member:discord.Member):
    embed = discord.Embed(title = f'Welcome to our server! {member}',descripytion='Hope you Enjoy',colour=discord.Colour.blue())
    embed.set_image(url='https://image.freepik.com/free-vector/colorful-welcome-composition-with-origami-style_23-2147907810.jpg')
    await ctx.send(embed=embed)

  @commands.command(aliases=['Hi','HI','HELLO','Hello','hello'])
  async def hi(self,ctx):
    embed=discord.Embed(title='Hello There!',colour=discord.Colour.blue())
    embed.set_image(url='https://i.redd.it/e06keab1qlq01.jpg')
    await ctx.send(embed=embed)

  @commands.command(aliases=['BYE','Bye'])
  async def bye(self,ctx):
    embed=discord.Embed(title='Bye..',colour=discord.Colour.blue())
    embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-r3y4CSzgjxBws69q11LI0WQrmC7mkR6m0w&usqp=CAU')
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Hiwelcome(client))