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
    segundos = objeto.second
    return f'{horas}:{minutos}'


class TermometroBot():
    def __init__(self, username, password, key):
        self.nav = Chrome()
        self.username = username
        self.password = password
        self.key = key
    
    def login(self):
        self.nav.get('https://twitter.com/login')
        sleep(2)
        username_input = self.nav.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        password_input = self.nav.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        login_button = self.nav.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        login_button.click()
        sleep(4)
    
    def tweet(self):
        data = pegarDados(self.key)
        temperature = data['results']['temp']
        description = data['results']['description']
        date = data['results']['date']
        time = pegarHora()
        
        tweet_string = f'Temperatura atual: {temperature}°C\nComo está o tempo: {description}\n\n{date}, {time}'
        tweet_input = self.nav.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_input.send_keys(tweet_string)
        tweet_button = self.nav.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()


username = os.getenv('TWITTER_USER')
password = os.getenv('TWITTER_PASSWORD')
key = os.getenv('HG_KEY')
bot = TermometroBot(username, password, key)
bot.login()
bot.tweet()