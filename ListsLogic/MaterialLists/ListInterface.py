from ..MaterialLists.CSVInteraction import listInfo, UpdateListInfo
from ..MaterialLists.ListGenerators import listEmbed, editedByEmbed
from ..ConfigsManagement import isAllowedTo, guildInfo
from ...Functions import *
from ...modules import *

def updateListFile(list_id: int, message: discord.Message) -> None:
    cmd = message.content.lower().strip().split(" ")[0]
    args = [int(x) for x in message.content.lower().strip().split(" ")[1:] if x.isdecimal()]
    
    if len(args) == 0:
        return
    elif not cmd in ['check', 'farming', 'uncheck']:
        return
    
    list_path = listInfo(list_id, ['path'])
    df_material_list = pd.read_csv(list_path)
    list_len = df_material_list.shape[0]

    value = {'check': '✅', 'farming': '📋', 'uncheck': '❌'}

    for arg in args:
        if arg <= list_len:
            df_material_list.loc[arg - 1, 'Available'] = value[cmd]
            df_material_list.loc[arg - 1, 'Last Edit By'] = message.author.display_name
    df_material_list.to_csv(list_path, index = False)

def updateListFileAll(list_id: int, value : str, user: discord.user) -> None:
    list_path = listInfo(list_id, ['path'])
    df_material_list = pd.read_csv(list_path)
    df_material_list['Available'] = value
    df_material_list['Last Edit By'] = user.display_name
    df_material_list.to_csv(list_path, index = False)
    
async def updateListEmbed(list_id: int, client:commands.Bot, update_views = False) -> None:
    df_material_lists_log = pd.read_csv(csv_path_material_lists_log, index_col = 'index')
    material_list = df_material_lists_log.loc[(df_material_lists_log['list_id'] == list_id)]
    channel_id = material_list['channel_id'].values[0]
    message_id = material_list['message_id'].values[0]

    list = await client.get_channel(channel_id).fetch_message(message_id)

    if update_views:
        await list.edit(content = '', embed = listEmbed(message_id, client), view = listsViews())
    else:
        await list.edit(content = '', embed = listEmbed(message_id, client))

async def updateListsStyle(guild_id:int, client: commands.Bot) -> None:
    df_material_list_log = pd.read_csv(csv_path_material_lists_log, index_col = 'index')
    material_lists = df_material_list_log.loc[(df_material_list_log['guild_id'] == guild_id) & (df_material_list_log['state'] == 'active')]
    channel_id = material_lists['channel_id'].values
    message_id = material_lists['message_id'].values
    list_id = material_lists['list_id'].values
    
    for i in range(len(list_id)):
        try:
            list = await client.get_channel(channel_id[i]).fetch_message(message_id[i])
            await list.edit(embed = listEmbed(list_id[i], client))
        except:
            pass

async def reactiveLists(client: commands.Bot) -> None:
    df_material_lists_log = pd.read_csv(csv_path_material_lists_log, index_col = 'index')
    material_lists = df_material_lists_log.loc[(df_material_lists_log['state'] == 'active')]
    
    guild_id = material_lists['guild_id'].values
    channel_id = material_lists['channel_id'].values
    message_id = material_lists['message_id'].values
    list_id = material_lists['list_id'].values
    
    for i in range(len(list_id)):
        try:
            list = await client.get_channel(channel_id[i]).fetch_message(message_id[i])
            if under_maintenance and  guild_id[i] != developer_discord_id:
                await list.edit(embed = listEmbed(list_id[i], client))
            else:
                await list.edit(embed = listEmbed(list_id[i], client), view = listsViews())
        except:
            pass

class listsViews(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
    
    @discord.ui.button( label = '<<',
                        style = discord.ButtonStyle.gray)
    async def first_page_button(view, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content = '')
        UpdateListInfo(interaction.message.id, {'current_page': 1})
        await updateListEmbed(interaction.message.id, interaction.client)

    @discord.ui.button( label = '<',
                        style = discord.ButtonStyle.gray)
    async def previous_page_button(view, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content = '')
        current_page = listInfo(interaction.message.id,['current_page'])
        if current_page == 1:
            return
        UpdateListInfo(interaction.message.id, {'current_page': current_page - 1})
        await updateListEmbed(interaction.message.id, interaction.client)

    @discord.ui.button( label = '>',
                        style = discord.ButtonStyle.gray)
    async def next_page_button(view, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content = '')
        current_page = listInfo(interaction.message.id,['current_page'])
        max_page = listInfo(interaction.message.id, ['max_page'])
        if current_page == max_page:
            return
        UpdateListInfo(interaction.message.id, {'current_page': current_page + 1})
        await updateListEmbed(interaction.message.id, interaction.client)
    
    @discord.ui.button( label = '>>',
                        style = discord.ButtonStyle.gray)
    async def last_page_button(view, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content = '')
        max_page = listInfo(interaction.message.id,['max_page'])
        UpdateListInfo(interaction.message.id, {'current_page': max_page})
        await updateListEmbed(interaction.message.id, interaction.client)

class editedByViews(discord.ui.View):
    def __init__(self, list_id):
        super().__init__(timeout = None)
        self.current_page = 1
        self.list_id = list_id
        self.max_page = listInfo(list_id,['max_page'])

    @discord.ui.button( label = '<<',
                        style = discord.ButtonStyle.gray)
    async def first_page_button(view, interaction: discord.Interaction, button: discord.ui.Button):
        view.current_page = 1
        await interaction.response.edit_message(embed = editedByEmbed(view.list_id, interaction.client, view.current_page))

    @discord.ui.button( label = '<',
                        style = discord.ButtonStyle.gray)
    async def previous_page_button(view, interaction: discord.Interaction, button: discord.ui.Button):
        if view.current_page == 1:
            return
        view.current_page -= 1
        await interaction.response.edit_message(embed = editedByEmbed(view.list_id, interaction.client, view.current_page))

    @discord.ui.button( label = '>',
                        style = discord.ButtonStyle.gray)
    async def next_page_button(view, interaction: discord.Interaction, button: discord.ui.Button):
        view.current_page += 1
        await interaction.response.edit_message(embed = editedByEmbed(view.list_id, interaction.client, view.current_page))

    @discord.ui.button( label = '>>',
                        style = discord.ButtonStyle.gray)
    async def last_page_button(view, interaction: discord.Interaction, button: discord.ui.Button):
        view.current_page = view.max_page
        await interaction.response.edit_message(embed = editedByEmbed(view.list_id, interaction.client, view.current_page))