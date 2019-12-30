# 爬取csdn第二页标题
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.csdn.net/')

soup = BeautifulSoup(r.text,'html.parser')
content_list = soup.find_all('div',attrs = {'class':'title'})

for content in content_list:
    print(content.h2.text)