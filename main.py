import os
from bot import TermometroBot


username = os.getenv('TWITTER_USER')
password = os.getenv('TWITTER_PASSWORD')
key = os.getenv('HG_KEY')

bot = TermometroBot(username, password, key)
bot.login()
bot.tweet()