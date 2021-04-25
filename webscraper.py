import sys
!{sys.executable} -m pip install BeautifulSoup4

import requests
from bs4 import BeautifulSoup
import sys
import time

def news_extractor():
    url = 'https://timesofindia.indiatimes.com/news'
    response = requests.get(url)

    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    # headings = soup.find_all('h2', {'class': 'sechead'})
    msid = wish()
    if msid == 'exit':
        print('Have a great day! Do come back for more news!')
        sys.exit(0)
    items = soup.find_all('ul', {'data-msid': msid})
    print('\n')
    for item in items:
        if msid == '-2128958273':
            head_lines = item.find_all('span', {'class': 'curpgcss'})
        else:
            head_lines = item.find_all('span')

        for head_line in head_lines:
            print('-->' + head_line.text)
        print('\n' + '*****' + '\n')


def wish():
        time.sleep(5)
        print('News Menu for the day!\n1: Entertainment\n2: Business\n3: Sports')
        print('4: TV\n5: Main Content\n0:Exit\nWhat\'s your interest?!')
        ch = input()
        switcher = {
                '1': '7507116',
                '2': '1898055',
                '3': '4440091',
                '4': '46096049',
                '5': '-2128958273',
                '0': 'exit'
            }

        return switcher[ch]


while 1:
    news_extractor()

