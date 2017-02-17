from string import ascii_lowercase

def is_pangram(phrase):
    alphabet_dictionary = {letter:False for letter in ascii_lowercase}
    for letter in phrase:
        letter = letter.lower()
        if letter in alphabet_dictionary:
            alphabet_dictionary[letter] = True

    return all(letter == True for letter in alphabet_dictionary.itervalues())

