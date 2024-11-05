from ..modules import *

async def call_behaviours(function: str, args: tuple):
    
    try: 
        module = importlib.import_module(f"{addon_name}.Behaviours")
        function = getattr(module, function)
        
        await function(*args)
    except AttributeError: 
        pass
    except: 
        print(f'Error in {function}() of {addon_name}:\n{traceback.format_exc()}\n')