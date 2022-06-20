from bs4 import BeautifulSoup
import requests
import unicodedata
import pandas as pd

# Webpage url                                                                                                               
url = 'https://www.ensenachile.cl/testimonios/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# Encontrar todos los div que tienen class 'item-hito'
divs = soup.find_all('div', {'class':['col-md-6']})
i=0
for div in divs:
    # find all the enclosing a tags.
    if(i == 0):
        print(div)
    i = i + 1