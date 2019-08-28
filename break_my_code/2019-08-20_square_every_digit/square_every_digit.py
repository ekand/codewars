def square_digits(num):
    s = ''
    for character in str(num):
        s += str(int(character) ** 2)
    return int(s)
