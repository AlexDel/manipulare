import json
import numpy
from features import countProAntiRatio

allData = []

with open('/home/alexdel/reactor/manipulare/biased_data/nyt_results.json') as data_file:
    data1 = json.load(data_file)
    allData.extend(data1)


with open('/home/alexdel/reactor/manipulare/biased_data/rt_results.json') as data_file:
    data2 = json.load(data_file)
    allData.extend(data2)

with open('/home/alexdel/reactor/manipulare/biased_data/wp_results.json') as data_file:
    data3 = json.load(data_file)
    allData.extend(data3)

proAntiRatioList = []
for article in allData:
    proAntiRatioList .append(countProAntiRatio(article['articleText']))

print(numpy.mean(proAntiRatioList))