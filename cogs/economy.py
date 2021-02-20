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
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def bal(self,ctx,member: discord.Member=None):
    if member == None:
      member=ctx.author

    bankinfo = collection.find_one({"user": member.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": member.id, "wallet": 0, "bank": 0})
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

  @commands.command(aliases=['BEG','Beg'])
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def beg(self,ctx):
    
    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
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
        collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank']})

        print(bankinfo["wallet"])
        await ctx.send(f'{random.choice(people)} gave you {result} fluxes!')

  @commands.command(aliases=['DEPOSIT','Deposit','Dep','DEP'])
  async def dep(self,ctx,amount:str):
    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    else:

      if amount.lower() == 'all' or amount.lower() == 'max':
        bankinfo['bank'] = bankinfo['bank'] + bankinfo['wallet']
        bankinfo['wallet'] = 0
        await ctx.send('All money Deposited')

      if bankinfo['wallet'] < int(amount):
        await ctx.send('You dont have that much money! :slight_smile:')

      else:
        bankinfo['wallet'] = bankinfo['wallet'] - int(amount)
        bankinfo['bank'] = bankinfo['bank'] + int(amount)
        await ctx.send(f'{int(amount)} fluxes deposited')

      collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank']})


  @commands.command(aliases=['WITHDRAW','Withdraw','WITH','With','with'])
  async def withdraw(self,ctx,amount:str):
    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    else:

      if amount.lower() == 'all' or amount.lower() == 'max':
        bankinfo['wallet'] = bankinfo['wallet'] + bankinfo['bank']
        bankinfo['bank'] = 0
        await ctx.send('All money Withdrawn')

      if bankinfo['bank'] < int(amount):
        await ctx.send('You dont have that much money in your bank! :slight_smile:')

      else:
        bankinfo['bank'] = bankinfo['bank'] - int(amount)
        bankinfo['wallet'] = bankinfo['wallet'] + int(amount)
        await ctx.send(f'{int(amount)} fluxes Withdrawn')

      collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank']})

  @commands.command(aliases=['SLOTS','Slots'])
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def slots(self,ctx,amount:int):

    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    else:

      if amount > bankinfo['wallet']:
        await ctx.send('You dont have that much money!')

      else:

        letters = ['O','Q','X','Y','M','N']

        a = random.choice(letters)
        b = random.choice(letters)
        c = random.choice(letters)

        if slots(a,b,c):
          await ctx.send(f'You Got {a},{b},{c} and you won {amount} fluxes! :sunglasses:')
          bankinfo['wallet'] += amount

        else:
          bankinfo['wallet'] -= amount
          await ctx.send(f'You Got {a},{b},{c} and you lost {amount} fluxes! :cry:')

        collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank']})
      

  @commands.command(aliases=['ROB','Rob'])
  
  #@commands.cooldown(1,120, commands.BucketType.user)
  async def rob(self,ctx,member:discord.Member):

    bankinfo = collection.find_one({"user": ctx.author.id})
    if not bankinfo:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
      await ctx.send(f'{ctx.author.name} is new, opening new bank account.')
      return

    bankinfo1 = collection.find_one({"user": member.id})
    if not bankinfo1:
      #make new entry
      collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
      await ctx.send(f'{member.name} is new, opening new bank account.')
      return

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
          amount_stolen = random.randint(20,(bankinfo['wallet']/2))

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

      collection.replace_one({"user": bankinfo['user']},{"user": bankinfo['user'], "wallet": bankinfo['wallet'], "bank": bankinfo['bank']})
      collection.replace_one({"user": bankinfo1['user']},{"user": bankinfo1['user'], "wallet": bankinfo1['wallet'], "bank": bankinfo1['bank']})




def slots(a,b,c):
  if a == b or a == c:
    return True

  if b == c:
    return True

  else:
    return False

def setup(client):
  client.add_cog(Economy(client))

