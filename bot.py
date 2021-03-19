from time import sleep
from selenium.webdriver import Chrome
from consulta import pegarDados, pegarHora

def criarTweet(temperature, description, date, time, condition):
    # Variantes de temperatura
    if int(temperature) > 32:
        temperature_variant = 'Calor pra caralho'
    if 25 < int(temperature) < 32:
        temperature_variant = 'Calor suportável'
    if 20 < int(temperature) < 25:
        temperature_variant = 'Fresquinho'
    if int(temperature) < 20:
        temperature_variant = 'TA FAZENDO FRIO EM PRUDENTE'

    # Variantes de condição temporal
    condition_variant = ''
    if condition == 'storm':
        condition_variant = 'Tendo tempestade'
    if condition == 'rain':
        condition_variant = 'Chovendo'
    
    # Montando o tweet com as variantes
    if condition_variant != '':
        tweet_string = f'{temperature}°C, {temperature_variant}, {description}\n\n Tá {condition_variant}\n\n{time}'
    else:
        tweet_string = f'{temperature}°C, {temperature_variant}, {description}\n\n{time}'

    return tweet_string

    
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
        condition = data['results']['condition_slug']
        
        tweet_string = criarTweet(temperature, description, date, time, condition)
        tweet_input = self.nav.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_input.send_keys(tweet_string)
        tweet_button = self.nav.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()
