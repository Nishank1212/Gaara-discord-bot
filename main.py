import discord
from os import getenv 
from discord.ext import commands, tasks
from itertools import cycle
from keep_alive import keep_alive
import os
from PIL import Image
from io import BytesIO
import random
import wikipedia
import json
import aiohttp
import requests
from aiohttp import ClientSession
import asyncio

# import youtube_dl
# from youtube_search import YoutubeSearch

def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes.get(str(message.guild.id), "~~")


intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = get_prefix,
intents=intents, owner_ids={793433316258480128})
status = cycle(['Gaara|Ping for more info','Gaara|Ping for more info'])
client.sniped_messages = {}
client.sniped_messages1 = {}
client.load_extension('jishaku')

client.remove_command("help")
global chat, chat_author_id
chat = 0
chat_author_id = 0

@client.event
async def on_ready():
  change_status.start()
  print('Bot is ready')


@client.command()
async def wiki(ctx, *, msg):
  try:
      content = wikipedia.summary(msg, auto_suggest=False, redirect=True)

      embed = discord.Embed(title="Wikipedia", colour=discord.Colour.blue())
      chunks = [content[i : i + 1024] for i in range(0, len(content), 2000)]
      for chunk in chunks:
          embed.add_field(name="\u200b", value=chunk, inline=False)
      await ctx.send(embed=embed)
  except:
      await ctx.send("**Failed to get information**")


@client.event
async def on_message(message):



  if message.author == client.user:
    return

  if message.author.bot:
    return

  with open('moderation.json','r') as f:

    mod = json.load(f)

  try:
    num = mod[str(message.guild.id)][0]
    mess = mod[str(message.guild.id)][1]
    yesno = mod[str(message.guild.id)][2]
    msg  = message.content.replace(' ','')
    a = list(msg)
    caps = 0
    for m in a:
      try:
        if m.isupper():
          caps += 1
          if str(num).isdigit():
            if caps >= int(num):

              try:
                await message.delete()
                if yesno == 'yes':
                  await message.author.send(f"{message.author.mention}\n{mess}")

                else:
                  msg1 = await message.channel.send(f"{message.author.mention}\n{mess}")
                await asyncio.sleep(20)
                await msg1.delete()

              except:
                pass#await message.channel.send('I do not have perms but too many caps are being used')

            else:
              pass
            
      except:
        pass

  except:
    pass


  if message.content.lower() == 'no u':

    if message.author.id == 793433316258480128:
      await message.channel.send('no u')

  if message.content == f'<@!{client.user.id}>':

      try:
      
        with open('prefixes.json','r') as f:
          prefixes = json.load(f)

        pre = prefixes[str(message.guild.id)]

      except:
        pre ='~~'

    

      embed=discord.Embed(colour=discord.Colour.blue())
      embed.set_author(name=f'My command prefix for this server is `{pre}`,type `{pre}help` for more info',icon_url=message.author.avatar_url)
      await message.channel.send(embed=embed)

    
    
  await client.process_commands(message)


@client.event
async def on_member_join(member):
  
      with open('welcome.json','r') as f:
        message = json.load(f)

      try:

        messages = message[str(member.guild.id)]
        print(messages)

      except:
        return
     
      with open('channel.json','r') as f:
        channelid = json.load(f)

      channel = channelid[str(member.guild.id)]
      print(channel)

      await client.get_channel(int(channel)).send(f"{member.mention}\n{messages}")

@tasks.loop(seconds=3600)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))

for filename in os.listdir('./cogs'):
#if filename.endswith('economy.py'):
  if filename.endswith('.py') and not(filename.startswith('miya')):
	  client.load_extension(f'cogs.{filename[:-3]}')
  else:
	  None

