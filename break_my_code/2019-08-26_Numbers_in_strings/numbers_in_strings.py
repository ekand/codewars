# my solution to kata found here:
# https://www.codewars.com/kata/numbers-in-strings

def solve(s):
    prev = '0'
    s2 = ''
    for character in s:
        if character.isalpha():
            character = ' '
        s2 += character
    t = s2.split()
    t2 = []
    for string in t:
        t2.append(int(string))
    return max(t2)



# maybe come back and figure out this one line solution on
# codewars
# def solve(s):
#    return max(map(int,re.findall(r"(\d+)", s)))
