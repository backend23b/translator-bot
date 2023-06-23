from telegram import Update
from telegram.ext import CallbackContext
from deep_translator import GoogleTranslator


def translater_callback(update: Update, context: CallbackContext):
    text = update.message.text

    # Use any translator you like, in this example GoogleTranslator
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    
    # send translated
    update.message.reply_html(translated)
