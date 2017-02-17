import re

def word_count(phrase):
    word_dict = dict()

    phrase_list = re.split('\_|\W+', phrase.decode('utf-8').lower(),flags=re.U)

    for word in phrase_list:
        if word_dict.has_key(word):
            word_dict[word] = word_dict[word] + 1
        elif len(word) > 0:
            word_dict[word] = 1

    return word_dict
