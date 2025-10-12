# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:57:29 2018
for loop with index
@author: u0015831
"""
fruitslist = ['banana', 'apple',  'mango']
for i in range(len(fruitslist)):
    print("Color {}: {}".format(i + 1, fruitslist[i]))
print
# use of enumerate
for line in enumerate(fruitslist, start=1):
    print(line)    
print# use of enumerate
for num, color in enumerate(fruitslist, start=1):
    print("Color {}: {}".format(num, color))    
print
# is this working?
fruitset = {'banana', 'apple',  'mango'}
for num, color in enumerate(fruitset, start=1):
    print("Color {}: {}".format(num, color))        