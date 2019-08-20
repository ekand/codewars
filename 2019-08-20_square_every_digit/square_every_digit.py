def square_digits(num):
    string = str(num)
    new_string = ""
    for character in string:
        new_string += str(int(character)**2)

    return int(new_string)
