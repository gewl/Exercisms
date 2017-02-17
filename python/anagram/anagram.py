def detect_anagrams(key, wordList):
    matches = []
    key_chars = granularize_word(key)

    for word in wordList:
        if word.lower() != key.lower() and granularize_word(word) == key_chars:
            matches.append(word)

    return matches

def granularize_word(word):
    chars = {}
    for letter in word:
        letter = letter.lower()
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1

    return chars
