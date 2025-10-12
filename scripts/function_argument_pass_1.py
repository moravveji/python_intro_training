# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 11:42:31 2018

source: https://cs.nyu.edu/courses/summer16/CSCI-UA.0002-002/slides/Python_Functions.pdf
@author: u0015831
"""

def change_me(v):
    print ("function got:", v, 'id(v) = ', id(v))
    v = 10
    print ("argument is now:", v, 'id(v) = ', id(v))

def change_me_bis(v):
    print ("function got:", v, 'id(v) = ', id(v))
    v.append(555)
    print ("argument is now:", v, 'id(v) = ', id(v))

def change_me_tris(v):
    print ("function got:", v, 'id(v) = ', id(v))
    v = v * 3
    print ("argument is now:", v, 'id(v) = ', id(v))


myvar = 5 
myvar2 = [1, 2, 3]

# testing change_me
print('\n testing change_me')
print ("starting with:", myvar)
print ("starting with id:", id(myvar))
change_me(myvar)
print ("ending with:", myvar)

print ("starting with:", myvar2)
print ("starting with id:", id(myvar2))
change_me(myvar2)
print ("ending with:", myvar2)


# testing change_me_bis
print('\n testing change_me_bis')

print ("starting with:", myvar2)
print ("starting with id:", id(myvar2))
change_me_bis(myvar2)
print ("ending with:", myvar2)



# testing change_me_tris
print('\n testing change_me_tris')

myvar = 5
print ("starting with:", myvar)
change_me_tris(myvar)
print ("ending with:", myvar)

myvar2 = [1, 2, 3]
print ("starting with:", myvar2)
change_me_tris(myvar2)
print ("ending with:", myvar2)
