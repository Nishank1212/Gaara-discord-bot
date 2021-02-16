import discord
from discord.ext import commands

class Help(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['HELP','Help'])
  async def help(self,ctx,choice=None):
    if choice == None:

      embed=discord.Embed(title='Help Me!',description='this command helps you by providing you commands',colour=discord.Colour.blue())
      embed.add_field(name='Type these for more information',value='```help general```\n```help starwars```\n```help fun```\n```help games```\n```help animals```\n```help admin```\n```help ChatBot```')
      # embed.set_image(url='https://thumbs.dreamstime.com/b/help-me-abstract-colorful-background-bokeh-design-illustration-isolated-yellow-red-banner-154777299.jpg')
      embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
      await ctx.send(embed=embed)

    elif choice.lower() == 'general':

      embed=discord.Embed(title='Help General',description='This shows all the general commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='`welcome - Welcomes a person to the group`\n`hi - Says hi to a person`\n`Avatar - Sends the avatar of a person`\n`intro - Introduces the bot`\n`totalcmds - says the total number of commands in the bot`\n`ping - Sends the latency of bot`\n`say - Says what you want Grogu to say`\n`invert - Inverts the colours of the avatar of specified person`\n`wasted - Wastes a picture of any persons avatar you choose`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUUE1iPh_mNvgXUQi7oQ2rhJ-0Enf5NZWrrA&usqp=CAU')
      embed.set_footer(text='Use command prefix "~~" ',icon_url=ctx.author.avatar_url)

  
      embed.add_field(name='cmds part 2',value='`invertgrey - inverts a persons avatar to grey scale`\n`blue - gives a blue tint of an avatar of a member`\n`bright - brightens the colours of the members avatar`\n`mute - mutes a person from a channel`\n`bye - says bye to a person`\n`remind - reminds you by pinging after specific amount of time`\n`userinfo - sends info about a person`\n`serverinfo - sends info about server`\n`mem - Shares the total amount of people in the server`',inline='False')
      await ctx.send(embed=embed)
     

  

    elif choice.lower() == 'fun':
      embed=discord.Embed(title='Help Fun',description='This shows all the fun commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='`joke - Sends a joke to server`\n`meme - Sends a meme to server`\n`Good Joke - Sends a good joke :D`\n`pat - Sends a pat`\n`spoonfeeding - Sends something about spoonfeeding`\n`8ball - Ask a yes or no question! Gaara will answer`\n`inspire - Sends a inspirational quote`\n`spam - spams what you want it to spam`\n`DM - dms anyone you want to`\n`addrole - adds any role to any person you want`\n`unroll-removes any roll from a person you want`\n`slap - slaps a person`\n`stab-stabs a person`\n`rip - kills a person`\n`gaara - send info on gaara`\n`hehe boi- sends a pic of hehe boi`\n`khopi told - sends a pic of khopdi told`\n`shoot - shoots a person`\n`snipe - shows the last deleted message`\n`admin - sends a pic of 5 people(need to mention all)`\n`team - sends a pic of 8 people(all need to be mentioned or cmd wont work)`\n`fight - fights a person`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGC0ViA9_darzbBsNjkPGGZBi8nKlIiOdQlA&usqp=CAU')
      embed.set_footer(text='Use command prefix "~~" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    elif choice.lower() == 'games':
      embed=discord.Embed(title='Help Games',description='This shows all the game commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='`RPS - Plays rock paper scissors against the bot`\n`guess - The bot thinks of a number which yo have to guess`\n`dice - plays a game of dice with the bot`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPiIQ8l8Lwm98IWfUgkE14lvRcBRasyUHdbA&usqp=CAU')
      embed.set_footer(text='Use command prefix "~~" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    elif choice.lower() == 'starwars':
      embed=discord.Embed(title='Help Star Wars',description='This shows all the star wars commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='`starwarsdialogues`\n`starwars  - shows info on famous characters on starwars(working..)`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRF1LrwuUhm18xvpPQcqjcD_fs9z2f9DF2_cQ&usqp=CAU')
      embed.set_footer(text='Use command prefix "~~" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    elif choice.lower() == 'animals':
      embed=discord.Embed(title='Help Animals',description='This shows all the animal commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='`cat - Shows a picture of a cat`\n`dog - Shows a picture of a dog`\n`fox - shows a picture of a fox`\n`panda - shows a picture or a panda`\n`redpanda - shows a picture of a red panda`\n`koala - shows a picture of a koala`\n`bird - shows a picture of a bird`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVgy78TcDxVTIpbrcmFGkzgWaeZM0sCcgUAw&usqp=CAU')
      embed.set_footer(text='Use command prefix "~~" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    elif choice.lower() == 'admin':
      embed=discord.Embed(title='Help Admin',description='admin commands',colour=discord.Colour.blue())
      embed.add_field(name='commands...',value='`kick - Kicks a person out of server`\n`ban - Bans a person from the server`\n`unban - Unbans a person from a server if he is banned`')
      embed.set_footer(text='Use command prefix "~~" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    elif choice.lower() == 'chatbot':
      embed=discord.Embed(title='Help ChatBot',description='ChatBot commands',colour=discord.Colour.blue())
      embed.add_field(name='commands...',value='`chatenable - starts an ai based chatbot with which u can talk too`\n`chatdisable - stops the chat if it is enabled, note: you can also type "gaara go to sleep(without prefix)" and it wil stop`')
      embed.set_footer(text='Use command prefix "~~" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)


    else:
      await ctx.send('No help command found try typing ***help*** for more info')

  

def setup(client):
  client.add_cog(Help(client))