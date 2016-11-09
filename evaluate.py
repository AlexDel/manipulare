import json
import codecs
from pprint import pprint

with codecs.open('data/articles-dump.json', 'r', 'utf-8') as data_file:
    data = json.load(data_file)

print(data[39]['features'])