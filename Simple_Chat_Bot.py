# Importing the discord library
import discord

# this is another test

# Create instance of a client to make a connection to discord
client = discord.Client()

@client.event # Decorator for a function
async def on_ready(): # Function or "event" called when the bot finishes logging in
    print('Howdy Tathluach! You have logged in as {0.user}'.format(client))

# Check messages
@client.event
async def on_message(message): # event called when the bot has received a message

    # Variables used
    member = discord.Member
    user_message = f'You have been warned for cursing in The Tath Server.\n {message.author}\'s Message: {message.content}.'

    if message.author == client.user: # ignore messages from ourselves
        return

    # Filter pre-set curse words
    if 'Fuck' in message.content or 'fuck' in message.content:
        await message.delete()
        await message.author.send(user_message)
        return

    if 'Bitch' in message.content or 'bitch' in message.content:
        await message.delete()
        await message.author.send(user_message)
        return

    if 'Whore' in message.content or 'whore' in message.content:
        await message.delete()
        await message.author.send(user_message)
        return

    if 'Bastard' in message.content or 'bastard' in message.content:
        await message.delete()
        await message.author.send(user_message)
        return

    if 'Shit' in message.content or 'shit' in message.content:
        await message.delete()
        await message.author.send(user_message)
        return

    if 'Nigga' in message.content or 'nigga' in message.content:
        await message.delete()
        await message.author.send(user_message)
        return

    if 'Nigger' in message.content or 'nigger' in message.content:
        await message.delete()
        await message.author.send(user_message)
        return

    if message.content == 'Howdy' or message.content == 'howdy': # check if the message starts with 'howdy'
        await message.channel.send('Gig \'em!') # send message in the channel it was used

# Event to welcome new members
@client.event
async def on_member_join(new_member):
    await new_member.channel.send(
        'Howdy {new_member.name}, welcome to the Tath server!'
    )

# run both with my token
client.run('')
