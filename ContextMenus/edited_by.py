import CubeHelper.ListsLogic.MaterialLists as MaterialLists

from ..Functions import *
from ..modules import *

class edited_by_command(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
        @client.tree.context_menu(name = 'Edited-By')
        async def edited_by_option(interaction: discord.Interaction, message: discord.Message):
            if under_maintenance and not isDev(interaction.user):
                return
            elif not MaterialLists.isActiveList(message.id):
                return
            elif not isAdmin(interaction.user):
                await interaction.response.send_message('✖ This option is restricted to administrators only.', ephemeral = True, delete_after = 5)
                return
            
            await interaction.response.send_message(embed = MaterialLists.editedByEmbed(message.id, interaction.client, 1), 
                                                    view = MaterialLists.editedByViews(message.id),
                                                    ephemeral = True)

async def setup(client: commands.Bot):
    await client.add_cog(edited_by_command(client))