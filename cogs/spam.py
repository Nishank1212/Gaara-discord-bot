import discord
from discord.ext import commands

class Spam(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 600, commands.BucketType.channel)
  async def spam(self,ctx,number = None,*,spam_item = None):

    if ctx.author.id == 793433316258480128:
      if spam_item == None and number == None:
        await ctx.send('Command = spam, spam <the number of times u want it to spam>(the thing u want it too spam))')

      elif spam_item != None and number != None:
        if int(number) < 100:
          for spam in range(int(number)):
            await ctx.send(spam_item)

        else:
          await ctx.send('NOT SO MUCH SPAM')

      else:
        pass

    else:
      await ctx.send('NO U ')
      

def setup(client):
  client.add_cog(Spam(client))