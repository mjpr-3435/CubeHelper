from ..ConfigsManagement.CSVInteraction import guildInfo
from ..MaterialLists.CSVInteraction import listInfo
from ...Functions import *
from ...modules import *

def listEmbed(list_id:int, client:commands.Bot, ) -> discord.Embed:
    path, guild_id, title, current_page, list_len = listInfo(list_id, ['path', 'guild_id', 'title', 'current_page', 'list_len'])
    list_style = guildInfo(guild_id,['list_style'])

    df_list = pd.read_csv(path)
    available   = df_list['Available'].to_list()
    items       = df_list['Item'].to_list()
    total       = df_list['Total'].to_list()

    embed = discord.Embed(
            title = f'> {title}',
            colour = default_embed_colour)
    k = current_page - 1
    
    if list_style == 'cellphone':
        materials = ''
        header = '```✅ Material                                  Total       ```'
        dummy = '                                                      \n'
        n_fields, n_rows = 4, 15
          
        for i in range(list_len):
            item_display, quantitie = f'{available[i]} {i+1}:{items[i]}', f'{total[i]}'
            materials += item_display + dummy[len(item_display):-13] + quantitie + dummy[-13+len(quantitie):]
        
        embed.add_field(name = '', inline = False, value = header)
        j = 0

        while len(materials[(j+k*n_fields)*n_rows*len(dummy):((j+k*n_fields)+1)*n_rows*len(dummy)]) != 0 and j < n_fields:
            embed.add_field(name = '', inline = False, value = '```\n' + materials[(j+k*n_fields)*n_rows*len(dummy):((j+k*n_fields)+1)*n_rows*len(dummy)] + '```')
            j += 1
    else:
        n_fields, n_rows = 2, 30

        for j in range(n_fields):
            checks, materials, quantities = '', '', ''

            for i in range((j+k*n_fields)*n_rows, (j+1+k*n_fields)*n_rows):
                if i < list_len:
                    checks += f'{available[i]}\n'
                    materials += f'{i+1}: {items[i]}\n'
                    quantities += f'{total[i]}\n'
            if j == 0:
                embed.add_field(name = '✅', value = checks[:-1],inline = True)\
                    .add_field(name = 'Material', value = materials[:-1], inline = True)\
                    .add_field(name = 'Total', value = quantities[:-1],inline = True)
            else:
                embed.add_field(name = '', value = checks[:-1],inline = True)\
                    .add_field(name = '', value = materials[:-1], inline = True)\
                    .add_field(name = '', value = quantities[:-1],inline = True)
    
    embed.add_field(inline = False,name = '**How to use:**', value = 
        'Right-click on the list and select reply.\n'
        'Use one of the following commands:\n'
        '`check numbers` : material collected\n'
        '`farming numbers` : collecting material\n'
        '`uncheck numbers` : material not collected\n'
        '`delete` : to delete the list\n\n'
        'Example : `check 1 2 3`')
    
    if under_maintenance:
        embed.add_field(inline = False,name = '', value=
            '```\nThe bot is currently under maintenance.\nExcuse the inconvenience.```')

    embed.set_footer(text = client.user.name, icon_url = client.user.display_avatar)
    return embed

def editedByEmbed(list_id:int, client:commands.Bot, current_page: int) -> discord.Embed:
    path, guild_id, title, list_len = listInfo(list_id, ['path', 'guild_id', 'title', 'list_len'])
    list_style = guildInfo(guild_id,['list_style'])

    df_list = pd.read_csv(path)
    available   = df_list['Available'].to_list()
    items       = df_list['Item'].to_list()
    edited_by   = df_list['Last Edit By'].to_list()
    
    embed = discord.Embed(
            title = f'> {title}',
            colour = default_embed_colour)
    k = current_page - 1

    if list_style == 'cellphone':
        materials = ''
        header = '```✅ Material                                    Total       ```'
        dummy = '                                                          \n'
        n_fields, n_rows = 4, 15
          
        for i in range(list_len):
            item_display, by = f'{available[i]} {i+1}:{items[i]}', f'{edited_by[i][:12]}'
            materials += item_display + dummy[len(item_display):-13] + by + dummy[-13+len(by):]
        
        embed.add_field(name = '', inline = False, value = header)
        j = 0

        while len(materials[(j+k*n_fields)*n_rows*len(dummy):((j+k*n_fields)+1)*n_rows*len(dummy)]) != 0 and j < n_fields:
            embed.add_field(name = '', inline = False, value = '```\n' + materials[(j+k*n_fields)*n_rows*len(dummy):((j+k*n_fields)+1)*n_rows*len(dummy)] + '```')
            j += 1
    else:
        n_fields, n_rows = 2, 30

        for j in range(n_fields):
            checks, materials, by = '', '', ''

            for i in range((j+k*n_fields)*n_rows, (j+1+k*n_fields)*n_rows):
                if i < list_len:
                    checks += f'{available[i]}\n'
                    materials += f'{i+1}: {items[i]}\n'
                    by += f'{edited_by[i][:12]}\n'
            if j == 0:
                embed.add_field(name = '✅', value = checks[:-1],inline = True)\
                    .add_field(name = 'Material', value = materials[:-1], inline = True)\
                    .add_field(name = 'Total', value = by[:-1],inline = True)
            else:
                embed.add_field(name = '', value = checks[:-1],inline = True)\
                    .add_field(name = '', value = materials[:-1], inline = True)\
                    .add_field(name = '', value = by[:-1],inline = True)
     
    embed.set_footer(text = client.user.name, icon_url = client.user.display_avatar)
    return embed
