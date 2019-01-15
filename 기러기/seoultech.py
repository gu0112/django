import requests
from bs4 import BeautifulSoup
from datetime import datetime

url ="http://itm.seoultech.ac.kr/bachelor_of_information/notice/"
req = requests.get(url)
html=req.text

soup=BeautifulSoup(html, 'html.parser')
templist =soup.select('div.wrap_title')

print(templist)

