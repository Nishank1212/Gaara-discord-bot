import discord
from discord.ext import commands
from datetime import date
import json

class Birthday(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command()
  async def date(self,ctx):
    await ctx.send(str(date.today())[4:])


  @commands.command()
  async def setbb(self,ctx,datee):
    datee2 = list(datee.split('-'))
    await ctx.send(f'Birthday Set to {int(datee2[0])}-{int(datee2[1])}')
    with open('bday.json','r') as f:
      m = json.load(f)

    try:
      del m[str(ctx.author.id)]
    except:
      pass
    m[ctx.author.id] = [ctx.channel.id,datee]

    with open('bday.json','w') as f:
      json.dump(m,f)



  @commands.command(aliases=['upc'])
  async def upcoming(self,ctx):
    with open('bday.json','r') as f:
      m = json.load(f)
    l = str(date.today())[5:]

    list_needed = {}
    cool = False
    count=1
    embed=discord.Embed(title='Upcoming birthdays',colour=discord.Colour.blue())
    for i in m.keys():
      channelid = m[i][0]
      for d in ctx.guild.channels:
        if int(d.id) == channelid:

          embed.add_field(name='\u200b',value=f'<@!{(i)}>, Birthday - {m[i][1]}')
          count+=1
        else:
          continue

    await ctx.send(embed=embed)

    
        
      


      




  @setbb.error
  async def setbb_error(self,ctx,error):
    await ctx.send('Make sure your Date Is in this format - month-day likke for example if my birthday is 1st feb then i will type `02-01`')





def setup(client):
  client.add_cog(Birthday(client))