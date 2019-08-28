# solution to kata from
# https://www.codewars.com/kata/remove-duplicate-words

def remove_duplicate_words(s):
    """ removes duplicate words from a string

    s:   a string of words separated by spaces
    """
    s = s.split()
    unique = []
    for word in s:
        if word not in unique:
            unique.append(word)
    s = ' '.join(unique)


    return s

print(remove_duplicate_words('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))
