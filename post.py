from asyncio import tasks
from datetime import datetime
import discord
from discord.ext import tasks,commands
import os
from dotenv import load_dotenv

from get_from_caldav import CalDAV
load_dotenv()
TOKEN = os.getenv('TOKEN')
CHANNELID = os.getenv('CHANNELID')

class MyClient(discord.Client):
    async def on_ready(self):
        self.caldav = CalDAV()
        self.send_schedules.start()
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'stop':
            self.send_schedules.cansel()


    @tasks.loop(hours=6)
    async def send_schedules(self):
        today = datetime.now()
        schedulelist = self.caldav.getSchedules(today,1)

        channel = self.get_channel(CHANNELID)
        await channel.send(schedulelist)
        #print(schedulelist)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

client.run(TOKEN)