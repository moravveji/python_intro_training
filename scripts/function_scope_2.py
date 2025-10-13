# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:28:19 2020
taken from: https://www.python-course.eu/python3_global_vs_local_variables.php
@author: u0015831
"""

def f(): 
    s = "I love London!"
    print(s) 

s = "I love Paris!" 
f()
print(s)