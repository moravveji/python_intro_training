# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:41:13 2022

source: https://sites.pitt.edu/~naraehan/python3/mbb20.html

@author: u0015831
"""


def isVow(char):
    return char.lower() in 'aeiou'

print(isVow('i'))
print(isVow('I'))
print(isVow('K'))
