import discord
from discord.ext import commands
import random

class Fight(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['FIGHT','Fight'])
  async def fight(self,ctx,member:discord.Member=None):
    if member == None:
      await ctx.send('Use the command again but this time actually mention who should I fight')

    else:
      player1 = ctx.author
      player2 = member
      player1_hp = 100
      player2_hp = 100
      game_on = True
      

      while game_on:
        await ctx.send(f'{random.choice([member.id,ctx.author.id]).mention} you go first')





def setup(client):
  client.add_cog(Fight(client))
