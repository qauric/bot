#Конечный код.
# -*- coding: utf-8 -*-

import telebot

bot = telebot.TeleBot("")
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, Дима чем я могу помочь?")
    
    elif message.text == "Как дела?" or message.text == "Как ты?":
        bot.send_message(message.from_user.id, "Хорошо, ты сам как?")
    
    else:
        bot.send_message(message.from_user.id, "Извини, я тебя не понял")

bot.polling(none_stop=True, interval=0)

# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass

 # Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass

bot.polling(none_stop=True, interval=0)

