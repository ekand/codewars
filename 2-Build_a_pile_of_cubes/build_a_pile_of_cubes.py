# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 07:58:27 2019

@author: user2
"""

# this is my first attempt. didn't go so well. It took
# a long time and got the wrong answer


def find_nb(m):
    vol = 0 # initialize a running count of the volume
    n = 1 # initialize count of number of cubes
    while vol < m:
        vol = vol + n^3
        n += 1
        print(vol)
    if vol == m:
        return n
    else:
        return -1
        
print(find_nb(4183059834009))
#should be 2022
# actually gave -1 and took a long time

