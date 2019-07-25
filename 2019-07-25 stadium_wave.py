# -*- coding: utf-8 -*-
"""
Created on %2019-07-25

@author: %(erik-kristofer-anderson)
"""

'''
Challenge is here:
https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
basic idea is to print out strings to simulate a wave like crowds do in
a stadium.
Below is my first pass at it. doesn't quite work in all cases:
it trips up when there are spaces.

Will work on this tomorrow.


'''



str = " gap "



def wave(str):
    output = []
    for i in range(len(str)):
        string = ''
        for j in range(len(str)):
            #print('i', i, 'j', j)
            character = str[j]
            if i == j:
                print(character.capitalize())
                #print(character.capitalize())

                #print('test 1')
                string = string + character.capitalize()
                #print(string)
            else:
                print(character)
                string = string + character
        output.append(string)
    return output

wave(str)
