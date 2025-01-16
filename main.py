# Get toke from the environment variable
import os
from bot import Bot
token = os.getenv("TOKEN")

bot = Bot(token)
CHAT_ID = "86775091"
bot.send_message(CHAT_ID, "Hello, world!")
