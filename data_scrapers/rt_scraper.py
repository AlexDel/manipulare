import csv
import json
import requests
from bs4 import BeautifulSoup

filename = '/home/alexdel/reactor/manipulare/biased_data/links/RT.csv';

linksCsv = csv.reader(open(filename,'r'), delimiter = ',', quotechar = '"')
links = [row[0] for row in linksCsv]

articlesContent = []

for link in links:
    print('scraping: ' + link)
    result = requests.get(link)
    soup = BeautifulSoup(result.content, 'lxml')
    item = {}

    item['articleText'] = soup.find('div', {'class':'article__text text '}).get_text()
    text_blocks = soup.find_all('p', {'class':"story-body-text"})
    item['articleHeader'] = soup.find('h1', {'class':'article__heading'}).get_text()
    item['articleSrc'] = 'RT'
    item['articleBiased'] = True
    item['articleUrl'] = link

    articlesContent.append(item)

with open('/home/alexdel/reactor/manipulare/biased_data/rt_results.json', 'w') as outfile:
    json.dump(articlesContent, outfile)

