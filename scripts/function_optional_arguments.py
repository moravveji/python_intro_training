# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 11:00:12 2018

source: https://www.pythoncentral.io/fun-with-python-function-parameters/
@author: u0015831
"""

def foo(val1, val2, val3, calcSum=True):
    # Calculate the sum
    if calcSum:
        return val1 + val2 - val3
    # Calculate the average instead
    else:
        return (val1 + val2 + val3) / 3
    
print(foo(10,20,30, True))
print(foo(10,20,30, False))
print(foo(10,20,30))

print(foo(val1=10,val3=20,val2=30,calcSum=True))


# will this work?
#print(foo(10,20))
#print(foo(10,20,False))
#print(foo(val1=10,val3=20,val2=30,True))
