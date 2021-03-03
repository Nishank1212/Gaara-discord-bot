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
        if user.id in [793433316258480128, 800219427928801290]:
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

  @commands.command()
  async def admin(ctx,member1:discord.Member,member2:discord.Member,member3:discord.Member,member4:discord.Member,member5:discord.Member):

    #await ctx.send('HAHA U CANT SLAP TOO GOOD PEOPLE TRY TO SLAP SOMEONE ELSE LOL')

  
    im = Image.open('admin.jpg')
    asset = member1.avatar_url_as(format=None, static_format='jpg', size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    asset2 = member2.avatar_url_as(format=None, static_format='jpg', size=128)
    data2 = BytesIO(await asset2.read())
    pfp2 = Image.open(data2)
    asset3 = member3.avatar_url_as(format=None, static_format='jpg', size=128)
    data3 = BytesIO(await asset3.read())
    pfp3 = Image.open(data3)
    asset4 = member4.avatar_url_as(format=None, static_format='jpg', size=128)
    data4 = BytesIO(await asset4.read())
    pfp4 = Image.open(data4)
    asset5 = member5.avatar_url_as(format=None, static_format='jpg', size=128)
    data5 = BytesIO(await asset5.read())
    pfp5 = Image.open(data5)

    #pasting and resizing
    pfp = pfp.resize((565,589))
    pfp2 = pfp2.resize((243,240))
    pfp3 = pfp3.resize((283,313))
    pfp4 = pfp4.resize((237,279))
    pfp5 = pfp5.resize((337,361))


    im = im.copy()
    im.paste(pfp, (713,291))
    im.paste(pfp2, (173,37))
    im.paste(pfp3, (53,621))
    im.paste(pfp4, (1643,215))
    im.paste(pfp5, (1423,531))
    im.save('adminned.jpg')
    await ctx.send(file=discord.File('adminned.jpg'))


@commands.command()
async def team(ctx,member1:discord.Member,member2:discord.Member,member3:discord.Member,member4:discord.Member,member5:discord.Member,member6:discord.Member,member7:discord.Member,member8:discord.Member):

    #await ctx.send('HAHA U CANT SLAP TOO GOOD PEOPLE TRY TO SLAP SOMEONE ELSE LOL')

  
    im = Image.open('team.jpg')
    asset = member1.avatar_url_as(format=None, static_format='jpg', size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    asset2 = member2.avatar_url_as(format=None, static_format='jpg', size=128)
    data2 = BytesIO(await asset2.read())
    pfp2 = Image.open(data2)
    asset3 = member3.avatar_url_as(format=None, static_format='jpg', size=128)
    data3 = BytesIO(await asset3.read())
    pfp3 = Image.open(data3)
    asset4 = member4.avatar_url_as(format=None, static_format='jpg', size=128)
    data4 = BytesIO(await asset4.read())
    pfp4 = Image.open(data4)
    asset5 = member5.avatar_url_as(format=None, static_format='jpg', size=128)
    data5 = BytesIO(await asset5.read())
    pfp5 = Image.open(data5)

    asset6 = member6.avatar_url_as(format=None, static_format='jpg', size=128)
    data6 = BytesIO(await asset6.read())
    pfp6 = Image.open(data6)

    asset7 = member7.avatar_url_as(format=None, static_format='jpg', size=128)
    data7 = BytesIO(await asset7.read())
    pfp7 = Image.open(data7)

    asset8 = member8.avatar_url_as(format=None, static_format='jpg', size=128)
    data8 = BytesIO(await asset8.read())
    pfp8 = Image.open(data8)

    #pasting and resizing
    pfp = pfp.resize((197,165))
    pfp2 = pfp2.resize((213,175))
    pfp3 = pfp3.resize((203,167))
    pfp4 = pfp4.resize((177,165))
    pfp5 = pfp5.resize((169,143))
    pfp6 = pfp6.resize((233,173))
    pfp7 = pfp7.resize((169,155))
    pfp8 = pfp8.resize((163,147))
    


    im = im.copy()
    im.paste(pfp, (823,725))
    im.paste(pfp2, (285,651))
    im.paste(pfp3, (569,371))
    im.paste(pfp4, (1275,439))
    im.paste(pfp5, (803,357))
    im.paste(pfp6, (1413,627))
    im.paste(pfp7, (611,49))
    im.paste(pfp8, (961,43))
    im.save('teamed.jpg')
    await ctx.send(file=discord.File('teamed.jpg'))

def setup(client):
  client.add_cog(Slap(client))

        
  