The comments on my code should be sufficient to understand

Here's a nifty solution
(from https://www.codewars.com/kata/54e6533c92449cc251001667/solutions/python)

```
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
```
