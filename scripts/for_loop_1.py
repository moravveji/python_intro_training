# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 16:51:05 2019
calculate the average of a list of numbers
@author: u0015831
"""

#rli = range(1, 10, 2)
#for i in rli:
#    print('i=', i)
    
    
sum=0
numbers =[1,22,31,45]
for num in numbers:
    print(num)
    sum=sum+num
avg=sum/len(numbers)
print ('Average:', avg)

    