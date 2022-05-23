# Importing the discord library
import discord

# this is another test

# Create instance of a client to make a connection to discord
client = discord.Client()

@client.event # Decorator for a function
async def on_ready(): # Function or "event" called when the bot finishes logging in
    print('Howdy Tathluach! You have logged in as {0.user}'.format(client))


# Example event when a user writes a message
@client.event
async def on_message(message): # event called when the bot has received a message
    if message.author == client.user: # ignore messages from ourselves
        return

    if message.content.startswith('Howdy'): # check if the message starts with '$hello'
        await message.channel.send('Gig \'em!') # send message in the channel it was used

# Event to welcome new members
@client.event
async def on_member_join(new_member):
    await new_member.channel.send(
        'Howdy {new_member.name}, welcome to the Tath server!'
    )


# run both with my token
client.run('OTc4MDcxNzIyNjQ3NDk0Njg2.GZai5K.VH_Nd2bzrJjdi2WTOc0AQ0sLlHbuMnnemtpBVA')