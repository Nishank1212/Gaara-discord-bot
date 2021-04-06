import discord
from discord.ext import commands
from typing import Optional
from discord import Member
from datetime import datetime

class Info(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['UI','info'])
  async def userinfo(self,ctx, target: Optional[Member]):
    target = target or ctx.author

    embed=discord.Embed(title='User Information',colour=target.colour,timestamp=datetime.utcnow())

    embed.set_thumbnail(url=target.avatar_url)

    fields = [("🆔ID", target.id, False),
              ("🤴Name", str(target),True),
              ("🤖Bot?", target.bot, True),
              (":crown:Top role",target.top_role.mention, True),
              (":blue_circle:Status", str(target.status).title(), True),
              (":clock10:Created at", str(target.created_at)[0:11], True),
              (":clock1:Joined at", str(target.joined_at)[0:11], True)]

    for name,value,inline in fields:
      embed.add_field(name=name,value=value,inline=inline)

    embed.set_footer(text=f'FBI agent:{ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command(aliases=['Si'])
  async def serverinfo(self,ctx):
    embed=discord.Embed(title='Server Information',colour=ctx.guild.owner.colour,timestamp=datetime.utcnow())

    embed.set_thumbnail(url=ctx.guild.icon_url)

    fields = [("🆔ID",ctx.guild.id, True),
              ("👑Owner",ctx.guild.owner.mention, True),
              (":earth_asia:Region",ctx.guild.region, True),
              (":alarm_clock:Created at",str(ctx.guild.created_at)[0:11], True),
              (":100:Members",len(ctx.guild.members), True),
              (":man::woman:Humans",len(list(filter(lambda m: not m.bot,ctx.guild.members))),True),
              ("🤖Bots",len(list(filter(lambda m:m.bot,ctx.guild.members))),True),
              ("\u200b","\u200b",True),]

    for name,value,inline in fields:
      embed.add_field(name=name,value=value,inline=inline)

    embed.set_footer(text=f'FBI agent:{ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command(aliases=['Bi'])
  async def botinfo(self,ctx):

    embed=discord.Embed(title='Bot Information',colour=discord.Colour.blue(),timestamp=datetime.utcnow())

    embed.set_thumbnail(url=self.client.user.avatar_url)

    mh = 0
    for i in self.client.guilds:
      
      mh += len([m for m in i.members if not m.bot])
      
    mh = mh - len(self.client.guilds)

 

    fields = [("🆔ID", 810818178464612363, True),
              ("👑Owner",'<@!793433316258480128>', True),
              ("🤴Second developer","<@!747451011484090479>",True),
              ("🤖Name", "Gaara",True),
              ("😀No. of servers", int(len(list(self.client.guilds))),True),
              ("📝Invite me","[Click Here to Add Me](https://discord.com/api/oauth2/authorize?client_id=800219427928801290&permissions=8&scope=bot)",True),
              ("⛭GitHub","[Click Here to See GitHub](https://github.com/Nishank1212/Gaara-discord-bot)",True),
              ('🦮Helping',f'{mh} members',True),
              ("🦮Join My server","[Click Here To Join](https://discord.gg/RSz98FM7c5)",True)
              ]
              

    for name,value,inline in fields:
      embed.add_field(name=name,value=value,inline=inline)

    embed.set_footer(text=f'FBI agent:{ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def invite(self,ctx):
    embed=discord.Embed(title='Invite Me here',description='[Click Here to Add me](https://discord.com/api/oauth2/authorize?client_id=810818178464612363&permissions=8&scope=bot)',colour=discord.Colour.blue())  
    await ctx.send(embed=embed)

  @commands.command()
  async def server(self,ctx):
    embed=discord.Embed(title='Join my Server',description='[Click Here to Join](https://discord.gg/RSz98FM7c5)',colour=discord.Colour.blue())  
    await ctx.send(embed=embed)

  @commands.command(aliases=['github'])
  async def git(self,ctx):
    embed=discord.Embed(title='GitHub(star repo)',description='[Click Here to See GitHub](https://github.com/Nishank1212/Gaara-discord-bot)',colour=discord.Colour.blue())  
    await ctx.send(embed=embed)

  @commands.command()
  async def vote(self,ctx):
    embed=discord.Embed(title='Vote Gaara!',description='discordbotlist\n[Vote here](https://discordbotlist.com/bots/gaara/upvote)',colour=discord.Colour.blue())  
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Info(client))