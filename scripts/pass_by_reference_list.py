# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 09:10:52 2020

@author: https://www.tutorialsteacher.com/python/python-user-defined-function
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

# this will not work
# mytuple=(10,20,30)
# print('mytuple before call', mytuple, ' id', id(mytuple))
# myfunction(mytuple)
# print('mytuple after call', mytuple, ' id', id(mytuple))
