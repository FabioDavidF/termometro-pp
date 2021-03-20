import os
from bot import TermometroBot
from time import sleep
from datetime import datetime


def pegarSoHora():
    objeto = datetime.now()
    hora = objeto.hour
    return hora


username = os.getenv('TWITTER_USER')
password = os.getenv('TWITTER_PASSWORD')
key = os.getenv('HG_KEY')
ja_fez_previsao = bool

bot = TermometroBot(username, password, key)
bot.login()
while True:
    hora_atual = pegarSoHora()
    if hora_atual == 22:
        bot.tweet('previsao')
    elif hora_atual in [9, 12, 15, 18, 21]:
        bot.tweet('atual')
    sleep(3600)
