import discord
from discord.ext import commands
from pymongo import MongoClient
from os import getenv
import json

cluster = MongoClient(getenv("RANK_PASS")) # Don't include "<" and ">" fill in those with your credentials
collection = cluster.rank.rank

class Rank(commands.Cog):
  
  def __init__(self,client):
    self.client=client

  @commands.Cog.listener()
  async def on_message(self,message):
    if message.author.bot:
      return
    if message.author == self.client.user:
      return

    # print(f"I heard a message from {message.author.name}, server {message.guild.name}")

    # This section below fails if the guild the message was sent from is not in the json file
    
    with open('lvle.json','r') as f:
        a = json.load(f)

        try:
        
          m = a[str(message.guild.id)]

        except:
          return #raise
   
        


    rankinfo = collection.find_one({"guild":message.guild.id,"member": message.author.id})

    if not rankinfo:
        collection.insert_one({"guild":message.guild.id,"member":message.author.id,"xp":2,"level":0})
        return

    

    rankinfo['xp'] += 2

    collection.replace_one({"guild":rankinfo['guild'],"member":rankinfo['member']},{"guild":rankinfo['guild'],"member":rankinfo['member'],"xp":rankinfo['xp'],"level":rankinfo['level']})

    if rankinfo['xp'] in level_check_point:
      if rankinfo['xp'] == 0:
        return

      await message.channel.send(f'Congratulations {message.author.mention} You are now level {rankinfo["level"]+1}🎉🥳!!!')
      rankinfo['level'] += 1

      collection.replace_one({"guild":rankinfo['guild'],"member":rankinfo['member']},{"guild":rankinfo['guild'],"member":rankinfo['member'],"xp":rankinfo['xp'],"level":rankinfo['level']})

      

  @commands.command(aliases=['Rank','RANK','LEVEL','LVL','lvl','Lvl','Level','level'])
  async def rank(self,ctx,member:discord.Member=None):
    
    with open('lvle.json','r') as f:
        a = json.load(f)

        try:
        
          m = a[str(ctx.guild.id)]

        except:
          return await ctx.send("Leveling is not enabled for this server...\nType levelenable or el for enabling")

    if member == None:
      member = ctx.author

    if member.bot:
      member = ctx.author

    rankinfo = collection.find_one({"guild":ctx.guild.id,"member": member.id})
    if not rankinfo:
        
        return await ctx.send(f'{member.name} needs to talk first')

    my_query = { "guild": ctx.guild.id }
    user_dic = collection.find(my_query).sort("xp",-1)
    print(user_dic)
    positions = []
    for user_data in user_dic:
      positions.append(user_data['member'])

    n = None
    print(positions)

    for i in range(1,len(positions)+1):
      print(positions)
      if positions[i-1] == member.id:
        print(i-1)
        print(i)
        n = i
        print(n)
        break
      else:
        continue


    embed = discord.Embed(title=f'Rank #{n}', description=f"{rankinfo['xp']} XP and {rankinfo['level']} level", color=discord.Color.blue())
    embed.set_author(name=member, icon_url=member.avatar_url)

    lvl = rankinfo['level']

    exp = rankinfo['xp']
    
    a = exp
    b = round(level_check_point[lvl+1])
    c = round(level_check_point[lvl])
    
    number_of_blue_squares = round((a-c)/(b-c) * 10) 
    number_of_white_squares = (int(10 - number_of_blue_squares))
    value =':blue_circle:' * number_of_blue_squares + ':white_circle:' * number_of_white_squares 
    # print(f'exp={a}\tb={b}\tc={c}\tbcircles={int(((a-c)/(b-c))*100)}\%\t')
    embed.add_field(name=f'Progress to next level - {int((a-c)/(b-c) * 100)}\%',value=value,inline=False)
    #embed.add_field(name='the first person is...',value=f'1)<@!{max_player}>, xp = {max_exp}')
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

  @commands.command(aliases=['lb','LB','Lb'])
  async def leaderboard(self,ctx,num:int=None):
    embed = discord.Embed(title=f"{ctx.guild.name} TOP Users", description='(EXPERIENCE POINTS)', colour=discord.Colour.blue())
    embed.set_thumbnail(url=ctx.guild.icon_url_as(size=64))
    embed.set_footer(text=f'Requested by: {ctx.author.name}', icon_url=ctx.author.avatar_url)

    my_query = { "guild": ctx.guild.id }
    user_dic = collection.find(my_query).sort("xp",-1)

    count = 0

    if num == None:
      for user_data in user_dic:
        m = ctx.guild.get_member(user_data['member'])
        embed.add_field(name=m, value=f"EXP : **{user_data['xp']}** LEVEL : {user_data['level']}", inline=False)

    else:

        for user_data in user_dic:
          if count == num:
            break

          else:

            m = ctx.guild.get_member(user_data['member'])
            embed.add_field(name=m, value=f"EXP : **{user_data['xp']}** LEVEL : {user_data['level']}", inline=False)
            count += 1

        

    await ctx.send(embed=embed)



level_check_point = [0,20, 100, 200, 350, 500, 700, 900, 1100, 1300, 1500,
                     1800, 2300, 2700, 3100, 3700, 4300, 5000, 5800, 6700, 7700, 9000, 10300,11600,13000,15000,17000,19000,22000,25000]





def setup(client):
  client.add_cog(Rank(client))