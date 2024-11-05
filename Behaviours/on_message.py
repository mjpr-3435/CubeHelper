from ..Functions import *
from ..modules import *

import CubeHelper.ListsLogic.MaterialLists as MaterialLists
import CubeHelper.ListsLogic.ConfigsManagement as ConfigsManagement
import CubeHelper.Banners.Introduction as Introduction

async def on_message(client: commands.Bot, message: discord.Message):
    if message.author.bot:
        return
    elif under_maintenance and not isDev(message.author):
        return
    elif message.reference and MaterialLists.isActiveList(message.reference.message_id):
        if message.content == 'delete':
            if not ConfigsManagement.isAllowedTo(message.author, message.guild.id):
                return
            
            material_list = await message.channel.fetch_message(message.reference.message_id)
            await material_list.delete()
            await message.delete()
            return
        
        MaterialLists.updateListFile(message.reference.message_id, message)
        await MaterialLists.updateListEmbed(message.reference.message_id, client)
        await message.delete()
        return
    
    if not isDev(message.author): return

    elif message.content == f'{prefix}create_banner':
        await message.channel.send(embed = Introduction.embed(client), view = Introduction.views())
        await message.delete()

    elif message.content == f'{prefix}servers':
        for guild in client.guilds:
            print(f'{guild.name}, {guild.id}')

    elif message.content.startswith(f'{prefix}invite '):
        server = message.content.removeprefix(f'{prefix}invite').strip()
        for guild in client.guilds:
            if guild.id == int(server):
                invite = await guild.text_channels[0].create_invite(
                    reason = 'Just want to peek at the server, hope you don\'t mind.', max_uses = 1)
                break  

        await message.channel.send(invite.url)
        await asyncio.sleep(20)
        await invite.delete()
