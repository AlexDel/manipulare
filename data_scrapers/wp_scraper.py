import csv
import json
import requests
from bs4 import BeautifulSoup

filename = '/home/alexdel/reactor/manipulare/unbiased_data/links/wp.csv';

linksCsv = csv.reader(open(filename,'r'), delimiter = ',', quotechar = '"')
links = [row[0] for row in linksCsv]

articlesContent = []

for link in links:
    print('scraping: ' + link)
    result = requests.get(link)
    soup = BeautifulSoup(result.content, 'lxml')
    item = {}

    item['articleText'] = soup.find('article', {'itemprop':'articleBody'}).get_text()
    item['articleHeader'] = soup.find('h1', {'itemprop':'headline'}).get_text()
    item['articleSrc'] = 'WP'
    item['articleBiased'] = False
    item['articleUrl'] = link

    articlesContent.append(item)

with open('/home/alexdel/reactor/manipulare/unbiased_data/wp_results.json', 'w') as outfile:
    json.dump(articlesContent, outfile)

