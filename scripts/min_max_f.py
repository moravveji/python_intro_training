# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:19:07 2018

usage: 
seq = [1, 9, 2, 4, 3, 540]
print min_max(seq)

string = 'Hello World'
print min_max(string)

@author: u0015831
"""

def min_max(t):
    """Returns the smallest and largest 
    elements of a sequence as a tuple"""
    return (min(t), max(t))

