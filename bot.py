#!/usr/bin/env python3
import requests
proxies = {'https': 'socks5://telegram:telegram@jcidw.tgproxy.me:1080'}
TOKEN = "692219844:AAGM5dcY5UJL58tDUL_zgohn0Pg4NqbCyFE"
MAIN_URL = "https://api.telegram.org/bot692219844:AAGM5dcY5UJL58tDUL_zgohn0Pg4NqbCyFE/sendMessage"

payload = {
    'chat_id': 373853051,
    'text': ' И тебе привет, КАЗЕЛ!',
    'reply_to_message_id': 4
}

r = requests.post(MAIN_URL, proxies=proxies, data=payload)
#r = requests.get(MAIN_URL, proxies=proxies)

print(r.json())
#https://t.me/socks?server=jcidw.tgproxy.me&port=1080&user=telegram&pass=telegram