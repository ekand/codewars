'''This is my solution to the kata found here:
https://www.codewars.com/kata/nth-smallest-element-array-series-number-4/python

The input is an array of numbers (arr) and a position (n)
The challenge is to return the n-th smallest element
'''



def nth_smallest(arr, pos):
    arr.sort()
    return arr[pos-1]
