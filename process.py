import json
import numpy
import scipy
from features import countProAntiRatio, countSovietRatio, countNaziTermRatio

from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.manipulation

# pos = db.articles.find({"articleBiased": True})
# neg = db.articles.find({"articleBiased": False})

articles = db.articles.find({})

for a in articles:
    print(a['features'])

# for a in articles:
#     db.articles.update({
#       '_id': a['_id']
#     },{
#       '$set': {
#         'features.naziTermsRatio': countNaziTermRatio(a['articleText'])
#       }
#     }, upsert=False, multi=False)


#print(scipy.stats.ttest_ind([i['features']['sovietRatio'] for i in pos], [i['features']['sovietRatio'] for i in neg], axis=0, equal_var=False))

