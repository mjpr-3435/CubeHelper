from ..Functions import *
from ..modules import *

import CubeHelper.ListsLogic.MaterialLists as MaterialLists

async def on_message_delete(client: commands.Bot, message: discord.Message):
    if MaterialLists.isActiveList(message.id):
        MaterialLists.UpdateListInfo(message.id, {'state':'deactivated'})