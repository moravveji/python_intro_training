# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 12:09:32 2022

@author: u0015831
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
