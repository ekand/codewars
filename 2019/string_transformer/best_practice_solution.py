# from the kata here
# https://www.codewars.com/kata/5878520d52628a092f0002d0/solutions/python/all/best_practice

def string_transformer(s):
    return ' '.join(s.swapcase().split(' ')[::-1])

# this works because .split(' ') is unlike .split()
# the first splits the string at each space, putting in
# empty strings into the list in the case that there are
# two consecutive white spaces. In contrast, .split()
# takes white space of any length as a delimiter and
# throws out that white space.

# the .swapcase is straightforward

# the [::-1] takes the list from the splitted string
# and reverses it

# finally, ' '.join(`all that`) puts the list back into a string,
# inserting white space between each of the words and, crucially,
# inserting white spaces between each of the empty strings in
# the list
