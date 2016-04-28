from cleaner import cleanTextData

def countProAntiRatio(text):
    words = cleanTextData(text)
    matchedWords = 0

    for word in words:
        if word.startswith('pro-') or word.startswith('anti'):
            matchedWords += 1

    return matchedWords/len(words)

def countSovietRatio(text):
    words = cleanTextData(text)
    matchedWords = 0

    for word in words:
        if word.find('soviet') > -1:
            matchedWords += 1

    return matchedWords/len(words)

def countNaziTermRatio(text):
    #prepare nazi words list
    with open('data/words/nazi_term.txt') as f:
        naziWords = f.readlines()
        naziWords = [w.lower()  for w in naziWords if w != '']

    normalText = text.lower()

    wordsFound = 0
    for w in naziWords:
        w = w.strip()
        if normalText.count(w) > 0 and len(w) > 2:
            print(w)
            wordsFound += normalText.count(w)


    return wordsFound/len(normalText.split())





