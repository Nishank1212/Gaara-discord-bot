import discord
from os import getenv 
from typing import Optional
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
import shutil
import urllib.parse
import requests
import asyncio
from PIL import Image,ImageFont,ImageDraw,ImageFilter
from aiohttp import ClientSession
# import youtube_dl
# from youtube_search import YoutubeSearch

def get_prefix(client, message):
    with open("prefixes.json", "r") as f:#why u copy paste mine was giving error even tho it was literraly the same thing as urs so i deleted and put it again
        prefixes = json.load(f)
    return prefixes.get(str(message.guild.id), "~~")


intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = get_prefix,
intents=intents, owner_ids={569105874912804874,793433316258480128,790459205038506055})
status = cycle(['Gaara|Ping for more info','Gaara|Ping for more info'])
client.sniped_messages = {}
client.sniped_messages1 = {}
client.load_extension('jishaku')
#client.help_command = commands.MinimalHelpCommand()



# class MyNewHelp(commands.MinimalHelpCommand):
#     async def send_pages(self):
#         destination = self.get_destination()
#         for page in self.paginator.pages:
#             emby = discord.Embed(description=page)
#             await destination.send(embed=emby)

# client.help_command = MyNewHelp()

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

  with open('filter.json','r') as f:

    filtered = json.load(f)

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
                pass

            else:
              pass
            
      except:
        pass

  except:
    pass

  try:
    listt = filtered[str(message.guild.id)][0]
    mess = filtered[str(message.guild.id)][1]
    yesno = filtered[str(message.guild.id)][2]
    msg  = message.content.replace(' ','')
    a = list(msg.split(' '))
    
    for i in a:
      if i.lower() in listt:
        await message.delete()

        if yesno == 'no':

          lolz = await message.channel.send(f'{message.author.mention}\n{mess}')
          await asyncio.sleep(10)
          await lolz.delete()

        if yesno == 'yes':

          await message.author.send(f'{message.author.mention}\n{mess}')

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

  if message.content == '<@!797519687147585546>':
     await message.channel.send('Hokage is my best friend!!!\nWe both were made by our masters...') 
    
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

@client.event
async def on_guild_join(guild):
  embed=discord.Embed(title=f'Thanks for adding Gaara to {guild}',description='Try using `~~help` for More info or `~~swm` to set a welcome message and `~~slm` to set a leave message you can join our community by tying `~~server`',colour=discord.Colour.blue())
  channel = guild.text_channels[0]
  await channel.send(embed=embed)


@client.event
async def on_member_remove(member):
    print('someone ;lefttttt')
    with open('leave.json','r') as f:
      lolz = json.load(f)

    message = lolz[str(member.guild.id)][0]
    dmornot = lolz[str(member.guild.id)][1]
  
    print(message)
    print(dmornot)
    if dmornot == 'DM':
      await member.send(f'{member.mention} {message}')

    else:
      channel = client.get_channel(dmornot)
      await channel.send(f'{member.mention} {message}')

  

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
    await ctx.send(f'SlowMode enabled for {amount} seconds')
  
  except:
    await ctx.send('I do not have Permissions')

@client.command(aliases=['disSlowMode','disableslowmode'])
@commands.has_permissions(manage_channels=True)
async def slowmode_disable(ctx):
  try:
    await ctx.channel.edit(reason='Bot Command Slowmode', slowmode_delay=0)
    await ctx.send('SlowMode disabled')
  
  except:
    await ctx.send('I do not have Permissions')


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
@commands.has_permissions(manage_messages=True)
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

      else:
        return await ctx.send('mission failed\n yes or no should have been said...')
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

      else:
        return await ctx.send('mission failed\n yes or no should have been said...')

    with open('moderation.json','w') as f:
      json.dump(mod,f)

@client.command()
@commands.has_permissions(manage_messages=True)
async def modoff(ctx):

  try:
    with open('moderation.json','r') as f:
      mod = json.load(f)

    del mod[str(ctx.guild.id)]

    with open('moderation.json','w') as f:
      json.dump(mod,f)

    await ctx.send('moderation switched off')

  except KeyError:
    await ctx.send('mod was never on')


@client.command()
@commands.has_permissions(change_nickname=True)
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


@client.command(hidden=True)
@commands.is_owner()
async def cl(ctx,member1:discord.Member,member2:discord.Member,member3:discord.Member):
  await ctx.send(f'`1){member1.name} - 5 points`\n`2){member2.name} - 3 points`\n`3){member3.name} - 1 points`')


