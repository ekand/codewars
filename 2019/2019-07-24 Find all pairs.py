'''
The challenge:
You are given array of integers, your task will be to count all pairs in that array and return their count.

Notes:

Array can be empty or contain only one value; in this case return 0
If there are more pairs of a certain number, count each pair only once. E.g.: for [0, 0, 0, 0] the return value is 2 (= 2 pairs of 0s)
Random tests: maximum array length is 1000, range of values in array is between 0 and 1000
'''

#my solution

def duplicates(arr):
    if arr == []:
        return 0
    counter = 0
    for i in range(min(arr),max(arr)+1):
        counter += arr.count(i) // 2
    return counter
