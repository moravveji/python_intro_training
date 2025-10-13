# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:46:02 2018

nested lists
@author: u0015831
"""

a = [1, 2]
b = [3, 4, 5]

ln1 = [10, a]

ln2 = [1, 2, a, b, ln1]

print(ln2)
print(ln2[-1])
print(ln2[-1][1])
print(ln2[-1][1][1])