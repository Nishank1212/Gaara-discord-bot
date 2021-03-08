import os
import shutil
import sqlite3
from typing import Dict
import discord
from discord.colour import Colour
from discord.ext import commands
from discord.ext.commands.core import command
from PIL import Image, ImageFilter, ImageDraw
from io import BytesIO
import re
import requests
import urllib.parse
from random import randint
from dotenv import load_dotenv

''' SQLite3 Database Stuff '''
# Creates connection to db in current directory
conn = sqlite3.connect(os.path.join(
    "./", "cogs", "images", "data", 'images.db'))
c = conn.cursor()

master_folder = os.path.join('./', 'cogs', 'images', 'masters')
output_folder = os.path.join('./', 'cogs', 'images', 'output')
gif_folder = os.path.join('./', 'cogs', 'images', 'gifs')
db_folder = os.path.join('./', 'cogs', 'images', 'data')
junk_folder = os.path.join('./', 'cogs', 'images', 'junk')
approved_users = [793433316258480128, 790459205038506055]


class images(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['pic', 'picture'], hidden=False)
    async def get_pic(self, ctx, *, search_txt=None):
        '''
        Provides an image using your search words (optional)
        Pictures retrieved using Pixabay's API
        '''

        if search_txt:
            embed = discord.Embed(title=f":mag: **{search_txt}** :mag:", colour=discord.Colour(
                0xE5E242), description=f"image provided by [Pixabay.com\'s API](https://pixabay.com/)")
        else:
            embed = discord.Embed(title=f"RANDOM PICTURE ... Good Luck :smile:", colour=discord.Colour(
                0xE5E242), description=f"image provided by [Pixabay.com\'s API](https://pixabay.com/)")

        result_link = pixabay_url_search(search_txt)

        embed.set_image(url=result_link)
        embed.set_thumbnail(
            url=self.client.user.avatar_url_as(size=64))
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=[x.split('.')[0] for x in os.listdir(master_folder)], hidden=True)
    async def fun_images(self, ctx, *, user=None):
        '''
        Manipulates images using locally stored 'master' images. Users may invoke using the name of the
        image in the master folder. The parameters are stored in a local database for each image.
        Images are manipulated using the message author and/or anyone mentioned in argument 'user'
        If a user is not given and the command expects two users, the message.author is used for both
        '''
        cmd = ctx.invoked_with

        # If image is not approved (development complete) - exit function
        if not cmd in approved_command_list():
            await ctx.send(f'{cmd} is not developed yet, you get what you get :smile:\nTry fun_list for a list of developed fun images.')

        # Check user validity using converter / if bad use message.author for user
        if (not user) or (user in ['me', 'ME']):
            tmp_member = ctx.message.author
        else:
            # retrieve member object using person (id or user.name or member reference)
            try:
                tmp_member = await commands.converter.MemberConverter().convert(ctx, user)
            except:
                await ctx.send(f"I don\'t know {user}, lets just use your avatar ...")
                tmp_member = ctx.message.author

        info = image_dic[cmd]
        im = Image.open(os.path.join(
            master_folder, image_dic[cmd]['filename']))
        im = im.copy()

        if im.mode != 'RGBA':
            im.convert('RGBA')
            im.putalpha(255)
            # Saving converted type if filename is .png --- still need method
            # To save converted to .png type and change db/dictionary before proceeding
            if image_dic[cmd]["filename"].split('.')[1] == '.png':
                im.save(os.path.join(master_folder,
                                     image_dic[cmd]['filename']))
            print(f'COG images : {cmd} converted to RGBA')

        asset = tmp_member.avatar_url_as(
            format=None, static_format='png', size=128)
        data = BytesIO(await asset.read())
        im1 = Image.open(data)

        im1 = im1.resize(info['size1'])
        im1 = mask_circle_transparent(im1)
        im1 = im1.rotate(info['rot1'])

        im.alpha_composite(im1, dest=info['paste1'])

        # process 2nd image (author) if not using message author for image1
        if (info['imgcount'] == 2) and (tmp_member != ctx.message.author):
            asset2 = ctx.author.avatar_url_as(
                format=None, static_format='png', size=128)
            data2 = BytesIO(await asset2.read())
            im2 = Image.open(data2)

            im2 = im2.resize(info['size2'])
            im2 = mask_circle_transparent(im2)
            im2 = im2.rotate(info['rot2'])

            im.alpha_composite(im2, dest=info['paste2'])

        # save results and send message in chat channel
        out_file = os.path.join(output_folder, f'{cmd}output.png')
        im.save(out_file)
        await ctx.send(file=discord.File(out_file))

    @commands.command(aliases=['slapmore', 'slap_more', 'slapagain', 'slap_again', 're-slap'], hidden=False)
    async def reslap(self, ctx, delay=500):
        '''
        Last person slapped gets slapped over and over
        Creates gif from last slap image created
        Optional delay can be used 100 - 1000 (lower number is faster)
        '''
        if not (100 <= delay <= 1000):
            delay = 500
        path = os.path.join(output_folder, 'slapoutput.png')
        im1 = Image.open(path)
        im1 = im1.copy()
        im2 = im1.copy()
        im2 = im2.transpose(Image.FLIP_LEFT_RIGHT)
        img_list = [im1, im2]
        outfile = os.path.join(gif_folder, "slapmore.gif")
        img_list[0].save(outfile,
                         save_all=True, append_images=img_list[1:], optimize=False, duration=delay, loop=0)
        file = (discord.File(outfile))
        await ctx.send(file=file)


    @commands.command(aliases=['alter', 'editpic', 'edit_pic', 'edit_img','edit_image'], hidden=False)
    async def edit_command(self, ctx, command_name=None, column=None, new_value=None):

        columns = {}
        columns['imgcount'] = "The number of user profile pics this command uses ex) edit dog **imgcount 2**"
        columns['size1'] = "image1\'s size in pixels (same x and y is normal) ex) edit dog **size1 200,200**"
        columns['rot1'] = "ccw rotation in degrees ex) edit dog **rot1 180**"
        columns['paste1'] = "(x,y) where image 1 will be pasted onto background image ex) edit dog **paste1 120,200**"
        columns['size2'] = "image2\'s size in pixels (same x and y is normal) ex) edit dog **size2 200,200**"
        columns['rot2'] = "ccw rotation in degrees for image 2 ex) edit dog **rot1 180**"
        columns['paste2'] = "(x,y) where image 2 will be pasted onto background image ex) edit dog **paste2 120,200**"
        columns['approved'] = "image is approved for use ex) edit dog **approved true**"

        # Check for valid command/column/value - give help and exit if not given
        if command_name not in image_dic.keys():
            temp_str = (f'missing valid command name ... **{command_name}** is not valid') + (
                f'\nCommand names : {"**"+"** **".join(image_dic.keys())}'+'**')
            await ctx.send(temp_str)
            return

        if column not in columns.keys():
            temp_str = f'Requires valid column_name ex) edit dog **size1** 200,200 ...\n column names are : {" ".join(columns.keys())}'
            await ctx.send(temp_str)
            return

        if not new_value:
            await ctx.send(f'Value required : {columns[column]}')
            return

        await ctx.send(f'MASTER **{command_name} {column} {new_value}** ready for processing ... keep working on this function')

        # format new_value based on column
        if column in ['imgcount', 'rot1', 'rot2']:
            new_value = int(new_value)
        elif column in ['size1', 'size2', 'paste1', 'paste2']:
            new_value = tuple(map(int, re.findall(r'[0-9]+', new_value)))
        elif column in ['approved']:
            if new_value.lower() in ['true', 'yes', '1']:
                new_value = True
            else:
                new_value = False

        # update image_dic
        image_dic[command_name][column] = new_value

        # create new image with updated image_dic
        await make_funfile(command_name, ctx.message.author, self.client.user)

        # display command image and info using updated image_dic
        await self.show_img_dic(ctx=ctx, command_name=command_name)

    @commands.command(aliases=['funlist'], hidden=False)
    async def fun_list(self, ctx):
        '''
        Get the list of fun image commands like 'dog' or 'slap' ...
        '''
        my_list = approved_command_list()
        temp_str = (', ').join(my_list)
        temp_str = temp_str + '\nex) dog oklahoma_bot'
        embed = discord.Embed(title='FUN IMAGE COMMANDS',
                              description='You can use these by themselves or mention another user', colour=discord.Colour.blue())
        embed.set_thumbnail(url=ctx.message.author.avatar_url_as(size=64))
        embed.set_image(
            url='https://cdn.tinybuddha.com/wp-content/uploads/2015/10/Having-Fun.png')
        embed.add_field(name='**Command List**', value=temp_str)
        await ctx.send(embed=embed)

    @commands.command(aliases=['cancel_edit', 'canceledit'], hidden=True)
    async def reload_dic(self, ctx):
        global image_dic
        image_dic = make_dic_from_db()
        await ctx.send('All pic information reloaded from db ... temporary changes are gone. ')

    @commands.command(aliases=['show'], hidden=True)
    async def show_img_dic(self, ctx, command_name='NOT ENTERED'):
        'Admin tool to show image manipulation dictionary values'

        # Exit if not in dictionary
        if not command_name in image_dic.keys():
            await ctx.send(f'**{command_name}** not in dictionary **image_dic** yet')
            return

        embed = discord.Embed(
            title=f':arrow_up: Last \"{command_name}\" Image Created :arrow_up:', description=':arrow_down: **current** image manipulation info\n(may not be last info used)', colour=discord.Colour.red())

        embed.set_thumbnail(url=ctx.message.author.avatar_url_as(size=64))

        temp = f'paste1: {image_dic[command_name]["paste1"]} rot1: {image_dic[command_name]["rot1"]} size1: {image_dic[command_name]["size1"]}'
        embed.add_field(name=f'avatar 1', value=temp, inline=False)

        if image_dic[command_name]["imgcount"] == 2:
            temp = f'paste2: {image_dic[command_name]["paste2"]} rot2: {image_dic[command_name]["rot2"]} size2: {image_dic[command_name]["size2"]}'
            embed.add_field(name=f'avatar 2', value=temp, inline=False)

        embed.add_field(
            name=f'summary', value=f'imgcount : {image_dic[command_name]["imgcount"]} approved : {"YES" if image_dic[command_name]["approved"] else "NO"}', inline=False)

        file = discord.File(os.path.join(
            output_folder, command_name + 'output.png'))
        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['save_img', 'saveimage', 'save_command'], hidden=False)
    async def save_image(self, ctx, command_name='UNDEFINED-COMMAND'):
        '''
        Saves all temporary edit command changes to database
        '''
        if command_name in image_dic.keys():
            save_command_to_db(command_name)
            await ctx.send(f'{command_name} saved')
        else:
            await ctx.send(f'{command_name} NOT FOUND in image_dic, nothing has been saved')

    @commands.command(aliases=['del_img', 'delete_img' 'delimage', 'del_image'], hidden=False)
    async def delete_command(self, ctx, command_name='UNDEFINED-COMMAND'):
        '''
        DELETES all information from the database and reloads image_dic
        '''
        if ctx.message.author.id not in approved_users:
            ctx.send(f'You are not authorized to run this command ... see approved_user list')
            return

        if command_name in image_dic.keys():
            delete_command_from_db(command_name)
        else:
            await ctx.send(f'{command_name} NOT FOUND in image_dic, nothing has been deleted')
            return

        # move image file from masters folder to junk folder
        move_file(master_folder, junk_folder,image_dic[command_name]['filename'])

        # remove command key from image_dic
        del image_dic[command_name]

    @commands.command(aliases=['unapproved', 'notdone'], hidden=False)
    async def unfinished(self, ctx):
        '''
        Shows list of images not yet developed into commands
        '''
        await ctx.send(f'Commands not yet finished : {approved_command_list(opposite=True)}')