@client.command(pass_context=True)
async def giphy(ctx, *, search):
    embed = discord.Embed(colour=discord.Colour.blue())
    session = aiohttp.ClientSession()

    if search == '':
        response = await session.get(f'https://api.giphy.com/v1/gifs/random?api_key={getenv("gify")}')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + f'&api_key={getenv("giphy_key")}')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()

    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def filteron(ctx):
  await ctx.send('Please send a list of words u want to filter and dont forget to put commas between them with no space... (ex: hi,bye) but these should be bad words u wanna filter...')

  def check(m):
        return ctx.author == m.author

  # def check(m):
  #   return m.author==ctx.author

  # msg = await client.wait_for('message',check=check)

  # # try:
  # filtered1 = list(msg.content.split(','))
  # with open('filter.json','r') as f:
  #   filtered = json.load(f)

  # filtered[ctx.guild.id] = filtered1

  # await ctx.send('DONE')

# except:
#   raise 
  #await ctx.send('an error occured\ntry again or check your message..')

  with open('filter.json','r') as f:
    mod = json.load(f)

  try:

      del mod[str(ctx.guild.id)] 
      mod[str(ctx.guild.id)] = []
    
      messaze = await client.wait_for('message',check=check)

      mod[str(ctx.guild.id)].append(list(messaze.content.split(',')))

      await ctx.send('What message do you want to send if they use a word in the filterred words?')
      messaxe = await client.wait_for('message',check=check)

      mod[str(ctx.guild.id)].append(messaxe.content)


      await ctx.send('Do you want me to DM the user or put it in the server\ntype `yes` for dm and `no` for not')
      checking = await client.wait_for('message',check=check)
      if checking.content.lower() == 'yes' or checking.content.lower() == 'y':
        await ctx.send('sending message via DM activated')
        mod[str(ctx.guild.id)].append('yes')

      elif checking.content.lower() == 'no' or checking.content.lower() == 'n':
        await ctx.send('sending message via server activated')
        mod[str(ctx.guild.id)].append('no')

      else:
        return await ctx.send('mission failed\n yes or no should have been said...')
    
  except:
      mod[str(ctx.guild.id)] = []
    
      messaze = await client.wait_for('message',check=check)

      mod[str(ctx.guild.id)].append(list(messaze.content.split(',')))

      await ctx.send('What message do you want to send if they use a word in the filtered words?')
      messaxe = await client.wait_for('message',check=check)

      mod[str(ctx.guild.id)].append(messaxe.content)


      await ctx.send('Do you want me to DM the user or put it in the server\ntype `yes` for dm and `no` for not')
      checking = await client.wait_for('message',check=check)
      if checking.content.lower() == 'yes' or checking.content.lower() == 'y':
        await ctx.send('sending message via DM activated')
        mod[str(ctx.guild.id)].append('yes')

      elif checking.content.lower() == 'no' or checking.content.lower() == 'n':
        await ctx.send('sending message via server activated')
        mod[str(ctx.guild.id)].append('no')

      else:
        return await ctx.send('mission failed\n yes or no should have been said...')

  with open('filter.json','w') as f:
      json.dump(mod,f)

@client.command()
@commands.has_permissions(manage_messages=True)
async def filteroff(ctx):

  try:
    with open('filter.json','r') as f:
      mod = json.load(f)

    del mod[str(ctx.guild.id)]

    with open('filter.json','w') as f:
      json.dump(mod,f)

    await ctx.send('filtering switched off')

  except KeyError:
    await ctx.send('mod was never on')

def mask_circle(im):
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    im.putalpha(mask)

    return im

