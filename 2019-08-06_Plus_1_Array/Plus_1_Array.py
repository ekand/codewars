'''This is a solution to the kata found here:
https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/python
'''


def up_array(arr):
    # first, test for invalid input
    if arr == []:
        return None
    for item in arr:
        if item <0 or item >9:
            return None

    #Convert array of numbers to a string
    s = ""
    for item in arr:
        s = s + str(item)

    # convert that string to an int and increment by one
    num = int(s)
    num += 1

    # put the digits of that int into a list
    output = []
    for digit in str(num):
        output.append(int(digit))
    return output
