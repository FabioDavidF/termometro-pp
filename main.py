import os
from bot import TermometroBot
from time import sleep
from datetime import datetime
from consulta import pegarSoHora

username = os.getenv('TWITTER_USER')
password = os.getenv('TWITTER_PASSWORD')
key = os.getenv('HG_KEY')

bot = TermometroBot(username, password, key)
bot.login()
while True:
    hora_atual = pegarSoHora()
    if hora_atual == 22:
        bot.tweet('previsao')
        sleep(3600)
    elif hora_atual in [1, 3, 6, 9, 12, 15, 18, 21]:
        bot.tweet('atual')
        sleep(3600)
    sleep(60)
