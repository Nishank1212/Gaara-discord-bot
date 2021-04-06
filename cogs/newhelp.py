import discord
from discord.ext import commands
import json
import asyncio

class Help(commands.Cog):
  def __init__(self,client):
    self.client = client


  @commands.command()
  async def help(self,ctx):

      try:
        with open('prefixes.json','r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)]

      except:
        pre = '~~'

  

      embed=discord.Embed(title='Help Me!',description='this command helps you by providing you commands',colour=discord.Colour.blue())
      embed.add_field(name='Type these for more information',value='`help general`\n`help fun`\n`help games`\n`help animals`\n`help admin`\n`help ChatBot`\n`help economy`\n`help rank`\n`help music`\n`help bot`\n`help image`')
      # embed.set_image(url='https://thumbs.dreamstime.com/b/help-me-abstract-colorful-background-bokeh-design-illustration-isolated-yellow-red-banner-154777299.jpg')
      embed.set_footer(text=f'Use command prefix "{pre}" ')
      #await ctx.send(embed=embed)

    #elif choice.lower() == 'general':

      embed11=discord.Embed(title='Help General',description='This shows all the general commands',colour=discord.Colour.blue())
      embed11.add_field(name='Commands',value=f'`welcome - Welcomes a person to the group`\n`hi - Says hi to a person`\n`Avatar - Sends the avatar of a person`\n`intro - Introduces the bot`\n`totalcmds - says the total number of commands in the bot`\n`ping - Sends the latency of bot`\n`say - Says what you want Grogu to say`\n`calc-calculates an expression`\n`lyrics - shares the lyrics of the song`\n`ascii - asciis any text`\n`wiki = searches anything in wikipedia`\n`edits - shows the last edit in server`\n`bots - shares the number of bots in server`\n`humans - shares the number of humans in server`\n`date - shares the date of today`\n`setbb - if my birthday is 1st feb i will type like {pre}setbb 02-01 Note:the monthh will be first and day second `')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUUE1iPh_mNvgXUQi7oQ2rhJ-0Enf5NZWrrA&usqp=CAU')
      embed11.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)

      embed111=discord.Embed(title='Help Meme',description='This shows all the Meme commands',colour=discord.Colour.blue())
      embed111.add_field(name='There are over 100 meme generator fun commands!!! To get these Simply type:',value='`meme_list`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUUE1iPh_mNvgXUQi7oQ2rhJ-0Enf5NZWrrA&usqp=CAU')
      embed111.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)

      embed112=discord.Embed(title='Help Giveaway',description='This shows all the giveaway commands',colour=discord.Colour.blue())
      embed112.add_field(name='only reroll and  start command:',value='`start - type it like this:`\n`~~start <some number> {hour/second/minute/day}<required role(optional)> <for what?>`\n`note:do not include the <> and {} and []`\n`reroll - reroll <message id>`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUUE1iPh_mNvgXUQi7oQ2rhJ-0Enf5NZWrrA&usqp=CAU')
      embed112.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)

  
      embed11.add_field(name='cmds part 2',value='`bye - says bye to a person`\n`remind - reminds you by pinging after specific amount of time`\n`reminders - Will show you your current reminders`\n`userinfo - sends info about a person`\n`serverinfo - sends info about server`\n`mem - Shares the total amount of people in the server`\n`credits - shows the credits of the bot`\n`botinfo -tells about the bot`\n`lenny - returns a lenny face`\n`swd - returns star wars dialogues`',inline='False')
      #await ctx.send(embed=embed)
     

  

    #elif choice.lower() == 'fun':
      embed10=discord.Embed(title='Help Fun',description='This shows all the fun commands',colour=discord.Colour.blue())
      embed10.add_field(name='Commands',value='`joke - Sends a joke to server`\n`meme - Sends a meme to server`\n`Good Joke - Sends a good joke :D`\n`pat - Sends a pat`\n`spoonfeeding - Sends something about spoonfeeding`\n`8ball - Ask a yes or no question! Gaara will answer`\n`inspire - Sends a inspirational quote`\n`DM - dms anyone you want to`\n`gaara - send info on gaara`\n`hehe boi- sends a pic of hehe boi`\n`khopi told - sends a pic of khopdi told`\n`snipe - shows the last deleted message`\n`spoiler - check it out...`\n`fmf - Check out this new command...(fmf <member>)`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGC0ViA9_darzbBsNjkPGGZBi8nKlIiOdQlA&usqp=CAU')
      embed10.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      #await ctx.send(embed=embed)

    #elif choice.lower() == 'games':
      embed9=discord.Embed(title='Help Games',description='This shows all the game commands',colour=discord.Colour.blue())
      embed9.add_field(name='Commands',value='`RPS - Plays rock paper scissors against the bot`\n`guess - The bot thinks of a number which yo have to guess`\n`dice - plays a game of dice with the bot`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPiIQ8l8Lwm98IWfUgkE14lvRcBRasyUHdbA&usqp=CAU')
      embed9.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      #await ctx.send(embed=embed)

    #elif choice.lower() == 'animals':
      embed8=discord.Embed(title='Help Animals',description='This shows all the animal commands',colour=discord.Colour.blue())
      embed8.add_field(name='Commands',value='`cat - Shows a picture of a cat`\n`dog - Shows a picture of a dog`\n`fox - shows a picture of a fox`\n`panda - shows a picture or a panda`\n`koala - shows a picture of a koala`\n`bird - shows a picture of a bird`')
      #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVgy78TcDxVTIpbrcmFGkzgWaeZM0sCcgUAw&usqp=CAU')
      embed8.set_footer(text=f'Use command prefix "{pre}"',icon_url=ctx.author.avatar_url)
      #await ctx.send(embed=embed)

    #elif choice.lower() == 'admin':
      embed7=discord.Embed(title='Help Admin',description='admin commands',colour=discord.Colour.blue())
      embed7.add_field(name='commands...',value='`kick - Kicks a person out of server`\n`ban - Bans a person from the server`\n`unban - Unbans a person from a server if he is banned`\n`warn - warns a person(5 warns = banned)`\n`case - shows how many warns`\n`cw - clears all warns`\n`setprefix - sets the prefix to anything you want`\n`addrole - adds a role to any person`\n`unrole - removes a role from a person`\n`set_welcome_message(swm) - sets a welcome message for new members`\n`set_welcome_channel(swc) - provide a chanel id where it will send the welcome message`\n `create (voice or text) <channelname> - creates a channel`\n`delete - removes the channel`\n`slowmode <num> - enables slow mode for num seconds`\n`modon <num> - after this any person who does more cpas in the message than <num> the message will be deleted`\n`modoff - switches the modon to off`\n`filteron - filter for bad words`\n`filteroff - turns filter off`\n`mute - mutes a person`\n`unmute - unmutes a person`\n`lock - locks the channel you are in`\n`unlock - unlocks the channel u are in`')
      embed7.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      #await ctx.send(embed=embed)

    #elif choice.lower() == 'chatbot':
      

    #elif choice.lower() == 'economy':
      embed5=discord.Embed(title='Help Economy',description='Economy commands',colour=discord.Colour.blue())
      embed5.add_field(name='commands...',value='`bal - tells the balance of a person`\n`beg - begs a person for an amount`\n`dep - deposits an amount to the bank`\n`with - withdraws an amount from bank`\n`slots - plays slots and u can bet a money on it also`\n`rob - robs any person`\n`search - searches for money`\n`give - gives money to any person you choose`\n`buy - buy an object from shop`\n`fish - fishes`\n`hunt - hunts for animals`\n`sell - you can sell any animal or fish via this cmd`\n`inv - shares the inventory of a person`\n`shop - shows the shop`\n`postmeme - posts a meme`\n`gamble - gambles an amount you choose`\n`enable rob - enables rob(disbled by default)`\n`disable rob - disable rob(disbled by default)`')
      embed5.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      #await ctx.send(embed=embed)

    #elif choice.lower() == 'rank':
      embed4=discord.Embed(title='Help Rank',description='Rank commands',colour=discord.Colour.blue())
      embed4.add_field(name='commands...',value='`rank - shows the rank of a person`\n`leaderboard - shows the leaderboard of top 5 people`\n`levelenable - enables leveling system(default switched off)`\n`leveldisable - disables level system (default switched off)`')
      embed4.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      #await ctx.send(embed=embed)

    #elif choice.lower() == 'music':
      embed3=discord.Embed(title='Help Music',description='Music commands',colour=discord.Colour.blue())
      embed3.add_field(name='commands...',value='`join - joins vc of the vc u r in`\n`leave - leaves the vc it is in`\n`play - plays a song`\n`skip - skips the current song`\n`queue - shows ur queue`\n`pause - pauses the song`\n`resume - resumes the song`\n`stop - stops the song and clears your queue`')
      embed3.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      #await ctx.send(embed=embed)

    #elif choice.lower() == 'bot':
      embed2=discord.Embed(title='Help bot',description='Info commands',colour=discord.Colour.blue())
      embed2.add_field(name='commands...',value="`server - joins official server of bot`\n`invite - invite Gaara to your server`\n`GitHub - see Gaara's GitHub page and star repo`")
      embed2.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      #await ctx.send(embed=embed)

    #elif choice.lower() == 'image':
      embed1=discord.Embed(title='Help Image',description='Image commands',colour=discord.Colour.blue())
      embed1.add_field(name='commands...',value="`mando,team(mentions = 8),admin(mentions = 5),slapmore,slap,shoot,stab,bounty,monkey,punch,rip,worthless,note,inspired,savehumanity,brain,trash,saymyname @<member> name,internal,invertgrey,blue,bright,invert,wasted`")
      embed1.set_footer(text=f'Use command prefix "{pre}" ',icon_url=ctx.author.avatar_url)
      # await ctx.send(embed=embed)

  

      contents = [embed11,embed10,embed9,embed8,embed7,embed5,embed4,embed3,embed2,embed1,embed111,embed112]
      pages = 12
      cur_page = 1
      message = await ctx.send(f"Page {cur_page}/{pages}",embed=contents[cur_page-1])
      # getting the message object for editing and reacting

      await message.add_reaction("◀️")
      await message.add_reaction("▶️")
      await message.add_reaction("⏹️")


      def check(reaction, user):
          return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️","⏹️"]
          # This makes sure nobody except the command sender can interact with the "menu"

      while True:
          
              reaction, user = await self.client.wait_for("reaction_add", check=check)
              # waiting for a reaction to be added - times out after x seconds, 60 in this
              # example

              if str(reaction.emoji) == "▶️":
                  if cur_page == pages:
                    cur_page = 1
                    await message.edit(content=f"Page {cur_page}/{pages}",embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)
                  else:

                    cur_page += 1
                    await message.edit(content=f"Page {cur_page}/{pages}",embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

              elif str(reaction.emoji) == "◀️":
                  if cur_page == 1:
                    cur_page = pages
                    await message.edit(content=f"Page {cur_page}/{pages}",embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)
                  else:

                    cur_page -= 1
                    await message.edit(content=f"Page {cur_page}/{pages}",embed = contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

              elif str(reaction.emoji) == "⏹️":
                await message.edit(content='Process Stopped!',embed=None)
                await asyncio.sleep(10)
                await message.delete()
                await ctx.message.delete()
                break
                return

            

  

def setup(client):
  client.add_cog(Help(client))	