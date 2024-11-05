from ...Functions import *
from ...modules import *

def guildInfo(guild_id: int, request: list) -> tuple:
    df_registered_servers = pd.read_csv(csv_path_registered_servers, index_col = 'index')
    guild = df_registered_servers.loc[df_registered_servers['guild_id'] == guild_id]
    
    if guild.empty:
        info = [0 for i in range(len(request))]
        return tuple(info)
    
    info = []
    for arg in request:
        info.append(guild[arg].values[0])
    
    if len(request) == 1:
        return info[0]
    
    return tuple(info)

def updateGuildInfo(guild_id: int, new_values: dict) -> None:
    df_registered_servers = pd.read_csv(csv_path_registered_servers, index_col = 'index')
    for key, value in new_values.items():
        df_registered_servers.loc[df_registered_servers['guild_id'] == guild_id, key] = value
    df_registered_servers.to_csv(csv_path_registered_servers)

def newServerLog(guild: discord.Guild) -> None:
    df_registered_servers = pd.read_csv(csv_path_registered_servers, index_col = 'index')
    
    if guild.id in df_registered_servers['guild_id'].values:
        return
    
    new_server = pd.DataFrame({ 'guild_id': guild.id,
                                'role_id': 0,
                                'list_style': 'default'}, index = [df_registered_servers.shape[0]])
    
    if df_registered_servers.shape[0] == 0:
        new_server.rename_axis('index').to_csv(csv_path_registered_servers)
    else:
        df_registered_servers = pd.concat([df_registered_servers, new_server]).rename_axis('index')
        df_registered_servers.to_csv(csv_path_registered_servers)

def isAllowedTo(user: discord.User, guild_id: int) -> bool:
    df_registered_servers = pd.read_csv(csv_path_registered_servers, index_col = 'index')
    
    if isAdmin(user):
        return True
    
    try:
        designated_role_id = df_registered_servers.loc[df_registered_servers['guild_id'] == guild_id, 'role_id'].values[0]
        return designated_role_id in [role.id for role in user.roles]

    except:
        return False 