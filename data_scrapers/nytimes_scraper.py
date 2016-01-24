import csv
import json
import requests
from bs4 import BeautifulSoup

filename = '/home/alexdel/reactor/manipulare/biased_data/links/NYT.csv';

linksCsv = csv.reader(open(filename,'r'), delimiter = ',', quotechar = '"')
links = [row[0] for row in linksCsv]

articlesContent = []

for link in links:
    result = requests.get(link)
    soup = BeautifulSoup(result.content, 'lxml')
    item = {}

    item['articleText'] = ''
    text_blocks = soup.find_all('p', {'class':"story-body-text"})
    item['articleHeader'] = soup.find('h1', {'itemprop':'headline'}).get_text()
    item['articleSrc'] = 'NYT'
    item['articleBiased'] = True
    item['articleUrl'] = link
    for block in text_blocks:
        item['articleText'] += ' ' + block.get_text()

    articlesContent.append(item)

with open('/home/alexdel/reactor/manipulare/biased_data/nyt_results.json', 'w') as outfile:
    json.dump(articlesContent, outfile)

