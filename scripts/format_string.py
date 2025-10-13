# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:11:26 2023

Number formatting in f-strings

"""

name = 'Jane'
age = 53
print('%s is %d years old' % (name, age))  # old school deprecated
print('{} is {} years old'.format(name, age)) 
print(f'{name} is {age} years old')  # preferred


# arithmetic expressions allowed
a = 5
b = 10
print(f'a plus b is {a + b} and 2 times a minus b is {2*a-b}')

# The = specifier will print the expression and its value:
fnum = 2007.12345
print(f"Simple = {fnum}")
print(f"Decimal Places specified = {fnum=:.2f}")
print(f"Significant Figures={fnum:.3g}")
