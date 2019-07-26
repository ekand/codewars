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

    if str[i] != ' ':
      for j in range(len(str)):
        if i == j:
          string = string + str[j].capitalize()
        else:
          string = string + str[j]
      print(string)  
      output.append(string)
  return output
print(wave(str))
