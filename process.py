import json
import numpy
import scipy
from features import countProAntiRatio, countSovietRatio

from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.manipulation

arts = db.articles.find({})

print(arts[0].keys())

pos = []
neg = []
for a in arts:
    if a['articleBiased']:
        pos.append(countSovietRatio(a['articleText']))
    else:
        neg.append(countSovietRatio(a['articleText']))

print(scipy.stats.ttest_ind(pos, neg, axis=0, equal_var=False))
