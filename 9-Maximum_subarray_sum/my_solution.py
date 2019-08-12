# this is my solutino to the kata Maximum subarray sum
# https://www.codewars.com/kata/maximum-subarray-sum

def maxSequence(arr):
    max = 0
    for i in range(len(arr)+1):
        for j in range(len(arr)+1):
            if j >= i:
                my_sum = sum(arr[i:j])
                if my_sum > max:
                    max = my_sum
    return max

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) #should = 6
