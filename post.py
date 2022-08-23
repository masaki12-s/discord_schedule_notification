from discordwebhook import discordwebhook
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('webhookURL'))
# discord = discordwebhook(url=URL,contents = "TEST")
# sent_webhook = discord.execute()
# sleep(10)
# discord.delete(sent_webhook)