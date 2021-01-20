import discord
import sys
from discord import utils
from discord.ext import commands
from datetime import datetime

from information import info

PREFIX = '/'
client = discord.Client()

chanel = id=int(input('''
░█████╗░██╗░░██╗░█████╗░████████╗
██╔══██╗██║░░██║██╔══██╗╚══██╔══╝
██║░░╚═╝███████║███████║░░░██║░░░
██║░░██╗██╔══██║██╔══██║░░░██║░░░
╚█████╔╝██║░░██║██║░░██║░░░██║░░░
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░

Создатель - NobodyForYou#3648

Введи ID канала: '''))

@client.event
async def on_ready():
	print('\nНачинаем следить ._.')


@client.event
async def on_message(message):
	if message.channel.id == chanel:

		form = '<%d/%m/%Y %H:%M:%S>'
		time = message.created_at.strftime(form)
		print(f'\n{time} [{message.author}]: {message.content}')


token = info['TOKEN']

client.run( token )	