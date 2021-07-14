# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:59:04 2019

@author: user2
"""

def longest_consec(strarr,k):
    n = len(strarr)
    if n == 0 or k > n or k <=0:
        return ""
    longest_combined_string = ''
    for i in range(len(strarr) - k + 1):
        short_strarr = strarr[i:i + k]
        combined_string = ''
        for string in short_strarr:
            combined_string = combined_string + string
            if len(combined_string) > len(longest_combined_string):
                longest_combined_string = combined_string
    return longest_combined_string


# a test case
#print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))

# the code voted best practice (copied by hand by me)

def longest_consec(strarr, k):
    result = ''

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = s.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
    return result

#this is basically functionally like mine, but much cleaner, sparser, and more expressive
