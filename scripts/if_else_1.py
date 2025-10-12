# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:43:06 2018

basic if else statement

@author: u0015831
"""

from random import randint

# use the input function, specify with int-casting that an integer is expected
x = int(input('Give me a number: '))
if x < 0:
    print(x, 'is negative')
else:
    print(x, 'is positive')
    

xr = randint(1, 100)
print('xr = ', xr)
xn = x + xr

if xn == 0:
    print("The sum is equal to 0")
else:
    if xn < 0:
        print(xn, 'is negative')
    else:
        print(xn, 'is positive')
