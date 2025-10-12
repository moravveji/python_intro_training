# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 17:12:27 2023

@author: u0015831
"""

count1 = 0
count2 = 0
a = 100
b = 6

while count1 < 10:
    a = a + 1
    while count2 < 10:
        b = b + 1
        count2 = count2 + 1
        print(b)
    print(a)
    count1 = count1 + 1
print('the end')