# -*- coding: utf-8 -*-
"""
create a list with floats, 
first part increment with 1
second part incremant with an additional step size 20

@author: u0015831
"""

x=1.
L=[x]
while x>0: 
    x=x+1.  
    L.append(x) 
    if x >= 10000.0 : break # break out of the loop once x >= 10000
    if x <100.0 : continue  # go to the next iteration when x < 100
    x=x+20.0 
    
print(L)