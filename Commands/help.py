import CubeHelper.Banners.Help as Help

from ..modules import *
from ..Functions import *

class help_command(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
        @client.tree.command(   name        =  'help', 
                                description =  'Provides an introduction to the bot',
                                extras      =  {'rank' : 0})
        async def help_commmand(interaction: discord.Interaction):
            if under_maintenance and not isDev(interaction.user):
                return
            
            await interaction.response.send_message(embed = Help.embed(interaction), view = Help.views())

async def setup(client: commands.Bot):
    await client.add_cog(help_command(client))