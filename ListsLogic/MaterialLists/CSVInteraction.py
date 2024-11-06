from ...Functions import *
from ...modules import *

async def updateStates(client: commands.Bot) -> None:
    df_material_lists_log = pd.read_csv(csv_path_material_lists_log, index_col = 'index')
    df_active_material_lists = df_material_lists_log.loc[df_material_lists_log['state'] == 'active']
    message_id = df_active_material_lists['message_id'].to_list()
    channel_id = df_active_material_lists['channel_id'].to_list()

    for i in range(len(message_id)):
        try:
            await client.get_channel(channel_id[i]).fetch_message(message_id[i])
        except:
            df_material_lists_log.loc[df_material_lists_log['message_id'] == message_id[i], 'state'] = 'deactivated'
    df_material_lists_log.to_csv(csv_path_material_lists_log)
  
def newListLog(interaction: discord.Interaction, list_title: str, message_id: int) -> None:
    list_path = os.path.join(path_lists_files,str(interaction.guild_id), f'{interaction.id}.csv')
    list_len = pd.read_csv(list_path).shape[0]
    df_material_list_log = pd.read_csv(csv_path_material_lists_log, index_col = 'index')
    
    if list_len/60%1 == 0: 
        max_page = list_len//60
    else:
        max_page = list_len//60 + 1

    df_new_material_list_log = pd.DataFrame({ 'title' : list_title,
                                              'current_page': 1,
                                              'max_page': max_page,
                                              'list_len': list_len,
                                              'state' : 'active',
                                              'guild_id': interaction.guild_id,
                                              'channel_id': interaction.channel_id,
                                              'message_id' : message_id,
                                              'list_id' : message_id,
                                              'file_name' : interaction.id,
                                              'path': list_path}, index = [df_material_list_log.shape[0]])
    
    if df_material_list_log.shape[0] == 0:
        df_new_material_list_log.rename_axis('index').to_csv(csv_path_material_lists_log)
    else:
        df_material_list_log = pd.concat([df_material_list_log,df_new_material_list_log]).rename_axis('index')
        df_material_list_log.to_csv(csv_path_material_lists_log)

def UpdateListInfo(list_id: int, new_values: dict) -> None:
    df_material_list_log = pd.read_csv(csv_path_material_lists_log, index_col = 'index')
    for key, value in new_values.items():
        df_material_list_log.loc[df_material_list_log['list_id'] == list_id, key] = value
    df_material_list_log.to_csv(csv_path_material_lists_log)

def listInfo(list_id: int, request: list) -> tuple:
    df_material_lists_log = pd.read_csv(csv_path_material_lists_log, index_col = 'index')
    material_list = df_material_lists_log.loc[df_material_lists_log['list_id'] == list_id]
    info = []
    for arg in request:
        info.append(material_list[arg].values[0])
    
    if len(request) == 1:
        return info[0]
    
    return tuple(info)

def lastTenLists(guild_id:int) -> discord.SelectOption:
    df_registered_servers = pd.read_csv(csv_path_registered_servers, index_col = 'index')

    if guild_id in df_registered_servers['guild_id'].values:
        df_material_lists_log = pd.read_csv(csv_path_material_lists_log, index_col = 'index')
        material_lists = df_material_lists_log.loc[(df_material_lists_log['guild_id'] == guild_id) & (df_material_lists_log['state'] == 'deactivated')]
        list_title = material_lists['title'].values
        list_id    = material_lists['list_id'].values
        return [discord.SelectOption(label = list_title[-i-1], value = str(list_id[-i-1])) for i in range(len(list_id)) if i < 10]

def canRecover(guild_id: discord.Guild) -> bool:
    df_material_lists_log = pd.read_csv(csv_path_material_lists_log, index_col = 'index')
    guilds_id = df_material_lists_log.loc[df_material_lists_log['state'] == 'deactivated']['guild_id'].to_list()
    
    if guild_id in guilds_id:
        return True
    
    return False

def isActiveList(list_id: int) -> bool:
    df_material_lists_log = pd.read_csv(csv_path_material_lists_log, index_col = 'index')
    material_list_match = (df_material_lists_log['list_id'] == list_id) & (df_material_lists_log['state'] == 'active')

    if material_list_match.any():
        return True
    
    return False  