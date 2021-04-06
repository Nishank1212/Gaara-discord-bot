import discord
from discord.ext import commands
from asyncio import sleep as s 
import asyncio
import time
import datetime

class Remind(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def remind(self,ctx,timee: int,hsr=None,*,msg):
    if hsr == None:
      await ctx.send('along with the reminder in the end even type s for seconds r m for minutes or h for hours')

    if hsr.lower() == 'h' or hsr.lower() == 'hour' or hsr.lower() == 'hours' or hsr.lower() == 'hrs' or hsr.lower() == 'hr':
      await ctx.send(f'Reminder set for {msg}')
      lol = 3600 * timee
      
      
    if hsr.lower() == 'm' or hsr.lower() == 'minutes' or hsr.lower() == 'minute' or hsr.lower() == 'mins' or hsr.lower() == 'min':
      await ctx.send(f'Reminder set for {msg}')
      lol = timee * 60
      
    
    if hsr.lower() == 's' or hsr.lower() == 'second' or hsr.lower() == 'seconds' or hsr.lower() == 'sec' or hsr.lower() == 'secs':
      await ctx.send(f'Reminder set for {msg}')
      lol = timee
      
      
    try :
      lolz = tempo[ctx.author.id]

      lolz[msg] = time.time() + lol

    except:
      tempo[ctx.author.id] = {msg : time.time() + lol}


    await asyncio.sleep(lol)
    del tempo[ctx.author.id][msg]
    await ctx.send(f'{msg},{ctx.author.mention}')
    await ctx.author.send(f'{msg},{ctx.author.mention}')

  @commands.command()
  async def reminders(self,ctx):
        print(tempo[ctx.author.id])
        embed=discord.Embed(title='Reminders',colour=discord.Colour.blue())
        for i in tempo[ctx.author.id].keys():
          lol = str(datetime.timedelta(seconds=tempo[ctx.author.id][i] - time.time()))
          print(lol)
          hsm  = list(lol.split(':'))
          lol1 = f'{hsm[0]} Hours, {hsm[1]} minutes, {round(float(hsm[2]))} Seconds'
          
          embed.add_field(name=f'Message: {i}',value = f'Time remaining = {lol1}')

        await ctx.send(embed=embed)

  @remind.error
  async def remind_error(self,ctx,error):
    await ctx.send('Retry again but this time do something like...\n`remind (integer) <h/m/s> (message)`')


tempo = {}

def setup(client):
  client.add_cog(Remind(client))