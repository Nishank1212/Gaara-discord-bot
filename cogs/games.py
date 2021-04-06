import discord
from discord.ext import commands
import asyncio
import random

class Games(commands.Cog):
  def __init__(self,client):
    self.client = client
    
  @commands.command()
  async def guess(self,ctx):
    await ctx.send('**Welcome to the guessing game**\nMy number is between 1 - 10, you have 3 guesses to guess my number')
    number = random.randint(1,10)
    guess_count = 0
    while guess_count < 3:
      await ctx.send('What is your guess?')

      def check(m):
        return m.author == ctx.author and m.content.isdigit()
      try:
        msg = await self.client.wait_for('message', timeout=10.0,check=check)
        guess = int(msg.content)
        if guess < number:
          await ctx.send('Your guess is smaller than my number')
        elif guess > number:
          await ctx.send('Your guess is bigger than my number')
        elif guess == number:
          await ctx.send('Your guess is correct!!!')          
          break
        guess_count += 1
        if guess_count == 3 and guess != number:
          await ctx.send(f'YOU LOOSE!!! MY NUMBER WAS {number}')
      except asyncio.TimeoutError:
        await ctx.send(f'Game ended with no response, my number was {number}')


  @commands.command()
  async def rps(self,ctx, user_choice):
    bot_choices = ['rock','paper','scissor']  
    bots_choice_made = random.choice(bot_choices)
    embed=discord.Embed(title='Rock Paper Scissor',colour=discord.Colour.blue())
    if bots_choice_made == user_choice.lower():
      embed.add_field(name=f'I chose {bots_choice_made}',value='Its a draw!')
    elif bots_choice_made == 'rock':
      if user_choice.lower() == 'paper':
        embed.add_field(name=f'I chose {bots_choice_made}',value='You won!')
      elif user_choice.lower() == 'scissor':
        embed.add_field(name=f'I chose {bots_choice_made}',value='I won!')

    elif bots_choice_made == 'paper':
      if user_choice.lower() == 'scissor':
        embed.add_field(name=f'I chose {bots_choice_made}',value='You won!')
      elif user_choice.lower() == 'rock':
        embed.add_field(name=f'I chose {bots_choice_made}',value='I won!')

    elif bots_choice_made == 'scissor':
      if user_choice.lower() == 'rock':
        embed.add_field(name=f'I chose {bots_choice_made}',value='You won!')
      elif user_choice.lower() == 'paper':
        embed.add_field(name=f'I chose {bots_choice_made}',value='I won!')
    await ctx.send(embed=embed)

  @commands.command()
  async def dice(self,ctx):
    a = random.randint(0,10)
    b = random.randint(0,10)

    embed=discord.Embed(title='Dice',colour=discord.Colour.blue())
    embed.add_field(name='I Got: ',value=f"{a}")
    embed.add_field(name='You Got: ',value=f"{b}")

    if a<b:
      embed.add_field(name='**You Won!**:cry:',value='\u200b',inline=False)
    elif a>b:
      embed.add_field(name='**I won!**:smile:',value='\u200b',inline=False)
    else:
      embed.add_field(name='**Its a Draw** :cry:',value='\u200b',inline=False)

    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Games(client))