from telegram.ext import (Updater, CommandHandler)
import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN=os.getenv("TELEGRAM_TOKEN")

def start_handler(update, context):
    update.message.reply_text("Hello, creater!")

if __name__ == '__main__':
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.start_polling()