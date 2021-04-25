import sys
!{sys.executable} -m pip install BeautifulSoup4

import requests
from bs4 import BeautifulSoup
import sys
import time

url = 'https://timesofindia.indiatimes.com/news'
response = requests.get(url)

data = response.text
soup = BeautifulSoup(data, 'html.parser')

"""
latest news : 'data-msid':"-2128958273"
entertainment : 'data-msid':"7507116"
business :'data-msid':"1898055"
TV news : 'data-msid':"46096049"
sports : 'data-msid':"4440091"
"""


msid_dictionary = {'Latest':"-2128958273", 'Entertainment':"7507116", 'Business':"1898055", 'TV news':"46096049",'Sports':"4440091"}

def extractor(msid):
    latest_news = soup.find('ul', {'data-msid':msid})
    items = latest_news.find_all('li')


    for i in range(len(items)):
        desc = items[i].find('span', {'class':'w_desc'})
        if desc is not None:
            if desc.text != "":         
                print(f'>> {desc.text}\n')
        else:
            desc = items[i].find('span', {'class':'w_tle'})
            print(f'>> {desc.text}\n')

for item in msid_dictionary:
    msid = msid_dictionary[item]
    print(f'\nToday\'s {item} News\n\n')
    extractor(msid)



    
