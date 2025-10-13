# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 13:44:00 2018

@author: u0015831
"""

my_file=open('lines_10.txt','r')

fa = my_file.read()
print(fa)

my_file.seek(0)  # return handle to first position
f3 = my_file.read(3)
print(f3)

# use readline
frl = my_file.readline()
print(frl)
