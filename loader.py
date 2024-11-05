from .modules import *

async def load(client: commands.Bot):
    print(f'\nLoading\t\tAddon\t\t{addon_name}')
    cogs = [os.path.join(addon_name, 'Commands'), os.path.join(addon_name, 'ContextMenus')]

    for cog in cogs:
        scripts = [filename for filename in os.listdir(cog) if filename.endswith('.py')]
        for script in scripts:
            await client.load_extension(f'{cog.replace(os.sep,".")}.{script[:-3]}')
            print(f'   • Loaded {os.path.basename(cog[:-1])} {script[:-3]}')
            
    print('   Loading Complete')
