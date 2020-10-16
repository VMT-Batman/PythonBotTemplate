import discord
import logging

from discord.ext import commands

prefix = '.'


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        # You can change this with other arguments that change the activity and status of the bot
        await commands.Bot.change_presence(self, activity=discord.Streaming(name='Tune into the Stream!',
                                                                            url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                                                                            platform='Twitch'))

    async def on_message(self, message):
        # Logs received messages from any server the bot is in
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.startswith(prefix + 'Desired Argument'):
            await message.channel.send('How you want the bot to respong to this argument')


client = MyClient()
# If the connected account is NOT a bot, add second argument to next line with 'bot=False'
client.run("YOURTOKENHERE")
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
