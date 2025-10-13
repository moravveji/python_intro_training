# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:25:31 2022

@author: u0015831
"""

x = lambda a : a + 10
f = lambda a, b: a + b 
v1 = 8.8

print('type x:', type(x))
print(x(6))
print(x(v1))

print('type f:', type(f))
print(f(5.6,6))