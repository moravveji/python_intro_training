# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 10:43:53 2018

source:
    Jake Van der Plas: A Whirlwind Tour of Python
@author: u0015831
"""
# x = 1/0

try:
    print("let's try something:")
    x = 1 / 0 # ZeroDivisionError
except:
    print("something bad happened!")