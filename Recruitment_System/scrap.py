import os
import telebot
import requests
from bs4 import BeautifulSoup

url = 'https://www.freelancer.com/job/'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

skill = soup.find_all('a', {'class': 'PageJob-category-link PageJob-category-link--contest'})#.attrs.get('title')
skill2 = soup.find_all('a', {'class' : 'PageJob-category-link'})
for i in skill:
    k = i.attrs.get('title')
    print(k)

for i in skill2:
    k = i.attrs.get('title')
    print(k)
'PageJob-category-link'