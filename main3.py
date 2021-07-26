import telebot
import time
import pyshorteners
import os

bot_token ='TOKEN'

bot = telebot.TeleBot(token=bot_token) 

def short(url):
    return pyshorteners.Shortener().tinyurl.short(url)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'{message.from_user.first_name},Hello, Welcome!')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Read My Description For Futher Help')

@bot.message_handler(content_types=['photo', 'video', 'audio', 'document'])
def file_sent(message):
    try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.document.file_id)))
    except AttributeError:
        try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[0].file_id)))
        except AttributeError:
              try:
                  bot.send_message(message.chat.id, short(bot.get_file_url(message.audio.file_id)))
              except AttributeError:
                    try:
                        bot.send_message(message.chat.id, short(bot.get_file_url(message.video.file_id)))
                    except AttributeError:
                        pass


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
