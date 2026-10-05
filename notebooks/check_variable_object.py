# -*- coding: utf-8 -*-
"""
check variable as an object

@author: u0015831
"""

a = 4.5
b = 56
c = 'Hello'
d = a + b

print(a, b, c, d)

print (type(a), type(b), type(c), type(d))

print(dir(a))
print('is a integer?', a.is_integer())
