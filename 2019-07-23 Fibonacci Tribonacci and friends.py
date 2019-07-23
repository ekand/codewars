# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 06:27:16 2019

@author: user2
"""

def Xbonacci(signature,n):
    m = len(signature)
    for i in range(n-m):
        sum = 0
        for j in range(m):
            sum += signature[i+j]
            
        signature.append(sum)
        print('n', n, 'm', m, 'i', i, 'j', j, 'sum', sum, 'signature', signature, 'signature[i+j]', signature[i+j])
    print(len(signature))
    if len(signature) > n:
        print('True')
        signature = signature[:n]
    return(signature)
        

signature = [5, 3, 13, 19, 12, 4, 1, 8, 3, 5, 8, 14, 12, 6, 5, 18, 8, 20, 6, 19]
n = 4


print(Xbonacci(signature, n))
