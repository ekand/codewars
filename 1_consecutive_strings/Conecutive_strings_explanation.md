# Cosecutive strings
## From Codewars

This is my solution to a challenge on Codewars, which can be found [here](https://www.codewars.com/kata/56a5d994ac971f1ac500003e).


## Explanation
First, here are the details from the kata website:
---
You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

Note
consecutive strings : follow one after another without an interruption
---

In my code, first I dealt with the special cases of n = 0, k > n or k <= 0. If any one of these conditions are met, the function will return and empty string, as the challenge requires. Note that, if this happens, the rest of the function will not execute.
```
n = len(strarr)
if n == 0 or k > n or k <=0:
    return ""
```
Next, let's unpack the folling nested for loops:
```
longest_combined_string = ''
for i in range(len(strarr) - k + 1):
    short_strarr = strarr[i:i + k]
    combined_string = ''
    for string in short_strarr:
        combined_string = combined_string + string
        if len(combined_string) > len(longest_combined_string):
            longest_combined_string = combined_string
```
The first step is to initialize `longest_combined_string` as an empty string (`''`). Then we loop `i` from zero up to `len(strarr) - k + 1`. The reason for `- k` is that we will be looking at `k` number or strings at a time, so we need want to stop at the index of `i` that will give us a collection of `k` strings, starting at `i`. The `- 1` is there because slice is exclusive at the ending index.

... (under construction)...





And finally, the function returns longest_combined_string.
```
    return longest_combined_string
```
