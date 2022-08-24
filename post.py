from asyncio import tasks
from datetime import datetime
import discord
import os
from dotenv import load_dotenv

from get_from_caldav import CalDAV
load_dotenv()
TOKEN = os.getenv('TOKEN')
class MyClient(discord.Client):
    async def on_ready(self):
        self.caldav = CalDAV()

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')


    @tasks.loop(seconds = 10)
    async def send_schedules(self):
        today = datetime.now()
        schedulelist = self.caldav.getSchedules(today,1)
        print(schedulelist)

        
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

client.run(TOKEN)