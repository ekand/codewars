This is a solution to the challenge found [here](https://www.codewars.com/kata/nth-smallest-element-array-series-number-4/python)  
My solution is in Nth_Smallest_Element.py

Another interesting solution was on the codewars website:

```
def nth_smallest(arr, pos):
    return sorted(arr)[pos-1] # Gotta love Python
```

If I'm reading this correctly, it seems like sorted(arr) is an
expression that returns a an array which has been sorted.

Yes, I tested it out and that's how it works. It's pretty cool how that can be
done on a single line.
