# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:16:29 2018

@author: u0015831
"""

fin=open('test_text.txt','r')
for line in fin: 
    line_in = line.rstrip('\r\n') #remove end of line
    data = line_in.split() #split line of text
    print(data)
