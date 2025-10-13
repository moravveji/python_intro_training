# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 10:15:02 2018

@author: u0015831
"""

s1 = 'hello'
s2 = 'world'
s3 = s1 + s2
print(s3)

#c1 = 5 + s1
#print(c1)

c2 = 5 * s1
print(c2)

#%%
my_long_string = ' this is a nice piece of text for you'
my_long_string.split()
my_words = my_long_string.split()

# split on a specified character
my_words_bis = my_long_string.split('i')

list(my_long_string)

#%% putting things together
' '.join(my_words_bis)
