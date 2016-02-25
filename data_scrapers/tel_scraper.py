import csv
import json
import requests
from bs4 import BeautifulSoup

filename = '/home/alexdel/reactor/manipulare/unbiased_data/links/tel.csv';

linksCsv = csv.reader(open(filename,'r'), delimiter = ',', quotechar = '"')
links = [row[0] for row in linksCsv]

articlesContent = []

for link in links:
    print('scraping: ' + link)
    result = requests.get(link)
    soup = BeautifulSoup(result.content, 'lxml')
    item = {}

    item['articleText'] = ''
    text_blocks = soup.find_all('div', {'itemprop':"articleBody"})
    item['articleHeader'] = soup.find('h1', {'itemprop':'headline name'}).get_text() or None
    item['articleSrc'] = 'TEL'
    item['articleBiased'] = False
    item['articleUrl'] = link
    for block in text_blocks:
        item['articleText'] += ' ' + block.get_text()

    articlesContent.append(item)

with open('/home/alexdel/reactor/manipulare/unbiased_data/tel_results.json', 'w') as outfile:
    json.dump(articlesContent, outfile)

