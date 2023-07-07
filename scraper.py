from bs4 import BeautifulSoup
import requests
html_text = requests.get(input("link: ")).text
content = BeautifulSoup(html_text, 'lxml')
tags = content.find_all('h3')
for tag in tags:
    print(tag.text)
