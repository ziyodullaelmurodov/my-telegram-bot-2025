# Get toke from the environment variable
import os
from telegram import Bot
token = os.getenv("TOKEN")

bot = Bot(token)
CHAT_ID = "86775091"
updates = bot.get_updates()
update = updates[0]
text = update.message.text
print(text)