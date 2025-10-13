# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:43:40 2020

@author: u0015831
"""

big_sum = 0   # accumumator as global variable

def my_accum(val):
    big_sum = big_sum + val
    return
# big_sum = 0
my_accum(5.7)
my_accum(6)
my_accum(99)
print('big_sum', big_sum)