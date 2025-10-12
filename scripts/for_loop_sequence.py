# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:46:16 2018
for loop on different sequences

source: https://www.tutorialspoint.com/python/python_for_loop.htm
@author: u0015831
"""

for letter in 'Python':     # First Example
   print('Current Letter :', letter)

fruitslist = ['banana', 'apple',  'mango']
for fruit in fruitslist:        # Second Example
   print('Current fruit :', fruit)
print()
fruitstuple = ('banana', 'apple',  'mango')
for fruit in fruitstuple:        # Third Example
   print('Current fruit :', fruit)
print()
fruitset = {'banana', 'apple',  'mango'}
for fruit in fruitset:        # Fourth Example
   print('Current fruit :', fruit)
