# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 11:04:44 2018

@author: u0015831
"""

fp = open('testfile-writelines.txt','w') 
 
fp.write('Hello World') 
fp.write('Hello World \n') 

# write the list
l = [1, 2, 3]
l_str = map(str, l)
fp.writelines(l_str)
    
 
fp.close() 

