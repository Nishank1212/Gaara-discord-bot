import discord
from discord.ext import commands
from os import getenv
import requests
import asyncio
import json
import time


class ChatBot(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command()
	async def chatdisable(self,ctx):
		pass

	@commands.command(name="chatenable",aliases=['CO','CHATENABLE','Co','co','Chatenable'])
	async def chatenable(self,ctx, *, message=None):

		with open('prefixes.json','r') as f:
			prefixes = json.load(f)
		try:

			pre = prefixes[str(ctx.guild.id)]

		except:
			
			pre = '~~'

		global chat, chat_author_id
		if int(ctx.author.id) == 'lol':
			await ctx.send('I dont wanna talk to you')
		else:
			chat = 1
		headers = {"pass": getenv("pass"), "auth": "Nishank#8839"}
		chat_author_id = ctx.author.id
		while chat == 1:
			message = await self.client.wait_for('message')
			if message.author == self.client.user:	
				return
			if chat_author_id == message.author.id:
				if message.content.lower() == "gaara go to sleep" or message.content.lower() == f"{pre}chatdisable":
				
					chat = 0
					chat_author_id = 0
				
				elif message.content.lower() == "795923067552661524":
					chat_author_id = 795923067552661524
					await message.channel.send("~chaton")
					await message.channel.send("hi")
			
				else:
					t0 = time.time()
					async with ctx.typing():
						response = requests.get(f"https://entropi.mythicalkitten.com/ChatBotAPIv0?message={discord.utils.escape_mentions(message.content)}&userid={chat_author_id}", headers=headers).json()
						response = response['Message']
					try:
						t1 = time.time()
						if (t1-t0) < 2:
							await asyncio.sleep(2-t1+t0)
							await message.channel.send(response)
						else:
							await message.channel.send(response)
					except discord.errors.HTTPException:
						await message.channel.send("I may be too good but can't do that hermano!")    


def setup(client):
  client.add_cog(ChatBot(client))