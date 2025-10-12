# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 10:27:05 2019

@author: u0015831
"""

def greetings_more(name):
    """This function greets the name passed as an argument"""
    greetings('Dear')
    greetings(name)   
    
def greetings(name):
    """This function greets the name passed as an argument"""
    print('Hello, ', name , '  Welcome!')
    

greetings_more('Marie')