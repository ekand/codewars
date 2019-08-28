# solution to a kata on codewars
# https://www.codewars.com/kata/exes-and-ohs/python
# idea is to determine whether there is an
# equal number of "x" and "o" in a string
# (count the total of both upper and lower case)

def xo(s):
    return s.lower().count('x') == s.lower().count('o')
