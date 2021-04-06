import discord
from discord.ext import commands
import asyncio
class Poll(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command()
  #@commands.cooldown(1, 120, commands.BucketType.user)
  async def poll(self,ctx):
    loli = await ctx.send('What is The question you want?(note:there will be only 4 options)')

    def check(m):
        return m.author == ctx.author
    msg1 = await self.client.wait_for('message',check=check)
  
    await loli.delete()

    lol1 = await ctx.send('What is option 1?')

    msg2 = await self.client.wait_for('message',check=check)

    lol2 = await ctx.send('What is option 2?')
    await msg1.delete()
    await lol1.delete()

    msg3 = await self.client.wait_for('message',check=check)

    await msg2.delete()
    await lol2.delete()

    lol3 = await ctx.send('What is option 3?')

    msg4 = await self.client.wait_for('message',check=check)

    await msg3.delete()
    await lol3.delete()

    lol4 = await ctx.send('What is option 4?')

    msg5 = await self.client.wait_for('message',check=check)
    await msg4.delete()
    await lol4.delete()

    lol5 = await ctx.send('How much time will this poll last for?(answer in a digit)')

    def check1(d):
      return d.author == ctx.author and d.content.isdigit()


    time1 = await self.client.wait_for('message',check=check)
    await msg5.delete()
    await lol5.delete()
    if not time1.content.isdigit():
      return await ctx.send('Poll cancelled\ncontent isnt digit')

    lol6 = await ctx.send('Minute or second?\nTry to keep it as low time as possible')

    hsr = await self.client.wait_for('message',check=check)

    await time1.delete()
    await lol6.delete()

    if hsr.content.lower() == 'm' or hsr.content.lower() == 'minute' or hsr.content.lower() == 'mins' or hsr.content.lower() == 'minutes' or hsr.content.lower() == 'min':
      delay = time1.content * 60
  

    elif hsr.content.lower() == 's' or hsr.content.lower() == 'secs' or hsr.content.lower() == 'sec' or hsr.content.lower() == 'second' or hsr.content.lower() == 'seconds':
      delay = time1.content 


    else:
      await ctx.send('Poll Cancelled due to wrong timing input')
      return


    message = await ctx.send(f'Q){msg1.content}\n:regional_indicator_a:{msg2.content}\n:regional_indicator_b:{msg3.content}\n:regional_indicator_c:{msg4.content}\n:regional_indicator_d:{msg5.content}')
    await ctx.message.delete()
    await hsr.delete()
    await message.add_reaction('\U0001f1e6')
    await message.add_reaction('\U0001f1e7')
    await message.add_reaction('\U0001f1e8')
    await message.add_reaction('\U0001f1e9')
    rec1 = 0
    rec2 = 0
    rec3 = 0
    rec4 = 0
    
    await asyncio.sleep(int(delay))

    msg = await message.channel.fetch_message(message.id)
    for i in msg.reactions:
      if str(i.emoji)=="🇦":
        rec1 += i.count
      elif str(i.emoji)=="🇧":
        rec2 += i.count
      elif str(i.emoji)=="🇨":
        rec3 += i.count

      elif str(i.emoji)=="🇩":
        rec4 += i.count
      else:
        continue
    
    if rec1 > rec2 and rec1 > rec3 and rec1 > rec4:
      await message.reply(f'{ctx.author.mention} `:regional_indicator_a:{msg2.content}` is the winner of the pole!')

    elif rec2 > rec3 and rec2 > rec4 and rec2 > rec1:
      await message.reply(f'{ctx.author.mention} `:regional_indicator_b:{msg3.content}` is the winner of the pole!')

    elif rec3 > rec1 and rec3 > rec2 and rec3 > rec4:
      await message.reply(f'{ctx.author.mention} `:regional_indicator_c:{msg4.content}` is the winner of the pole!')

    elif rec4 > rec2 and rec4 > rec3 and rec4 > rec1:
      await message.reply(f'{ctx.author.mention} `:regional_indicator_d:{msg5.content}` is the winner of the pole!')

    else:
      await message.reply('Noone wins! because of equal reactions')


def setup(client):
  client.add_cog(Poll(client))