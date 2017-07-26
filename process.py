import os.path
import sklearn
from sklearn import tree
from sklearn.feature_extraction import FeatureHasher
import pickle
from features import countProAntiRatio, countSovietRatio, countNaziTermRatio, countCustomMarkersRatio, countMilitaryTermsRatio, countPutinRatio

from pymongo import MongoClient


def process(text):
  return {
    'ProAntiRatio': countProAntiRatio(text),
    'SovietLexicalRatio': countSovietRatio(text),
    'NaziLexicalRatio': countNaziTermRatio(text),
    'CustomMarkersRatio': countCustomMarkersRatio(text),
    'MilitaryLexicalRatio': countMilitaryTermsRatio(text),
    'PoliticalLexicalRation': countPutinRatio(text),
  }


def getModel():
  fileName = 'mymodel.pkl'
  if os.path.isfile(fileName):
    with open(fileName, 'rb') as f:
      clf = pickle.load(f)
  else:
    client = MongoClient('localhost:27017')
    db = client.manipulation
    articles = list(db.articles.find({}))
    features = FeatureHasher(n_features=6).transform([process(article['articleText']) for article in articles]).toarray()
    labels = [article['articleBiased'] for article in articles]

    clf = tree.DecisionTreeClassifier(criterion='entropy', splitter='random',class_weight={True:1, False: 10})
    clf = clf.fit(features, labels)
    pickle.dump(clf, open("mymodel.pkl", "wb"))
  return clf


def predict(text):
  clf = getModel()
  featuresValues = process(text)
  vector = FeatureHasher(n_features=6).transform([featuresValues]).toarray()
  result = clf.predict(vector)

  #tweak for correct Boolean json serialization
  if result[0] and sum(featuresValues.values()):
    jsonRes = True
  else:
    jsonRes = False

  return {'result': jsonRes, 'values': featuresValues}