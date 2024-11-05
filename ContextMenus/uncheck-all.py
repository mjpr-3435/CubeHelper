import CubeHelper.ListsLogic.MaterialLists as MaterialLists

from ..Functions import *
from ..modules import *

class uncheck_all_command(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
        @client.tree.context_menu(name = 'Uncheck-all')
        async def uncheck_all_option(interaction: discord.Interaction, message: discord.Message):
            if under_maintenance and not isDev(interaction.user):
                return
            elif not MaterialLists.isActiveList(message.id):
                return
            elif not isAdmin(interaction.user):
                await interaction.response.send_message('✖ This option is restricted to administrators only.', ephemeral = True, delete_after = 5)
                return
                
            class message_modal(discord.ui.Modal, title = 'Confirmation Required'):
                confirmation = discord.ui.TextInput(label = 'Type \'confirmation\' here', style = discord.TextStyle.paragraph)
                
                async def on_submit(modal, interaction: discord.Interaction):
                    if str(modal.confirmation).lower() == 'confirmation': 
                        MaterialLists.updateListFileAll(message.id,'❌', interaction.user)
                        await MaterialLists.updateListEmbed(message.id, interaction.client)
                        await interaction.response.send_message('✔', ephemeral = True, delete_after = 1)  
            
            await interaction.response.send_modal(message_modal())

async def setup(client: commands.Bot):
    await client.add_cog(uncheck_all_command(client))