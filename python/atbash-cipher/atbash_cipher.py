import string, re
ALPHABET = string.ascii_lowercase

def encode(phrase):
    return re.sub(r'(\w{5}\B)', r'\1 ', switch(phrase))


def decode(phrase):
    return switch(phrase)

def switch(phrase):
    phrase_list = []
    phrase = re.sub('[\W+]', '', phrase)

    for i, char in enumerate(phrase):
        char = char.lower()
        if char in ALPHABET:
            idx = ALPHABET.index(char)
            phrase_list.append(ALPHABET[len(ALPHABET) - idx - 1])
        elif char.isdigit():
            phrase_list.append(char)

    return ''.join(phrase_list)
