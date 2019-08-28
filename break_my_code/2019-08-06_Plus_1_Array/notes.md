The challenge:

Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

Examples
For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]

-----

My code has comments to explain what is happening.
```
def up_array(arr):
    # first, test for invalid input
    if arr == []:
        return None
    for item in arr:
        if item <0 or item >9:
            return None

    #Convert array of numbers to a string
    s = ""
    for item in arr:
        s = s + str(item)

    # convert that string to an int and increment by one
    num = int(s)
    num += 1

    # put the digits of that int into a list
    output = []
    for digit in str(num):
        output.append(int(digit))
    return output
```

---

There's a clever solution that does most of it on one line

```
def up_array(arr):
  if not arr or min(arr) < 0 or max(arr) > 9:
    return None
  else:
    return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]
```

Let's break this down.  
First, there's an if statement with multiple parts. `if` starts it off. Then there is the expression `not arr`. This is nice. It takes advantage of the fact that data type like list can have a boolean interpretation. In this case, if array is empty, `not arr` will evaluate to True (because `arr` would evaluate to false).  
This is attached to the next bit by `or`. The next two parts are more straightfoward. If the minimum of the array is less than zero or if the maximum of the array is greater than nine, the if statement will evaluate to true.  
So, if the list is empty or contains elements out of range, the function will return `None`.

Now the real meat of it.  
`return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]`
Wheh! That's a mouthful.  
At the center of the parenthesis and brackets we have: `str(x) for x in arr`. That seems straightfoward enough. It looks similar to what I saw in lecture yesterday in Metis Beginner Python and Math for Data Science.  
It seems like this would be functionally equivilant to the following (which is psuedo code):
```
y = []
for x in arr:
    y = str(x)
```

The point is, I think that `str(x) for x in arr` would return an array of strings which have been converted from the integers in arr.  
Let's test this.  
```
In      arr = [2,3,9]

In      [str(x) for x in arr]
Out     ['2', '3', '9']
```
Yes. That's how it works.

Next step: `"".join([str(x) for x in arr])`. It looks like we are joining an empty string to the array of strings. Or maybe we are joining the array of strings into one array with the empty string between them. I can test this.
```
In[4]:     [str(x) for x in arr]
Out[4]:    ['2', '3', '9']

In[5]:     "".join([str(x) for x in arr])
Out[5]:    '239'


In[6]      "-".join([str(x) for x in arr])
Out[6]:    '2-3-9'
```
Yes. It joins together the strings of the array, with either nothing ("") or a dash ("-") between the strings.

What next?
We have `(int("".join([str(x) for x in arr])) + 1)`. This is pretty straight forward. Take the result from above, convert it to an integer, then add one. Cool.

Next, we have `str(int("".join([str(x) for x in arr])) + 1)`. This is an easy step. We're just taking the resulting integer and converting it to a string.

This next bit is a bit more tricky. `[int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]`. I believe this does something analogous to:
```
new_list = []
for y in my_string:
    y = int(y)
    new_list.append(y)
```
So it should take each character from the string, convert that to an integer, and put it into a list. Let's test it.
```
In[7]:    [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]
Out[7]:   [2, 4, 0]
```
Yes. that's what it does. Good.

Then there's just one more step: `return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]`. That means take the result of all that code, and return it as the function output.

## Summary
So, to summarize that code, we have:
```
def up_array(arr):
  if not arr or min(arr) < 0 or max(arr) > 9:
    return None
  else:
    return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]
```
Which, if I translate to psuedo code, would look something like:
```
define function up_array as a function of the array, arr:
    if there are problems with the input:
        return nothing
    otherwise:
        take a list of integers, convert each to a string and put them together into a string, convert that string to an int, add one to that int, and convert that result to a string. Then pull out the characters of that string one by one, converting each into a string and populating a list with those strings.
        Return that list.
