from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext
from deep_translator import GoogleTranslator
from db import ConfigDB


db = ConfigDB()

def start(update: Update, context: CallbackContext):
    # set config
    db.set_config(chat_id=update.message.chat.id)
    # send translated
    update.message.reply_html(
        text='Select language',
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='🇺🇿 🔄 🇺🇸', callback_data='uz->en')]])
    )

def settings(update: Update, context: CallbackContext):
    # get lan
    lan = update.callback_query.data.split('->')[1]
    # set config
    db.set_config(chat_id=update.effective_user.id, lan=lan)
    # send translated
    update.callback_query.message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='🇺🇸 🔄 🇺🇿', callback_data='en->uz')]])
    )


def translater_callback(update: Update, context: CallbackContext):
    text = update.message.text

    # Use any translator you like, in this example GoogleTranslator
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    
    # send translated
    update.message.reply_html(translated)
