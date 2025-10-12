# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:12:20 2019

processing a file with readline
the file is read into a list

@author: u0015831
"""

txtfile = open("test_text.txt","r")

aline = txtfile.readline()
values = aline.split()

while aline:
    if len(values) > 10:
        print('some text', values[0], values[1], ' and also ', values[10] )
    aline = txtfile.readline()
    values = aline.split()

txtfile.close()
