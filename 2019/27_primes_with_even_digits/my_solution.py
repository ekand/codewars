# solution to kata found here:
# https://www.codewars.com/kata/582dcda401f9ccb4f0000025/train/python

""" new approach: start at x =  n - 1.
set max_even_digits = 0
if x is prime: count even digits.
    if even_digits greater than max_even_digits:
        set max_even_digits = even_digits
        result = x
increment x down by one and repeat from `set max_even_digits = 0`
continue until length of x (digits) less than or equal to max_even_digits + 1
(if we have i digits, we can have at most i-1 even digits.)
(so if we have k even digits, we can have no less than k+1 digits)
( )
"""
def f(n):
    x = n - 1
    starting = True
    max_even_digits = 0
    while starting or (not len(str(x)) <= (max_even_digits+1)):
        #print(x)
        if is_prime(x):
            even_digits = count_even_digits(x)
            if even_digits > max_even_digits:
                max_even_digits = even_digits
                result = x
                starting = False
        x -= 1
    return(result)


def is_prime(x):
    if x == 1:
        return False
    else:
        for i in range(2, x//2):
            if (x % i) == 0:
                return False
        return True



def count_even_digits(x):
    t = list(str(x))
    count = 0
    for digit in t:
        for num_str in (['0', '2', '4', '6', '8']):
            if digit == num_str:
                count += 1
    return count



print(f(691510))
