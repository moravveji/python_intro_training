# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 16:40:19 2023

@author: u0015831
"""

def test(p1=10):
    
    if (p1 < 10):
        return ('abc', 100)
    elif (p1 == 10):
        return ('default value')
    else:
        return 0
    

#
t1 = test(6)
print(type(t1), t1)

t1 = test()
print(type(t1), t1)

t1 = test(1000)
print(type(t1), t1)
