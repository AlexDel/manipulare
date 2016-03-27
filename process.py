import json
import numpy
import scipy
from features import countProAntiRatio, countSovietRatio

from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.manipulation

pos = db.articles.find({"articleBiased": True})
neg = db.articles.find({"articleBiased": False})


# pos = []
# neg = []
# for a in arts:
#     if a['articleBiased']:
#         pos.append(countSovietRatio(a['articleText']))
#     else:
#         neg.append(countSovietRatio(a['articleText']))
#
print(scipy.stats.ttest_ind([i['features']['sovietRatio'] for i in pos], [i['features']['sovietRatio'] for i in neg], axis=0, equal_var=False))
