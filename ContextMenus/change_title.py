import CubeHelper.ListsLogic.MaterialLists as MaterialLists
import CubeHelper.ListsLogic.ConfigsManagement as ConfigsManagement

from ..Functions import *
from ..modules import *

class change_list_title_command(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
        @client.tree.context_menu(name = 'Change-Title')
        async def change_list_title_option(interaction: discord.Interaction, message: discord.Message):
            if under_maintenance and not isDev(interaction.user):
                return
            elif not MaterialLists.isActiveList(message.id):
                return
            elif not ConfigsManagement.isAllowedTo(interaction.user, interaction.guild_id):
                await interaction.response.send_message(f'✖ This command is only allowed for users with the designated role {ConfigsManagement.designated_role_id(interaction.guild_id)} or administrators.', allowed_mentions = False, ephemeral = True, delete_after = 8)
                return
            
            class message_modal(discord.ui.Modal, title = 'New title'):
                new_title = discord.ui.TextInput(label = 'Enter the new title here', style = discord.TextStyle.paragraph)
                
                async def on_submit(modal, interaction: discord.Interaction):
                    MaterialLists.UpdateListInfo(message.id, {'title': modal.new_title.value})
                    await MaterialLists.updateListEmbed(message.id, interaction.client)
                    await interaction.response.send_message('✔', ephemeral = True, delete_after = 1)                
                
            await interaction.response.send_modal(message_modal())

async def setup(client: commands.Bot):
    await client.add_cog(change_list_title_command(client))