# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 11:04:44 2018

@author: u0015831
"""

fp = open('testfile-write.txt','w') 
 
fp.write('Hello World') 
fp.write('Hello World \n') 

# write the list
# note, here print is used
# It inserts spaces between arguments and appends the line terminator.
l = [0, 1, 2, 3]
print(l, file=fp)
for i in l:
    print(i, file=fp)

for i in l:
    print(i, end=' ', file=fp)


# write the individual elements
for i in l:
    fp.write(str(i))
    
# write the individual elements with a separator
for i in l:
    fp.write(str(i) + '/')

fp.write('\n')
 
fp.close() 
