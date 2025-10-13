# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:43:22 2018

source: https://jakevdp.github.io/WhirlwindTourOfPython/03-semantics-variables.html

Variables are pointers 
check with id()
 The identity of the object is an integer, 
 which is guaranteed to be the unique and constant for this object 
 during its lifetime. 
 The id() is an inbuilt function in Python. 
 In CPython implementation, it is an address of the object in memory.

@author: u0015831
"""

#%%
x = 1
print('x = ', x, 'id(x) = ', id(x))
x = 'abc'
print('x = ', x, 'id(x) = ', id(x))
x = [1, 2, 3]
print('x = ', x, 'id(x) = ', id(x))
y = x
print('y = ', y, 'id(y) = ', id(y))


#%%

x = 'something else'
print('x = ', x, 'id(x) = ', id(x))
print('y = ', y, 'id(y) = ', id(y)) # y is unchanged

#%%
x = [1, 2, 3]
y = x
print('y = ', y)

#%%
x = [1,2,3,4]
print('y = ', y)

#%%
x = 5
print('x = ', x, 'id(x) = ', id(x))
y = x
print('y = ', y, 'id(y) = ', id(y))

x = x + 5
print('x = ', x, 'id(x) = ', id(x))
print('y = ', y, 'id(y) = ', id(y))
#%%
# example with mutable list
x = [1, 2, 3]
print('x = ', x, 'id(x) = ', id(x))
y = x
print('y = ', y, 'id(y) = ', id(y))

#%%
x.append(4) # append 4 to the list pointed to by x
print('x = ', x, 'id(x) = ', id(x))
print('y = ', y, 'id(y) = ', id(y)) # y's list is modified as well!
