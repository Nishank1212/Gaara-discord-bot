from os import getenv
import discord
from discord.ext import commands
from pymongo import MongoClient
import random

cluster = MongoClient(getenv("ECONOMY_PASS")) # Don't include "<" and ">" fill in those with your credentials
collection = cluster.economy1.economy1

class Economy(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['BAL','Bal','BALANCE','Balance','balance'])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def bal(self,ctx,member: discord.Member=None):
    if member == None:
      member=ctx.author

    bankinfo = collection.find_one({"user": member.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": member.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{member.name} is new, opening new bank account.')
      return
    else:
      # print(f'bankinfo : {bankinfo}')
      wallet = bankinfo['wallet']
      money_amount = bankinfo['bank']
      embed=discord.Embed(title=f"{member.name}'s balance",colour=discord.Colour.blue())
      embed.add_field(name='Wallet', value=wallet,inline=False)
      embed.add_field(name='Bank', value=money_amount)
      await ctx.send(embed=embed)
      print(bankinfo['inventory'])

  @commands.command(aliases=['BEG','Beg'])
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def beg(self,ctx):
    
    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return


    else:
      choice = [0,1]
      people = ['Donald Trump','Elon Musk','Henry Ford','Billie Eyelash','Adam Levine']
      lines_for_fail = ['No u','Go ask someone else','I am poor','UGHHHHHHH NO']
      if random.choice(choice) == 0:
        await ctx.send(f'{random.choice(people)} : {random.choice(lines_for_fail)}')
            
      else:
        result = random.randint(1,100)
        bankinfo["wallet"] += result

        # add info back to db
        print(f'Adding {bankinfo} back to db')
        collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank'],"inventory" : bankinfo['inventory']})

        print(bankinfo["wallet"])
        await ctx.send(f'{random.choice(people)} gave you {result} fluxes!')

  @commands.command(aliases=['DEPOSIT','Deposit','Dep','DEP','deposit'])
  async def dep(self,ctx,amount:str):
    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    else:

      if amount.lower() == 'all' or amount.lower() == 'max':
        wallet = bankinfo['wallet']
        bankinfo['bank'] += wallet
        bankinfo['wallet'] -= wallet
        await ctx.send('All money Deposited')

      elif bankinfo['wallet'] < int(amount):
        await ctx.send('You dont have that much money! :slight_smile:')

      else:
        bankinfo['wallet'] = bankinfo['wallet'] - int(amount)
        bankinfo['bank'] = bankinfo['bank'] + int(amount)
        await ctx.send(f'{int(amount)} fluxes deposited')

      collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank'],"inventory" : bankinfo['inventory']})


  @commands.command(aliases=['WITHDRAW','Withdraw','WITH','With','with'])
  async def withdraw(self,ctx,amount:str):
    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    else:

      if amount.lower() == 'all' or amount.lower() == 'max':
        bank = bankinfo['bank']
        bankinfo['wallet'] += bank
        bankinfo['bank'] -= bank
        await ctx.send('All money Withdrawn')

      elif bankinfo['bank'] < int(amount):
        await ctx.send('You dont have that much money in your bank! :slight_smile:')

      else:
        bankinfo['bank'] = bankinfo['bank'] - int(amount)
        bankinfo['wallet'] = bankinfo['wallet'] + int(amount)
        await ctx.send(f'{int(amount)} fluxes Withdrawn')

      collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank'],"inventory" : bankinfo['inventory']})

  @commands.command(aliases=['SLOTS','Slots'],cooldown_after_parsing=True)
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def slots(self,ctx,amount:int):

    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    else:

      if amount > bankinfo['wallet']:
        await ctx.send('You dont have that much money!')

      else:

        letters = [':blue_circle:',':red_circle:',':white_circle:',':green_circle:',':yellow_circle:',':purple_circle:']

        a = random.choice(letters)
        b = random.choice(letters)
        c = random.choice(letters)

        if slots(a,b,c):

          if a == b and a == c:
            await ctx.send(f'You Got {a},{b},{c} and you won {amount*2} fluxes! :sunglasses:')

            bankinfo['wallet'] += amount*2

          else: 

            await ctx.send(f'You Got {a},{b},{c} and you won {amount} fluxes! :sunglasses:')
            bankinfo['wallet'] += amount

        else:
          bankinfo['wallet'] -= amount
          await ctx.send(f'You Got {a},{b},{c} and you lost {amount} fluxes! :cry:')

        collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank'],"inventory" : bankinfo['inventory']})
      

  @commands.command(aliases=['ROB','Rob'],cooldown_after_parsing=True)
  
  @commands.cooldown(1,120, commands.BucketType.user)
  async def rob(self,ctx,member:discord.Member = None):

    if member == None:
      await ctx.send('Try to run the command after 2 minutes again but this time actually mention who u want to rob :rolling_eyes:')

    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    bankinfo1 = collection.find_one({"user": member.id})
    if not bankinfo1:
      #make new entry
      collection.insert_one({"user": member.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{member.name} is new, opening new bank account.')
      return

    if ctx.author.id == member.id:
      await ctx.send('You cannot rob yourself DUMMY! :rolling_eyes:')

    else:
      robbed = random.choice([0,1])
      if bankinfo1['wallet'] >= 500 and bankinfo['wallet'] >= 500:
        if robbed == 0:

          if bankinfo['wallet'] > 1000 or bankinfo['bank'] > 1000:

            await ctx.send(f'HAHAHA YOU WERE CAUGHT YOU PAYED {member.mention} 1000 fluxes!!!')
            if bankinfo['wallet'] > 1000:

              bankinfo['wallet'] -= 1000
              bankinfo1['wallet'] += 1000

            else:
              bankinfo['bank'] -= 1000
              bankinfo1['wallet'] += 1000


          else:
            await ctx.send(f'HAHAHA YOU WERE CAUGHT YOU PAYED {member.mention} 500 fluxes!!!')
            if bankinfo['wallet'] > 500:

              bankinfo['wallet'] -= 500
              bankinfo1['wallet'] += 500

            else:
              bankinfo['bank'] -= 500
              bankinfo1['wallet'] += 500

        else:
          amount_stolen = random.randint(20,int(bankinfo['wallet']/2))

          await ctx.send(f'You stole {amount_stolen} fluxes from {member.mention}')
          bankinfo['wallet'] += amount_stolen
          bankinfo1['wallet'] -= amount_stolen

      else:
        if bankinfo1['wallet'] < 500:
          await ctx.send('The victim doesnt have atleat 500 fluxes, Not worth it man!')
          return

        if bankinfo['wallet'] < 500:
          await ctx.send('You need atleast 500 fluxes to try and rob someone')
          return

      collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank'],"inventory" : bankinfo['inventory']})
      collection.replace_one({"user": bankinfo1['user']},{"user": bankinfo1['user'], "wallet": bankinfo1['wallet'], "bank": bankinfo1['bank'],"inventory" : bankinfo1['inventory']})


  @commands.command(aliases=['SEARCH','Search'])
  @commands.cooldown(1,30, commands.BucketType.user)
  async def search(self,ctx):
    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    else:
      searching_places = ['van','area51','air','grass','hospital','dog','bank','shoe','tree','house','discord','pocket']
      messages = {
        'van':'This would happen in real life also! Very nice Gaara!',
        'area51':'NOW RUN! the government is behind you',
        'air': 'How the Heck? Why were you even looking there?',
        'grass':'How? I wonder if somebody left there wallet',
        'hospital':'Are you proud of yourself Now?',
        'dog':'That poor poor Dog',
        'bank':'Did you just roub the bank?!',
        'shoe':'Why were you looking in your shoe?',
        'tree':'Why were you searching in a tree?',
        'house':'Be happy Your mother was nice',
        'discord':'Your DMs are valuable :thinking:',
        'pocket':'Now it is in your wallet!'}

      a = random.choice(searching_places)
      searching_places.remove(a)
      b = random.choice(searching_places)
      searching_places.remove(b)
      c = random.choice(searching_places)
      searching_places.remove(c)

      await ctx.send(f'**Where do you want to search** {ctx.author.mention}\nchoose from the following and type in the chat\n`{a}`,`{b}` or `{c}`')


      def check(m):
        return m.author == ctx.author

      msg = await self.client.wait_for('message',check=check)
     
      if msg.content.lower() != a and msg.content.lower() != b and msg.content.lower() != c:
          await ctx.send(f'What Are You Thinking {ctx.author.mention}, Thats Not a valid Option')
          
      else:
          coins = random.randint(60,500)
          if msg.content.lower() == a:
            await ctx.send(f'{ctx.author.mention} searched the {a}\nYou Found {coins} fluxes,{messages[a]}')

          if msg.content.lower() == c:
            await ctx.send(f'{ctx.author.mention} searched the {c}\nYou Found {coins} fluxes,{messages[c]}')

          if msg.content.lower() == b:
            await ctx.send(f'{ctx.author.mention} searched the {b}\nYou Found {coins} fluxes,{messages[b]}')

          bankinfo['wallet'] += coins



      collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank'],"inventory" : bankinfo['inventory']})


  @commands.command(aliases=['GIVE','GIB','Gib','gib','Give'])
  async def give(self,ctx,amount:int,member:discord.Member=None):
    if member == None:
      await ctx.send('Try running the command again but this time tell who do you want to give your money to! :rolling_eyes:')
      return

    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    bankinfo1 = collection.find_one({"user": member.id})
    if not bankinfo1:
      #make new entry
      collection.insert_one({"user": member.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{member.name} is new, opening new bank account.')
      return

    else:
      if bankinfo['wallet'] < amount:
        await ctx.send('You do not have that much money in your wallet')

      else:
        bankinfo['wallet'] -= amount
        bankinfo1['wallet'] += amount
        await ctx.send(f"{ctx.author.mention} gave {amount} fluxes to {member.mention}, Now {ctx.author.mention} has {bankinfo['wallet']} fluxes and {member.mention} has {bankinfo1['wallet']} fluxes")
        collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank'],"inventory" : bankinfo['inventory']})
        collection.replace_one({"user": bankinfo1['user']},{"user": bankinfo1['user'], "wallet": bankinfo1['wallet'], "bank": bankinfo1['bank'],"inventory" : bankinfo1['inventory']})

        
  @commands.command(aliases=['BUY','Buy'])
  async def buy(self,ctx,*,thing):
    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    else:
      if thing.lower() == 'fishing pole':

        
        if ctx.author.bot:
          return

        else:


          if bankinfo['wallet'] >= 500:
            await ctx.send('You have succesfully bought a fishing pole for 500 fluxes')
            bankinfo['wallet'] -= 500
            if 'fishing pole' in bankinfo['inventory'].keys():
              bankinfo['inventory']['fishing pole'] += 1

            else:
            
              bankinfo['inventory']['fishing pole'] = 1

          else:
            await ctx.send('far out! you dont have that much money')

      elif thing.lower() == 'hunting rifle' or thing.lower() == 'rifle':

        if ctx.author.bot:
          return
        else:


          if bankinfo['wallet'] >= 500:
            await ctx.send('You have succesfully bought a rifle for 500 fluxes')
            if 'rifle' in bankinfo['inventory'].keys():
              bankinfo['inventory']['rifle'] += 1

            else:
            
              bankinfo['inventory']['rifle'] = 1

          else:
            await ctx.send('far out! you dont have that much money')

      elif thing.lower() == 'laptop':
        
        if ctx.author.bot:
          return

        else:
          if bankinfo['wallet'] >= 1000:
            await ctx.send('You have succesfully bought a laptop for 1000 fluxes')
            if 'laptop' in bankinfo['inventory'].keys():
              bankinfo['inventory']['laptop'] += 1

            else:
            
              bankinfo['inventory']['laptop'] = 1

          else:
            await ctx.send('far out! you dont have that much money')      

      collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank'],"inventory" : bankinfo['inventory']})

  @commands.command(aliases=['FISH','Fish'])
  @commands.cooldown(1,20, commands.BucketType.user)
  async def fish(self,ctx):
    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    else:
      caught = random.choice([0,1])

      if 'fishing pole' not in bankinfo['inventory'].keys():
        await ctx.send('First buy a fishing pole!')

      else:

        if not bankinfo['inventory']['fishing pole'] >= 1:
          return await ctx.send('First buy a fishing pole!')

        if caught == 0:
          await ctx.send('LOL you are BAD You couldnt find anything')

        else:
          fishes = random.randint(1,5)
          await ctx.send(f'You brough back {fishes} fish 🐟!')
          if 'fish' in bankinfo['inventory'].keys():
            bankinfo['inventory']['fish'] += fishes

          else:
            bankinfo['inventory']['fish'] = fishes

      collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank'],"inventory" : bankinfo['inventory']})

  
  @commands.command(aliases=['HUNT','Hunt'])
  @commands.cooldown(1,20, commands.BucketType.user)
  async def hunt(self,ctx):
    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    else:
      caught = random.choice([0,1])

      if 'rifle' not in bankinfo['inventory'].keys():
        await ctx.send('First buy a rifle!')

      else:

        if not bankinfo['inventory']['rifle'] >=1:
          return await ctx.send('First buy a rifle!')

        if caught == 0:
          await ctx.send('LOL you are BAD You couldnt find anything')

        else:
          animals = ['rabbit🐇','deer🦌','horse🐎'] 
          animal = random.choice(animals)
          animalnum = random.randint(1,3)
          await ctx.send(f'You brough back {animalnum} {animal}!')
          if animal == 'rabbit🐇':
            if 'rabbit' in bankinfo['inventory'].keys():
              bankinfo['inventory']['rabbit'] += animalnum

            else:
              bankinfo['inventory']['rabbit'] = animalnum

          if animal == 'deer🦌':
            if 'deer' in bankinfo['inventory'].keys():
              bankinfo['inventory']['deer'] += animalnum

            else:
              bankinfo['inventory']['deer'] = animalnum

          if animal == 'horse🐎':
            if 'horse' in bankinfo['inventory'].keys():
              bankinfo['inventory']['horse'] += animalnum

            else:
              bankinfo['inventory']['horse'] = animalnum

      collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank'],"inventory" : bankinfo['inventory']})


  @commands.command(aliases=['SELL','Sell'])
  async def sell(self,ctx,thing,amount):
    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return


    else:
      if thing in bankinfo['inventory'].keys():
        if thing.lower() == 'fish':
          if amount.isdigit():
            
            if 'fish' in bankinfo['inventory'].keys():
              if bankinfo['inventory']['fish'] >= int(amount):
                await ctx.send(f'Succesfully sold {int(amount)} fish 🐟 for {int(amount)*50} fluxes')
                bankinfo['inventory']['fish'] -= int(amount)
                bankinfo['wallet'] += int(amount) * 50
                


              else:
                await ctx.send(f'you do not have {amount} fishes!')

          elif str(amount) == 'all':
            num = bankinfo['inventory']['fish']
            if num >= 1:
              bankinfo['wallet'] += 50 * int(num)

              bankinfo['inventory']['fish'] -= num

            else:
              await ctx.send('You do not have any fish!!!')

        if thing.lower() == 'rabbit':

          if amount.isdigit():
            
            if 'rabbit' in bankinfo['inventory'].keys():
              if bankinfo['inventory']['rabbit'] >= int(amount):
                await ctx.send(f'Succesfully sold {int(amount)} rabbit 🐇 for {int(amount)*100} fluxes')
                bankinfo['inventory']['rabbit'] -= int(amount)
                bankinfo['wallet'] += int(amount) * 100
                


              else:
                await ctx.send(f'you do not have {amount} rabbits!')

          elif str(amount) == 'all':
            num = bankinfo['inventory']['rabbit']
            if num >= 1:
              await ctx.send(f'Succesfully sold {num} rabbit 🐇 for {num * 100} fluxes')
              bankinfo['wallet'] += 100 * int(num)

              bankinfo['inventory']['rabbit'] -= num

            else:
              await ctx.send('You do not have any rabbit!!!')


        if thing.lower() == 'horse':

          if amount.isdigit():
            
            if 'horse' in bankinfo['inventory'].keys():
              if bankinfo['inventory']['horse'] >= int(amount):
                await ctx.send(f'Succesfully sold {int(amount)} horse 🐎 for {int(amount)*100} fluxes')
                bankinfo['inventory']['fish'] -= int(amount)
                bankinfo['wallet'] += int(amount) * 100
                


              else:
                await ctx.send(f'you do not have {amount} horses!')

          elif str(amount) == 'all':
            num = bankinfo['inventory']['horses']
            if num >= 1:
              bankinfo['wallet'] += 100 * int(num)

              bankinfo['inventory']['horse'] -= num

            else:
              await ctx.send('You do not have any fish!!!')

        if thing.lower() == 'deer':

          if amount.isdigit():
            
            if 'deer' in bankinfo['inventory'].keys():
              if bankinfo['inventory']['deer'] >= int(amount):
                await ctx.send(f'Succesfully sold {int(amount)} deer🦌 for {int(amount)*100} fluxes')
                bankinfo['inventory']['deer'] -= int(amount)
                bankinfo['wallet'] += int(amount) * 100
                


              else:
                await ctx.send(f'you do not have {amount} deers!')

          elif str(amount) == 'all':
            num = bankinfo['inventory']['deer']
            if num >= 1:
              bankinfo['wallet'] += 100 * int(num)

              bankinfo['inventory']['deer'] -= num

            else:
              await ctx.send('You do not have any deer!!!')
      else:
        await ctx.send('You dont own the item?')

      collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank'],"inventory" : bankinfo['inventory']})

  @commands.command(aliases=['INVENTORY','Inventory','inventory','INV','Inv'])
  async def inv(self,ctx,member:discord.Member = None):
    if member == None:
      member=ctx.author

    bankinfo = collection.find_one({"user": member.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": member.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{member.name} is new, opening new bank account.')
      return

    else:
      sellable_collectable = {'fishing pole':'object/sellable','rabbit':'sellable','deer':'sellable','horse':'sellable','fish':'sellable','rifle':'object/sellable','laptop':'object/sellable'}
      embed=discord.Embed(title=f"{member.name}'s Inventory'",colour=discord.Colour.blue())
      for i in bankinfo['inventory'].keys():
        if bankinfo['inventory'][i] >= 1:
          embed.add_field(name=f'{i}',value=f'{sellable_collectable[i]},amount = {bankinfo["inventory"][i]}',inline=True)

      await ctx.send(embed=embed)

  @commands.command(aliases=['SHOP','Shop'])
  async def shop(self,ctx):

    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    embed=discord.Embed(title='SHOP',colour=discord.Colour.blue())
    embed.add_field(name='1)Fishing Pole 🎣',value='500 fluxes, object')          
    embed.add_field(name='2)Rifle 🥆',value='500 fluxes, object')
    embed.add_field(name='2)Laptop 💻',value='1000 fluxes, object') 
    await ctx.send(embed=embed)    


  @commands.command(aliases=['POSTMEME','Postmeme','PM','Pm','postmeme'])
  @commands.cooldown(1, 20, commands.BucketType.user) 
  
  async def pm(self,ctx):
    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    else:
      if 'laptop' not in bankinfo['inventory'].keys():
        await ctx.send('You need to buy a laptop for this!')

      else:
        if bankinfo['inventory']['laptop'] < 1:
          return await ctx.send('You need to buy a laptop for this!')

        await ctx.send('What type of meme do you want to post online:\n`a`Kind Meme\n`b`Inspirational Meme\n`c`Copypasta\n`d`Fresh Meme\n`e`Random Meme')

        def check(m):
          return m.author == ctx.author

        msg = await self.client.wait_for('message',check=check)

        if msg.content.lower() == 'a':
          choice = random.choice([0,1])
          if choice == 0:
            await ctx.send('Nobody Liked Your Kind Meme LOL!')

          else:
            decent_nice = random.choice(['decent','awesome'])
            if decent_nice == 'decent':
              amount = random.randint(300,600)
              bankinfo['wallet'] += amount
              await ctx.send(f'Your Kind meme got decent response online! you got {amount} fluxes from the ads!')

            else:
              amount = random.randint(600,800)
              bankinfo['wallet'] += amount
              await ctx.send(f'Your Kind meme is VIRAL!!! you got {amount} fluxes by the ads')

        elif msg.content.lower() == 'b':
          choice = random.choice([0,1])
          if choice == 0:
            await ctx.send('Nobody Liked Your Inspirational Meme LOL!')

          else:
            decent_nice = random.choice(['decent','awesome'])
            if decent_nice == 'decent':
              amount = random.randint(100,300)
              bankinfo['wallet'] += amount
              await ctx.send(f'Your Inspirational meme got decent response online! you got {amount} fluxes from the ads!')

            else:
              amount = random.randint(300,500)
              bankinfo['wallet'] += amount
              await ctx.send(f'Your Inspirational meme went VIRAL online! you got {amount} fluxes from the ads!')

        elif msg.content.lower() == 'c':
          choice = random.choice([0,1])
          if choice == 0:
            await ctx.send('Nobody Liked Your CopyPasta Meme LOL!')

          else:
            decent_nice = random.choice(['decent','awesome'])
            if decent_nice == 'decent':
              amount = random.randint(100,400)
              bankinfo['wallet'] += amount
              await ctx.send(f'Your CopyPasta meme got decent response online! you got {amount} fluxes from the ads!')
              
            else:
              amount = random.randint(400,600)
              bankinfo['wallet'] += amount
              await ctx.send(f'Your CopyPasta meme went VIRAL online! you got {amount} fluxes from the ads!')
              

        elif msg.content.lower() == 'd':
          choice = random.choice([0,1])
          if choice == 0:
            await ctx.send('Nobody Liked Your Fresh Meme LOL!')

          else:
            decent_nice = random.choice(['decent','awesome'])
            if decent_nice == 'decent':
              amount = random.randint(300,600)
              bankinfo['wallet'] += amount
              await ctx.send(f'Your Fresh meme got decent response online! you got {amount} fluxes from the ads!')

            else:
              amount = random.randint(600,1000)
              bankinfo['wallet'] += amount
              await ctx.send(f'Your Fresh meme went VIRAL online! you got {amount} fluxes from the ads!')

        elif msg.content.lower() == 'e':
          choice = random.choice([0,1])
          if choice == 0:
            await ctx.send('Nobody Liked Your Random Meme LOL!')

          else:
            decent_nice = random.choice(['decent','awesome'])
            if decent_nice == 'decent':
              amount = random.randint(100,300)
              bankinfo['wallet'] += amount
              await ctx.send(f'Your Random meme decent response online! you got {amount} fluxes from the ads!')

            else:
              amount = random.randint(300,500)
              bankinfo['wallet'] += amount
              await ctx.send(f'Your Random meme went VIRAL online! you got {amount} fluxes from the ads!')

        else:
          await ctx.send('Thats Not a Valid Option')

      collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank'],"inventory" : bankinfo['inventory']})

            
  @commands.command(aliases=['Gamble','GAMBLE'])
  @commands.cooldown(1, 20, commands.BucketType.user) 
  async def gamble(self,ctx,amount:int=None):

    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0,"inventory":{}})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return


    else:
    

      if amount == None:
        await ctx.send('Try the cmd again but next time tell me How much money are you betting?')

      elif amount > bankinfo['wallet']:
        await ctx.send('You cant bet more than how much money you have ')

      else:

        a = random.randint(0,10)
        b = random.randint(0,10)

        embed=discord.Embed(title=f"{ctx.author.name}'s Gambling Game",colour=discord.Colour.blue())
        embed.add_field(name=f'Gaara rolled `{a}`',value="\u200b")
        embed.add_field(name=f'{ctx.author.name} rolled `{b}`',value="\u200b")

        if a<b:
          embed.add_field(name='**You Won!** :cry:',value=f'You win {amount} fluxes!',inline=False)
          bankinfo['wallet'] += amount
        elif a>b:
          embed.add_field(name='**I won!** :smile:',value=f'You loose {amount} fluxes!',inline=False)
          bankinfo['wallet'] -= amount
        else:
          embed.add_field(name='**Its a Draw** :cry:',value='Noone wins or looses any money',inline=False)

        await ctx.send(embed=embed)
  
        collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank'],"inventory" : bankinfo['inventory']})

          
def slots(a,b,c):
  if a == b or a == c:
    return True

  if b == c:
    return True

  else:
    return False


def setup(client):
  client.add_cog(Economy(client))

