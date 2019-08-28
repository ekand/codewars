def remove_duplicate_words(s):
    return ' '.join(dict.fromkeys(s.split()))

s = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

# print(s.split())
# # returns a list of words from the string
#
# print(dict.fromkeys(s.split()))
# # returns a dictionary with keys from the list of
# # words and None for each value
# # note: why dict and not set?
#
# print(' '.join(dict.fromkeys(s.split())))
# # joins the list of words into a string with the
# # words separated by spaces


# why not use set?
# my_set = set(s.split())
# print(my_set)
# my_string = ' '.join(my_set)
# print(my_string)

# okay I see: the set is not ordered,
# but a dictionary apparently is ordered?
# yes. according to
# https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6/39980744
# dictionaries are ordered in python 3.7 according to
# insertion order (and also in 3.6)

# question: what if the dict had actual values in it?

my_dict = dict.fromkeys(s.split())
print(my_dict)
my_dict['alpha'] = 4
print(my_dict)
print(' '.join(my_dict))
'''
output was:
{'alpha': None, 'beta': None, 'gamma': None, 'delta': None}
{'alpha': 4, 'beta': None, 'gamma': None, 'delta': None}
alpha beta gamma delta
'''
# so apparetnly when you .join a dict, it just throws
# out the values