@client.command()
async def note(ctx,member:discord.Member=None, *,text = "No text entered"):

    if member == None:
      member = ctx.author

    im = Image.open ("note.png")

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("Pacifico.ttf", 30)

    draw.text((396,511), text, (0,0,0),font = font)
    
    asset = member.avatar_url_as(format=None, static_format='jpg', size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    asset2 = ctx.author.avatar_url_as(format=None, static_format='jpg', size=128)
    data2 = BytesIO(await asset2.read())
    pfp2 = Image.open(data2)
    pfp = pfp.resize((198,209))
    mask_circle(pfp)
    pfp2 = pfp2.resize((96, 93))
    mask_circle(pfp2)
    # im.paste(pfp, (108, 388))
    im.alpha_composite(pfp, dest=(108,388))
    pfp = pfp.resize((97,97))
    mask_circle(pfp)
    # im.paste(pfp, (488, 20))
    # im.paste(pfp2, (122, 48))
    im.alpha_composite(pfp, dest=(488,20))
    im.alpha_composite(pfp2, dest=(122,48))
    im.save("noteoutput.png")

    await ctx.send(file = discord.File("noteoutput.png"))


@client.command()
async def worthless(ctx, victim : Optional[discord.User] = None, message : str = None):
    im = Image.open ("meme.jpg")

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("Pacifico.ttf", 20)
    if victim == None:

      draw.text((98,93), message, (0,0,0),font = font)
      
      im = convert_mode(im)
      asset = ctx.author.avatar_url_as(format=None, static_format='png', size=128)
      data = BytesIO(await asset.read())
      pfp = Image.open(data)
      pfp = convert_mode(pfp)
      pfp = pfp.resize((117, 117))
      mask_circle(pfp)
      im.alpha_composite(pfp, dest=(157,304))
      im.save("worthless1.png")

      return await ctx.send(file = discord.File("worthless1.png"))

    else:
      #draw.text((98,93), message, (0,0,0),font = font)
      
      im = convert_mode(im)
      asset = ctx.author.avatar_url_as(format=None, static_format='png', size=128)
      data = BytesIO(await asset.read())
      pfp = Image.open(data)
      pfp = convert_mode(pfp)
      pfp = pfp.resize((117, 117))
      asset2 = victim.avatar_url_as(format=None, static_format='png', size=128)
      data2 = BytesIO(await asset2.read())
      pfp2 = Image.open(data2)
      pfp2 = convert_mode(pfp2)
      pfp2 = pfp2.resize((131, 131))
      mask_circle(pfp)
      mask_circle(pfp2)
      im.alpha_composite(pfp, dest=(157,304))
      im.alpha_composite(pfp2, dest=(139,81))
      im.save("worthless1.png")

      return await ctx.send(file = discord.File("worthless1.png"))
def convert_mode(im):
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
        im.putalpha(255)
    return im

@client.command()
async def inspired(ctx,member:discord.Member=None, *,text = "No text entered"):

    if member == None:
      member = ctx.author

    im = Image.open ("inspired.png")

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("Pacifico.ttf", 20)

    draw.text((93,613), text, (0,0,0),font = font)
    
    asset = member.avatar_url_as(format=None, static_format='jpg', size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    mask_circle(pfp)
    pfp = pfp.resize((170,170))
    mask_circle(pfp)
    im.alpha_composite(pfp, dest=(724,731))
    im.save("inspiredoutput.png")

    await ctx.send(file = discord.File("inspiredoutput.png"))


@client.command()
async def brain(ctx,text1=None,text2=None,text3=None,text4=None):

    

      if text1 == None or text2 == None or text3 == None or text4 == None:
          text1 = 'You Need'
          text2 = '4 Values'
          text3 = 'Seperated by '
          text4 = 'Spaces'

          im = Image.open ("brain.png")

          draw = ImageDraw.Draw(im)
          font = ImageFont.truetype("Pacifico.ttf", 15)

          draw.text((6, 4), text1, (0,0,0),font = font)
          draw.text((6, 73), text2, (0,0,0),font = font)
          draw.text((6, 141), text3, (0,0,0),font = font)
          draw.text((6, 204), text4, (0,0,0),font = font)
          
          im.save('brained.png')

          return await ctx.send(file = discord.File("brained.png"))


      im = Image.open ("brain.png")

      draw = ImageDraw.Draw(im)
      font = ImageFont.truetype("Pacifico.ttf", 15)

      draw.text((6, 16), text1, (0,0,0),font = font)
      draw.text((6, 83), text2, (0,0,0),font = font)
      draw.text((6, 150), text3, (0,0,0),font = font)
      draw.text((6, 211), text4, (0,0,0),font = font)
      
      im.save('brained.png')

      await ctx.send(file = discord.File("brained.png"))

    




@client.command()
async def savehumanity(ctx, *,text = "No text entered"):

   

    im = Image.open ("savee.png")

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("Pacifico.ttf", 20)

    draw.text((488,446), text, (0,0,0),font = font)

    im.save("savehumanty.png")

    await ctx.send(file = discord.File("savehumanty.png"))


@client.command()
async def trash(ctx,member:discord.Member=None):
  if member == None:
    member = ctx.author

  im = Image.open('trash.png')

  asset = member.avatar_url_as(format=None, static_format='jpg', size=128)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pfp = pfp.filter(ImageFilter.BLUR)
  pfp = pfp.resize((480,480))

  im.paste(pfp, (480,0))

  im.save('trashed.png')

  await ctx.send(file=discord.File('trashed.png'))

  
@client.command()
async def saymyname(ctx,member:discord.Member=None,*,name=None):


    if name == None:
      return await ctx.send('Send the name and the person who tells your name')

    text = 'Say My Name'
    text1 = "You're goddamn right!"

    im = Image.open ("saymyname.png")

    im = convert_mode(im)

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("Pacifico.ttf", 20)

    draw.text((16,133), text, (0,0,0),font = font)
    draw.text((5,660), text1, (0,0,0),font = font)
    draw.text((291,318), name, (0,0,0),font = font)
    
    asset = member.avatar_url_as(format=None, static_format='jpg', size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    mask_circle(pfp)
    pfp = pfp.resize((101,125))
    mask_circle(pfp)

    asset2 = ctx.author.avatar_url_as(format=None, static_format='jpg', size=128)
    data2 = BytesIO(await asset2.read())
    pfp2 = Image.open(data2)
    mask_circle(pfp2)
    pfp2 = pfp2.resize((187,206))
    mask_circle(pfp2)

    im.alpha_composite(pfp, dest=(158,260))
    im.alpha_composite(pfp2, dest=(260,0))
    pfp2 = pfp2.resize((231,220))
    im.alpha_composite(pfp2, dest=(218,469))
    im.save("sayed.png")

    await ctx.send(file = discord.File("sayed.png"))
  

@client.command()
async def internal(ctx,member:discord.Member=None):


    if member == None:
      member=ctx.author


    im = Image.open ("internal.jpg")

    im = convert_mode(im)
    
    asset = member.avatar_url_as(format=None, static_format='jpg', size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((71,101))
    mask_circle(pfp)
    im.alpha_composite(pfp, dest=(323,45))
    pfp = pfp.resize((71,101))
    mask_circle(pfp)
    im.alpha_composite(pfp, dest=(323,311))
    pfp = pfp.resize((119,129))
    mask_circle(pfp)
    im.alpha_composite(pfp, dest=(278,525))
    im.save('internalled.png')

    await ctx.send(file=discord.File('internalled.png'))


@client.command(aliases=['NUKE','Nuke'])
@commands.has_permissions(manage_messages=True)
async def nuke(ctx):
  mannel = await ctx.channel.clone()
  await ctx.channel.delete()
  message = await mannel.send(f'Nuked channel by command from {ctx.author.mention}')
  await asyncio.sleep(10)
  await message.delete()

@client.command()
async def spoiler(ctx,*,arg):
  spoilers = list(arg)
  newlist = []
  for i in spoilers:
    newlist.append(f'||{i}||')

  await ctx.send(''.join(newlist))

@client.command(aliases=['triggered'])
async def trigger(ctx, *,user=None):

		if user:
				try:
						user = await commands.converter.MemberConverter().convert(ctx,user)
				except:
						await ctx.send(f"I don\'t know {user}, lets just use your avatar ...")
						user = ctx.author
		else:
				user = ctx.author

		getVars = {'avatar': user.avatar_url_as(format='png')}
		url = 'https://some-random-api.ml/canvas/triggered/?'
		response = requests.get(
				url + urllib.parse.urlencode(getVars), stream=True)

		if response.status_code != 200:
				await ctx.send('Well ... that did not work for some reason.')
				return

		response.raw.decode_content = True
		with open('triggered.gif', 'wb') as out_file:
				shutil.copyfileobj(response.raw, out_file)
		del response

		await ctx.send(file=discord.File('triggered.gif'))

@client.command()
async def humans(ctx):
  await ctx.send(f'{len([i for i in ctx.guild.members if not i.bot])} Humans in {ctx.guild.name}')

@client.command()
async def bots(ctx):
  await ctx.send(f'{len([i for i in ctx.guild.members if i.bot])} Bots in {ctx.guild.name}')

@client.command()
async def prank(ctx):
  await ctx.send(f'Are you sure you want to delete {ctx.guild.name}? send yes or no')
  def check(m):
    return m.author == ctx.author
  lolz = await client.wait_for('message',check=check)
  if lolz.content.lower() == 'yes':
    await ctx.send('Deleting server...')
    await ctx.guild.owner.send('You server Was deleted...')

@client.command(aliases=['findMyFriend'])
async def fmf(ctx,member:discord.Member):
  await ctx.send(f'{member.mention} is {ctx.author.name} close to you?\nDo you approve me of showing him servers common between us both?\ntype `yes` or `y` to approve...')
  def check(m):
    return m.author == member

  approval = await client.wait_for('message',check=check)
  if approval.content.lower() == 'yes' or approval.content.lower() == 'y':
    edit = await ctx.send('Looking at my servers...')
    nope = []
    for i in client.guilds:
      if member in i.members and ctx.author not in i.members:
        nope.append(i.name)
      else:
        continue

    await edit.edit(content='Looking if he is there in any of my servers...')
    await asyncio.sleep(3)
    await edit.edit(content='Looking if you arent there in that server...')
    await asyncio.sleep(3)
    await edit.edit(content=f'Process executed Check your DM {ctx.author.name}')
    await edit.add_reaction('\u2705')
    if nope == []:
      await ctx.author.send('He is there in all servers you are there where I am...')

    else:
      embed=discord.Embed(title='The servers...',colour=discord.Colour.blue())
      count = 1
      for m in nope:
        embed.add_field(name=count,value=m)
        count+=1

      await ctx.author.send(embed=embed)

  else:
    await ctx.send('OOF! you got rejected...')

@client.command()
@commands.has_permissions(view_audit_log=True)
async def audit(ctx,num:int=5):
  if num>10:
    return await ctx.send('Too many will create spam make sure your num is less than 10')
  embed=discord.Embed(title='Latest Audit Logs...',colour=discord.Colour.blue())
  async for entry in ctx.guild.audit_logs(limit=num):
    if isinstance(entry.target, discord.Object): 
      blah = entry.target.id

    else:
      blah = entry.target

    embed.add_field(name='\u200b',value=f'{entry.user} did {str(entry.action).split(".")[1]}  to {blah}')

  await ctx.send(embed=embed)
    
@client.command(aliases=['SLM','Slm','slm'])
async def setleavemessage(ctx):
  await ctx.send('What is the message you want to send??\n***TYPE THE SUFFIX***(the message will start as a mention to the member...)\nSo example type `has left` unless you wanna send in DM')
  def check(m):
    return m.author == ctx.author
  message1 = await client.wait_for('message',check=check)
  with open('leave.json','r') as f:
    lolz = json.load(f)

  try:
    del lolz[str(ctx.guild.id)]
    lolz[str(ctx.guild.id)] = [message1.content]
    await ctx.send('Do you want me to send it in a channel or dms???,type `yes` for channel and `no` for dms')
    message2 = await client.wait_for('message',check=check)
    if message2.content.lower() == 'yes':
      await ctx.send('Send the channel ID for sending the message')
      id = await client.wait_for('message',check=check)
      id = int(id.content)
      list1 = []
      for i in ctx.guild.channels:
        list1.append(int(i.id))
      if id in list1:

          lolz[str(ctx.guild.id)].append(id)
          
          with open('leave.json','w') as f:
            json.dump(lolz,f)
          return await ctx.send('Process Completed!!!')

      return await ctx.send('Invalid ID provided')
    elif message2.content.lower() == 'no':
      lolz[str(ctx.guild.id)].append('DM')
      with open('leave.json','w') as f:
          json.dump(lolz,f)

  except:
    lolz[str(ctx.guild.id)] = [message1.content]

    await ctx.send('Do you want me to send it in a channel or dms???,type `yes` for channel and `no` for dms')
    message2 = await client.wait_for('message',check=check)
    if message2.content.lower() == 'yes':
      await ctx.send('Send the channel ID for sending the message')
      id = await client.wait_for('message',check=check)
      id = int(id.content)
      list1 = []
      for i in ctx.guild.channels:
        list1.append(int(i.id))
      if id in list1:

          lolz[str(ctx.guild.id)].append(id)
          
          with open('leave.json','w') as f:
            json.dump(lolz,f)
          return await ctx.send('Process Completed!!!')

      return await ctx.send('Invalid ID provided')

    elif message2.content.lower() == 'no':
      lolz[str(ctx.guild.id)].append('DM')
      with open('leave.json','w') as f:
            json.dump(lolz,f)

    else:
      return await ctx.send('yes or no should have been said')

@client.command()
async def tips(ctx):
  await ctx.send('')

@client.command()
@commands.has_permissions(manage_messages=True)
async def lock(ctx,channelid:int=None):
  if channelid == None:
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    return await ctx.send(f'Unlocked <#{ctx.channel.id}>')
  for i in ctx.guild.channels:
    if i.id == channelid:
      break
    else:
      continue
  await ctx.send(f'Locked <#{i.channel.id}>')
  await i.set_permissions(ctx.guild.default_role, send_messages=False)

@client.command()
@commands.has_permissions(manage_messages=True)
async def unlock(ctx,channelid:int=None):
  if channelid == None:
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)

    await ctx.send(f'Unlocked <#{ctx.channel.id}>')
    return
  for i in ctx.guild.channels:
    if i.id == channelid:
      break
    else:
      continue
  await ctx.send(f'Unlocked <#{ctx.channel.id}>')
  await i.set_permissions(ctx.guild.default_role, send_messages=True)


keep_alive()


client.run(getenv('TOKEN'))