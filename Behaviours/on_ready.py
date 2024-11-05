from ..modules import *
import CubeHelper.ListsLogic.MaterialLists as MaterialLists

async def on_ready(client: commands.Bot):
    print(f'Logged in as {client.user}!')
    
    if under_maintenance:
        presence_message            = 'Under Maintenance'
    else:
        presence_message            = 'Use /help'

    await client.change_presence(
            activity = discord.CustomActivity(
            name = presence_message,
            status = discord.Status.online)
        )
    
    await MaterialLists.updateStates(client)
    await client.tree.sync()
    await MaterialLists.reactiveLists(client)