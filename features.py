from cleaner import cleanTextData

def countProAntiRatio(text):
    words = cleanTextData(text)
    matchedWords = 0

    for word in words:
        if word.startswith('pro') or word.startswith('pro'):
            matchedWords += 1

    return matchedWords/len(words)



