# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 12:11:11 2022

@author: u0015831
"""

def myfunction (seq):
    print ("Entering sequence inside a function: ", seq, ' id', id(seq))
    seq.append(40)
    print ("Modified sequence inside a function: ", seq, ' id', id(seq))
    seq = [1, 2, 3]
    print ("New sequence inside a function: ", seq, ' id', id(seq))
    return

mylist=[10,20,30]
print('mylist before call', mylist, ' id', id(mylist))
myfunction(mylist)
print('mylist after call', mylist, ' id', id(mylist))
