from .Embeds import commands_embed, context_menus_embed
from ...modules import *

class views(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        self.add_item(discord.ui.Button(label = 'Invite', url = link_bot_invite, style = discord.ButtonStyle.url))
    
    @discord.ui.button(label = 'Slash Commands',
                        style = discord.ButtonStyle.gray)
    async def slash_commands_button(view: discord.ui.View, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embed = commands_embed(interaction.client), ephemeral = True)

    @discord.ui.button(label = 'Context Menus',
                        style = discord.ButtonStyle.gray)
    async def context_menus_button(view: discord.ui.View, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embed = context_menus_embed, ephemeral = True)