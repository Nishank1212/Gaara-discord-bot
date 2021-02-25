import discord
from discord.ext import commands
import json

class Help(commands.Cog):
  def __init__(self,client):
    self.client = client


  @commands.command(aliases=['HELP','Help'])
  async def help(self,ctx,choice=None):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    pre = prefixes[str(ctx.guild.id)]

    if choice == None:

      embed=discord.Embed(title='Help Me!',description='this command helps you by providing you commands',colour=discord.Colour.blue())
      embed.add_field(name='Type these for more information',value='`help general`\n`help starwars`\n`help fun`\n`help games`\n`help animals`\n`help admin`\n`help ChatBot`\n`help economy`\n`help rank`\n`help music`\n`help bot`')
      # embed.set_image(url='https://thumbs.dreamstime.com/b/help-me-abstract-colorful-background-bokeh-design-illustration-isolated-yellow-red-banner-154777299.jpg')
      embed.set_footer(text=f'Use command prefix "{pre}" ')
      await ctx.send(embed=embed)

    elif choice.lower() == 'general':

      embed=discord.Embed(title='Help General',description='This shows all the general commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='`welcome - Welcomes a person to the group`\n`hi - Says hi to a person`\n`Avatar - Sends the avatar of a person`\n`intro - Introduces the bot`\n`totalcmds - says the total number of commands in the bot`\n`ping - Sends the latency of bot`\n`say - Says what you want Grogu to say`\n`invert - Inverts the colours of the avatar of specified person`\n`wasted - Wastes a picture of any persons avatar you choose`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUUE1iPh_mNvgXUQi7oQ2rhJ-0Enf5NZWrrA&usqp=CAU')
      embed.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)

  
      embed.add_field(name='cmds part 2',value='`invertgrey - inverts a persons avatar to grey scale`\n`blue - gives a blue tint of an avatar of a member`\n`bright - brightens the colours of the members avatar`\n`bye - says bye to a person`\n`remind - reminds you by pinging after specific amount of time`\n`userinfo - sends info about a person`\n`serverinfo - sends info about server`\n`mem - Shares the total amount of people in the server`\n`credits - shows the credits of the bot`\n`botinfo -tells about the bot`\n`lenny - returns a lenny face`',inline='False')
      await ctx.send(embed=embed)
     

  

    elif choice.lower() == 'fun':
      embed=discord.Embed(title='Help Fun',description='This shows all the fun commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='`joke - Sends a joke to server`\n`meme - Sends a meme to server`\n`Good Joke - Sends a good joke :D`\n`pat - Sends a pat`\n`spoonfeeding - Sends something about spoonfeeding`\n`8ball - Ask a yes or no question! Gaara will answer`\n`inspire - Sends a inspirational quote`\n`spam - spams what you want it to spam`\n`DM - dms anyone you want to`\n`slap - slaps a person`\n`stab-stabs a person`\n`rip - kills a person`\n`gaara - send info on gaara`\n`hehe boi- sends a pic of hehe boi`\n`khopi told - sends a pic of khopdi told`\n`shoot - shoots a person`\n`snipe - shows the last deleted message`\n`admin - sends a pic of 5 people(need to mention all)`\n`team - sends a pic of 8 people(all need to be mentioned or cmd wont work)`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGC0ViA9_darzbBsNjkPGGZBi8nKlIiOdQlA&usqp=CAU')
      embed.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    elif choice.lower() == 'games':
      embed=discord.Embed(title='Help Games',description='This shows all the game commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='`RPS - Plays rock paper scissors against the bot`\n`guess - The bot thinks of a number which yo have to guess`\n`dice - plays a game of dice with the bot`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPiIQ8l8Lwm98IWfUgkE14lvRcBRasyUHdbA&usqp=CAU')
      embed.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    elif choice.lower() == 'starwars':
      embed=discord.Embed(title='Help Star Wars',description='This shows all the star wars commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='`starwarsdialogues`\n`starwars  - shows info on famous characters on starwars(working..)`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRF1LrwuUhm18xvpPQcqjcD_fs9z2f9DF2_cQ&usqp=CAU')
      embed.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    elif choice.lower() == 'animals':
      embed=discord.Embed(title='Help Animals',description='This shows all the animal commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='`cat - Shows a picture of a cat`\n`dog - Shows a picture of a dog`\n`fox - shows a picture of a fox`\n`panda - shows a picture or a panda`\n`koala - shows a picture of a koala`\n`bird - shows a picture of a bird`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVgy78TcDxVTIpbrcmFGkzgWaeZM0sCcgUAw&usqp=CAU')
      embed.set_footer(text=f'Use command prefix "{pre}"',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    elif choice.lower() == 'admin':
      embed=discord.Embed(title='Help Admin',description='admin commands',colour=discord.Colour.blue())
      embed.add_field(name='commands...',value='`kick - Kicks a person out of server`\n`ban - Bans a person from the server`\n`unban - Unbans a person from a server if he is banned`\n`warn - warns a person(5 warns = banned)`\n`case - shows how many warns`\n`cw - clears all warns`\n`setprefix - sets the prefix to anything you want`\n`addrole - adds a role to any person`\n`unrole - removes a role from a person`')
      embed.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    elif choice.lower() == 'chatbot':
      embed=discord.Embed(title='Help ChatBot',description='ChatBot commands',colour=discord.Colour.blue())
      embed.add_field(name='commands...',value='`chatenable - starts an ai based chatbot with which u can talk too`\n`chatdisable - stops the chat if it is enabled, note: you can also type "gaara go to sleep(without prefix)" and it wil stop`')
      embed.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    elif choice.lower() == 'economy':
      embed=discord.Embed(title='Help Economy',description='Economy commands',colour=discord.Colour.blue())
      embed.add_field(name='commands...',value='`bal - tells the balance of a person`\n`beg - begs a person for an amount`\n`dep - deposits an amount to the bank`\n`with - withdraws an amount from bank`\n`slots - plays slots and u can bet a money on it also`\n`rob - robs any person`\n`search - searches for money`\n`give - gives money to any person you choose`\n`buy - buy an object from shop`\n`fish - fishes`\n`hunt - hunts for animals`\n`sell - you can sell any animal or fish via this cmd`\n`inv - shares the inventory of a person`\n`shop - shows the shop`\n`postmeme - posts a meme`\n`gamble - gambles an amount you choose`')
      embed.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    elif choice.lower() == 'rank':
      embed=discord.Embed(title='Help Rank',description='Rank commands',colour=discord.Colour.blue())
      embed.add_field(name='commands...',value='`rank - shows the rank of a person`\n`leaderboard - shows the leaderboard of top 5 people`')
      embed.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    elif choice.lower() == 'music':
      embed=discord.Embed(title='Help Music',description='Music commands',colour=discord.Colour.blue())
      embed.add_field(name='commands...',value='`join - joins vc of the vc u r in`\n`leave - leaves the vc it is in`\n`play - plays a song`\n`skip - skips the current song`\n`queue - shows ur queue`\n`pause - pauses the song`\n`resume - resumes the song`\n`stop - stops the song and clears your queue`')
      embed.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
    elif choice.lower() == 'bot':
      embed=discord.Embed(title='Help bot',description='Info commands',colour=discord.Colour.blue())
      embed.add_field(name='commands...',value="`server - joins officialserver of bot`\n`invite - invite Gaara to your server`\n`GitHub - see Gaara's GitHub page and star repo`")
      embed.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

    else:
      await ctx.send(f'No help command found try typing ***{pre}help*** for more info')


  # @commands.command()
  # async def help2(self,ctx):
  #   helptext = "`"
  #   for command in self.client.commands:
  #       helptext+=f"{command}\n"
  #   helptext+="`"
  #   await ctx.send(helptext)


  

def setup(client):
  client.add_cog(Help(client))	