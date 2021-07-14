# my solution to
# https://www.codewars.com/kata/find-the-missing-letter/python

def find_missing_letter(chars):
    prev = chars[0]
    print(prev)
    print(ord(prev))
    for letter in chars[1:]:
        print(letter)
        print(ord(letter))
        if ord(letter) != ord(prev) + 1:
            return chr(ord(letter)-1)
        prev = letter
