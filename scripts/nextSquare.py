# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 16:30:26 2019

source: https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
"""

# A Python program to generate squares from 1 
# to 100 using yield and therefore generator 
  
# An infinite generator function that prints 
# next square number. It starts with 1 
def nextSquare(): 
    i = 1; 
  
    # An Infinite loop to generate squares  
    while True: 
        yield i*i                 
        i += 1  # Next execution resumes  
                # from this point      
  
# Driver code to test above generator  
# function 
for num in nextSquare(): 
    if num > 1000: 
         break    
    print(num) 