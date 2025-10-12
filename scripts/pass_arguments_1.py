# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:08:08 2018

@author: u0015831
"""

def double_the_values ( l ):
    print(" in double_the_values : l =  ", l)
    for i in range (len( l )):
        l [ i ] = l [ i ] * 2
    print(" in double_the_values : changed l to l = ", l)

l_global = [0 , 1 , 2 , 3 , 10]
print(" In main : s = ", l_global )
double_the_values ( l_global )
print(" In main : s = ",  l_global )