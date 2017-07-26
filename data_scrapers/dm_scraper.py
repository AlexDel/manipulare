import csv
import json
import requests
from bs4 import BeautifulSoup

filename = '/home/alexdel/reactor/manipulare/unbiased_data/links/dm.csv';

linksCsv = csv.reader(open(filename,'r'), delimiter = ',', quotechar = '"')
links = [row[0] for row in linksCsv]

articlesContent = []

for link in links:
    print('scrping: ' + link)
    result = requests.get(link)
    soup = BeautifulSoup(result.content, 'lxml')
    item = {}

    item['articleText'] = ''
    text_blocks = soup.find('div', {'itemprop':"articleBody"}).find_all('p')
    item['articleHeader'] =  soup.find('div', {'itemprop':"articleBody"}).find('h1').get_text()
    item['articleSrc'] = 'DM'
    item['articleBiased'] = False
    item['articleUrl'] = link
    for block in text_blocks:
        item['articleText'] += ' ' + block.get_text()

    articlesContent.append(item)

with open('/home/alexdel/reactor/manipulare/unbiased_data/dm_results.json', 'w') as outfile:
    json.dump(articlesContent, outfile)

