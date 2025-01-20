# Get toke from the environment variable
import os
from telegram import Bot
token = os.getenv("TOKEN")

bot = Bot(token)
CHAT_ID = "6521343766"
updates = bot.get_updates()
message = bot.send_message(CHAT_ID, "Assalomu alaykum!")
photo = 'C:/Users/ziyod/Downloads/Telegram Desktop/photo_2025-01-07_13-19-16.jpg'

bot.send_photo(CHAT_ID, photo=photo)
print(bot.send_document(chat_id=CHAT_ID, document='C:/Users/ziyod/OneDrive/Desktop/Kiberxavfsizlik.docx'))
print(bot.send_audio(chat_id=CHAT_ID, audio='C:/Users/ziyod/Downloads/Telegram Desktop/listening3.mp3'))
print(bot.send_video(chat_id=CHAT_ID, video='C:/Users/ziyod/Downloads/Telegram Desktop/video_2025-01-19_00-04-16.mp4'))
update = updates[0]
text = update.message.text
print(text)