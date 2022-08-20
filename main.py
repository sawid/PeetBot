import discord
from regression import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content:
        print(message)
        print(message.content)
        announcement = "Social Credit +1 to " + "<@" + str(message.author.id) + "> total "
        await message.channel.send(announcement)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

     
client.run("")