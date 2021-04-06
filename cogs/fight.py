import discord
from discord.ext import commands
import random
import asyncio

class Fight(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def fight(self,ctx,member:discord.Member=None):

    if member == None:
      await ctx.send('Try again but this time mention who do you want to fight with?')

    else:
        def check(m):
          return m.author == ctx.author

        def check1(m):
          return m.author == member

        await ctx.send(f"{ctx.author.mention} enter the name of your choice")
        try:
          player1 = await self.client.wait_for('message',check=check,timeout=30.0)

          

        except asyncio.TimeoutError:

          return await ctx.send(f'{ctx.author.mention} didnt answer in time what a loser')
        
        await ctx.send(f"{member.mention} enter the name of your choice")

        try:

          player2 = await self.client.wait_for('message',check=check1,timeout=30.0)

        except asyncio.TimeoutError:

          return await ctx.send(f'{member.mention} didnt answer in time what a loser')
        player1 = player1.content
        player2 = player2.content
        embed=discord.Embed(title=f'welcome {player1} and {player2}',description='These are the Weapons and their uses',colour=discord.Colour.blue())
        embed.add_field(name="⛏️Axe",value='axes are heavy on attack, and have high possibility of disabling the enemy weapon')
        embed.add_field(name='⚔️Sword',value="swords do medium attack, have medium attack speed, and medium defense")
        embed.add_field(name='🏹Spear',value="spears do heavy attack, at a fast speed, but r bad on defense")
        embed.add_field(name='🗡️Dagger',value="daggers do less damage, but have the fastest attack speed in the game")
        embed.add_field(name='🔨Hammer',value="hammers have less chance of hitting but if they hit they do the most damage in the game")
        embed.add_field(name='🍢Club',value='"clubs have the highest defense, in the game')
        embed.add_field(name='🔱Trident',value="tridents never miss and they do good damage and have good defense")
        await ctx.send(embed=embed)
        await ctx.send(f'what do you want to choose? {player1}')
        player1_weapon = await self.client.wait_for('message',check=check)
        await ctx.send(f'what do you want to choose? {player2}')
        player2_weapon = await self.client.wait_for('message',check=check1)
        player1_weapon = player1_weapon.content
        player2_weapon=player2_weapon.content
        #player1 stats
        lives1 = 200 
        damage1 = 0
        defense1 = 0
        
        #player2 stats
        lives2 = 200
        damage2 = 0
        defense2 = 0
        #player1 weapon stats
        if player1_weapon.lower() == "sword":
            maxdamage1 = 25
            maxdefense1 = 30
            maxdisable_chance1 = 11
            maxchance1 = 20
        elif player1_weapon.lower() == "spear":
            maxdamage1 = 40
            maxdefense1 = 10
            maxdisable_chance1 = 11
            maxchance1 = 25
        elif player1_weapon.lower() == "axe":
            maxdamage1 = 35
            maxdefense1 = 20
            maxdisable_chance1 = 14
            maxchance1 = 15
        elif player1_weapon.lower() == "club":
            maxdamage1 = 20
            maxdefense1 = 60
            maxdisable_chance1 = 11
            maxchance1 = 15
        elif player1_weapon.lower() == "daggers" or player2_weapon.lower() == 'dagger':
            maxdamage1 = 15
            maxdefense1 = 20
            maxdisable_chance1 = 11
            maxchance1 = 40
        elif player1_weapon.lower() == "hammer":
            maxdamage1 = 80
            maxdefense1 = 15
            maxdisable_chance1 = 11
            maxchance1 = 20
        elif player1_weapon.lower() == "trident":
            maxdamage1 =  30
            maxdefense1 = 20
            maxdisable_chance1 = 11
            maxchance1 = 30
        else:
            await ctx.send('game over due to wrong weapon choosing')
            return     #player2 weapon stats
        if player2_weapon.lower() == "sword":
            maxdamage2 = 25
            maxdefense2 = 30
            maxdisable_chance2 = 11
            maxchance2 = 20
        elif player2_weapon.lower() == "spear":
            maxdamage2 = 40
            maxdefense2 = 10
            maxdisable_chance2 = 11
            maxchance2 = 25
        elif player2_weapon.lower() == "axe":
            maxdamage2 = 35
            maxdefense2 = 20
            maxdisable_chance2 = 14
            maxchance2 = 15
            
        elif player2_weapon.lower() == "club":
            maxdamage2 = 20
            maxdefense2 = 60
            maxdisable_chance2 = 11
            maxchance2 = 15
        elif player2_weapon.lower() == "daggers" or player2_weapon.lower() == 'dagger':
            maxdamage2 = 15
            maxdefense2 = 20
            maxdisable_chance2 = 11
            maxchance2 = 40
        elif player2_weapon.lower() == "hammer":
            maxdamage2 = 80
            maxdefense2 = 15
            maxdisable_chance2 = 11
            maxchance2 = 20
        elif player2_weapon.lower() == "trident":
            maxdamage2 =  30
            maxdefense2 = 20
            maxdisable_chance2 = 11
            maxchance2 = 20
        else:
            await ctx.send('Game over due to wrong weapon choosing')
            return
            
        while lives1 > 0 and lives2 > 0:
            #to check whos chance it is
            player1_chance = random.randint(0,int(maxchance1))
            player2_chance = random.randint(0,int(maxchance2))
            if player1_chance >= player2_chance:
                await ctx.send(f'since {player1} is faster than {player2}, its {player1}s chance') 
                await ctx.send("Do u want to attack or defend?")
                attack = await self.client.wait_for('message',check=check)
                attack = attack.content
                if attack.lower() == "attack":
                    damage_delt = random.randint(5,int(maxdamage1))
                    if damage_delt > 10:
                        damage1 += damage_delt
                        damage1 -= defense2
                        lives2 -= damage1
                        damage1 = 0
                        defense2=0
                        await ctx.send(f"You hit {player2} and dealt {damage_delt} damage\n{player2} has {lives2} health left")
                        # if random.randint(0, int(maxdisable_chance1)) >= 10:
                        #     await ctx.send("you have been disabled")
                        #     player2_weapon = None
                    else:
                        print(f"{player1} delt no damage lol :rofl:")
                elif attack.lower() == "defend":
                    defense1 += random.randint(10, int(maxdefense1))
                    await ctx.send(f'Your defense now is {defense1}')

                else:
                  await ctx.send('Not a valid option lol your chance gets skipped')

                while lives1 > 0 and lives2 > 0:
                  await ctx.send(f"Do u want to attack or defend? {player2}")
                  attack = await self.client.wait_for('message',check=check1)
                  attack = attack.content
                  if attack.lower() == "attack":
                      damage_delt = random.randint(5,int(maxdamage2))
                      if damage_delt > 10:
                          damage2 += damage_delt
                          damage2 -= defense1
                          lives1 -= damage2
                          damage2 = 0
                          defense1=0
                          await ctx.send(f"You hit {player1} and dealt {damage_delt} damage\n{player1} has {lives1} health left")
                          if random.randint(0, int(maxdisable_chance1)) >= 10:
                              print("you have been disabled")
                              player1_weapon = None
                              await ctx.send(f'Weapon of {player1} is disabled!!! {player2} wins badly with {lives2} health left')
                              lives1=0
                              break
                              return
                            
                            
                              
                      else:
                          await ctx.send(f"{player2} delt no damage lol :rofl:")

                  elif attack.lower() == "defend":
                      defense1 += random.randint(10, int(maxdefense1))
                      print(f'Your defense now is {defense1}')

                  else:
                    await ctx.send('Not a valid option lol your chance gets skipped')

                  await ctx.send(f"Do u want to attack or defend? {player1}")
                  attack = await self.client.wait_for('message',check=check)
                  attack = attack.content
                  if attack.lower() == "attack":
                      damage_delt = random.randint(5,int(maxdamage1))
                      if damage_delt > 10:
                          damage1 += damage_delt
                          damage1 -= defense2
                          lives2 -= damage1
                          damage1 = 0
                          defense2 = 0
                          await ctx.send(f"You hit {player2} and dealt {damage_delt} damage\n{player2} has {lives2} health left")
                          if random.randint(0, int(maxdisable_chance2)) >= 10:
                              await ctx.send(f'{player1} absolutely trashed {player2}  because he disbaled {player2}s weapon!!!')
                              player2_weapon = None
                              lives2 = 0
                              break
            
                              return
                              
                      else:
                          await ctx.send(f"{player1} delt no damage lol :rofl:")
                          
                  elif attack.lower() == "defend":
                      defense1 += random.randint(10, int(maxdefense1))
                      await ctx.send(f'Your defense now is {defense1}')

                  else:
                    await ctx.send('Not a valid option lol your chance gets skipped')

            elif player2_chance > player1_chance:
                await ctx.send(f'since {player2} is faster than {player1}, its {player2}s chance') 
                await ctx.send("Do u want to attack or defend?")
                attack = await self.client.wait_for('message',check=check1)
                attack = attack.content
                if attack.lower() == "attack":
                    damage_delt = random.randint(5,int(maxdamage2))
                    if damage_delt > 10:
                        damage2 += damage_delt
                        damage2 -= defense1
                        lives1 -= damage2
                        defense1 = 0
                        damage2 = 0
                        await ctx.send(f"You hit {player1} and dealt {damage_delt} damage\n{player1} has {lives1} health left")
                        # if random.randint(0, int(maxdisable_chance1)) >= 10:
                        #     await ctx.send("you have been disabled")
                        #     player2_weapon = None
                    else:
                        print(f"{player2} delt no damage lol :rofl:")
                elif attack.lower() == "defend":
                    defense1 += random.randint(10, int(maxdefense2))
                    await ctx.send(f'Your defense now is {defense2}')

                else:
                  await ctx.send('Not a valid option lol your chance gets skipped')

                while lives1 > 0 and lives2 > 0:
                  await ctx.send(f"Do u want to attack or defend? {player1}")
                  attack = await self.client.wait_for('message',check=check)
                  attack = attack.content
                  if attack.lower() == "attack":
                      damage_delt = random.randint(5,int(maxdamage1))
                      if damage_delt > 10:
                          damage1 += damage_delt
                          damage1 -= defense2
                          lives2 -= damage1
                          defense2 = 0
                          damage1 = 0
                          await ctx.send(f"You hit {player2} and dealt {damage_delt} damage\n{player2} has {lives2} health left")
                          if random.randint(0, int(maxdisable_chance1)) >= 10:
                              print("you have been disabled")
                              player2_weapon = None
                              await ctx.send(f'Weapon of {player2} is disabled!!! {player1} wins badly with {lives2} health left')
                              lives2 = 0
                              break
                              return
                              
                      else:
                          await ctx.send(f"{player2} delt no damage lol :rofl:")

                  elif attack.lower() == "defend":
                      defense1 += random.randint(10, int(maxdefense1))
                      print(f'Your defense now is {defense1}')

                  else:
                    await ctx.send('Not a valid option lol your chance gets skipped')

                  await ctx.send(f"Do u want to attack or defend? {player2}")
                  attack = await self.client.wait_for('message',check=check1)
                  attack = attack.content
                  if attack.lower() == "attack":
                      damage_delt = random.randint(5,int(maxdamage2))
                      if damage_delt > 10:
                          damage2 += damage_delt
                          damage2 -= defense1
                          defense1 = 0
                          lives1 -= damage2
                          damage2 = 0
                          await ctx.send(f"You hit {player1} and dealt {damage_delt} damage\n{player1} has {lives1} health left")
                          if random.randint(0, int(maxdisable_chance2)) >= 10:
                              await ctx.send(f'{player2} absolutely trashed {player1} with {lives2} health remaining because he disbaled {player1}s weapon!!!')
                              player1_weapon = None
                              lives1 = 0
                              break
                              return

                             
                              
          
                      else:
                          await ctx.send(f"{player2} delt no damage lol :rofl:")
                          
                  elif attack.lower() == "defend":
                      defense1 += random.randint(10, int(maxdefense2))
                      await ctx.send(f'Your defense now is {defense2}')

                  else:
                    await ctx.send('Not a valid option lol your chance gets skipped')

            if lives1 == 0:
              await ctx.send(f'{player2}({member.mention}) absolutely crushed {player1}({ctx.author.mention}) with {lives2} health remaining')

            else:
              await ctx.send(f'{player1}({ctx.author.mention}) absolutely crushed {player2}({member.mention}) with {lives1} health remaining')



       

def setup(client):
  client.add_cog(Fight(client))
