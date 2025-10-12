# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 16:04:50 2023

source: https://www.w3schools.com/python/python_try_except.asp


@author: u0015831
"""

# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error
# some of the more commonly encountered ones.

# NameError - You probably misspelled a variable or function name, or you otherwise referenced a name that was never defined.
# IOError - I/O operation failed.
# SystemError - Internal error in the Python interpreter.
# ZeroDivisionError - Second argument to a division or modulo operation was zero.

x = 5 # put in comment to test

try:
  print(x/0)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")