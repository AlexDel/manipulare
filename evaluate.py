import json
import codecs
from random import shuffle
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier

with codecs.open('data/articles.json', 'r', 'utf-8') as data_file:
    data = json.load(data_file)

# prepara features as matrix
vec = DictVectorizer()

#split dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(data, [i['articleBiased'] for i in data], test_size=0.1, random_state=12)

# train
clf = DecisionTreeClassifier(random_state=0)
clf.fit(vec.fit_transform([i['features'] for i in X_train]).toarray(), y_train)

print(vec.get_feature_names())
print(clf.feature_importances_)