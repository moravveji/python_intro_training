# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 09:04:02 2020

@author: https://www.tutorialsteacher.com/python/python-user-defined-function
"""

def myfunction(arg):
    print ('value received:',arg,'id:',id(arg))
    arg = 8
    print ('value changed:',arg,'id:',id(arg))
    return

#id() function returns a unique integer corresponding to the identity of an object.

x=10
print ('value passed:',x, 'id:',id(x))

myfunction(x)
print ('value after function call:',x, 'id:',id(x))
