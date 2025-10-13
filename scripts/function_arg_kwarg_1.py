# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 13:14:08 2022

@author: u0015831
"""

def arg_printer(*args, **kwargs):
    if args:
        print('positional')
    for arg in args:
        print(arg)
    if kwargs:
        print('named')
    for k, v in kwargs.items():
        print("{}={}".format(k, v))
        
print('first test')        
arg_printer(1,2,3)

print('test 2')
arg_printer(1,2,3,sweater=100,hat=5)

