from ...modules import *

def embed(client: commands.Bot) -> discord.Embed:
    embed = discord.Embed( 
            title = '> Introduction to ' + client.user.display_name,
            colour = default_embed_colour,
            description = 
            f'{client.user.display_name} is a public bot designed to generate interactive material lists, facilitating coordination among server members when farming materials.')\
        .set_image(url=link_introduction_banner)
    
    return embed

def commands_embed(client: commands.Bot) -> discord.Embed:
    commands = [f'- `/{command.name}` : ' for command in client.tree.get_commands(type = discord.AppCommandType.chat_input)]
    descriptions = [f'{command.description}' for command in client.tree.get_commands(type = discord.AppCommandType.chat_input)]
    
    embed = discord.Embed( 
            title = '> Slash Commands',
            colour = default_embed_colour,
            description = '\n'.join([f'{commands[i]}{descriptions[i]}' for i in range(len(commands))]))\
        .set_image(url = link_features_4)
    
    return embed

context_menus_embed = discord.Embed(
        title = '> Context Menus',
        colour = default_embed_colour,
        description = 
        'If you right-click on a list, you can use one of the following options:\n'
        '- `Check-all`: Mark all materials as collected.\n'
        '- `Uncheck-all`: Mark all materials as not collected.\n'
        '- `Edited-By`: Show who last modified the status of a material.\n'
        '- `Change-Title`: Change the title of the material list.\n')\
    .set_image(url = link_features_3)