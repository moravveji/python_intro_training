# -*- coding: utf-8 -*-
"""

basic example using function

demo 1: copy main part in front of the function definitions
        check the behavior of the IDE

demo 2: run program in editor / debug mode

@author: u0015831
"""


# main part, calling the functions


def my_func_1 ():
    """
    this function writes hello, no input, no output
    """
    print('Hello')
    
def my_func_2(a, b):
    """
    parameters:
        a: first part of mathematical manip
        b: second part in mathematical manip
        
    """
    res = a + b
    return (res)

def my_func_3(a, b):
    """
    parameters:
        a: first part of mathematical manip
        b: second part in mathematical manip
    """
    res1 = a + b
    res2 = a - b
    return (res1, res2)



my_func_1()
    
my_func_2(5,6) # effect?
r1 = my_func_2(5,6)
print(type(r1))
print(r1)

r2 = my_func_3(5,6)
print(type(r2))
print(r2)

r3 = my_func_3(b=5,a=6)
print(type(r3))
print(r3)