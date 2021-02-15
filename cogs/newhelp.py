import discord
from discord.ext import commands

class Help(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['HELP','Help'])
  async def help(self,ctx,choice=None):
    if choice == None:

      embed=discord.Embed(title='Help Me!',description='this command helps you by providing you commands',colour=discord.Colour.blue())
      embed.add_field(name='Type these for more information',value='```help general```\n```help starwars```\n```help fun```\n```help games```\n```help animals```')
      # embed.set_image(url='https://thumbs.dreamstime.com/b/help-me-abstract-colorful-background-bokeh-design-illustration-isolated-yellow-red-banner-154777299.jpg')
      embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
      await ctx.send(embed=embed)

    elif choice.lower() == 'general':

      embed=discord.Embed(title='Help General',description='This shows all the general commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='`1)kick - Kicks a person out of server`\n`2)ban - Bans a person from the server`\n`3)unban - Unbans a person from a server if he is banned`\n`4)welcome - Welcomes a person to the group`\n`5)hi - Says hi to a person`\n`6)Avatar - Sends the avatar of a person`\n`7)intro - Introduces the bot`\n`8)totalcmds - says the total number of commands in the bot`\n`9)ping - Sends the latency of bot`\n`10)say - Says what you want Grogu to say`\n`11)clear - Clears the amount of messages you want from the server`\n`12)invert - Inverts the colours of the avatar of specified person`\n`13)wasted - Wastes a picture of any persons avatar you choose`\n`14)userinfo - sends info about a person`\n`15)serverinfo - sends info about server`\n`16)mem - Shares the total amount of people in the server`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUUE1iPh_mNvgXUQi7oQ2rhJ-0Enf5NZWrrA&usqp=CAU')
      embed.set_footer(text='Use command prefix "~" ')

      emb=discord.Embed(title='Page 2',colour=discord.Colour.blue())
      emb.add_field(name='cmds part 2',value='`16)invertgrey - inverts a persons avatar to grey scale`\n`17)blue - gives a blue tint of an avatar of a member`\n`18)bright - brightens the colours of the members avatar`\n`19)mute - mutes a person from a channel`\n`20)welcome - welcomes a member to the server`\n`21)bye - says bye to a person`\n`22)remind - reminds you by pinging after specific amount of time`',inline='False')
      await ctx.send(embed=embed)
      await ctx.send(embed=emb)

  

    elif choice.lower() == 'fun':
      embed=discord.Embed(title='Help Fun',description='This shows all the fun commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='1)joke - Sends a joke to server\n\n2)meme - Sends a meme to server\n\n2)Good Joke - Sends a good joke :D\n\n4)pat - Sends a pat\n\n5)spoonfeeding - Sends something about spoonfeeding\n\n6)8ball - Ask a yes or no question! Gaara will answer\n\n7)inspire - Sends a inspirational quote\n\n8)spam - spams what you want it to spam\n\n9)DM - dms anyone you want to\n\n10)chatenable - starts an ai based chatbot with which u can talk too\n\n11)addrole - adds any role to any person you want\n\n12)unroll-removes any roll from a person you want\n\n13)slap - slaps a person\n\n14)stab-stabs a person\n\nripp - kills a person\n\n15)gaara - send info on gaara\n\n16)hehe boi- sends a pic of hehe boi\n\n17)khopi told - sends a pic of khopdi told\n\n18)shoot - shoots a person\n\n19)snipe - shows the last deleted message\n\n20)admin - sends a pic of 5 people(need to mention all)\n\n21)team - sends a pic of 8 people(all need to be mentioned or cmd wont work)\n\n22)fight - fights a person')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGC0ViA9_darzbBsNjkPGGZBi8nKlIiOdQlA&usqp=CAU')
      embed.set_footer(text='Use command prefix "~" ')
      await ctx.send(embed=embed)

    elif choice.lower() == 'games':
      embed=discord.Embed(title='Help Games',description='This shows all the game commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='1)RPS - Plays rock paper scissors against the bot\n\n2)guess - The bot thinks of a number which yo have to guess\n\n3)dice - plays a game of dice with the bot')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPiIQ8l8Lwm98IWfUgkE14lvRcBRasyUHdbA&usqp=CAU')
      embed.set_footer(text='Use command prefix "~" ')
      await ctx.send(embed=embed)

    elif choice.lower() == 'starwars':
      embed=discord.Embed(title='Help Star Wars',description='This shows all the star wars commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='1)starwarsdialogues\n\n2)starwars  - shows info on famous characters on starwars(working..)')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRF1LrwuUhm18xvpPQcqjcD_fs9z2f9DF2_cQ&usqp=CAU')
      embed.set_footer(text='Use command prefix "~" ')
      await ctx.send(embed=embed)

    elif choice.lower() == 'animals':
      embed=discord.Embed(title='Help Animals',description='This shows all the animal commands',colour=discord.Colour.blue())
      embed.add_field(name='Commands',value='1)cat - Shows a picture of a cat\n\n2)dog - Shows a picture of a dog\n\n3fox - shows a picture of a fox\n\n4)panda - shows a picture or a panda\n\n5)redpanda - shows a picture of a red panda\n\n6)koala - shows a picture of a koala\n\n7)bird - shows a picture of a bird')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVgy78TcDxVTIpbrcmFGkzgWaeZM0sCcgUAw&usqp=CAU')
      embed.set_footer(text='Use command prefix "~" ')
      await ctx.send(embed=embed)

    else:
      await ctx.send('No help command found try typing ***help***for more info')

  

def setup(client):
  client.add_cog(Help(client))