This time I did it in one line - a CodeWars challenge explanation



I've developed a habit of writing [posts](https://dev.to/erikkristoferanderson/how-did-they-do-that-in-one-line-part-2-isograms-52p6) about one-line solutions to Kata (challenges) on CodeWars.  
In the past they've all been about one-line solutions written by other code warriors. But this time, I came up with the one-liner. I wasn't the first, but I did come up with it myself.  
The idea of this [kata](https://www.codewars.com/kata/exes-and-ohs/python) was to determine if a string had an equal number of "x"s and "o"s.  
Here's my solution:  
```
def xo(s):
    return s.lower().count('x') == s.lower().count('o')
```
Note: by one line I mean one line of function body.

I started with a return statement because the expression following it will return a boolean value: `True` if the "x"s and "o"s are the same in number, and otherwise `False`.

Now it gets a little dense, so I'll pick it apart. On each side of the equality test, we start with `s.lower()`. The result of this expression will be a lower case string. Let's call it `s.low`.  
Now we can see that `s.lower().count('x')` is equivilant to s_low.count('x'), which would return the number of the character 'x' in the string `s`.  
`s.lower().count('o')` will do the same thing.  
Now, on either side of the `==`, we have an expression for the number of one of those characters in the string `s`. If those numbers are equal, the function returns `True`. Else, the function returns `False`.


Note: a more readable solution would be:
```
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
```
This was actually my first idea, and it's the most popular solution for this kata on CodeWars. Since Python is all about readability, I'd have to say this is the better solution, but I've developed a fancy for one-line solutions.

I suspect I'll be back with another of these in the near future. Until then, enjoy and be well.

~Erik