# HELPER FUNCTIONS


async def make_funfile(cmd, user1, user2=None):
    '''
    Creates image using 1 or two Discord user/member(s) avatars
    Background image is taken from <<master_folder>> specified by <cmd>.
    Pasting parameters stored in <<image_dic>>.
    Typical use - user1 is invoking message's author
    This function returns the file_path for the new image.
    '''

    info = image_dic[cmd]
    im = Image.open(os.path.join(master_folder, info['filename']))
    im = im.copy()

    # May not be necessary
    if im.mode != 'RGBA':
        im.convert('RGBA')
        im.putalpha(255)
        # Saving converted type if filename is .png --- still need method
        # To save converted to .png type and change db/dictionary before proceeding
        if info["filename"].split('.')[1] == '.png':
            im.save(os.path.join(master_folder, info['filename']))
        print(f'{cmd} converted to RGBA')

    # First image pasted will be user1 unless user2 specified
    if user2:
        asset = user2.avatar_url_as(format=None, static_format='png', size=128)
    else:
        asset = user1.avatar_url_as(format=None, static_format='png', size=128)

    data = BytesIO(await asset.read())
    im1 = Image.open(data)
    im1 = im1.resize(info['size1'])
    im1 = mask_circle_transparent(im1)
    if info['rot1']:
        im1 = im1.rotate(info['rot1'])
    im.alpha_composite(im1, dest=info['paste1'])

    # Second image pasted will be user1 if command requires second image pasting
    if (info['imgcount'] == 2) and (user2):
        asset = user1.avatar_url_as(format=None, static_format='png', size=128)
        data = BytesIO(await asset.read())
        im2 = Image.open(data)
        im2 = im2.resize(info['size2'])
        im2 = mask_circle_transparent(im2)
        if info['rot2']:
            im2 = im2.rotate(info['rot2'])
        im.alpha_composite(im2, dest=info['paste2'])

    # save results and send return new_img_path
    new_img_path = os.path.join(output_folder, f'{cmd}output.png')
    im.save(new_img_path)
    # file = discord.File(out_file)
    return new_img_path


