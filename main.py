from telegram import Bot
from telegram import Update 
from telegram.ext import Updater,Filters,CommandHandler,MessageHandler
from telegram.ext import CallbackContext
from echo.config import TG_TOKEN

def doStart(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Привет! Отправь мне что-нибудь",
    )

def doEcho( context: CallbackContext, update: Update):
    #text = update.message.text
    update.message.reply_text(
        text = update.message,
    )

    
def main():

    bot = Bot(
        token = TG_TOKEN,
    )

    updater = Updater(
        bot = bot,
    )
    start_handler = CommandHandler('start',doStart)
    message_handler = MessageHandler(Filters.text,doEcho)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    