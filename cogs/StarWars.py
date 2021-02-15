import discord
from discord.ext import commands
import random

class Starwars(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['STARWARSDIALOGUES','StarWarsDialogues','Starwarsdialogues','swd','Swd','SWD','starwarsdialogues'])
  async def star_wars_dialogues(self,ctx):
    dialogues=['Do or donot there is no try','I have the high ground','Hello There!','This is the way','I have spoken','May the force be with you','I can bring you in warm or I can bring you in cold']
    random_dialogue = random.choice(dialogues)
    embed=discord.Embed(title='Star Wars Dialogues',description=random_dialogue, colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=embed)

  @commands.command(aliases=['STARWARS','Starwars','sw','SW','Sw'])
  async def starwars(self,ctx,message,surname=None):
    if message.lower() == 'luke':
      if surname =='skywalker' or surname == 'SKYWALKER' or surname == 'Skywalker' or surname == None:

        embed = discord.Embed(title='Luke Skywalker',description='Star Wars haracter',colour=discord.Colour.blue())
        embed.add_field(name='Info...',value='Luke Skywalker is a fictional character and the main protagonist of the original film trilogy of the Star Wars franchise created by George Lucas. Portrayed by Mark Hamill, Luke first appeared in Star Wars (1977),and he returned in The Empire Strikes Back (1980) and Return of the Jedi (1983). Three decades later, Hamill returned as Luke in the Star Wars sequel trilogy, appearing in all three films: The Force Awakens (2015), The Last Jedi (2017), and The Rise of Skywalker (2019). He reprised the role in The Mandalorian episode "Chapter 16: The Rescue" (2020), voicing the character that was portrayed by a body double with digital de-aging',inline=False)
        embed.add_field(name='More info...',value='He was originally a farmer on Tatooine living with his uncle and aunt, Luke becomes a pivotal figure in the Rebel Alliances struggle against the Galactic Empire. The son of fallen Jedi Knight Anakin Skywalker (turned Sith Lord Darth Vader) and Padmé Amidala, Luke is the twin brother of Rebellion leader Princess Leia and eventual brother-in-law of the smuggler Han Solo. Luke trains to be a Jedi under Jedi Masters Obi-Wan Kenobi and Yoda, and rebuilds the Jedi Order. He later trains his nephew, Ben Solo, and mentors Rey. Though Luke dies at the end of The Last Jedi, he returns as a Force spirit in The Rise of Skywalker, encouraging Rey to face her grandfather, the resurrected Emperor Palpatine.')
        embed.add_field(name='Spoilers',value='At the end of the film, Luke and Leia give Rey their blessing to adopt the Skywalker surname and continue their familys legacy.The character also briefly appears in the prequel film Episode III – Revenge of the Sith as an infant. In the de-canonized Star Wars Expanded Universe (renamed Legends), Luke is a main character in many stories set after Return of the Jedi, which depict him as a powerful Jedi Master, the husband of Mara Jade, father of Ben Skywalker and maternal uncle of Jaina, Jacen and Anakin Solo.',inline=False)
        embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdNayvbbx7DMXHX68tNdsZHBdmW7ZiFN_JGw&usqp=CAU')
        await ctx.send(embed=embed)
      else:
        await ctx.send('DATA NOT FOUND ')

    elif message.lower() == 'anakin':
      if surname =='skywalker' or surname == 'SKYWALKER' or surname == 'Skywalker' or surname == None:
        embed=discord.Embed(title='Anakin Skywalker AKA Darth Vader',description='Star Wars character',colour=discord.Colour.blue())
        embed.add_field(name='Info...',value='Darth Vader is a fictional character in the Star Wars franchise. The character is a primary antagonist in the original trilogy and a primary protagonist in the prequel trilogy. Star Wars creator George Lucas has collectively referred to the first six episodic films of the franchise as "the tragedy of Darth Vader"',inline=False)
        embed.add_field(name='More info...',value='Originally a slave on Tatooine, Anakin Skywalker is a Jedi prophesied to bring balance to the Force. He is lured to the dark side of the Force by Palpatine and becomes a Sith lord. After a lightsaber battle with his former mentor Obi-Wan Kenobi, in which he is severely injured, Vader is transformed into a cyborg. He then serves the Galactic Empire as its chief enforcer until he ultimately redeems himself by saving his son, Luke Skywalker, and killing Palpatine, sacrificing his own life in the process.He is also the secret husband of Padmé Amidala, father of Princess Leia, and grandfather of Kylo Ren.',inline=False)
        embed.add_field(name='Overall',value='Darth Vader has become one of the most iconic villains in popular culture, and has been listed among the greatest villains and fictional characters ever. The American Film Institute listed him as the third greatest movie villain in cinema history on 100 Years... 100 Heroes and Villains, behind Hannibal Lecter and Norman Bates.His role as a tragic hero in the saga was also met with positive reviews.')
        embed.set_image(url='https://images.uncyclomedia.co/uncyclopedia/en/3/3d/Anakinvader.gif')
        await ctx.send(embed=embed)

      else:
        await ctx.send('DATA NOT FOUND')

    elif message.lower() == 'darth':
      if surname == 'VADER' or surname == 'Vader' or surname == 'vader':
        embed=discord.Embed(title='Anakin Skywalker AKA Darth Vader',description='Star Wars character',colour=discord.Colour.blue())
        embed.add_field(name='Info...',value='Darth Vader is a fictional character in the Star Wars franchise. The character is a primary antagonist in the original trilogy and a primary protagonist in the prequel trilogy. Star Wars creator George Lucas has collectively referred to the first six episodic films of the franchise as "the tragedy of Darth Vader"',inline=False)
        embed.add_field(name='More info...',value='Originally a slave on Tatooine, Anakin Skywalker is a Jedi prophesied to bring balance to the Force. He is lured to the dark side of the Force by Palpatine and becomes a Sith lord. After a lightsaber battle with his former mentor Obi-Wan Kenobi, in which he is severely injured, Vader is transformed into a cyborg. He then serves the Galactic Empire as its chief enforcer until he ultimately redeems himself by saving his son, Luke Skywalker, and killing Palpatine, sacrificing his own life in the process.He is also the secret husband of Padmé Amidala, father of Princess Leia, and grandfather of Kylo Ren.',inline=False)
        embed.add_field(name='Overall',value='Darth Vader has become one of the most iconic villains in popular culture, and has been listed among the greatest villains and fictional characters ever. The American Film Institute listed him as the third greatest movie villain in cinema history on 100 Years... 100 Heroes and Villains, behind Hannibal Lecter and Norman Bates.His role as a tragic hero in the saga was also met with positive reviews.')
        embed.set_image(url='https://images.uncyclomedia.co/uncyclopedia/en/3/3d/Anakinvader.gif')
        await ctx.send(embed=embed)

      else:
        await ctx.send('DATA NOT FOUND')

    elif message.lower() == 'obiwan' or message.lower()=='obi-wan':
      if surname == 'kenobi' or surname == 'KENOBI' or surname == 'Kenobi' or surname == None:
        embed=discord.Embed(title='Obiwan/Ben Kenobi',description='Star Wars character',colour=discord.Colour.blue()) 
        embed.add_field(name='Info...',value='Obi-Wan Kenobi , also known as Ben Kenobi, is a character in the Star Wars franchise.Within the original trilogy, Obi-Wan is a Jedi Master as a supporting character and is portrayed by English actor Alec Guinness. In the later-released prequel trilogy, a younger version of the character serves as one of the two main protagonists alongside Anakin Skywalker and is portrayed by Scottish actor Ewan McGregor. In the original trilogy, he is a mentor to Luke Skywalker, to whom he introduces the ways of the Jedi. After sacrificing himself in a duel against Darth Vader, Obi-Wan guides Luke in his fight against the Galactic Empire',inline=False)
        embed.add_field(name='More info...',value=" In the prequel trilogy, set decades earlier, he is initially a Padawan (apprentice) to Jedi Master Qui-Gon-Jinn and later the mentor and friend to Luke's father Anakin, who falls to the dark side of the Force and becomes Vader. The character briefly appears in the sequel trilogy as a disembodied voice, speaking to Rey. He is frequently featured as a main character in various other Star Wars media",inline=False)
        embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRG-yGRZGy7npdCw1UZ_BJUyFL2U3t-rp5rCg&usqp=CAU')
        await ctx.send(embed=embed)

      else:
        await ctx.send('DATA NOT FOUND')

    elif message.lower() == 'ben':
      if surname == None:
        embed=discord.Embed(title='lol',description='it can be either ben solo or ben kenobi',colour=discord.Colour.blue())
        embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkaNlVZMRrRZUOnMs8IX8gF6zVcdeEAjUBrg&usqp=CAU')
        await ctx.send(embed=embed)
      if surname == 'kenobi' or surname == 'KENOBI' or surname == 'Kenobi':
        embed=discord.Embed(title='Obiwan/Ben Kenobi',description='Star Wars character',colour=discord.Colour.blue()) 
        embed.add_field(name='Info...',value='Obi-Wan Kenobi , also known as Ben Kenobi, is a character in the Star Wars franchise.Within the original trilogy, Obi-Wan is a Jedi Master as a supporting character and is portrayed by English actor Alec Guinness. In the later-released prequel trilogy, a younger version of the character serves as one of the two main protagonists alongside Anakin Skywalker and is portrayed by Scottish actor Ewan McGregor. In the original trilogy, he is a mentor to Luke Skywalker, to whom he introduces the ways of the Jedi. After sacrificing himself in a duel against Darth Vader, Obi-Wan guides Luke in his fight against the Galactic Empire',inline=False)
        embed.add_field(name='More info...',value=" In the prequel trilogy, set decades earlier, he is initially a Padawan (apprentice) to Jedi Master Qui-Gon-Jinn and later the mentor and friend to Luke's father Anakin, who falls to the dark side of the Force and becomes Vader. The character briefly appears in the sequel trilogy as a disembodied voice, speaking to Rey. He is frequently featured as a main character in various other Star Wars media",inline=False)
        embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRG-yGRZGy7npdCw1UZ_BJUyFL2U3t-rp5rCg&usqp=CAU')
        await ctx.send(embed=embed) 
      elif surname == 'SOLO' or surname == 'Solo' or surname == 'solo':
        pass

      else:
        await ctx.send('DATA NOT FOUND')

    elif message.lower() == 'ahsoka':
      if surname == 'tano' or surname == 'TANO' or surname == 'Tano' or surname == None:
        embed=discord.Embed(title='Ahsoka Tano',description='Star Wars character',colour=discord.Colour.blue())
        embed.add_field(name='Info...',value="Ahsoka Tano is a character in the Star Wars franchise. Introduced as the Jedi Padawan of Anakin Skywalker, who later becomes Sith Lord Darth Vader, she is a protagonist of the 2008 animated film Star Wars: The Clone Wars and the subsequent television series. Ahsoka reappears in Star Wars Rebels, where she uses the codename Fulcrum, and as a voiceover cameo in Star Wars: The Rise of Skywalker. Ashley Eckstein voices Ahsoka in these appearances. Ahsoka is also the main character of the eponymous novel Star Wars: Ahsoka, which has Eckstein narrating the audiobook version. Ahsoka's live-action debut was in the second season of The Mandalorian, portrayed by Rosario Dawson. Dawson will return to play Ahsoka in her own series Ahsoka on Disney+.",inline = False)
        embed.add_field(name='More Info...',value='Although initially disliked by both fans and critics, Ahsoka eventually developed into a more complex, well-rounded character, and ultimately became a fan favorite. Serving as a foil for Anakin Skywalker, she has been highlighted as a strong female character of the franchise.',inline = False)
        embed.set_image(url='https://consequenceofsound.net/wp-content/uploads/2020/03/Ahsoka-Tano.jpg?quality=80&w=807') 
        await ctx.send(embed=embed)
      else:
        await ctx.send('DATA NOT FOUND')
        
def setup(client):
  client.add_cog(Starwars(client))