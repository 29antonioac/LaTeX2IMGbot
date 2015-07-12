#!/usr/bin/env python3
import telebot
import time
from LaTeX2IMG import LaTeX2IMG
from time import sleep
from threading import current_thread

TOKEN = ''


def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            if text[0:7] == "/latex ":
                text = text[7:]
            elif text[0] == "@":
                text = text[13:]
            else:
                break

            filename = 'resultado' + current_thread().name

            LaTeX2IMG.main(['LaTeX2IMG',text,filename,'webp'])
            equation = open(filename + '.webp','rb')
            tb.send_sticker(chatid, equation)
            #tb.send_photo(chatid,photo)
            # tb.send_message(chatid, text)

with open("token.txt","r") as file:
    TOKEN = file.readline().strip()
tb = telebot.TeleBot(TOKEN)
tb.set_update_listener(listener) #register listener
tb.polling()

while True: # Don't let the main Thread end.
    sleep(5)
