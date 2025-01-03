from telegram.ext import (Updater, CommandHandler)


def start_handler(update, context):
    update.message.reply_text("Hello, creater!")

if __name__ == '__main__':
    updater = Updater("7977898419:AAGXKQrn9xGCGoiCks-sics8zFGxCTidft8", use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.start_polling()