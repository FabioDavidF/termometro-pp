import requests
import json
import os
from time import sleep
from selenium.webdriver import Chrome
from datetime import datetime


def pegarDados(chave):
    url = f'https://api.hgbrasil.com/weather?woeid=12582226&key={chave}'
    result = requests.get(url)
    return json.loads(result.text)

def pegarHora():
    objeto = datetime.now()
    horas = objeto.hour
    minutos = objeto.minute
    if minutos < 10:
        minutos = '0'+ str(minutos)
    segundos = objeto.second
    return f'{horas}:{minutos}'
