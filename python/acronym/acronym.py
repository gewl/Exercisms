import re

def abbreviate(string):
    replace_pattern = re.compile('([a-z])([A-Z])')
    string = replace_pattern.sub('\g<1> \g<2>', string)
    pattern = re.compile('(?:^| |\W)(\w)')

    letters = pattern.findall(string)
    return ''.join(letters).upper()
