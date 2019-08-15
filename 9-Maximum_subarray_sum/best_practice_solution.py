# the solution voted best practice for the kata
# Maximum subarray sum on codewars
# https://www.codewars.com/kata/maximum-subarray-sum


def maxSequence(arr):
    print('arr:', arr)
    max,curr=0,0
    print('max:', max)
    print('curr:', curr)
    print('')
    print('`for x in arr:`')
    for x in arr:
        print('x:', x)
        print('curr:', curr)
        curr+=x
        print('`curr+=x`, curr:', curr)
        if curr<0:curr=0
        print('`if curr<0:curr=0`, curr:', curr)
        if curr>max:max=curr
        print('`if curr>max:max=curr`, max:', max)
        print('')
    print('`return max`, max:', max)
    print('')
    return max


print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) #should = 6
