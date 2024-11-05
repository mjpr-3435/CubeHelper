import CubeHelper.ListsLogic.ConfigsManagement as ConfigsManagement
import CubeHelper.ListsLogic.MaterialLists as MaterialLists

from ..modules import *
from ..Functions import *

class set_view_style_command(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        @client.tree.command(   name =         'list_style',   
                                description =  'Sets how lists will be displayed',
                                extras =       {'rank' : 1})
        @choices(view_style = [Choice(name = 'Default', value = 0), Choice(name = 'Cellphone', value = 1)])
        async def set_view_style_command(interaction: discord.Interaction, view_style : Choice[int]):
            await interaction.response.defer(ephemeral = True)
            
            if under_maintenance and not isDev(interaction.user):
                return
            elif not isAdmin(interaction.user):
                response = await interaction.followup.send('✖ This command is restricted to administrators only.')
                await response.delete(delay = 5)
                return
            
            ConfigsManagement.newServerLog(interaction.guild)
            ConfigsManagement.updateGuildInfo(interaction.guild_id, {'list_style': view_style.name.lower()})
            await MaterialLists.updateListsStyle(interaction.guild.id, interaction.client)
            response = await interaction.followup.send('✔')
            await response.delete(delay = 1)

async def setup(client: commands.Bot):
    await client.add_cog(set_view_style_command(client))