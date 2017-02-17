#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    what = what.rstrip()
    if what.isupper():
        return "Whoa, chill out!"
    elif len(what.strip()) == 0:
        return "Fine. Be that way!"
    elif what.endswith('?'):
        return "Sure."
    else:
        return "Whatever."
