# my solution
# https://www.codewars.com/kata/find-the-odd-int/python


def find_it(seq):
    dict_1 = {}
    for digit in seq:
        if digit not in dict_1:
            dict_1[digit] = 1
        else:
            dict_1[digit] += 1
    for key in dict_1:
        if dict_1[key] % 2 == 1:
            return key



""" best practice solution

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

"""
