# Importing the discord library
import discord

print("Test")

# Create instance of a client to make a connection to discord
client = discord.Client()

# Decorator to register an event
@client.event
# Callback - function called when something happens
async def on_ready(): # event called when the bot finishes logging in
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): # event called when the bot has received a message
    # ignore messages from ourselves
    if message.author == client.user:
        return

    # check if the message starts with '$hello'
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!') # send message in the channel it was used

# run both with my token
client.run('OTc4MDcxNzIyNjQ3NDk0Njg2.GZai5K.VH_Nd2bzrJjdi2WTOc0AQ0sLlHbuMnnemtpBVA')