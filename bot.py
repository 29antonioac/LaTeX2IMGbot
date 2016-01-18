#!/usr/bin/env python3
"""
d
"""
from threading import current_thread
from LaTeX2IMG.LaTeX2IMG import latex2img
import telebot
from telebot import logging
from telebot import types


TOKEN = ''

with open("token.txt", "r") as file:
    TOKEN = file.readline().strip()

bot = telebot.TeleBot(TOKEN)

def send_equation(chat_id, text):
    bot.send_chat_action(chat_id, 'upload_document')

    filename = 'resultado' + current_thread().name

    latex2img(text, filename, 'webp')

    with open(filename + '.webp', 'rb') as equation:
        bot.send_sticker(chat_id, equation)

def send_expression_callback(message):
    chat_id = message.chat.id
    text = message.text

    send_equation(chat_id, text)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "You can convert LaTeX expression using\n\n/latex expression")

@bot.message_handler(commands=['latex'])
def send_expression(message):
    chat_id = message.chat.id
    text = message.text[7:]

    if text and text != "LaTeX2IMGbot":
        send_equation(chat_id, text)
    else:
        markup = types.ForceReply(selective=True)

        new_msg = bot.reply_to(message, "Send me the LaTeX expression", reply_markup=markup)
        bot.register_for_reply(new_msg, send_expression_callback)



logger = telebot.logger
formatter = logging.Formatter('[%(asctime)s] %(thread)d {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
                                  '%m-%d %H:%M:%S')
ch = logging.FileHandler("log.txt")
logger.addHandler(ch)
logger.setLevel(logging.INFO)  # or use logging.INFO
ch.setFormatter(formatter)

bot.polling()
