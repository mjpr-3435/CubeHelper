from ..modules import *

def isDev(user: discord.User) -> bool:
    return user.id == developer_id

def isAdmin(member: discord.Member) -> bool:
    return member.guild_permissions.administrator