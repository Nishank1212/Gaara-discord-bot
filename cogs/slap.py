from PIL import Image, ImageFilter
from io import BytesIO
import discord
from discord.ext import commands
import requests
from os import getenv

def killmessages(user, killer, mention):
	  killmessage = requests.get(f"http://entropi.mythicalkitten.com/KillMessage?user={user}&killer={killer}&mention={mention}", headers={"pass": getenv("pass"), "auth": "Nishank#8839"}).json()['Message']
	  return killmessage

class Slap(commands.Cog):
  def __init__(self,client):
    self.client = client  


  @commands.command(aliases=['SLAP','Slap'])
  async def slap(self,ctx, user : discord.Member):
        if user.id in [793433316258480128, 800219427928801290, 747451011484090479]:
          await ctx.send('HAHA U CANT SLAP TOO GOOD PEOPLE TRY TO SLAP SOMEONE ELSE LOL')

        else:
          user = ctx.author if not user else user
          im = Image.open('slap.png')
          asset = user.avatar_url_as(format=None, static_format='png', size=128)
          data = BytesIO(await asset.read())
          pfp = Image.open(data)
          asset2 = ctx.author.avatar_url_as(format=None, static_format='png', size=128)
          data2 = BytesIO(await asset2.read())
          pfp2 = Image.open(data2)
          pfp = pfp.resize((300, 300))
          pfp2 = pfp2.resize((300, 300))
          im = im.copy()
          im.paste(pfp, (808, 350))
          im.paste(pfp2, (500, 60))
          im.save('slapped.png')
          await ctx.send(file=discord.File('slapped.png'))

  @commands.command(aliases=['STAB','Stab'])
  async def stab(self,ctx,member:discord.Member=None):
    if member == None:
      member = ctx.author

    if member.id in [793433316258480128, 800219427928801290, 747451011484090479]:
          await ctx.send('HAHA U CANT SLAP TOO GOOD PEOPLE TRY TO SLAP SOMEONE ELSE LOL')

    else:
          im = Image.open('stab.jpg')
          asset = member.avatar_url_as(format=None, static_format='jpg', size=128)
          data = BytesIO(await asset.read())
          pfp = Image.open(data)
          asset2 = ctx.author.avatar_url_as(format=None, static_format='jpg', size=128)
          data2 = BytesIO(await asset2.read())
          pfp2 = Image.open(data2)
          pfp = pfp.resize((99,92))
          pfp2 = pfp2.resize((99, 92))
          im = im.copy()
          im.paste(pfp, (138, 81))
          im.paste(pfp2, (13, 35))
          im.save('stabbed.png')
          await ctx.send(file=discord.File('stabbed.png'))
        
  

  @commands.command(aliases=['RIP','Rip','KILL','Kill','kill'])
  async def rip(self,ctx,user:discord.Member=None):
    if not user:
      user = ctx.author
    asset = user.avatar_url_as(format=None, static_format='png', size=256)

    data = BytesIO(await asset.read())
		 
    user1 = Image.open(data)


    im = Image.open('rip.png')
	
    im = im.copy()
    im.paste(user1, (372, 333))
    im.save('killed.png')
    await ctx.send(file=discord.File('killed.png'))
    await ctx.send(killmessages(user.id, ctx.author.id, 'True'))

  @commands.command(aliases=['BOUNTY','Bounty','WANTED','Wanted','wanted'])
  async def bounty(self,ctx,user:discord.Member = None):
    if user == None:
      user = ctx.author
  
    wanted = Image.open('wanted.jpg')

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((265,267))

    wanted.paste(pfp,(92,192))

    wanted.save('profile.jpg')

    await ctx.send(file = discord.File('profile.jpg'))

  @commands.command(aliases=['FIGHT','Fight'])
  async def fight(self,ctx, user : discord.Member=None):
    if user == None:
      user = ctx.author
      
      im = Image.open('fight.png')
      asset = user.avatar_url_as(format=None, static_format='png', size=128)
      data = BytesIO(await asset.read())
      pfp = Image.open(data)
      asset2 = ctx.author.avatar_url_as(format=None, static_format='png', size=128)
      data2 = BytesIO(await asset2.read())
      pfp2 = Image.open(data2)
      pfp = pfp.resize((94, 92))
      pfp2 = pfp2.resize((94, 92))
      im = im.copy()
      im.paste(pfp, (31, 9))
      im.paste(pfp2, (181, 4))
      im.save('fought.png')
      await ctx.send(file=discord.File('fought.png'))


def setup(client):
  client.add_cog(Slap(client))

        
  