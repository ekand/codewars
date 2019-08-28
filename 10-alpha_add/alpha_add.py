# solution to the kata found here
# https://www.codewars.com/kata/alphabetical-addition/train/python

def add_letters(*letters):
    if list(letters) == []:
        return 'z'
    total = 96
    for element in letters:
        total += ord(element) - 96
    print(total)
    while total > 122:
        total -= 26
    return chr(total)
