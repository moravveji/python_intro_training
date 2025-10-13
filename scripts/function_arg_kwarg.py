# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 10:14:49 2018

source: 
    https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
    https://code.tutsplus.com/articles/understanding-args-and-kwargs-in-python--cms-29494
    https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3
@author: u0015831
"""

def test_var_args(farg, *args):
    print("formal arg:", farg)
    for arg in args:
        print("another arg:", arg, " - type", type(arg))
        
def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))

def multiply(*args):
    z = 1
    for num in args:
        z *= num
        print(z)
    print('final result: ',z)

        
#using the functions
test_var_args(1, "two", 3)

test_var_kwargs(farg=1, myarg2="two", myarg3=3)
test_var_kwargs(100, myarg2="two", myarg3=3)
#test_var_kwargs(101, "two", myarg3=3)  # only 1 argument

multiply(2, 3)
multiply(2, 3, 99, 12.7)
