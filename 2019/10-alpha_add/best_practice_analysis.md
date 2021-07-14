best_practice_analysis

one liner solution to the kata Alphabetical Addition

The kata is not very clearly defined, but all of the necessary directions to solve the challenge can be gleaned from the examples:

Your task is to add up letters to one letter.

The function will be given a variable amount of arguments, each one being a letter to add.

Notes:
Letters will always be lowercase.
Letters can overflow (see second to last example of the description)
No letters should return 'z'
Examples:
add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'


From this we can surmise that we are to add the letters based on their position in the alphabet. a = 1, b = 2, c = 3, etc... so a + b + c --> 1 + 2 + 3 = 6 --> f.

Here's the one liner:
```
def add_letters(*letters):
    return chr( (sum(ord(c)-96 for c in letters)-1)%26 + 97)
```
Let's break it down.

ord(c)-96
ord gives us the ASCII character code for each letter. Since ord('a') = 97, subtracting 96 from any letter's character code gives us its position in the alphabet, indexed from 1.

Next is to take a sum.
(sum(ord(c)-96 for c in letters)

This might look more familiar as a for loop

total = 0
for c in letters:
    total += ord(c) - 96

to be continued    
