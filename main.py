# Get toke from the environment variable
import os
from bot import Bot
token = os.getenv("TOKEN")

bot = Bot(token)
print(bot.get_info())
