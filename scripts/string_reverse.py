# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:36:09 2019

source: https://swcarpentry.github.io/python-novice-inflammation/02-loop/index.html
@author: u0015831
"""

newstring = ''
oldstring = 'Newton'
for char in oldstring:
    newstring = char + newstring
print(newstring)