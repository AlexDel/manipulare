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
        naziWords = [w.lower().strip()  for w in naziWords if w != '']

    textWords = text.lower().split()

    wordsFound = 0
    for w in textWords:
        if w in naziWords and len(w) > 2:
            wordsFound += 1


    return wordsFound/len(textWords)

def countCustomMarkersRatio(text):
    #prepare nazi words list
    with open('data/words/manip_markers.txt') as f:
        customMarkers = f.readlines()
        customMarkers = [w.lower()  for w in customMarkers if w != '']

    normalText = text.lower()

    wordsFound = 0
    for w in customMarkers:
        w = w.strip()
        if normalText.count(w) > 0 and len(w) > 2:
            wordsFound += normalText.count(w)

    return wordsFound/len(normalText.split())

def countMilitaryTermsRatio(text):
    #prepare nazi words list
    with open('data/words/military_terms.txt') as f:
        militaryTerms = f.readlines()
        militaryTerms = [w.lower()  for w in militaryTerms if w != '']

    normalText = text.lower()

    wordsFound = 0
    for w in militaryTerms:
        w = w.strip()
        if normalText.count(w) > 0 and len(w) > 2:
            wordsFound += normalText.count(w)


    return wordsFound/len(normalText.split())

def countPutinRatio(text):
    words = cleanTextData(text)
    matchedWords = 0

    for word in words:
        if word.find('putin') > -1:
            matchedWords += 1

    return matchedWords/len(words)






