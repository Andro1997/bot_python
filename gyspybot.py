#!/usr/bin/env python3
#import json, urllib2
import requests
import random
import telebot
from telebot import apihelper
from telebot.types import Message

TOKEN = '692219844:AAGM5dcY5UJL58tDUL_zgohn0Pg4NqbCyFE'
STICKER_ID = 'CAADAgADWgADkWgMAAH3LFe8jOAWMQI'
apihelper.proxy = {'https': 'socks5://telegram:telegram@jcidw.tgproxy.me:1080'}

bot = telebot.TeleBot(TOKEN)



# Weath Krasnodar
LAT = '45.26904'
LON = '38.58561'
url = f'https://api.weather.yandex.ru/v1/forecast?lat={LAT}&lon={LON}&extra=true'
headers = {'X-Yandex-API-Key': '39990a62-8040-4a51-a296-deb741c345ed'}
w = requests.get(url, headers=headers)

print(w.json())
# Weath Krasnodar

USERS = {
    'user_id': set()
}


# Message start/help list commands
@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'There is no answer =(')


# Message start/help list commands


# Message from Gyspy
@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    if 'Цыган' in message.text:
        bot.reply_to(message, 'Что то про Цыганей говорится')
        return
    reply = str(random.random())
    if message.from_user.id in USERS:
        reply += f"  {message.from_user}, hello again"
    bot.reply_to(message, reply)
    USERS.add(message.from_user.id)


# Message from Gyspy

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id, STICKER_ID)


# Inline
@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


# Inline

bot.polling(timeout=60)
