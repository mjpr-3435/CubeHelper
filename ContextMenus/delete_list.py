import CubeHelper.ListsLogic.MaterialLists as MaterialLists
import CubeHelper.ListsLogic.ConfigsManagement as ConfigsManagement

from ..Functions import *
from ..modules import *

class delete_list_command(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
        @client.tree.context_menu(name = 'Delete List')
        async def delete_list_option(interaction: discord.Interaction, message: discord.Message):
            if under_maintenance and not isDev(interaction.user):
                return
            elif not MaterialLists.isActiveList(message.id):
                return
            elif not ConfigsManagement.isAllowedTo(interaction.user, interaction.guild_id):
                await interaction.response.send_message(f'✖ This command is only allowed for users with the designated role {ConfigsManagement.designated_role_id(interaction.guild_id)} or administrators.', allowed_mentions = False, ephemeral = True, delete_after = 8)
                return
            
            await message.delete()
            MaterialLists.UpdateListInfo(message.id, {'state':'deactivated'})
            await interaction.response.send_message('✔', ephemeral = True, delete_after = 1)   

async def setup(client: commands.Bot):
    await client.add_cog(delete_list_command(client))