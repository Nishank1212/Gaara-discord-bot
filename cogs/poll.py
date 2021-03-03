import discord
from discord.ext import commands
import asyncio
class Poll(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command(aliases=['POLL','Poll'])
  @commands.cooldown(1, 120, commands.BucketType.user)
  async def poll(self,ctx):
    await ctx.send('What is The question you want?(note:there will be only 4 options)')

    def check(m):
        return m.author == ctx.author
    msg1 = await self.client.wait_for('message',check=check)

    await ctx.send('What is option 1?')

    msg2 = await self.client.wait_for('message',check=check)

    await ctx.send('What is option 2?')

    msg3 = await self.client.wait_for('message',check=check)

    await ctx.send('What is option 3?')

    msg4 = await self.client.wait_for('message',check=check)

    await ctx.send('What is option 4?')

    msg5 = await self.client.wait_for('message',check=check)

    await ctx.send('How much tome will this poll last for?(answer in a digit)')

    def check1(d):
      return d.author == ctx.author and d.content.isdigit()


    time1 = await self.client.wait_for('message',check=check1)

    await ctx.send('Minute, second or hour???')

    hsr = await self.client.wait_for('message',check=check)

    if hsr.content.lower() == 'm' or hsr.content.lower() == 'minute' or hsr.content.lower() == 'mins' or hsr.content.lower() == 'minutes' or hsr.content.lower() == 'min':
      delay = time1.content * 60
      


    elif hsr.content.lower() == 'h' or hsr.content.lower() == 'hour' or hsr.content.lower() == 'hrs' or hsr.content.lower() == 'hours' or hsr.content.lower() == 'hr':
      delay = time1.content * 3600
      


    elif hsr.content.lower() == 's' or hsr.content.lower() == 'secs' or hsr.content.lower() == 'sec' or hsr.content.lower() == 'second' or hsr.content.lower() == 'seconds':
      delay = time1.content 


    else:
      await ctx.send('Poll Cancelled due to wrong timing input')
      return


    message = await ctx.send(f'Q){msg1.content}\n:regional_indicator_a:{msg2.content}\n:regional_indicator_b:{msg3.content}\n:regional_indicator_c:{msg4.content}\n:regional_indicator_d:{msg5.content}')
    await message.add_reaction('\U0001f1e6')
    await message.add_reaction('\U0001f1e7')
    await message.add_reaction('\U0001f1e8')
    await message.add_reaction('\U0001f1e9')
    def reaction_check(e):
      return e.startswith('\U0001f1e6','\U0001f1e7','\U0001f1e8','\U0001f1e9') 

    res1 = await self.client.wait_for_reaction(emoji="\U0001f1e6", message=message, check=reaction_check)
    res2 = await self.client.wait_for_reaction(emoji="\U0001f1e7", message=message, check=reaction_check)
    res3 = await self.client.wait_for_reaction(emoji="\U0001f1e8", message=message, check=reaction_check)
    res4 = await self.client.wait_for_reaction(emoji="\U0001f1e9", message=message, check=reaction_check)

    rec1 = 0
    rec2 = 0
    rec3 = 0
    rec4 = 0

    while res1:
      rec1 += 1

    while res2:
      rec2 += 1

    while res3:
      rec3 += 1

    while res4:
      rec4 += 1

    await asyncio.sleep(int(delay))
    
    if rec1 > rec2 and rec1 > rec3 and rec1 > rec4:
      await message.reply(f'{msg2.content} is the winner of the pole!')

    elif rec2 > rec3 and rec2 > rec4 and rec2 > rec1:
      await message.reply(f'{msg3.content} is the winner of the pole!')

    elif rec3 > rec1 and rec3 > rec2 and rec3 > rec4:
      await message.reply(f'{msg4.content} is the winner of the pole!')

    elif rec4 > rec2 and rec4 > rec3 and rec4 > rec1:
      await message.reply(f'{msg5.content} is the winner of the pole!')

    else:
      await message.reply('Noone wins! because of equal reactions')

    await message.reply(f'The Poll is done {ctx.author.mention} check the results')


def setup(client):
  client.add_cog(Poll(client))