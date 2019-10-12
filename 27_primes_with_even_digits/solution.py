# someone else's succesful solutino on code wars:
# https://www.codewars.com/kata/primes-with-even-digits/solutions?show-solutions=1

def is_prime(n):
    if n % 2 == 0: return False
    for x in xrange(3, int(n**0.5) + 1, 2):
        if n % x == 0: return False
    return True

def f(n):
    max_prime, max_even_cnt = 0, 0

    for x in range(n-1, 0, -1):
        if len(str(x)) <= max_even_cnt + 1:
            break

        if is_prime(x):
            even_cnt = sum(d in "02468" for d in str(x))
            if even_cnt > max_even_cnt:
                max_prime = x
                max_even_cnt = even_cnt

    return max_prime
