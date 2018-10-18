import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game



Client = discord.client
client = commands.Bot(command_prefix = '-')
Clientdiscord = discord.Client()

@client.event
async def on_ready():
	await client.change_presence(game=Game(name='CS:GO'))
	print('Ready')
	


@client.event
async def on_message(message):
	if ("fasz") in message.content:
		await client.delete_message(message)
		await client.send_message(message.channel,'Nincs csúnya beszéd!')
	if ("geci") in message.content:
		await client.delete_message(message)
		await client.send_message(message.channel,'Nincs csúnya beszéd!')
	if ("anyád") in message.content:
		await client.delete_message(message)
		await client.send_message(message.channel,'Nincs csúnya beszéd!')
	if message.content == "-megymar":
		em = discord.Embed(description='Mi?')
		em.set_image(url='http://www.swansea.ac.uk/accommodation/applying-for-accommodation/what-happens-next/web-shutterstock-105518339.jpg')
		await client.send_message(message.channel. embed-em)

client.run("NTAyNTQxNDYxNzc0OTI1ODM0.Dqpb3w.NNMkoYLQuAoa3YujA-4aBoR0ask")