@client.command(aliases=['SHOOT','Shoot'])
async def shoot(ctx,member:discord.Member=None):

  if member == None:
      member = ctx.author

  else:
    im = Image.open('shoot.jpg')
    asset = member.avatar_url_as(format=None, static_format='jpg', size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    asset2 = ctx.author.avatar_url_as(format=None, static_format='jpg', size=128)
    data2 = BytesIO(await asset2.read())
    pfp2 = Image.open(data2)
    pfp = pfp.resize((113,105))
    pfp2 = pfp2.resize((102, 88))
    im = im.copy()
    im.paste(pfp, (415, 173))
    im.paste(pfp2, (188, 137))
    im.save('shot.png')
    await ctx.send(file=discord.File('shot.png'))

@client.command(aliases=['GAARA','Gaara'])
async def gaara(ctx):
  embed=discord.Embed(title='GAARA',description=' number one God',colour = discord.Colour.blue())
  embed.add_field(name='Info...',value="Gaara (我愛羅) is a fictional character in the Naruto manga and anime series created by Masashi Kishimoto. Originally debuting as an antagonist, Gaara is a shinobi affiliated with Sunagakure and is the son of Sunagakure's leader, the Fourth Kazekage. He was born as a demon's host as part of his father's intention to have a weapon to restore their village. However, a combination of being ostracized by the Sunagakure villagers, his early inability to control the Tailed Beast, and the notion that his deceased mother called him her curse on the village caused Gaara to become a ruthless killer who believes his own purpose is to kill his enemies. ",inline=False)

  embed.set_image(url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQR3XWDTzsVVZjDn1TaSQsPitUotvJZjNy7Ag&usqp=CAU')

  embed.add_field(name='More...',value="Gaara was created a foil to the series' eponymous character, Naruto Uzumaki, as the two were born through similar circumstances, but develop vastly different personalities due to a troubled upbringing. His designs and name underwent major changes in the making of his final one which also was modified in later arcs to give Gaara a design that is easier to draw.")

  await ctx.send(embed=embed)

# @client.event
# async def on_message_delete(message):
#   client.sniped_messages[message.author.id] = (message.content,message.author,message.channel.name,message.created_at)
#   client.sniped_messages1[message.guild.id] = (message.content,message.author,message.channel.name,message.created_at)

@client.command()
@commands.has_permissions(administrator=True)
async def create(ctx,typ,*,name):
  if typ.lower() == 'text':
     name.replace(' ','-')
     await ctx.guild.create_text_channel(f'{name}')
     await ctx.send(f'Text channel created by name {name}')

  elif typ.lower() == 'voice':
    await ctx.guild.create_voice_channel(f'{name}')
    await ctx.send(f'Text channel created by name {name}')

  else:
    await ctx.send(f'No type named {typ}')
  
@client.command()
@commands.has_permissions(administrator=True)
async def delete(ctx,typ,*,name):
  if typ.lower() == 'text':
     name.replace(' ','-')
     existing_channel = discord.utils.get(ctx.guild.channels, name=name)
     if existing_channel is not None:

      await  existing_channel.delete()
      await ctx.send(f'Text channel deleted by name {name}')

     else:
      await ctx.send(f'No Text channel by name {name}')

  elif typ.lower() == 'voice':
  
    existing_channel = discord.utils.get(ctx.guild.channels, name=name)
    if existing_channel is not None:

      await  existing_channel.delete()
      await ctx.send(f'Text channel deleted by name {name}')

    else:
      await ctx.send(f'No voice channel by name {name}')


@client.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx,amount:int):
  try:
    await ctx.channel.edit(reason='Bot Command Slowmode', slowmode_delay=int(amount))
  
  except:
    await ctx.send('I do not have Permissions')

@client.command(aliases=['disSlowMode','disableslowmode'])
@commands.has_permissions(manage_channels=True)
async def slowmode_disable(ctx):
  try:
    await ctx.channel.edit(reason='Bot Command Slowmode', slowmode_delay=0)
  
  except:
    await ctx.send('I do not have Permissions')

@client.event
async def on_guild_join(guild):

  with open("prefixes.json",'r') as f:
    prefixes = json.load(f)

  prefixes[str(guild.id)] = '~~'

  with open('prefixes.json','w'):
    json.dump(prefixes,f,indent=4)


@client.command()
@commands.has_permissions(administrator = True)
async def setprefix(ctx,prefix):


    with open('prefixes.json','r') as f:
      prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json','w') as f:
      json.dump(prefixes,f)

    await ctx.send(f'The prefix was changed to {prefix}')

@client.command(aliases=['cre','Cre','CRE','Creditz','CREDITZ','creditz','CREDITS','Credits'])
async def credits(ctx):
  embed=discord.Embed(title='Credits',description='Contributors for the bot',colour=discord.Colour.blue())
  embed.add_field(name=':eyes: Nishank',value='Creator/owner')
  embed.add_field(name=':slight_smile: Dr_Gamer',value='Helping Mostly in Music!!! ')
  embed.add_field(name=':sunglasses: oklahoma_bot',value='Helping in rank system and other problems...')
  embed.add_field(name=':eyes: Entropy',value='Helping in chatbot and debugging...')
  await ctx.send(embed=embed)

@client.command(aliases=['Lenny','LENNY'])
async def lenny(ctx):
  lenny = ['( ͡° ͜ʖ ͡°)','( ‾ʖ̫‾)','(☭ ͜ʖ ☭)','(ᴗ ͜ʖ ᴗ)','(° ͜ʖ °)','( ಠ ͜ʖಠ)','( ° ͜ʖ °)','(⟃ ͜ʖ ⟄) ','( ‾ ʖ̫ ‾)','(͠≖ ͜ʖ͠≖)','( ✧≖ ͜ʖ≖)','(✿❦ ͜ʖ ❦)','(▀̿Ĺ̯▀̿ ̿)']

  await ctx.send(random.choice(lenny))

@client.command(aliases=['ASCII','Ascii'])
async def ascii(ctx,*,word):

     async with aiohttp.ClientSession() as session:
                #
                async with session.get(
                    f"https://artii.herokuapp.com/make?text={word}"
                ) as response:
                    #
                    fancy_text = await response.text()
                    await ctx.send(f"```{fancy_text}```")
                    await ctx.send(f"{ctx.author.mention}")

@client.command()
async def calc(ctx,*,expression):
  calculator = expression.replace("+", "%2B")
  calculator = calculator.replace('x','*')
  async with aiohttp.ClientSession() as session:
                #
    async with session.get(f"https://api.mathjs.org/v4/?expr={calculator}") as response:

      answer = await response.text()
      embed=discord.Embed(title='Expression',description=f'```{expression}```',colour=discord.Colour.blue())
      embed.add_field(name='Answer!',value=f'```{answer}```')

      embed.set_author(name='Calculator',icon_url='https://www.webretailer.com/wp-content/uploads/2018/10/Flat-calculator-representing-Amazon-FBA-calculators.png')

      await ctx.send(embed=embed)

@client.command(aliases=["lyrics"])
async def ly(ctx, *, lyrics):
    if lyrics is None:
        await ctx.send("You forgot lyrcis")
    else:
        words = "+".join(lyrics.split(" "))
        print(words)
        URL = f"https://some-random-api.ml/lyrics?title={words}"

        def check_valid_status_code(request):
            if request.status_code == 200:
                return request.json()

            return False

        def get_song():
            request = requests.get(URL)
            data = check_valid_status_code(request)

            return data

        song = get_song()
        if not song:
            await ctx.channel.send("Couldn't get lyrcis from API. Try again later.")

        else:
            music = song["lyrics"]
            ti = song["title"]
            au = song["author"]

            embed = discord.Embed(
                timestamp=ctx.message.created_at,
                Title="Title: Song",
                color=discord.Colour.blue()
            )

            embed.add_field(name=f"Title: {ti}", value=f"Author: {au}")
            embed.set_thumbnail(url=song['thumbnail']['genius'])
            chunks = [music[i : i + 1024] for i in range(0, len(music), 2000)]
            for chunk in chunks:
                embed.add_field(name="\u200b", value=chunk, inline=False)

            # embed.add_field(name='Song',value=f'{music}', inline=True)
            embed.set_footer(
                text=f"{song['links']['genius']}",
                icon_url=f"{ctx.author.avatar_url}",
            )
            await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def modon(ctx,amount:int):

    def check(m):
      return m.author == ctx.author
    with open('moderation.json','r') as f:
      mod = json.load(f)

    try:
      del mod[str(ctx.guild.id)] 
      mod[str(ctx.guild.id)] = [int(amount)]

    
      await ctx.send(f'caps lock limit set to {amount}')
      await ctx.send('What is the message you want to send to them after they break the limit of number of caps?')

      message = await client.wait_for('message',check=check)

      mod[str(ctx.guild.id)].append(str(message.content))

      await ctx.send(f'message set to {message.content}')
      await ctx.send('Do you want me to DM the user or put it in the server\ntype `yes` for dm and `no` for not')
      checking = await client.wait_for('message',check=check)
      if checking.content.lower() == 'yes' or checking.content.lower() == 'y':
        await ctx.send('sending message via DM activated')
        mod[str(ctx.guild.id)].append('yes')

      elif checking.content.lower() == 'no' or checking.content.lower() == 'n':
        await ctx.send('sending message via server activated')
        mod[str(ctx.guild.id)].append('no')
    except:
      mod[str(ctx.guild.id)] = [int(amount)]
      await ctx.send(f'caps lock limit set to {amount}')
      await ctx.send('What is the message you want to send to them after they break the limit of number of caps?')

      message = await client.wait_for('message',check=check)

      mod[str(ctx.guild.id)].append(str(message.content))

      await ctx.send(f'message set to {message.content}')
      await ctx.send('Do you want me to DM the user or put it in the server\ntype `yes` for dm and `no` for not')
      checking = await client.wait_for('message',check=check)
      if checking.content.lower() == 'yes' or checking.content.lower() == 'y':
        await ctx.send('sending message via DM activated')
        mod[str(ctx.guild.id)].append('yes')

      elif checking.content.lower() == 'no' or checking.content.lower() == 'n':
        await ctx.send('sending message via server activated')
        mod[str(ctx.guild.id)].append('no')

    with open('moderation.json','w') as f:
      json.dump(mod,f)

@client.command()
@commands.has_permissions(administrator=True)
async def modoff(ctx):

  #try:
    with open('moderation.json','r') as f:
      mod = json.load(f)

    del mod[str(ctx.guild.id)]

    with open('moderation.json','w') as f:
      json.dump(mod,f)

    await ctx.send('moderation switched off')

  #except KeyError:
    #await ctx.send('mod was never on')


@client.command()
@commands.has_permissions(administrator=True)
async def chnick(ctx,member:discord.Member,*,nick):
  await member.edit(nick=nick)
  await ctx.send(f'Nickname was changed for {member.mention} ')

@client.command()
async def mhs(ctx, member : discord.Member, *, message : str):

        await ctx.message.delete()

        url = None
        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
            if webhook.name == 'Nishank':
                url = webhook.url

        if url is None:
            webhook = await ctx.channel.create_webhook(name = 'Nishank')
            url = webhook.url

        async with ClientSession() as session:
            webhook = discord.Webhook.from_url(url, adapter = discord.AsyncWebhookAdapter(session))


            await webhook.send(content = message, username = member.name, avatar_url = member.avatar_url)

@client.command()
async def eval(ctx,*,code):
  result = eval(code)
  await ctx.send(result)

keep_alive()


client.run(getenv('TOKEN'))