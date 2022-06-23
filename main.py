from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import unicodedata
import pandas as pd
from pandas import DataFrame
from tabulate import tabulate
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
# Webpage url                                                                                                               
url = "https://www.clinicaalemana.cl/profesional/resultado?nombreMedico=&paternoMedico=&maternoMedico="
driver_path="chromedriver"
service = Service(driver_path)
driver = webdriver.Chrome(service=service,options=chrome_options)
driver.implicitly_wait(30)
driver.get(url)
driver.find_element(by=By.CLASS_NAME, value="w-item-res")
soup=BeautifulSoup(driver.page_source, 'html.parser')

table = []
# Encontrar todos los div que tienen class 'item-hito'
divs = soup.find_all('div', {'class':['item-res', 'i-res']})
for div in divs:
    text = div.find_all('div', {'class':['texto-res']})
    print(text[0].text)
    img = div.find_all('img', {'class':['foto-medico']})
    print(img[0])
    # we clean up the text from the group of 3 li tags and add them as a list to our table list.
    table.append([unicodedata.normalize("NFKD",text[0].text).strip()])

headers = ['Nombre']
df = DataFrame(table, columns=headers)
print (df)
driver.quit()
