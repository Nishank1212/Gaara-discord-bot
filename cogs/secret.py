import discord
import sys
from discord.ext import commands
from replit import db
from PIL import Image, ImageColor

class secret(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Secret_Command', 'secret_command'], hidden=True)
    async def secret(self, ctx, message=None):

        if not message:
            description = inspect_records()
        else:
            description = inspect_records(message)

        embed = discord.Embed(title='SECRET TITLE', colour=discord.Colour(
            0xE5E242), description=description)

        embed.set_image(
            url="https://images.pexels.com/photos/3156660/pexels-photo-3156660.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
        embed.set_thumbnail(url=ctx.message.author.avatar_url_as(size=64))

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)

    @commands.Cog.listener("on_message")
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def rankdoor(self, message):

        if message.author.bot:
            return
            
        exp, lvl = get_stats(message.author.id)

        if lvl > 10:

          add_exp(message.author.id,1)

        else:

          add_exp(message.author.id,2)


        

        # Check for level promotion
        if exp in level_check_point:
            if exp == 0:
              pass
            else:
              update_level(message.author.id)
              await message.channel.send(f'Congratulations {message.author.mention} You are now level {lvl}🎉🥳!!!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                title='Cooldown!', description=f'woah! slow it down buddy, this command is in a cooldown you can try after {round(error.retry_after)} seconds', colour=discord.Colour.blue())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):

      
            embed=discord.Embed(title='Missing Permissions',description='You are missing permissions to run this command buddy',colour=discord.Colour.blue())
            await ctx.send(embed=embed)

        elif isinstance(error, commands.CommandNotFound):

      
             embed=discord.Embed(title='Missing Command',description='Command Not Found buddy! :thinking:',colour=discord.Colour.blue())
             await ctx.send(embed=embed)




        else:
          raise error

        



    @commands.command(aliases=['restart_db', 'nuke_db'], hidden=True)
    async def delete_db(self, ctx):
        if ctx.message.author.id in masters:
            nuke_db()
            await ctx.send(f'*Explosion Noises* What have you done {ctx.message.author.name}?')
        else:
            await ctx.send(f'You do not have that power {ctx.message.author.name}')
        return

    @commands.command(aliases=['rank', 'lvl', 'level'], hidden=True)
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def level_request(self, ctx, member: discord.Member = None):

        if not member:  # Command user requests own info

            max_exp, max_player = get_leader()

            print(max_player, max_exp)
            exp, lvl = get_stats(ctx.author.id)

            # blue =  exp/level_xp * 10
            # white = ':white_square:' * 10 - blue

            # percentage = exp/level_check_point[lvl] * 100
            # bar = get_bar(percentage)
          
            embed = discord.Embed(title='Level {}'.format(
                lvl), description=f"{exp} XP ", color=discord.Color.blue())
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            
            a = exp
            b = round(level_check_point[lvl+1])
            c = round(level_check_point[lvl])

            print(lvl)
            
            number_of_blue_squares = round((a-c)/(b-c) * 10) 
            number_of_white_squares = (int(10 - number_of_blue_squares))
            value =':blue_circle:' * number_of_blue_squares + ':white_circle:' * number_of_white_squares 
            # print(f'exp={a}\tb={b}\tc={c}\tbcircles={number_of_blue_squares}\t')
            embed.add_field(name=f'Progress to next level - {int((a-c)/(b-c) * 100)}\%',value=value,inline=False)
            embed.add_field(name='the first person is...',value=f'1)<@!{max_player}>, xp = {max_exp}')
    
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            #await ctx.send(image=bar)

        else:  # Command user requests info on someone else
            # Creates a user in db with 0 xp
            if member.id not in db.keys():
                db[member.id] = '0,0'

            max_exp, max_player = get_leader()

            exp, lvl = get_stats(member.id)
            lvl = user_level(exp)
            embed = discord.Embed(title='Level {}'.format(
                lvl), description=f"{exp} XP", color=discord.Color.blue())
            embed.set_author(name=member, icon_url=member.avatar_url)
            
            a = exp
            b = round(level_check_point[lvl+1])
            c = round(level_check_point[lvl])
            
            number_of_blue_squares = round((a-c)/(b-c) * 10) 
            number_of_white_squares = (int(10 - number_of_blue_squares))
            value =':blue_circle:' * number_of_blue_squares + ':white_circle:' * number_of_white_squares 
            # print(f'exp={a}\tb={b}\tc={c}\tbcircles={int(((a-c)/(b-c))*100)}\%\t')
            embed.add_field(name=f'Progress to next level - {int((a-c)/(b-c) * 100)}\%',value=value,inline=False)
            embed.add_field(name='the first person is...',value=f'1)<@!{max_player}>, xp = {max_exp}')
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(aliases=['LEADERBOARD','Leaderboard'])
    async def leaderboard(self,ctx):
      my_dic = {}
      for index in db.keys():
          exp, lvl = db[index].split(',')
          my_dic[index] = [exp]
          my_dic[index].append(lvl)
      # print('-------- my_dic ---------')
      # print(my_dic)

      # sort from new dictionary and report results
      top_list = sorted(my_dic.items(), key=lambda x: int(x[1][0]), reverse=True)
      print('------- TOP 5 --------')
      embed=discord.Embed(title='Leaderboard',colour=discord.Colour.blue())
      for x in range(5):
        embed.add_field(name=f'Rank #{x+1}', value=f'User <@!{top_list[x][0]}>, Exp={top_list[x][1][0]}, Level={top_list[x][1][1]}',inline=False)
      await ctx.send(embed=embed)

    @commands.command(aliases=['db_count', 'db_records'], hidden=True)
    async def print_all(self, ctx, pre=''):

        # Testing for displaying records in console
        # should print number of records in discord message also

        if ctx.message.author.id in masters:
            temp_txt = inspect_records(pre)
            await ctx.send(temp_txt)
        else:
            await ctx.send(f'You do not have that power {ctx.message.author.name}')
        return

    @commands.command(aliases=['guilds', 'my_guilds', 'listguilds', 'servers', 'my_servers'], hidden=False)
    async def list_guilds(self, ctx):
        ''' Returns a list of servers where Hokage is a member '''
        await ctx.channel.purge(limit=1)
        if ctx.author.id == 793433316258480128:
            temp_txt, index = '', 0
            async for guild in self.client.fetch_guilds(limit=150):
                    index += 1
                    temp_txt = temp_txt + \
                            f'**{index})** {guild.name}\n'
            embed = discord.Embed(title=f"{self.client.user.display_name}\'s Servers", colour=discord.Colour(
                    0xE5E242), description=temp_txt)

            embed.set_image(
                    url="https://image.shutterstock.com/image-vector/yay-vector-handdrawn-lettering-banner-260nw-1323618563.jpg")

            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

            await ctx.author.send(embed=embed)
        else:
            await ctx.send('You are not eligible for this command')


# Helper functions below


def add_exp(id,num):
    if id in db.keys():
        exp, lvl = db[id].split(',')
        db[id] = f'{str(int(exp)+int(num))},{lvl}'
        update_level(id)
    else:
        db[id] = f'{str(num)},{lvl}'


def user_level(exp):
    lvl = 0
    for index, num in enumerate(level_check_point):
        if exp >= num:
            lvl = index
    return lvl


def update_level(id):
    if not id:  # No id given
        return

    if id not in db.keys():  # id not in db
        db[id] = '0,0'

    exp, lvl = db[id].split(',')
    lvl = str(user_level(int(exp)))
    db[id] = f'{exp},{lvl}'


def get_bar(percentage=50, size=(300, 25), fill_color='blue'):
    '''
    This function returns a rectangular image based on percentage (0-100)
    "filled in" from left->right using the fill_color
    '''
    empty_bar = Image.new('RGB', size, ImageColor.getrgb('white'))
    fill_bar = Image.new(
        'RGB', ((size[0]*percentage)//100, size[1]), ImageColor.getrgb(fill_color))
    empty_bar.paste(fill_bar)

    return empty_bar


def get_stats(id=None):
    if not id:
        return 0, 0

    if id not in db.keys():
        db[id] = '0,0'

    exp, lvl = db[id].split(',')
    return int(exp), int(lvl)


def nuke_db():
    for k in db.keys():
        if k != 'encouragements':
            del db[k]
    print('Invoking NUKE function')
    return


def get_leader(guild=None):
    max_exp, max_player = 0, 0

    for player_id in db.keys():
        # Temp until restructure - skips data not user data
        if not player_id in ['encouragements', 'responding']:
            exp = int(db[player_id].split(',')[0])
            if exp > max_exp:
                max_exp = exp
                max_player = player_id

    return max_exp, max_player


level_check_point = [0,20, 100, 200, 350, 500, 700, 900, 1100, 1300, 1500,
                     1800, 2300, 2700, 3100, 3700, 4300, 5000, 5800, 6700, 7700, 9000, 10300,11600,13000,15000,17000,19000]
# level_check_point = [10,20,30,40,50,60,70,80,90,100,1000]
masters = [793433316258480128, 790459205038506055]


def inspect_records(pre=''):

    try:
        matches = db.prefix(pre)
        print(
            '-'*10 + f'Printing {len(matches)} db records matching prefix {pre}'+'-'*10)
        for item in matches:
            print(f'{item:18} : {db[item]}')
        print('-DONE-')
    except:
        return sys.exc_info()[0]

    if pre == '':
        return f'{len(matches)} db rows processed my MASTER'
    else:
        return f'{len(matches)} db rows processed using prefix {pre} my MASTER'

      
  

def setup(client):

    client.add_cog(secret(client))
