import nltk
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")

def cleanTextData(textString):
    words = tokenizer.tokenize(textString)
    words = [w.lower() for w in words]
    return words