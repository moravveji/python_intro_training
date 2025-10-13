# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 11:38:15 2018

list_cheat

beased on http://ehmatthes.github.io/pcc/cheatsheets/README.html
@author: u0015831
"""

# Use square brackets to define a list, and use commas to separate individual items in the list. Use plural names for lists, to make your code easier to read.
# []
zips = [3001, 3000, 1000, 9000, 8000]

# Individual elements in a list are accessed according to their index. The index is 0 based.
# Use square brackets []"
first = zips[0]
last = zips[-1]

#Refer to the index of the item you want to modify.
zips[1] = 8500
zips[-2] = 2000

# Add elements to the end of a list, 
# or insert at wherever position in the list."
zips.append(3500)
zips.insert(0, 3050)
zips.insert(3,4000)

# remove elements by their position in a list, 
# or by the value of the item.  Python removes only the first occurrence of that value"
del zips[1]
zips.remove(4000)

# pop() returns the last element in the list, but any index can be specified.
recent_zip = zips.pop()
first_zip = zips.pop(0)

# The len() function returns the number of items
num_zip = len(zips)

# The sort() method changes the order of a list permanently. 
# The sorted() function returns a copy of the list, leaving the original list unchanged. "
zips.sort()
zips.sort(reverse=True)
zs = sorted(zips)

#Python loop pulls each item from the list one at a time and stores it in a temporary variable, which you provide a name for.
for zip in zips:
    print(zip)
    
# The range() function starts at 0 by default, and stops  below the  upper boundary.
# range(start, stop[, step]) 
for number in range(1001): 
    print(number)
# create a list of numbers, interlaced by 100
numbers = list(range(1, 1000001, 100))

# Simple statistics are possible on a list containing numerical data.
smallest = min(zips)
largest = max(zips)
sumzips = sum(zips)

# A portion of a list is called a slice. To slice a list start with the index of the first item , colon,  index after the last item. 
first3 = zips[:3]
last3 = zips[-3:]
middle3 = zips[2:5]

#Copy a list:  make a slice from the first to the last element. Remember that a variable name is a label, pointer to some spot in memory
copy_of_zips = zips[:]
