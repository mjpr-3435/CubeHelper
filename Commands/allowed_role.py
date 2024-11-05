import CubeHelper.ListsLogic.ConfigsManagement as ConfigsManagement

from ..modules import *
from ..Functions import *

class allowed_role_command(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
        @client.tree.command(   name =         'allowed_role',   
                                description =  'Sets the role allowed to create lists',
                                extras =       {'rank' : 1})
        async def allowed_role_command(interaction: discord.Interaction, role : discord.Role):
            await interaction.response.defer(ephemeral = True)
            
            if under_maintenance and not isDev(interaction.user):
                return
            elif not isAdmin(interaction.user):
                response = await interaction.followup.send('✖ This command is restricted to administrators only.')
                await response.delete(delay = 5)
                return
            
            ConfigsManagement.newServerLog(interaction.guild)
            ConfigsManagement.updateGuildInfo(interaction.guild_id, {'role_id': role.id})
            response = await interaction.followup.send('✔')
            await response.delete(delay = 1)

async def setup(client: commands.Bot):
    await client.add_cog(allowed_role_command(client))