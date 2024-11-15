import pandas as pd
import discord
import traceback
import importlib
import os

from discord.app_commands import describe, choices, Choice
from discord.ext import commands
from datetime import datetime
from typing import Union

addon_name                  = os.path.basename(os.path.dirname(__file__))
prefix                      = '!'
developer_id                = 444582897253351424
developer_discord_id        = 1114598011864105010
default_embed_colour        = 0x2b2d31
under_maintenance           = False
emoji_white_github          = '<:WhiteGitHub:1303607374061502477>'
emoji_github                = '<:GitHub:1303202173357785118>'
emoji_discord               = '<:Discord:1303202151979421746>'
emoji_white_logo            = '<:CubeLogoWhite:1303202188587307008>'
emoji_blue_logo             = '<:CubeLogoBlue:1303202126880702605>'
emoji_loading               = '<:Loading:1297713326251311114>'

# Paths
path_database               = os.path.join('CubeHelper', 'Database')
path_lists_files            = os.path.join(path_database, 'MaterialListsFiles')
csv_path_material_lists_log = os.path.join(path_database, 'MaterialListsLog.csv')
csv_path_registered_servers = os.path.join(path_database, 'RegisteredServers.csv')

# Links
link_repository             = 'https://github.com/mjpr-3435/CubeHelper'
link_ae                     = 'https://discord.gg/pXwV7BWd2P'
link_bot_invite		        = 'https://discord.com/api/oauth2/authorize?client_id=1208898496237805630&permissions=8&scope=bot'
link_discord_invite       	= 'https://discord.gg/xB9N38HBJY'
link_developer_portal       = 'https://discord.com/developers/applications'
link_developer_github       = 'https://github.com/mjpr-3435?tab=repositories'
link_introduction_banner    = 'https://cdn.discordapp.com/attachments/1247423010000867389/1263009621757530163/Logo_Banner.png'
link_default_thumbnail      = 'https://cdn.discordapp.com/attachments/1247423010000867389/1263009621359202335/Cube_Logo_2.png'
link_features_1             = 'https://cdn.discordapp.com/attachments/1247423010000867389/1263009622260977724/Features_1.png'
link_features_2             = 'https://cdn.discordapp.com/attachments/1247423010000867389/1263009622483271742/Features_2.png'
link_features_3             = 'https://cdn.discordapp.com/attachments/1247423010000867389/1263009622701113374/Features_3.png'
link_features_4             = 'https://cdn.discordapp.com/attachments/1247423010000867389/1263009622042607688/Features_4.png'


os.makedirs(path_database, exist_ok = True)