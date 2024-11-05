import CubeHelper.ListsLogic.ConfigsManagement as ConfigsManagement
import CubeHelper.ListsLogic.MaterialLists as MaterialLists

from ..modules import *
from ..Functions import *

class material_list_command(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
        @client.tree.command(   name =         'material_list', 
                        description =  'Generates a material list',
                        extras =       {'rank' : 0})
        async def material_list_command(interaction: discord.Interaction, title: str, attachment: discord.Attachment):
            await interaction.response.defer(ephemeral = True)

            if under_maintenance and not isDev(interaction.user):
                return
            elif not ConfigsManagement.isAllowedTo(interaction.user, interaction.guild_id):
                response = await interaction.followup.send(f'✖ This command is only allowed for users with the designated role {ConfigsManagement.designated_role_id(interaction.guild_id)} or administrators.', allowed_mentions = False)
                await response.delete(delay = 8)
                return
            
            ConfigsManagement.newServerLog(interaction.guild)

            saved = await MaterialLists.tryToSaveAttachment(interaction, attachment)
            if not saved: return

            response = await interaction.followup.send('✔')
            await response.delete(delay = 1)
            message = await interaction.channel.send('Generating list...')
            MaterialLists.newListLog(interaction, title, message.id)
            await MaterialLists.updateListEmbed(message.id, interaction.client, update_views = True)

async def setup(client: commands.Bot):
    await client.add_cog(material_list_command(client))