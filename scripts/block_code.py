# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:06:18 2022

@author: u0015831
"""

from math import sqrt

my_list = [1, 2, 3, 4]
result = 0
for i in my_list:
    if i%2 == 0:
       result = result + sqrt(i)
    print(result)