# How did they do that in one line? Part 2: Isograms

I just solved another challenge on codewars, and, like in my previous [post](https://dev.to/erikkristoferanderson/how-did-they-do-all-that-in-one-line-a-codewars-challenge-explanation-3e2c), the most popular solution used far fewer lines than mine did.

The challenge for this [kata](https://www.codewars.com/kata/isograms) is to take a string and indicate whether it's an isogram. An isogram is a word with no repeating letters.

Here's the popular solution:
```
def is_isogram(string):
    return len(string) == len(set(string.lower()))
```

And here's mine

```
def is_isogram(string):
    result = False
    string = string.lower()
    my_list = []
    for character in string:
        if character in my_list:
            return False
        my_list.append(character)
    return True
```

Wow. Big difference.

Let's pick apart that short solution.

```
def is_isogram(string):
    return len(string) == len(set(string.lower()))
```

The right side of the equality test is simple enough. It's just the length of the string. The right side is a little more dense but it's not actually that bad. Its function is to calculate the length of the set of unique elements in `string`.  
Let's see how it does that.  
First, `string.lower` is necessary because there may be upper and lower case instances of the same letter, and the program should recognize these as being the same letter.  
Next, `set(string.lower())` gives us a set data type with all the unique elements in string. That is, if the letter `b` occurs twice in string, it will only occur once in the set.  
Then `len(set(string.lower()))` calculates the length of this set.  
We're now ready to consider the `==` comparison. If the length of the string is equal to to the length of the set, the function will return `True`, indicating that `string` is an isogram. On the other hand, if the length of the set is different from the length of the string, that means at least one letter occurs at least twice in string. The function will then return `False`, because `string` is not an isogram.

As a final note, it's interesting to consider the case where `string` is the empty string. In that case, both the length of the set and the length of the string are zero, so the function will return True.  
Fortunately, the instructions indicate that we should assume an empty string is an isogram.  
That's convenient. It means we don't need extra code to handle the case of an empty string. The function body stays at a pithy one line.
