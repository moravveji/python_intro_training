# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:21:52 2020
taken from: https://www.python-course.eu/python3_global_vs_local_variables.php
@author: u0015831
"""

def f(): 
    print(a)
    print(s) 

a = 1    
s = "I love Paris in the summer!"
f()