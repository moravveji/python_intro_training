# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:32:20 2018

@author: u0015831
"""
# what is range?
xr = range(10)
print(type(xr))

for i in range(10):
    print(i, end=' ')

print('\n')    
    
for value in [2, 4, 6, 8, 10]:
# do some operation
    print(value + 1, end=' ')
print('\n') 
  
# enumerate
L1 = [2, 4, 6, 8, 10]
for i, val in enumerate(L1):
    print(i, val)
print('\n') 
    
L2 = ['pizza', 'pasta', 'salad', 'nachos']
print(list(enumerate(L2)))
for i, val in enumerate(L2):
    print(i, val)

# zip
L3 = [12.3, 44.56, 99.9, 768.02, 123, 123.56]
zipped = zip(L1, L2, L3)
print(list(zip(L1, L2, L3)))
for v1, v2, v3  in zipped:
    print(v1, v2, v3)
print('\n')

# unzip
e1, e2, e3 = zip(*zip(L1, L2, L3))

# map
square = lambda x: x ** 2
for val in map(square, range(10)):
    print(val, end=' / ')    
print('\n')
    
# find values up to 10 for which x % 2 is zero
is_even = lambda x: x % 2 == 0
for val in filter(is_even, range(10)):
    print(val, end=' ')
print('\n')

