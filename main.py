import discord
from regression import *
from database import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

client.setResponseData = False


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('/setResponse'):
        string1 = message.content
        string2 = "/setResponse"
        tempWord = string1[string1.index(string2) + len(string2):].strip().lower()
        if(tempWord == "true"):
            client.setResponseData = True
        else:
            client.setResponseData = False
        announcement = "Set Response Bot to " + str(client.setResponseData)
        await message.channel.send(announcement)
        return

    if message.content:
        if message.author != client.user:
            addSentence(message.content, message.author.id)
        if (client.setResponseData):
            announcement = "Social Credit +1 to " + "<@" + str(message.author.id) + "> total "
            await message.channel.send(announcement)
        else:
            print("No Response")
     
client.run("MTAwOTgzOTUzMjk5ODQwNjIzNA.GU-H_c.uwZW7dv_0hGjMWKpIlUqQ5GSP5lKW6ve9LvuD0")