from .Embeds import setup_embed,features_embeds,credits_embed, github_embed
from ...modules import *

class views(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
    
    @discord.ui.button( label = '✖',
                        style = discord.ButtonStyle.red)
    async def delete_button(view: discord.ui.View, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.message.delete()
    
    @discord.ui.button(label = 'Setup',
                        style = discord.ButtonStyle.gray)
    async def configuration_button(view: discord.ui.View, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embed = setup_embed(interaction), ephemeral = True)
    
    @discord.ui.button(label = 'Features',
                        style = discord.ButtonStyle.gray)
    async def features_button(view: discord.ui.View, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embeds = features_embeds(), ephemeral = True)
    
    @discord.ui.button(label = 'GitHub',
                       emoji = emoji_white_github,
                        style = discord.ButtonStyle.gray)
    async def github_button(view: discord.ui.View, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embed = github_embed(), ephemeral = True)

    @discord.ui.button( emoji = emoji_white_logo,
                        style = discord.ButtonStyle.gray)
    async def credits_button(view: discord.ui.View, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embed = credits_embed(), ephemeral = True)