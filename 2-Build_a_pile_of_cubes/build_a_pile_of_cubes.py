# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 07:58:27 2019

@author: user2
"""
# on the second attempt, using some math tricks, it works
# but only for some of the 'attempt' cases on codewars 


def find_nb(m):
    # takes a volume m and returns the number of 
    # cubes n needed to construct that volume
    
    # define a function to calculate (sum(n^3) n = 1 ... x) 
    # which, via wolfram alpha, = (1 / 4) * (x ^ 2) * (x + 1) ^ 2
    def sum(x):
        return (x * x) * (x + 1) * (x + 1) / 4
    
    # loop over guesses for n, the number of cubes
    # until we are <= the target volume
    n = 0
    type(sum(n))
    type(m)
    while sum(n) < m:
        n += 1

    # check if we got the target volume
    if sum(n) == m:
        return n 
    else:
        return -1

print(find_nb(4183059834009))
#should be 2022

