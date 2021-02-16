import discord
from os import getenv 
from discord.ext import commands, tasks
# from discore import Utils
# from discore.ImageManipulation import ImageManipulation
from itertools import cycle
from keep_alive import keep_alive
import os
# import discore.Utils as dsu
from PIL import Image
from io import BytesIO
import youtube_dl

from youtube_search import YoutubeSearch



intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = '~~',
intents=intents, owner_ids={793433316258480128})
status = cycle(['Gaara|Ping for more info','Gaara|Ping for more info'])
client.sniped_messages = {}
client.load_extension('jishaku')

client.remove_command("help")
global chat, chat_author_id
chat = 0
chat_author_id = 0

@client.event
async def on_ready():
  
    


  change_status.start()
  print('Bot is ready')

@client.event
async def on_message(message):

  if message.author == client.user:
    return


  prefix = '~'
  func_name = message.content.split(' ')[0].replace(prefix, '')
  # IM = ImageManipulation(message, client, prefix + func_name)
  # try:
  # 	await message.channel.send(file=discord.File(await eval(f'IM.{func_name}()')))
  # except:
  #   None
	
  if message.content.lower() == 'no u':
     await message.channel.send('no u')
#Entropy was here!
  # if message.content.lower() == 'lol' or message.content.lower() == 'lmao':
  #    await message.channel.send('lol so funny hahaha')

  # if message.content.lower() == 'hi':
  #    await message.channel.send('HI DA')

  # if message.content.lower() == 'bye':
  #    await message.channel.send('bye! May the force be with you')

  if message.content == f'<@!{client.user.id}>':
      

      embed=discord.Embed(colour=discord.Colour.blue())
      embed.set_author(name='My command prefix is `~~`,type `~~help` for more info',icon_url=message.author.avatar_url)
      await message.channel.send(embed=embed)
	
  await client.process_commands(message)

@client.event
async def on_member_remove(member):
	embed=discord.Embed(title='We will miss you...',description='Hope you come back',colour=discord.Colour.blue())
	embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAO9PYZJ_QJye90N9bgbnp0CiUXM5SkvyDVA&usqp=CAU')
	await member.send(embed=embed)


@client.event
async def on_member_join(member):
  #await member.channel.send(f'{member.mention} left the server')
  embed=discord.Embed(title='Welcome to Our Group',description='Hope you Enjoy here',colour=discord.Colour.blue())
  embed.set_image(url='https://image.freepik.com/free-vector/colorful-welcome-composition-with-origami-style_23-2147907810.jpg')

  await member.send(embed=embed)


# @client.event
# async def on_message(message):

#   if message.author == client.user:
#     return

#   prefix = '~'
#   func_name = message.content.split(' ')[0].replace(prefix, '')
#   IM = ImageManipulation(message, client, prefix + func_name)
#   try:
#     await message.channel.send(file=discord.File(await eval(f'IM.{func_name}()')))
#   except:
#     pass


@tasks.loop(seconds=3600)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
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
  client.sniped_messages[message.guild.id] = (message.content,message.author,message.channel.name,message.created_at)


@client.command()
async def snipe(ctx):
  contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]

  embed=discord.Embed(description = contents, colour=discord.Colour.blue(),timestamp=time)
  embed.set_author(name=f'{author.name}#{author.discriminator}',icon_url=author.avatar_url)
  embed.set_footer(text=f'Deleted in : #{channel_name}')
  await ctx.send(embed=embed)
  
  await ctx.send(f'{author.name} has beened sniped 🔫')


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

# @client.command()
# async def getemoji(ctx, *, message: str):

#     msg = dsu.getemoji(message, ctx.message.guild.emojis)
    
#     try:
#         await ctx.send(msg)
#     except:
#         await ctx.send('No Emoji Found')

@client.command()
async def joinvc(ctx):
  
  #author = ctx.message.author
  channel = client.get_channel(ctx.message.author.voice.channel.id)
  await channel.connect()


queue = {}
@client.command()
async def play(ctx,*,DASONG):
  await ctx.message.add_reaction('\U0001f60e')
  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
  await ctx.send("DASONG IS: "+DASONG)
  results = YoutubeSearch(DASONG, max_results=1).to_dict()
  


  with youtube_dl.YoutubeDL({}) as ytdl:
    x = ytdl.extract_info("https://youtube.com/watch?v="+results[0]['id'], download=False)
    # await ctx.send(str(x['title']))
    # await ctx.send(str(x['channel']))
    # await ctx.send(str(x['duration']))
    # #await ctx.send(str(x['views']))
    # await ctx.send(f'https://youtube.com/watch?v={str(x["url_suffix"])}')
    discord.FFmpegPCMAudio(x['formats'][0]['url'])

    for i in client.voice_clients:
      if i.guild == ctx.guild:
        
        if i.is_playing():
          # await ctx.send('Song added to queue!')
          # try:
          #   if type(queue[ctx.guild.id]) == list:
          #     queue[ctx.guild.id].append(DASONG)
          # except KeyError:
          #   queue.update({ctx.guild.id:[DASONG]})
          pass
          
        else: 
          i.play(discord.FFmpegPCMAudio(x['formats'][0]['url'],**FFMPEG_OPTIONS))

          # resultsqueue = YoutubeSearch(DASONG, max_results=1).to_dict()


          # with youtube_dl.YoutubeDL({}) as ytdl:
          #   x = ytdl.extract_info("https://youtube.com/watch?v="+resultsqueue[0]['id'], download=False)
          #   discord.FFmpegPCMAudio(x['formats'][0]['url'])
        
          # i.play(discord.FFmpegPCMAudio(x['formats'][0]['url']))

        
  

@client.command()
async def leave(ctx):
  
  #author = ctx.message.author
  channel = client.voice_client_in(ctx.message.author.guild)
  await channel.disconnect()


# nav = Navigation(":discord:743511195197374563", "👎", "\U0001F44D")
# color = discord.Color.dark_gold()

# client.help_command = PrettyHelp(navigation=nav, color=color, active_time=60) 


keep_alive()


client.run(getenv('TOKEN'))