# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:45:23 2018

@author: u0015831
"""
# a regular function definition
def my_sub(a,b):
    res = a - b
    return (res, a, b)

# defining a function with default values
def my_min(a=9, b = 2):
    res = a - b
    return (res, a, b)

# calling the functions
res = my_sub(1, 2)
print(res)

res = my_sub(b=10, a=5)
print(res)

c = 1
d = 2
res = my_sub(c, d)
print(res)

res = my_min()
print(res)

res = my_min(7, 8)
print(res)
