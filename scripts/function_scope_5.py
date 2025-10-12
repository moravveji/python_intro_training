# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 09:25:39 2020

@author: https://www.tutorialsteacher.com/python/local-and-global-variables-in-python
"""

def SayHello():
    user='John'
    print ("user = ", user)
    return

def SayHello_implicit():
    # user must be known
    print ("user = ", user)
    return

def SayHello_global():
    global user
    print ("user = ", user)
    user = 'Mary'
    val_k = 0
    return


user = 'Jeff'
SayHello_implicit()
print('user', user)

user = 'Jeff'
SayHello()
print('user', user)

user = 'Jeff'
SayHello_global()
print('user', user)
#print(val_k)

