import discord
from discord.ext import commands
import json

class rr(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command()
  @commands.has_permissions(manage_roles=True)
  async def rrmake(self,ctx):
    

    def check(m):
      return m.author == ctx.author and m.channel.id == ctx.channel.id 



    await ctx.send('Which Channel Do you want me to make a reaction role??? `type the id of the channel`')

    channelid = await self.client.wait_for('message',check=check)

    if not channelid.content.isdigit():
      return await ctx.send('An id should have been sent {}'.format(ctx.author.mention))

    nice = False

    for channel in ctx.guild.channels:
      if str(channel.id) == str(channelid.content):
        nice=True
        break
      else:
        continue

    if not nice:
      return await ctx.send('Invalid ID provided')
    
    await ctx.send(f'Alright I will send the message in <#{int(channelid.content)}>')


    await ctx.send('Now tell me how do you want the embed to look?, seperate the title and description like this > ``` title here | description here ```')

    embed_t_d = await self.client.wait_for('message',check=check)
    list_t_d = list(embed_t_d.content.split('|'))
    if len(list_t_d) < 2:
      return await ctx.send('Error occured please check your content')
    
    await ctx.send('Now send the colour of the embed `black`, `blue` , `red` , `green` any of these choices are available')

    msg = await self.client.wait_for('message',check=check)
    print(msg.content.lower())
    if msg.content.lower() not in ['blue','black','green','red'] :
      return await ctx.send('INVALID COLOUR')

    color = msg.content.lower()

    titles = list_t_d[0]
    descriptions = list_t_d[1]

    if color == 'blue':
      embed=discord.Embed(title=titles,description = descriptions,colour=discord.Colour.blue())

    elif color == 'red':
      embed=discord.Embed(title=titles,description = descriptions,colour=discord.Colour.red())

    elif color == 'black':
      embed=discord.Embed(title=titles,description = descriptions)

    elif color == 'green':
      embed=discord.Embed(title=titles,description = descriptions,colour=discord.Colour.green())

    await ctx.send('Alright! The embed will look something like this-', embed=embed)

    await ctx.send('Tell the number of reaction roles u want...')
    num = await self.client.wait_for('message',check=check)
    if not num.content.isdigit():
      return await ctx.send('Should Have Been a Number bruh')

    else:
      list_needed = {}
      count = 1
      for j in range(int(num.content)):
        await ctx.send(f'Send an emoji for the {count} reaction role')
        emoji = await self.client.wait_for('message',check=check)
        try:
          await emoji.add_reaction(str(emoji.content))
        except:
          return await ctx.send('An emoji should have been sent...')

        await ctx.send('Send the Role id which will be gotten by reacting with {}'.format(emoji.content))
        role_id = await self.client.wait_for('message',check=check)
        if not role_id.content.isdigit():
          return await ctx.send('A role id should have been sent')

        try:
          role = ctx.guild.get_role(int(role_id.content))
          if role.position > ctx.author.top_role.position:
            return await ctx.send('U have no perms to add that role bruhh')
          if role.position > ctx.guild.me.top_role.position:
            return await ctx.send('Role higher than my top role')
        except:
          return await ctx.send('Invalid id')

        list_needed[str(emoji.content)] = role.id
        
        count += 1

      for s in list_needed.keys():
          role = ctx.guild.get_role(list_needed[s])
          embed.add_field(name=s,value=role.name)
      channel = ctx.guild.get_channel(int(channelid.content))
      print(list_needed)
      
      message_id = await channel.send(embed=embed)
      
      for q in list_needed.keys():
          await message_id.add_reaction(q)

      await ctx.send(f'Check it out in this link below\nhttps://discord.com/channels/{ctx.guild.id}/{channelid.content}/{message_id.id}')

      with open('rr.json','r') as f:
        m = json.load(f)

      m[str(message_id.id)] = list_needed


      with open('rr.json','w') as f:
        json.dump(m,f)

  @commands.Cog.listener()
  async def on_raw_reaction_add(self,payload):
    with open('rr.json','r') as f:
      n = json.load(f)

    try:
   
      data=n[str(payload.message_id)]
      for i in data.keys():

          if str(payload.emoji) == i:
            guild = self.client.get_guild(payload.guild_id)
            role = guild.get_role(int(data[i]))
            await payload.member.add_roles(role)
            break
          else:
            print('no found breh')
            continue

            nice=False
      
          if not nice:
            print('emoji aint in json file')
 
    except:
      pass

    

  @commands.command()
  @commands.has_permissions(manage_roles=True)
  async def rrdelete(self,ctx,message_id=None):
    if message_id == None:
      return await ctx.send('Send a Message id to delete like `~~rrdelete <message id of the reaction role>`')
    if not message_id.isdigit():
      return await ctx.send('Send a Message id to delete like `~~rrdelete <message id of the reaction role>`')

    try:
      with open('rr.json','r') as f:
        m = json.load(f)

      nice = False
      for i in ctx.guild.channels:
        try:
          message = await i.fetch_message(id=message_id)
          nice = True
          break
        except:
          continue
          pass
      if nice:

        del m[str(message_id)]
        if message.author.id == self.client.user.id:
          await message.delete()
          await ctx.send('Done...')

      with open('rr.json','w') as f:
        m = json.dump(m,f)
    except:
      pass
    
  @commands.command()
  async def rrmini(self,ctx,emoji,role_id : int,channel:discord.TextChannel,*,message):
    try:

      await ctx.message.add_reaction(str(emoji))

    except:
      return await ctx.send('Try again Like this `~~rrmini <emoji> (role_id) [channel to send] <title or message>`')

    role_check = ctx.guild.get_role(role_id)

    if not role_check:
      return await ctx.send('Try again Like this `~~rrmini <emoji> (role_id) [channel to send] <title or message>`')

    embed=discord.Embed(description=message,colour=discord.Colour.blue())
    embed.add_field(name='\u200b',value=f'{emoji} : {role_check}')


    lol = await channel.send(embed=embed)
    await lol.add_reaction(str(emoji))
    await ctx.send(f'Check it out in this link below\nhttps://discord.com/channels/{ctx.guild.id}/{channel.id}/{lol.id}')
    

    with open('rr.json','r') as f:
      m = json.load(f)

    list_needed = {str(emoji) : role_check.id}

    m[str(lol.id)] = list_needed

    with open('rr.json','w') as f:
      json.dump(m,f)

  @rrmini.error
  async def rrmini_error(self,ctx,error):
    await ctx.send('Try again Like this `~~rrmini <emoji> (role_id) [channel to send] <title or message>`')

  @commands.command(aliases=['armake','autorolemake'])
  async def autorole(self,ctx):
    await ctx.send('OK so now say THE role id you want to add when someone joins\nnote: only one role allowed')
    def check(m):
      return m.author==ctx.author and m.channel.id == ctx.channel.id 
    role_id = await self.client.wait_for('message',check=check)
    if not role_id.content.isdigit():
      return await ctx.send('a role id should have been sent')


    roleid = int(role_id.content)
    for i in ctx.guild.roles:
      if int(i.id) == roleid:
        nice = True
        break

      else:
        nice = False
        continue

    if not nice:
      return await ctx.send('Sorry There is No role with that ID')
    role = ctx.guild.get_role(roleid)

    
    await ctx.send(f'Alright I will add {role.name} role to the person who joins and note this I wont add the role to any bots... If you want to add for bots then use the `~~bar` or `~~BotAutoRole` command')

    with open('ar.json','r') as f:
      m = json.load(f)

    try:
      del m[str(ctx.guild.id)]
    except:
      pass
    
    m[ctx.guild.id] = roleid

    with open('ar.json','w') as f:
      json.dump(m,f)

  @commands.command(aliases=['barmake','botautorolemake'])
  async def br(self,ctx):
    await ctx.send('OK so now say THE role id you want to add when some `bot` joins\nnote: only one role allowed')
    def check(m):
      return m.author==ctx.author and m.channel.id == ctx.channel.id 
    role_id = await self.client.wait_for('message',check=check)
    if not role_id.content.isdigit():
      return await ctx.send('a role id should have been sent')


    roleid = int(role_id.content)
    for i in ctx.guild.roles:
      
      if int(i.id) == roleid:
        nice = True
        break

      else:
        nice = False
        continue

    if not nice:
      return await ctx.send('Sorry There is No role with that ID')
    role = ctx.guild.get_role(roleid)

    
    await ctx.send(f'Alright I will add {role.name} role to the bot who joins and note this I wont add the role to any humans... If you want to add for bots then use the `~~armake` or `~~autorole` command')

    with open('bar.json','r') as f:
      m = json.load(f)

    try:
      del m[str(ctx.guild.id)]
    except:
      pass
    
    m[ctx.guild.id] = roleid

    with open('bar.json','w') as f:
      json.dump(m,f)
    

  @commands.command()
  async def ardelete(self,ctx):
    with open('ar.json','r') as f:
      m = json.load(f)

    try:
      del m[str(ctx.guild.id)]
      await ctx.send('Deleted Auto Role System For humans!!!')

      with open('ar.json','w') as f:
        json.dump(m,f)
    except:
      await ctx.send('There Was No Auto Role in this server')

  @commands.command()
  async def bardelete(self,ctx):
    with open('ar.json','r') as f:
      m = json.load(f)

    try:
      del m[str(ctx.guild.id)]
      await ctx.send('Deleted Auto Role System For bots!!!')

      with open('bar.json','w') as f:
        json.dump(m,f)
    except:
      await ctx.send('There Was No bot Auto Role in this server')


def setup(client):
  client.add_cog(rr(client))