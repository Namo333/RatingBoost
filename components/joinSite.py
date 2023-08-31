import requests
from bs4 import BeautifulSoup
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

url = config['SITE']['urlSite']

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'http://www.banki.ru.com/',
    'Accept': '*/*'
}

def joinSite(url):
    resaise = requests.get(url, headers=headers)
    print(resaise.text)

def mainJoin():
    joinSite(url=url)