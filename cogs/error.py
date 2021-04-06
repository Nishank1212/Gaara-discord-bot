import discord
from discord.ext import commands



class Error(commands.Cog):
    def __init__(self,client):
      self.client=client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
				
        if isinstance(error, commands.MissingPermissions):

			
            embed=discord.Embed(title='Missing Permissions',description='You are missing permissions to run this command buddy',colour=discord.Colour.blue())
            await ctx.send(embed=embed)

  
        # elif isinstance(error, commands.CommandNotFound):
        #   embed = discord.Embed(
        #   title='Commmand Not Found', description="That's not a valid command", colour=discord.Colour.blue())
        #   await ctx.send(embed=embed)
        # elif isinstance(error, commands.MissingRequiredArgument):
        #   embed = discord.Embed(
        #   title='That wont work', description="Please fill in all the required arguments", colour=discord.Colour.blue())
        #   await ctx.send(embed=embed)
        elif isinstance(error,commands.MemberNotFound):
          embed=discord.Embed(title='Member Not Found',description='Thats Not A Valid Member',colour=discord.Colour.blue())
          await ctx.send(embed=embed)
#         # elif isinstance(error, commands.CommandNotFound):

      
#         #      embed=discord.Embed(title='Missing Command',description='Command Not Found buddy! :thinking:',colour=discord.Colour.blue())
#         #      await ctx.send(embed=embed)




        else:
	        raise error#u are not magic


def setup(client):
  client.add_cog(Error(client))