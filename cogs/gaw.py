import discord
from discord.ext import commands
import asyncio
from typing import Optional
import random

class gaw(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def start(self,ctx,timee:int,hsmd,roles:commands.Greedy[discord.Role],*,message):
    print(roles)


    if roles is None:
      nice=False
    else:
      nice=True

    print(nice)

    if nice:
      role = []

      for i in list(roles):
        role.append(i.name)

      print(role)

    roles = list(roles)

    

    if hsmd.lower() == 's' or hsmd.lower() == 'seconds' or hsmd.lower() == 'second' or hsmd.lower() == 'sec' or hsmd.lower() == 'secs':
      timetowait = timee

    elif hsmd.lower() == 'h' or hsmd.lower() == 'hours' or hsmd.lower() == 'hour' or hsmd.lower() == 'hr' or hsmd.lower() == 'hrs':
      timetowait = timee*3600

    elif hsmd.lower() == 'm' or hsmd.lower() == 'minute' or hsmd.lower() == 'minutes' or hsmd.lower() == 'min' or hsmd.lower() == 'mins':
      timetowait = timee*60

    elif hsmd.lower() == 'd' or hsmd.lower() == 'days' or hsmd.lower() == 'day' or hsmd.lower() == 'dy' or hsmd.lower() == 'dys':
      timetowait = timee*86400

    else:
      return await ctx.send('Try again But this time type it like this:\n`~~start <some number> {hour/second/minute/day} <required role(optional)> <for what?>`\nnote:do not include the <> and {} and []')

    if not nice:
      message = f'{message}'

      roles = 'None'


      embed=discord.Embed(title='React with 🎉 to enter',description=f'**{message}**\nduration : {timetowait} seconds\nhosted by : {ctx.author.mention}\nRequired Role:{roles}',colour=discord.Colour.blue())

    else:
      embed=discord.Embed(title='React with 🎉 to enter',description=f'**{message}**\nduration : {timetowait} seconds\nhosted by : {ctx.author.mention}\nRequired Role:{"".join(role)}',colour=discord.Colour.blue())

    msg = await ctx.send(embed=embed)
    await msg.add_reaction('\U0001f389')
    await asyncio.sleep(int(timetowait))
    new_msg = await ctx.channel.fetch_message(msg.id)
    # users = []
    # for l in new_msg.reactions:
    #   if str(l.emoji) == '🎉':
    #     if l.message.author == self.client.user:
    #       continue
    #     else:
    #       users.append(l.message.author)
    #   print(users)

    users = await new_msg.reactions[0].users().flatten()
    
    users.pop(users.index(self.client.user))
    if users == []:
      return await ctx.send('Noone Reacted Hence Noone Won!!!')

    if nice:

      n = False

      for x in role:


        for o in users:
          for y in roles:
            if y in o.roles:
              n = True

            else:
              n = False
              await new_msg.remove_reaction("🎉",discord.Object(id=o.id))
              break
          # if not roles in o.roles:
          #   await new_msg.remove_reaction("🎉",discord.Object(id=o.id))

          # else:
          #   continue

    
    users = await new_msg.reactions[0].users().flatten()
    try:

      users.pop(users.index(self.client.user))

    except:
      pass

    if users == []:
      return await ctx.send('Noone Reacted Hence Noone Won!!!')

    winner = random.choice(users)
    

    await ctx.channel.send(f"Congratulations! {winner.mention} won the prize: {message}!\nhttps://discordapp.com/channels/{ctx.guild.id}/{ctx.channel.id}/{new_msg.id}")

    embed=discord.Embed(title='**GIVEAWAY ENDED**',description=f'**{message}**\nduration : {timetowait} seconds\nhosted by : {ctx.author.mention}\nwinner:{winner}',colour=discord.Colour.blue())

    await msg.edit(embed=embed)

  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def reroll(self,ctx,id):
    try:
      new_msg = await ctx.channel.fetch_message(id)
      print(new_msg.author)

      if new_msg.author == self.client.user:
          pass
      else:
          return await ctx.send("The ID that was entered was incorrect, make sure you have entered the correct giveaway message ID.")


    except:
       return await ctx.send("The ID that was entered was incorrect, make sure you have entered the correct giveaway message ID.")

    new_msg = await ctx.channel.fetch_message(id)
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(self.client.user))
    
    
    if users == []:
      await ctx.send('Noone Reacted To that message')

    winner = random.choice(users)

    await ctx.send(f"Congratulations the new winner is: {winner.mention} for the giveaway rerolled!\nhttps://discordapp.com/channels/{ctx.guild.id}/{ctx.channel.id}/{new_msg.id}")

  @start.error
  async def start_error(self,ctx,error):
      await ctx.send('Try again But this time type it like this:\n`~~start <some number> {hour/second/minute/day} <required role(optional)> <for what?>`\nnote:do not include the <> and {} and []')

    


def setup(client):
  client.add_cog(gaw(client))