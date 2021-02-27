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



  # try:
  # 	await message.channel.send(file=discord.File(await eval(f'IM.{func_name}()')))
  # except:
  #   None
	
  if message.content.lower() == 'no u':

    if message.author.id == 793433316258480128:
      await message.channel.send('no u')

#Entropy was here!
  # if message.content.lower() == 'lol' or message.content.lower() == 'lmao':
  #    await message.channel.send('lol so funny hahaha')

  # if message.content.lower() == 'hi':
  #    await message.channel.send('HI DA')

  # if message.content.lower() == 'bye':
  #    await message.channel.send('bye! May the force be with you')

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

      messages = message[str(member.guild.id)]
      print(messages)
     
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

@client.event
async def on_message_delete(message):
  client.sniped_messages[message.guild.id][message.author.id] = (message.content,message.author,message.channel.name,message.created_at)
  client.sniped_messages1[message.guild.id] = (message.content,message.author,message.channel.name,message.created_at)
@client.command()
async def snipe(ctx,member:discord.Member=None):
  

  if member == None:

    try:

      contents, author, channel_name, time = client.sniped_messages1[ctx.guild.id]

      embed=discord.Embed(description = contents, colour=discord.Colour.blue(),timestamp=time)
      embed.set_author(name=f'{author.name}#{author.discriminator}',icon_url=author.avatar_url)
      embed.set_footer(text=f'Deleted in : #{channel_name}')
      await ctx.send(embed=embed)
      
      await ctx.send(f'{author.name} has beened sniped 🔫')

    except:
      await ctx.send('No message to snipe!')

  else:

    try:
      contents, author, channel_name, time = client.sniped_messages[ctx.guild.id][member.id]

      embed=discord.Embed(description = contents, colour=discord.Colour.blue(),timestamp=time)
      embed.set_author(name=f'{member.name}#{member.discriminator}',icon_url=member.avatar_url)
      embed.set_footer(text=f'Deleted in : #{channel_name}')
      await ctx.send(embed=embed)
      
      await ctx.send(f'{member.name} has been sniped 🔫')

    except KeyError:
      await ctx.send('No message found')




@client.command()
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


@client.command()
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

  # letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

  # letter = prefix.split()

  # if letter[-1] in letters:
  #   with open('prefixes.json','r') as f:
  #     prefixes = json.load(f)

  #   prefixes[str(ctx.guild.id)+ ' '] = prefix 

  #   with open('prefixes.json','w') as f:
  #     json.dump(prefixes,f)

  #   await ctx.send(f'The prefix was changed to {prefix}')

  # else:


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
async def ascii(ctx,word):

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

keep_alive()


client.run(getenv('TOKEN'))