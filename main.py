import discord
import logging

from discord.ext import commands
# Whatever string is initialized here will be the prefix of your commands. (ex prefix = '!' will make commands begin with ! like !help)
prefix = '.'


class MyClient(discord.Client):
    # Creating a class of actions for when the bot first initializes
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        # You can change this with other arguments that change the activity and status of the bot
        await commands.Bot.change_presence(self, activity=discord.Streaming(name='Tune into the Stream!',
                                                                            url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                                                                            platform='Twitch'))

    async def on_message(self, message):
        # Logs received messages from any server the bot is in
        print('Message from {0.author}: {0.content}'.format(message))
        # Changing the 'Desired Argument' will be the command name basically (ex. invite will become .invite because of the prefix and this is now the command the bot will listen for)
        if message.content.startswith(prefix + 'Desired Argument'):
            # The next line makes the bot respond with a message, but you can change the statement to do anything as a response (read Discord.py documentation)
            await message.channel.send('How you want the bot to respond to this argument')


client = MyClient()
# If the connected account is NOT a bot, add second argument to next line with 'bot=False'
client.run("YOURTOKENHERE")
# Logging of messages so you could test different command arguments and make sure the bot is actually seeing the message to begin with. This will show incoming messages in the console
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