def pixabay_url_search(search_by=None):
    '''
    Uses Pixabay's API to search for a pic url based on search_by
    If None given a random one will be supplied
    '''
    if search_by:
        getVars = {'key': PIXABAY_API_KEY,
                   'q': search_by, 'safesearch': 'true', 'page': 1}
    else:
        getVars = {'key': PIXABAY_API_KEY, 'safesearch': 'true', 'page': 1}

    url = 'https://pixabay.com/api/?'
    response = requests.get(url + urllib.parse.urlencode(getVars))
    data = response.json()
    if len(data['hits']) > 0:
        rndpic = randint(0, len(data['hits'])-1)
        return data['hits'][rndpic]['webformatURL']
    else:
        return ('https://cdn.dribbble.com/users/283708/screenshots/7084432/media/451d27c21601d96114f0eea20d9707e2.png?compress=1&resize=400x300')


def mask_circle_transparent(pil_img, blur_radius=0, offset=0):
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse(
        (offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
    # mask.putalpha(0) may remove red effect in background if inserted here
    result = pil_img.copy()
    result.putalpha(mask)

    return result


def process_new_images():

    # Create new db record if necessary
    with conn:
        for filename in os.listdir(master_folder):
            # check if record already exists
            c.execute(
                f"SELECT EXISTS(SELECT 1 FROM paste_info WHERE command='{filename.split('.')[0]}')")
            if not bool(c.fetchone()[0]):  # New Command/Image not in db

                fun_size(master_folder, filename, 1500)

                # make new db record using default values
                print(
                    f'**NEW MASTER PIC DETECTED** {master_folder} + {filename}')
                text = "INSERT OR IGNORE INTO paste_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)"
                c.execute(text, (filename.split('.')[0], 1, 300, 300, 0,
                                 0, 0, 300, 300, 0, 0, 0, filename, 0))

        return


def make_dic_from_db():

    process_new_images()

    with conn:
        # Make commands_dictionary with info from db
        # Index is command_name and values are stored in a dictionary
        c.execute("SELECT * FROM paste_info")
        rows = c.fetchall()
        return_dic = {}
        for row in rows:
            info = {}
            info['name'] = row[0]
            info['imgcount'] = row[1]
            info['size1'] = tuple([row[2], row[3]])
            info['rot1'] = row[4]
            info['paste1'] = tuple([row[5], row[6]])
            info['size2'] = tuple([row[7], row[8]])
            info['rot2'] = row[9]
            info['paste2'] = tuple([row[10], row[11]])
            info['filename'] = row[12]
            info['approved'] = row[13]
            return_dic[row[0]] = info
        # Copy new_command_pics to output folder
        create_initial_output_pics()
        return return_dic


def create_initial_output_pics():
    '''
    Compare images in master folder and make corresponding
    images in output folder if missing
    '''
    master_filenames = os.listdir(master_folder)
    cmd_list = [f.split('.')[0] for f in master_filenames]

    outpics = os.listdir(output_folder)
    outpics = [f.replace("output", "").split('.')[0] for f in outpics]

    missing = set(cmd_list) - set(outpics)

    if missing:
        file_dic = {cmd_list[i]: master_filenames[i]
                    for i in range(len(cmd_list))}
        print(
            f'COG image : Attempting to add MISSING output files : {missing}')
        for file in missing:
            im = Image.open(os.path.join(master_folder, file_dic[file]))
            im = im.copy()
            if im.mode != 'RGBA':
                im = im.convert('RGBA')
            im.save(os.path.join(output_folder, file + 'output.png'))

    return


def save_command_to_db(cmd=None):
    # Use current image_dic[cmd] values
    with conn:
        temp = ('UPDATE paste_info SET '
                'imgcount = ?, sizex1 = ?, sizey1 = ?,rot1 = ?, '
                'pastex1 = ?, pastey1 = ?, sizex2 = ?, sizey2 = ?, '
                'rot2 = ?, pastex2 = ?, pastey2 = ?, approved = ? '
                'WHERE command = ' + f'\"{cmd}\"')
        info = image_dic[cmd]
        values = (info['imgcount'], info['size1'][0], info['size1'][1], info['rot1'],
                  info['paste1'][0], info['paste1'][1], info['size2'][0],
                  info['size2'][1], info['rot2'], info['paste2'][0], info['paste2'][1],
                  info['approved'])
        c.execute(temp, values)

def delete_command_from_db(cmd=None):
    # Use current image_dic[cmd] values
    with conn:
        temp = ('DELETE FROM paste_info WHERE command = ' + f'\"{cmd}\"')
        c.execute(temp)
        print(f'COG images : fun image command {cmd} deleted from db')

def approved_command_list(opposite=False):
    approved_list = []
    unfinished = []
    for command_name in image_dic.keys():
        if image_dic[command_name]['approved']:
            approved_list.append(command_name)
        else:
            unfinished.append(command_name)
    approved_list.sort()
    unfinished.sort()
    return unfinished if opposite else approved_list


def fun_size(folder, filename, max_dimension):
    '''
    image will be resized such that largest
    dimension will equal max_dimension
    Intended to be performed once upon new image
    file detection in master_folder
    '''
    im = Image.open(os.path.join(folder, filename))
    im = im.copy()
    x, y = im.size
    xbiggest = True if x >= y else False
    ratio = max_dimension/x if xbiggest else max_dimension/y
    newsize = int(x*ratio), int(y*ratio)
    im = im.resize(newsize)

    # save image in original folder
    im.save(os.path.join(folder, filename))
    print(f'IMAGE COG : {filename} resized from ({x},{y}) to {im.size}')

    return


def move_file(from_folder, to_folder, filename):
    dest = shutil.move(os.path.join(from_folder, filename),
                       os.path.join(to_folder, filename))
    return

image_dic = make_dic_from_db()


# get api token for image APIs
load_dotenv()
PIXABAY_API_KEY = os.getenv('PIXABAY_API_KEY')


def setup(client):  # Cog setup command
    client.add_cog(images(client))
