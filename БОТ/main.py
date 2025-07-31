import requests
import time
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7596427516:AAGuvAu9W9iwsEuROSmQ65JUUf7mD0iM5Es'
TEXT = 'Ура! Классный апдейт!'
MAX_COUNTER = 100
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        print(updates)
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1