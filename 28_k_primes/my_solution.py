### kata found here
# https://www.codewars.com/kata/k-primes/train/python

import math

def countPrimeFactors(n):
	counter = 0
	if n == 0:
		return 0
	while n % 2 == 0:
		counter += 1
		n = n / 2

	for i in range(3,int(math.sqrt(n)) + 1, 2):
		while n % i == 0:
			counter += 1
			n = n / i

	if n > 2:
		counter += 1
	return counter

def count_Kprimes(k, start, nd):
	res = []
	for i in range(start, nd + 1):
		if countPrimeFactors(i) == k:
			res.append(i)
	return res

# print(count_Kprimes(2, 0, 100)) # works correctly



def puzzle(n):
	one_primes = count_Kprimes(1, 0, n)
	three_primes = count_Kprimes(3, 0, n)
	seven_primes = count_Kprimes(7, 0, n)
	counter = 0
	for one_prime in one_primes:
		for three_prime in three_primes:
			for seven_prime in seven_primes:
				if one_prime + three_prime + seven_prime == n:
					counter += 1
	return counter

# print(puzzle(143)) # works!!! passed!
