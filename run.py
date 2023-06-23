from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from callbacks import (
    translater_callback,
)

TOKEN = os.environ.get('TOKEN')
if TOKEN is None:
    print("set TOKEN env variable.")

def main():
    # create udpate
    updater = Updater(TOKEN)

    # get updater from updater obj
    dp = updater.dispatcher

    # add handlers
    dp.add_handler(MessageHandler(Filters.text, translater_callback))

    # start polling 
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()