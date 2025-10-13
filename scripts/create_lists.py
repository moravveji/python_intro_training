# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 11:52:06 2019

create lists

"""
# classic approach
squares = []
for i in range(10):
    squares.append(i * i)
squares

# list comprehension
squares = [i * i for i in range(10)]
squares