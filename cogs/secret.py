import discord
import sys
from discord.ext import commands
from replit import db
from PIL import Image, ImageColor
import json

class secret(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command(aliases=['guilds', 'my_guilds', 'listguilds', 'servers', 'my_servers'], hidden=False)
	async def list_guilds(self, ctx):
				''' Returns a list of servers where Hokage is a member '''
				await ctx.channel.purge(limit=1)
				if ctx.author.id == 793433316258480128 or 569105874912804874:
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


	@commands.command(aliases=['el','levelenable'])
	@commands.has_permissions(manage_messages=True)
	async def enableleveling(self,ctx):
		with open('lvle.json','r') as f:
			a = json.load(f)

		try:
			m = a[str(ctx.guild.id)]
			return await ctx.send('Already enabled Type leveldisable to disable it')
		except:

			a[ctx.guild.id] = 'enabled'

		with open('lvle.json','w') as f:
			json.dump(a,f)
		await ctx.send('Leveling Enabled for this server')

	@commands.command(aliases=['de','leveldisable'])
	@commands.has_permissions(manage_messages=True)
	async def disableleveling(self,ctx):
		with open('lvle.json','r') as f:
			a = json.load(f)

		try:

			del a[str(ctx.guild.id)]

		except:
			return await ctx.send('Already disabled by default type levelenable to enable it')

		with open('lvle.json','w') as f:
			json.dump(a,f)
		await ctx.send('Leveling disabled for this server')

	# # Helper functions below


	# def add_exp(id,num):
	#     if id in db.keys():
	#         exp, lvl = db[id].split(',')
	#         db[id] = f'{str(int(exp)+int(num))},{lvl}'
	#         update_level(id)
	#     else:
	#         db[id] = f'{str(num)},{lvl}'


	# def user_level(exp):
	#     lvl = 0
	#     for index, num in enumerate(level_check_point):
	#         if exp >= num:
	#             lvl = index
	#     return lvl


	# def update_level(id):
	#     if not id:  # No id given
	#         return

	#     if id not in db.keys():  # id not in db
	#         db[id] = '0,0'

	#     exp, lvl = db[id].split(',')
	#     lvl = str(user_level(int(exp)))
	#     db[id] = f'{exp},{lvl}'


	# def get_bar(percentage=50, size=(300, 25), fill_color='blue'):
	#     '''
	#     This function returns a rectangular image based on percentage (0-100)
	#     "filled in" from left->right using the fill_color
	#     '''
	#     empty_bar = Image.new('RGB', size, ImageColor.getrgb('white'))
	#     fill_bar = Image.new(
	#         'RGB', ((size[0]*percentage)//100, size[1]), ImageColor.getrgb(fill_color))
	#     empty_bar.paste(fill_bar)

	#     return empty_bar


	# def get_stats(id=None):
	#     if not id:
	#         return 0, 0

	#     if id not in db.keys():
	#         db[id] = '0,0'

	#     exp, lvl = db[id].split(',')
	#     return int(exp), int(lvl)


	# def nuke_db():
	#     for k in db.keys():
	#         if k != 'encouragements':
	#             del db[k]
	#     print('Invoking NUKE function')
	#     return


	# def get_leader(guild=None):
	#     max_exp, max_player = 0, 0

	#     for player_id in db.keys():
	#         # Temp until restructure - skips data not user data
	#         if not player_id in ['encouragements', 'responding']:
	#             exp = int(db[player_id].split(',')[0])
	#             if exp > max_exp:
	#                 max_exp = exp
	#                 max_player = player_id

	#     return max_exp, max_player


	# level_check_point = [0,20, 100, 200, 350, 500, 700, 900, 1100, 1300, 1500,
	#                      1800, 2300, 2700, 3100, 3700, 4300, 5000, 5800, 6700, 7700, 9000, 10300,11600,13000,15000,17000,19000]
	# # level_check_point = [10,20,30,40,50,60,70,80,90,100,1000]
	# masters = [793433316258480128, 790459205038506055]


	# def inspect_records(pre=''):

	#     try:
	#         matches = db.prefix(pre)
	#         print(
	#             '-'*10 + f'Printing {len(matches)} db records matching prefix {pre}'+'-'*10)
	#         for item in matches:
	#             print(f'{item:18} : {db[item]}')
	#         print('-DONE-')
	#     except:
	#         return sys.exc_info()[0]

	#     if pre == '':
	#         return f'{len(matches)} db rows processed my MASTER'
	#     else:
	#         return f'{len(matches)} db rows processed using prefix {pre} my MASTER'

		


def setup(client):

    client.add_cog(secret(client))
