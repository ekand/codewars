# my (attempted) solution to this kata:
# https://www.codewars.com/kata/unique-in-order

def unique_in_order(iterable):
    if type(iterable) == str:
        iterable_string = iterable
        iterable = []
        for character in iterable_string:
            iterable.append(character)

    while len(iterable) > len(set(iterable)):
        for i, item in enumerate(iterable[:-1]):
            print('i', i, 'item', item, 'iterable', iterable)
            if iterable[i+1] == item:
                del iterable[i+1]
                break
#
    return iterable
