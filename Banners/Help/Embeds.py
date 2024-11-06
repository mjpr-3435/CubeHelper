import CubeHelper.ListsLogic.ConfigsManagement as ConfigsManagement
from ...modules import *

def embed(interaction: discord.Interaction) -> discord.Embed:
    embed = discord.Embed(
            title = '> Introduction to ' + interaction.client.user.display_name,
            colour = default_embed_colour,
            description = 
            f'{interaction.client.user.display_name} is a bot designed to generate interactive material lists. '
            f'By default, only administrators are allowed to create lists, if you want to grant permissions to users, check `setup`.')\
        .add_field(name = '> How to create a list?', inline = False, value =
            f'- Generate the material list in `.csv` format using Litematica.\n'
            f'- Execute the `/material_list` command.\n'
            f'- Attach the `.csv` file and give the list a title.\n')\
        .set_footer(text = 'If you have any suggestions or encounter any issues, I would appreciate it if you let me know.')\
        .set_thumbnail(url = link_default_thumbnail)

    return embed

def setup_embed(interaction: discord.Interaction) -> discord.Embed:
    designated_role, designated_style = ConfigsManagement.guildInfo(interaction.guild_id, ['role_id','list_style'])
    
    if not designated_role:
        designated_role = '`None`'
    else:
        designated_role = f'<@&{designated_role}>'

    if not designated_style:
        designated_style = 'None'

    embed = discord.Embed(
            title = 'Configuration Commands',       
            colour = default_embed_colour)\
        .add_field(name = '> /allowed_role', inline = False, value = 
            f'Designate the role that can interact with the bot to create lists.\n'
            f'Currently designated role: {designated_role}')\
        .add_field(name = '> /list_style', inline = False, value =
            f'Designate the style for material lists.\n'
            f'Currently designated style: `{designated_style}`')
    
    return embed

def features_embeds() -> list[discord.Embed]:
    embeds = [
        discord.Embed(
            title = '> Two List Styles',
            colour = default_embed_colour,
            description = 'Currently, the bot offers two styles for lists. The default style is designed to be more compact, but it doesn\'t display well on cellphones. If you prefer the list to look good on both platforms, you can use the cellphone style.')\
            .set_image(url = link_features_1),
        discord.Embed(
            title = '> Recover',
            colour = default_embed_colour,
            description = 'If you accidentally delete a list, you can recover it using the `/recover` command.')\
            .set_image(url = link_features_2),
        discord.Embed(
            title = '> Context Menus',
            colour = default_embed_colour,
            description = 
            'If you right-click on a list, you can use one of the following options:\n'
            '- `Check-all`: Mark all materials as collected.\n'
            '- `Uncheck-all`: Mark all materials as not collected.\n'
            '- `Edited-By`: Show who last modified the status of a material.\n'
            '- `Change-Title`: Change the title of the material list.\n')\
            .set_image(url = link_features_3)
             ]
    
    return embeds

def credits_embed() -> discord.Embed:
    embed = discord.Embed(
        title = '> Credits',
        colour = default_embed_colour,
        description = 
        f'Hosted by Aeternum Host.\n[[Aeternum Discord]](https://discord.gg/pXwV7BWd2P)\n\n'
        f'Coded by KassiuLo.\n[[Kassius\' Discord]]({link_discord_invite})\n\n'
        f'Logo by XMasi.')
    
    return embed

def github_embed() -> discord.Embed:
    embed = discord.Embed(
        title = '> Repository',
        colour = default_embed_colour,
        description = 
        f'GitHub. [[Link]]({link_repository})')
    
    return embed