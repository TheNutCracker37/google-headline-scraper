#import the modules
from bs4 import BeautifulSoup
import requests
#get the page from google link
html_text = requests.get(input("link: ")).text
#create the BS object by the lxml parser
content = BeautifulSoup(html_text, 'lxml')
#find headlines
tags = content.find_all('h3')
#print them
for tag in tags:
    print(tag.text)
