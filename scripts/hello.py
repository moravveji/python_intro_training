# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:14:17 2019

@author: u0015831
"""

def hello():
   """
   Prints "Hello World".
   Returns:
      None
   """
  
   print('Hello World')
   return

def hello_again():
   """
   Prints "Hello World again".
   Returns:
      None
   """
  
   print('Hello World again')
   return

print('The docstring of the function hello: ' + hello.__doc__)
print('The docstring of the function hello_again: ' + hello_again.__doc__)
