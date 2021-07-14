# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/solutions/python

def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))
