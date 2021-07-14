# solution to kata found here:
# https://www.codewars.com/kata/582dcda401f9ccb4f0000025/train/python

def get_primes(n):
    t = range(2, n)
    p = 2
    d = {}
    while True:
        while p in d:
            p += 1
        i = 2
        while i * p < n:
            d[i*p] = 0 # 0 for not prime
            i += 1
        p += 1
        if p >= n:
            break
    primes = []
    for number in t:
        if number not in d:
            primes.append(number)
    return primes

def count_evens(prime):
    t = list(str(prime))
    count = 0
    for digit in t:
        for num_str in (['0', '2', '4', '6', '8']):
            if digit == num_str:
                count += 1
    return count


def f(n):
    print(n)
    primes = get_primes(n)
    max_evens = 0
    for prime in primes:
        evens = count_evens(prime)
        if evens >= max_evens:
            max_evens = evens
            result = prime
    print(result)
    return result

print(f(691510))
