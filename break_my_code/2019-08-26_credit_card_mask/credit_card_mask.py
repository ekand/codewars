# solution to kata found here
# https://www.codewars.com/kata/5412509bd436bd33920011bc/solutions/python


def maskify(cc):
    s2 = ''
    for i in range(len(cc)):
        character = cc[-(i+1)]
        if (i+1) > 4:
            character = '#'
        s2 += character
    s2 = s2[::-1]
    return s2



'''
here's the solution voted best practice
it's a one-liner

# return masked string
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

and I actually understand how it works
'''
