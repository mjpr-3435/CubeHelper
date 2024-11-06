from .modules import *
import CubeHelper.ListsLogic.MaterialLists  as MaterialLists

async def load(client: commands.Bot):
    print(f'\nLoading\t\tAddon\t\t{addon_name}')
    cogs = [os.path.join(addon_name, 'Commands'), os.path.join(addon_name, 'ContextMenus')]

    for cog in cogs:
        scripts = [filename for filename in os.listdir(cog) if filename.endswith('.py')]
        for script in scripts:
            try:
                await client.load_extension(f'{cog.replace(os.sep,".")}.{script[:-3]}')
                print(f'   • Loaded {os.path.basename(cog[:-1])} {script[:-3]}')
            except Exception:
                print(f'   • Unable to load {os.path.basename(cog[:-1])} {script[:-3]}')
    
    if under_maintenance:
        presence_message            = 'Under Maintenance'
    else:
        presence_message            = 'Use /help'

    await client.change_presence(
            activity = discord.CustomActivity(
            name = presence_message,
            status = discord.Status.online)
        )
    
    print(f'   • Updating Logs...')
    await MaterialLists.updateStates(client)
    print(f'   • Logs updated')
    print(f'   • Reactivating lists...')
    await MaterialLists.reactiveLists(client)
    print(f'   • Lists reactivated')
            
    print('   Loading Complete')
