# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:31:46 2019

@author: user2
"""


'''
challenge details
https://www.codewars.com/kata/556e0fccc392c527f20000c5

If you have completed the Tribonacci sequence kata, you would know by now that 
mister Fibonacci has at least a bigger brother. If not, give it a quick look 
to get how things work.

Well, time to expand the family a little more: think of a Quadribonacci 
starting with a signature of 4 elements and each following element is the 
sum of the 4 previous, a Pentabonacci (well Cinquebonacci would probably 
sound a bit more italian, but it would also sound really awful) with a 
signature of 5 elements and each following element is the sum of 
the 5 previous, and so on.


Well, guess what? You have to build a Xbonacci function that takes a 
signature of X elements - and remember each next element is the sum of 
the last X elements - and returns the first n elements of the so seeded sequence.


'''

'''
Here's the broken code:

def Xbonacci(signature,n):
    m = len(signature)
    for i in range(n-m):
        signature = []
        sum = 0
        for j in range(m):
            sum += signature[i+j]
        signature.append(sum)
    if len(signature) >= n:
        signature = signature[:-n]
    return(signature)

signature = [5, 3, 13, 19, 12, 4, 1, 8, 3, 5, 8, 14, 12, 6, 5, 18, 8, 20, 6, 19]
n = 4

'''

#and here I'll fix it
#what is this code even suposed to do? And does the n mean.
# I think it was how many get added up

def Xbonacci(signature,n):
    m = len(signature)
    
    for i in range(m+n):
        
        #signature = []
        sum = 0
        for j in range(m):
            sum += signature[i+j]
            pass
        signature.append(sum)
    if len(signature) >= n:
        signature = signature[:n]
    return(signature)

signature = [5, 3, 13, 19, 12, 4, 1, 8, 3, 5, 8, 14, 12, 6, 5, 18, 8, 20, 6, 19]
n = 4

print(Xbonacci(signature, n))

signature = [1,1,1,1]
n = 10
print(Xbonacci(signature, n))








