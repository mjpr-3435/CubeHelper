import CubeHelper.ListsLogic.ConfigsManagement as ConfigsManagement
import CubeHelper.ListsLogic.MaterialLists as MaterialLists

from ..modules import *
from ..Functions import *

class recover_command(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
        @client.tree.command(   name =         'recover', 
                        description =  'Recover a material list',
                        extras =       {'rank' : 0})
        async def recover_command(interaction: discord.Interaction):
            await interaction.response.defer(ephemeral = True)

            if under_maintenance and not isDev(interaction.user):
                return
            elif not MaterialLists.canRecover(interaction.guild_id):
                response = await interaction.followup.send('✖ To use this command, you need to have created at least one list and deleted it.')
                await response.delete(delay = 8)
                return
            elif not ConfigsManagement.isAllowedTo(interaction.user, interaction.guild_id):
                response = await interaction.followup.send(f'✖ This command is only allowed for users with the designated role <@&{ConfigsManagement.guildInfo(interaction.guild.id, ["role_id"])}> or administrators.', allowed_mentions = False)
                await response.delete(delay = 8)
                return

            Embed = discord.Embed(
                title = '',
                colour = default_embed_colour,
                description = 
                'In the dropdown below, you\'ll find the last 10 lists for this server.\n'
                'Select the one you want to recover.')

            class selection_view(discord.ui.View):
                def __init__(self):
                    super().__init__(timeout = None)
                
                @discord.ui.select( placeholder = 'Select a list', 
                                    options = MaterialLists.lastTenLists(interaction.guild_id))
                async def list_selection(views, interaction: discord.Interaction, selection):
                    try:
                        await interaction.response.edit_message(content = '✔', embed = None, view = None, delete_after = 1)
                    except:
                        await interaction.response.send(content = '✔', embed = None, view = None, delete_after = 1)

                    message = await interaction.channel.send('Generating list...')
                    
                    new_values = {'state': 'active', 
                                'channel_id': message.channel.id, 
                                'message_id': message.id, 
                                'list_id': message.id}

                    MaterialLists.UpdateListInfo(int(selection.values[0]), new_values)
                    await MaterialLists.updateListEmbed(message.id, interaction.client, update_views = True)
                
            await interaction.followup.send(embed = Embed, view = selection_view())

async def setup(client: commands.Bot):
    await client.add_cog(recover_command(client))