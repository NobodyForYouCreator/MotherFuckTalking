import discord
from discord import utils
from discord.ext import commands
import sys

from information import info

PREFIX = '/'



async def greatSender():

    channel = client.get_channel(id=int(input('Айди канала: ')))

    while True:
    	x = input('Отправить сообщение: ')
    	if x.startswith(f'{PREFIX}back'):

    	    await greatSender()


    	await channel.send(x)


    

client = discord.Client()

@client.event

async def on_ready():
    print( '''
████████╗░█████╗░██╗░░░░░██╗░░██╗
╚══██╔══╝██╔══██╗██║░░░░░██║░██╔╝
░░░██║░░░███████║██║░░░░░█████═╝░
░░░██║░░░██╔══██║██║░░░░░██╔═██╗░
░░░██║░░░██║░░██║███████╗██║░╚██╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

Создатель - NobodyForYou#3648''' )

    await greatSender()


token = info['TOKEN']

client.run( token )	