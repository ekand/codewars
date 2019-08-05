def count(string):
    #initialize empty dictionary
    d = {}
    # either create an entry for each character
    # or increment that entry by one
    for character in string:
        if character in d:
            d[character] += 1
        else:
            d[character] = 1
    return d
