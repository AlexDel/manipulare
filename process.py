import json
import numpy
import scipy
from features import countProAntiRatio, countSovietRatio, countNaziTermRatio, countCustomMarkersRatio

from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.manipulation

articles = db.articles.find({})

featureName = 'customMarkersRatio'

for a in articles:
    db.articles.update({
      '_id': a['_id']
    },{
      '$set': {
        'features.' + featureName: countCustomMarkersRatio(a['articleText'])
      }
    }, upsert=False, multi=False)


pos = db.articles.find({"articleBiased": True})
neg = db.articles.find({"articleBiased": False})

print(scipy.stats.ttest_ind([i['features'][featureName ] for i in neg], [i['features'][featureName ] for i in pos], axis=0, equal_var=False))

