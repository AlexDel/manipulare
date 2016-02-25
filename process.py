import json
import numpy
from features import countProAntiRatio

biasedData = []

with open('/home/alexdel/reactor/manipulare/biased_data/nyt_results.json') as data_file:
    data1 = json.load(data_file)
    biasedData.extend(data1)


with open('/home/alexdel/reactor/manipulare/biased_data/rt_results.json') as data_file:
    data2 = json.load(data_file)
    biasedData.extend(data2)

with open('/home/alexdel/reactor/manipulare/biased_data/wp_results.json') as data_file:
    data3 = json.load(data_file)
    biasedData.extend(data3)

proAntiRatioListPos = []
for article in biasedData:
    proAntiRatioListPos.append(countProAntiRatio(article['articleText']))


unBiasedData = []

with open('/home/alexdel/reactor/manipulare/unbiased_data/nyt_results.json') as data_file:
    unBiasedData.extend(json.load(data_file))

with open('/home/alexdel/reactor/manipulare/unbiased_data/dm_results.json') as data_file:
    unBiasedData.extend(json.load(data_file))

with open('/home/alexdel/reactor/manipulare/unbiased_data/tel_results.json') as data_file:
    unBiasedData.extend(json.load(data_file))

with open('/home/alexdel/reactor/manipulare/unbiased_data/wp_results.json') as data_file:
    unBiasedData.extend(json.load(data_file))

for article in biasedData:
    proAntiRatioListPos.append(countProAntiRatio(article['articleText']))
