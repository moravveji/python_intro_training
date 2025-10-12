# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:36:15 2018

handson lists
@author: u0015831
"""

NumList=list(range(10))

# Print the length of the list
ll = len(NumList)
print("length list", ll)

# Change the fourth element to 11
NumList[3] = 11

# Extend the list with L=[20,30,40]
NumList.extend([20, 30, 40])
print(NumList)

# Print the index of the item 9
i9 = NumList.index(9)
print("index of item 9", i9)

# Remove that item from the list
NumList.remove(9)

# Print the current length of the list
print("current length of list: ", len(NumList))

# Sort the list and then reverse the sorted version
NumList.sort
Lreversed=NumList[::-1]
print(Lreversed)