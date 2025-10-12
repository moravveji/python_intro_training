# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:22:42 2019

command line IO

example command line: python command_line_io.py o m g
example in Spyder: run command_line_io.py o m g

@author: u0015831
"""

import sys
print('This is the name of the script: ', sys.argv[0])
print('Number of arguments: ', len(sys.argv))
print('The arguments are: ', sys.argv)


for arg in sys.argv:
    print(type(arg), arg) 