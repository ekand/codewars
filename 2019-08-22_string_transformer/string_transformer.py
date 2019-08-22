# from the kata here
# https://www.codewars.com/kata/string-transformer/python

import re

def string_transformer(s):
    """ takes a string with spaces and returns
    a string with the words reversed, the white spaces
    preserved, and upper/lower case swapped for
    each character in the words
    s:   a string
    """
    s2 = ''
    for character in s:
        if character.islower():
            character = character.upper()
        elif character.isupper():
            character = character.lower()
        s2 += character
    l = re.split(r'(\s+)', s2)
    l[:] = l[:: -1]
    s3 = ''.join(l)
    return s3

example = " Example  Input"
print(string_transformer(example))
