# my (attempted) solution to this kata:
# https://www.codewars.com/kata/unique-in-order

def unique_in_order(iterable):
    # need to convert str to list
    if type(iterable) == str:
        iterable_string = iterable
        iterable = []
        for character in iterable_string:
            iterable.append(character)

    # remove adjacent duplicates until there are none left
    test = False
    while test == False:
        test = True
        for i, item in enumerate(iterable[:-1]):
            # look for cases of repeated letters next to one another
            if iterable[i+1] == item:
                del iterable[i+1]
                test = False
                break

    return iterable
