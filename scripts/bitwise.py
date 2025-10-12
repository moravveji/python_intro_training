# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:19:09 2018
bitwise

@author: u0015831
"""
x = 10
print(bin(x))

y = 13
print(bin(y))

print('x&y',x&y)
print('x&y',bin(x&y))

print('x|y',x|y)
print('x|y',bin(x|y))

print('x', x)
print('x<<2',x<<2)
print('x<<2',bin(x<<2))

print('x', x)
print('x>>1',x>>1)
print('x>>1',bin(x>>1))

print('x', x)
print('~x',~x)
print('~x',bin(~x))