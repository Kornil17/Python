import requests
from bs4 import BeautifulSoup

class Bot:

    def get_first(self):
        headers = {
            "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }

        url = 'https://habr.com/ru/news/'
        r = requests.get(url=url, headers=headers)
        