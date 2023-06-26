from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
from deep_translator import GoogleTranslator


def start(update: Update, context: CallbackContext):
    text = update.message.text
    
    # send translated
    update.message.reply_html(translated)


def translater_callback(update: Update, context: CallbackContext):
    text = update.message.text

    # Use any translator you like, in this example GoogleTranslator
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    
    # send translated
    update.message.reply_html(translated)
