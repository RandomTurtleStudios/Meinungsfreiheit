#########################################################################################
# Samstagsalptraum - Ein Bot, der jede:n Arcaneposter bestraft (ein paar Sekunden mutet)
# (c) 2021 Fake
#
# BGI says: Trans Rights!
#########################################################################################

import discord
import asyncio

#########################################################################################

def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')

#########################################################################################

client = discord.Client()
mutedUsers = []

#########################################################################################

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#########################################################################################

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.author in mutedUsers:
        await message.delete()
        return

    string = message.content.lower()

    if contains_word(string, "arcane"):
        await message.delete()
        mutedUsers.append(message.author)
        print(mutedUsers)
        await asyncio.sleep(30)
        mutedUsers.remove(message.author)
        
#########################################################################################
f = open("key.key", "r")
client.run(f.read())