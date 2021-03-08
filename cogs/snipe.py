import discord
from discord.ext import commands

class Snipe(commands.Cog):
  def __init(self,client):
    self.client=client

  @commands.Cog.listener()
  async def on_message_delete(self, message):
    if message.author.bot:
      return

    snipe[message.guild.id] = (message.content,message.author,message.created_at,message.channel.name)
    #await message.channel.send(f'I sniped : \"{snipe[message.guild.id][0]}\" from {snipe[message.guild.id][1]} :smile:')

  @commands.Cog.listener()
  async def on_message_edit(self,before,after):
    # if before.author.bot:
    #   return

    edit[before.guild.id]= (before.content,before.author,before.channel.name,before.created_at,after.content)
   

  @commands.command()
  async def snipe(self,ctx):
    try:
 
      content,author,timee,channel = snipe[ctx.guild.id]
      embed=discord.Embed(description = content, colour=discord.Colour.blue(),timestamp=timee)
      embed.set_author(name=f'{author.name}#{author.discriminator}',icon_url=author.avatar_url)
      embed.set_footer(text=f'Deleted in : #{channel}')
      await ctx.send(embed=embed)
      
      await ctx.send(f'{author.name} has beened sniped 🔫')

    except KeyError:
      embed=discord.Embed(colour=discord.Colour.blue())
      embed.set_author(name='There is no message to snipe',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

  @commands.command(aliases=['edits','le'])
  async def editss(self,ctx):

    try:
      content,author,channel,timee,after = edit[ctx.guild.id]
      embed=discord.Embed(description = f'{content}\n edited to\n{after}', colour=discord.Colour.blue(),timestamp=timee)
      embed.set_author(name=f'{author.name}#{author.discriminator}',icon_url=author.avatar_url)
      embed.set_footer(text=f'Edited in : #{channel}')
      await ctx.send(embed=embed)

    except KeyError:
     
      embed=discord.Embed(colour=discord.Colour.blue())
      embed.set_author(name=f'There is no message to check',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

snipe={}
edit={}
def setup(client):
  client.add_cog(Snipe(client))