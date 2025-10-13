# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:12:20 2019

processing a file in a for-loop

@author: u0015831
"""

txtfile = open("test_text.txt","r")

for aline in txtfile:
    values = aline.split()
    if len(values) > 10:
        print('some text', values[0], values[1], ' and also ', values[10] )

txtfile.close()
